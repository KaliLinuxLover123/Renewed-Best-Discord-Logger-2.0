import subprocess
import sys

# List of packages to install
packages = [
    'discord-webhook',  # Correct package name for Discord webhook functionality
    'requests',
    'DiscordWebhook',
    'DiscordEmbed',
    'Embed',
    'http.client',
    'discord_webhook'
]

def install(package):
    """Install a package using pip."""
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])


if __name__ == "__main__":
    # Install packages
    for package in packages:
        try:
            install(package)
            print(f"Successfully installed {package}")
        except Exception as e:
            print(f"Failed to install {package}. Error: {e}")

# if you'r looking at this code, its so that you have all the modules set up BEFORE running the script, because if you don't have the packages installed yet, then you aint able to run it
# Thanks for wasting your time reading this