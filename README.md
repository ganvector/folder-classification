# Folder Classification using Watchdog

This Python script monitors a folder for changes and automatically classifies files based on their extensions. When new files are detected, the script moves them to designated folders according to their file extensions.

## Table of Contents
- [Installation](#Installation)
- [Usage](#usage)

## Installation

1. Clone this repository into your local machine:
    ```bash
    git clone https://github.com/ganvector/folder-classification.git
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
     
    * On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    * On Linux and macOS:
        ```bash
        source ./venv/bin/activate
        ```

4. Install the required dependencies using [Poetry](https://python-poetry.org/)
    ```bash 
    poetry install
    ```
   
## Usage
1. Run the script to start monitoring the folder
    ```bash
    poetry run start
    ```
2. Put all the files inside the folder inside `app/test-folder`
3. To stop the script, press `CRTL + c`