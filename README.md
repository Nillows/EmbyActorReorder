# Emby Actor Reorder Tool

## Description 
This project provides a utility to reorder the actors in the pre-generated`.nfo` files created by Emby. It features a user-friendly interface that allows users to specify a new order for the actors being displayed, supporting both full and partial reordering.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)
- [Features](#features)
- [How to Contribute](#how-to-contribute)
- [Tests](#tests)
- [Questions](#questions)

## Installation

### All Users:
1. **Install Python**:
   - Visit the official Python website: [Download Python](https://www.python.org/downloads/).
   - Choose the version appropriate for your operating system and download the installer.
   - Run the installer. Ensure to check the box that says "Add Python to PATH" at the beginning of the installation process on Windows. This step makes Python and pip accessible from the command line.

2. **Verify Python and pip Installation**:
   - Open your command line interface (CLI), which could be Command Prompt on Windows or Terminal on macOS.
   - Type `python --version` and press Enter to ensure Python was installed correctly. If necessary, use `python3 --version` especially on macOS.
   - Type `pip --version` and press Enter to confirm that pip, Python’s package installer, is installed correctly. On macOS, you might need to use `pip3 --version`.

3. **Download the Project**:
   - Clone or download this repository to your local machine. If you are unfamiliar with how to clone a repository, visit GitHub's guide on [Cloning a Repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository). Or, you can simply click the green "Code" button in the repo and select "Download as Zip" to download it directly; be sure to unzip the files before attempting to use the tool if you download this way.

### Windows Users:
4. **Prepare to Run the Application**:
   - Locate the `RunActorReorder.bat` file within the downloaded project files.
   - Double-click the `RunActorReorder.bat` file to start the application. This batch file will handle the creation of a virtual environment, activate it, install necessary dependencies from `requirements.txt`, and run the script. This file streamlines the process by managing Python virtual environments and dependencies, allowing you to run the application with just a double-click.

### Mac Users:
4. **Prepare to Run the Application**:
   - Locate the `ActorReorder.sh` file within the downloaded project files.
   - Open Terminal and navigate to the directory containing `ActorReorder.sh`.
   - Before running the script for the first time, you need to make it executable. Type the following command in Terminal:
     ```
     chmod +x ActorReorder.sh
     ```
   - To run the script, type the following command in Terminal:
     ```
     ./ActorReorder.sh
     ```
   - This script will handle the creation of a virtual environment, activate it, install necessary dependencies from `requirements.txt`, and run the script, similar to the batch file on Windows.

## Usage

### Windows Users:
Run the `RunActorReorder.bat` file by double-clicking on it. This batch file automates the setup and execution process, ensuring a smooth operation:
- **Checks for an Existing Virtual Environment**: If not present, it creates one to isolate dependency installations from the global Python environment.
- **Activates the Virtual Environment**: Ensures all commands and packages are run within this isolated environment.
- **Installs Required Packages**: Automatically installs all necessary Python packages from `requirements.txt` to ensure that all dependencies needed by the script are available within the virtual environment.
- **Runs the Python Script**: Executes the script that:
  - Asks for the file directory containing your `.nfo` files. (e.g., `C:\Users\thomw\Desktop\tvshows`)
  - Allows you to reorder the actors listed in each `tvshow.nfo` file found in the given directory.
  - Optionally lets you provide full or partial reordering.
  - Locks the data after reordering to prevent other processes from overwriting the changes.
- **Deactivates the Virtual Environment**: After running the script, it deactivates the environment and returns to the original state.

### Mac Users:
Run the `ActorReorder.sh` script by using the Terminal. This  shell script automates the setup and execution process similarly to the Windows batch file:
- **Navigate to the Script Location**: Open Terminal and change to the directory where `ActorReorder.sh` is located.
- **Run the Script**: Execute the script by typing `./ActorReorder.sh`. You may need to ensure the script is executable by running `chmod +x ActorReorder.sh` if you haven't done so already.
- **Script Operations**:
  - **Checks for an Existing Virtual Environment**: Creates one if it doesn’t exist to ensure all dependencies are managed separately.
  - **Activates the Virtual Environment**: All commands and package installations are performed within this controlled environment.
  - **Installs Required Packages**: Dependencies listed in `requirements.txt` are installed to meet the script's requirements.
  - **Runs the Python Script**: The script prompts you to:
    - Specify the directory containing your `.nfo` files. (e.g., `/Users/thomw/Desktop/tvshows`)
    - Reorder the actors as listed in each `tvshow.nfo` file found.
    - Optionally, provide full or partial reordering.
    - Ensures data is locked after modifications to avoid overwriting by other processes.
- **Deactivates the Virtual Environment**: The script deactivates the environment upon completion to restore the system to its original configuration.

## Known Issues
**Microsoft Defender SmartScreen Warning**:
- **Issue**: When running the `RunActorReorder.bat` file for the first time, Windows Defender SmartScreen may display a warning saying, "Windows protected your PC" and prevent the app from starting, citing an "Unknown publisher."
- **Resolution**: Click on "More info" then choose "Run anyway" to proceed with running the script. This warning occurs because the script is unrecognized by Microsoft's security services. Uusing the "Run anyway" option will allow you to bypass this security check.

## Credits
Developed by Thomas Wollin

## License
This project is covered under the MIT license.

## Features
1. Full and partial reordering of actor entries in `.nfo` files.
2. Easy to use batch file for running the application on Windows.
3. Locks the data after changes to prevent accidental overwriting.
4. Supports processing multiple `.nfo` files in a given directory.

## How to Contribute
Contributions are welcome. Please submit pull requests or issues through the project's GitHub page.

## Tests
Currently, there are no automated tests for this script. Manual testing is recommended by running the tool on test `.nfo` files to ensure functionality.

## Questions
Find me on GitHub: [Nillows](https://github.com/Nillows)
Email me with any questions: thomwollin@gmail.com
