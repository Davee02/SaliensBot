# Saliens-Bot

## What is it?

This is a "bot" for the Steam Summer Sale 2018 game, called *Saliens*. It easily manages to pass the *hard* tiles.

## How to install it?

You need to have the following things installed on you local computer:
- Python 3
- OpenCV
- PyAutoGui
- Numpy
- MatPlotLib
- Pillow

I heavily recommend you using [Chocolatey](https://chocolatey.org) and [PiP](https://pypi.org/project/pip/) for installing the programs / packets.
For installing with chocolatey do the following things:
1. Install Chocolatey
    1. Open Powershell **as Admin** and input `Set-ExecutionPolicy AllSigned`
    2. Input `Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))` into powershell
    3. Reopen your Powershell **as Admin**
2. Install Python
    1. Input `choco install python3`
    2. When you're asked to confirm something, confirm it with `Y`
3. Install Python packages
    1. After Chocolatey finished to install python, execute the following commands in the powershell:
        - `pip install numpy`
        - `pip install matplotlib`
        - `pip install opencv-python`
        - `pip install pyautogui`
        - `pip install pillow`

## How to use it?

**Note: This script only works on a FullHD (1920 * 1080) monitor!**

To use the script, do the following things:
1. Open your Steam Client and maximize it
2. Open the Saliens-Game
3. Start a new round of the game
4. Double-Click the script (`steam_summersale_bot.pyw`)
5. When the round is about to end (about 1-2 seconds before the end), input the combination `CTRL + ALT + DEL` to end it.

## How to report a bug / issue?

Just use the GitHub function for reporting a bug.
