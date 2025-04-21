#!/bin/bash

# Check if Poetry is available
if command -v poetry &> /dev/null; then
    echo "Poetry is available. Using Poetry to run the project."
    poetry run python src/p2/__init__.py
    exit 0
fi

# Initialize Python virtual environment
if [ -d "./.venv" ]; then
    source ./.venv/bin/activate
else
    echo "Virtual environment not found. Please create it first."
    exit 1
fi

# Run the __init__.py file
python src/p2/__init__.py