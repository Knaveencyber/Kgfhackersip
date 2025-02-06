import requests
import time
import os
import webbrowser
from colorama import Fore, init

# Initialize Colorama for color support
init(autoreset=True)

# Define colors for animation
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

# Animated Header
def animated_header():
    header_text = "___ IP FINDER ___"
    for i in range(5):  # Loop to create animation
        os.system("clear")  # Clear screen
        print(colors[i % len(colors)] + header_text.center(40))  # Center header
        time.sleep(0.3)

# Function to get IP details
def get_ip_details():
    try:
        response = requests.get("http://ip-api.com/json/")  # Get IP details
        data = response.json()

        if data['status'] == 'success':
            print(Fore.YELLOW + "\n📍 IP Details 📍")
            print(Fore.GREEN + f"IP Address: {data['query']}")
            print(Fore.CYAN + f"City: {data['city']}, {data['regionName']}, {data['country']}")
            print(Fore.MAGENTA + f"Latitude: {data['lat']}, Longitude: {data['lon']}")
            print(Fore.RED + f"ISP: {data['isp']}")
        else:
            print(Fore.RED + "Failed to retrieve IP details.")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

# Function to open Instagram properly in Termux
def open_instagram():
    instagram_urls = [
        "https://www.instagram.com/kutty_rolex_naveen?igsh=cGg4bzcxaDlncHF1",
        "https://www.instagram.com/kgf_kgf_hackers?igsh=MTBvcnVhaDJzZnZmbQ=="
    ]

    for url in instagram_urls:
        print(Fore.CYAN + f"\nOpening Instagram: {url} ...")
        time.sleep(2)
        os.system(f"am start -a android.intent.action.VIEW -d {url}")  # Open Instagram app
        time.sleep(3)  # Wait before opening the next one

# Main execution
if __name__ == "__main__":
    animated_header()
    get_ip_details()
    open_instagram()
