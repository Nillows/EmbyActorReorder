@echo off
echo Preparing to run the Actor Reorder Script...

:: Check if virtual environment exists, if not create one
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

:: Install required packages from requirements.txt
echo Installing required dependencies...
pip install -r requirements.txt

:: Run the Python script
echo Running the script...
python ActorReorder.py

:: Deactivate the virtual environment and close
call venv\Scripts\deactivate
echo Script has completed. Closing...
pause
