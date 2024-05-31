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
1. **Install Python**:
   - Visit the official Python website: [Download Python](https://www.python.org/downloads/).
   - Choose the version appropriate for your operating system and download the installer.
   - Run the installer. Make sure to check the box that says "Add Python to PATH" at the beginning of the installation process. This step makes Python and pip accessible from the command line.

2. **Verify Python and pip Installation**:
   - Open your command line interface (CLI), which could be Command Prompt on Windows.
   - Type `python --version` and press Enter to ensure Python was installed correctly.
   - Type `pip --version` and press Enter to confirm that pip, Python’s package installer, is installed correctly.

3. **Download the Project**:
   - Clone or download this repository to your local machine. If you are unfamiliar with how to clone a repository, visit GitHub's guide on [Cloning a Repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

4. **Prepare to Run the Application**:
   - Locate the `RunActorReorder.bat` file within the downloaded project files.
   - Double-click the `RunActorReorder.bat` file to start the application. This batch file will handle the creation of a virtual environment, activate it, install necessary dependencies from `requirements.txt`, and run the script.

The `.bat` file streamlines the process by managing Python virtual environments and dependencies, allowing you to run the application with just a double-click.

## Usage 
Run the `RunActorReorder.bat` file by double-clicking on it. This batch file automates the setup and execution process, ensuring a smooth operation:
- **Checks for an Existing Virtual Environment**: If not present, it creates one to isolate dependency installations from the global Python environment.
- **Activates the Virtual Environment**: Ensures all commands and packages are run within this isolated environment.
- **Installs Required Packages**: Automatically installs all necessary Python packages from `requirements.txt` to ensure that all dependencies needed by the script are available within the virtual environment.
- **Runs the Python Script**: Executes the script that:
  - Asks for the file directory containing your `.nfo` files. (e.g., `C:\Users\thomw\Desktop\tvshows`)
  - Allows you to reorder the actors listed in each and every `tvshow.nfo` file found in the given directory.
  - Optionally lets you provide full or partial reordering.
  - Locks the data after reordering to prevent other processes from overwriting the changes.
- **Deactivates the Virtual Environment**: After running the script, it deactivates the environment and returns to the original state.

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
