import discord
from discord.ext import commands
import asyncio
import os

TOKEN = 'YOUR_BOT_TOKEN_HERE'

GREEN = "\033[1;32m"
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
MAGENTA = "\033[1;35m"
RESET = "\033[0m"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

target_channel_id = None
messages_list = []
is_running = True

def print_banner():
    os.system('clear')
    print(MAGENTA + "================================================" + RESET)
    print(CYAN +    "             DEVELOPED BY: Vex Tool             " + RESET)
    print(YELLOW +  "         CUSTOM DISCORD AUTO-TYPER v2.0         " + RESET)
    print(MAGENTA + "================================================" + RESET)

def get_user_input():
    global target_channel_id, messages_list, is_running
    print_banner()
    
    try:
        print(BLUE + "\n[?] Please enter the channel details:" + RESET)
        channel_input = input(CYAN + "➥ ID of the room: " + RESET).strip()
        target_channel_id = int(channel_input)
        
        print(BLUE + "\n[?] Enter your messages (Type 'DONE' when finished):" + RESET)
        print(YELLOW + "------------------------------------------------" + RESET)
        
        count = 1
        while True:
            msg = input(CYAN + f" ✎ Text #{count}: " + RESET).strip()
            if msg.upper() == 'DONE':
                break
            if msg:
                messages_list.append(msg)
                count += 1
        
        if not messages_list:
            print(RED + "\n❌ Error: You must enter at least one text!" + RESET)
            is_running = False
            returns

        print(YELLOW + "------------------------------------------------" + RESET)
        print(GREEN + f"✔ Total messages saved: {len(messages_list)}" + RESET)
        print(RED + "[!] Starting... Press Ctrl+C in Termux to STOP." + RESET)
        print(MAGENTA + "================================================\n" + RESET)
        
    except ValueError:
        print(RED + "\n❌ Error: ID must be a number!" + RESET)
        is_running = False
    except KeyboardInterrupt:
        print(RED + "\n\n[-] Cancelled by user." + RESET)
        is_running = False

@bot.event
async def on_ready():
    print_banner()
print(GREEN + f"🤖 Bot [{bot.user}] is connected successfully!\n" + RESET)