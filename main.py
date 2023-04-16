import os
import socket
import subprocess
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types


# Load Telegram API key from .env file
load_dotenv()
API_TOKEN = os.getenv('TELEGRAM_API_KEY')
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def get_ip_address() -> str:
    """
    Retrieves the IP address of the machine.

    Returns:
        str: The IP address.
    """

    # Execute the command to get the IP address.
    command = "ip addr show | egrep inet | awk '{print $2}' | awk -F'/' '{print $1}' | egrep -v '^127' | xargs"
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    # Get the output and decode it.
    output, _ = proc.communicate()
    output = output.decode().strip()

    # Replace unnecessary characters from the output.
    replace_chars = ["\'", "\"", "::1 "]
    for char in replace_chars:
        output = output.replace(char, "")

    # Return the IP address
    return output

def get_computer_name():
    # Get current computer name
    return socket.gethostname()


def get_pc_info():
    """
    Returns the computer name and ip address of the device.
    """
    ip_address = get_ip_address()
    computer_name = get_computer_name()
    return (computer_name, ip_address)


@dp.message_handler(commands=['ip'])
async def send_ip_name(message: types.Message):
    """
    This handler will be called when user sends `/ip` command.
    It retrieves the computer name and ip address of the device, formats 
    them into a string, and replies to the user with the message.
    """
    computer_name, ip_address = get_pc_info()
    response = f"PC: {computer_name}. IP: {ip_address}."
    await message.reply(response)
    

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
