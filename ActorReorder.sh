#!/bin/bash

echo "Preparing to run the Actor Reorder Script..."

# Check if virtual environment exists, if not create one
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install required packages from requirements.txt
echo "Installing required dependencies..."
pip install -r requirements.txt

# Add 30 blank lines for visual space
for i in {1..30}
do
    echo ""
done

# Run the Python script
echo "Running the script..."
python3 ActorReorder.py

# Deactivate the virtual environment and close
deactivate
echo "Script has completed. Closing..."
