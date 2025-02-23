# Super Smash Bros. Ultimate Modpack

This is just a mirror of the mods selection I currently run on my switch, most of which are downloaded from Gamebanana and a few worked on specifically by me and friends.

## Prerequisites

1. Install the latest [Atmosphere-NX release](https://github.com/Atmosphere-NX/Atmosphere/releases/) on your SD card.
2. Install the latest [Arcropolis](https://github.com/Raytwo/ARCropolis/releases).
3. _(Optional)_ Set up FTP on your Switch to wirelessly transfer files. Here's a [video tutorial](https://youtu.be/sbXilm14lPw).

## First Time Setup

1. Install [Git](https://gitforwindows.org/) if you don't already have it on your PC.
2. Open Windows Explorer on your PC and go to a directory where you would want to save these mods.
3. Right click in Windows Explorer and click either `Open in Terminal` or `Open Git Bash here`.
4. When the terminal opens, paste `git clone <repository link>` and click enter.
5. It will copy the latest versions of all the mods to that folder in your PC. When it completes feel free to close the terminal.
6. On your Switch's SD card, delete any existing version of the `ultimate` folder and `atmosphere/contents/01006A800016E000`.
7. Copy everything inside of the `Soraalam1_Shared_Modpack` folder that appeared during the git clone on your PC and paste them into the root of your Switch's SD card.

## How to Update your Mods

Now that you're set up and have the Git repository cloned, updating is easier.

1. Open the folder Soraalam1_Shared_Modpack on your PC with Windows Explorer, right click and click either `Open in Terminal` or `Open Git Bash here`.
2. When the terminal opens, type `git pull` and press enter. If there are updates available you will see them be copied over now. Feel free to close the terminal after it completes.
3. On your Switch's SD card, delete any existing version of the `ultimate` folder and `atmosphere/contents/01006A800016E000`.
4. Copy everything inside of the `Soraalam1_Shared_Modpack` folder that you have on your PC and paste them into the root of your Switch's SD card.
