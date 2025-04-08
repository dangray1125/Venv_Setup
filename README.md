This application is a simple python script that will take a directory path as an argument and create a virtual environment in that directory path. While creating the environment it will check for the existence of a requirements.txt file and if it exists it will install all packages contained in the requirements.txt. If there isnt a requirements.txt file it will skip the package installation step. 

How to use 
- Open a terminal and navigate to the directory where the script lives
- Execute the script from the command line and add the directory path you'd like to create the virtual environment in. 

  python3 Venv_Setup.py <directorypath>
  
example:
dangray@Dans-MBP Venv_Setup % python3 Venv_Setup.py /Users/dangray/Repos/Python/Scripts/TestProject

If the set up was complete it will prompt you the it was complete and instruct you on how to activate the virtual envrionment for development. (See message below)

'Setup complete. You can activate the virtual environment by running:
source /Users/dangray/Repos/Python/Scripts/TestProject/venv/bin/activate'


***Notes**
- You can change your version of python based on the base default version you are using or by passing in a different version when calling the script.
example:
python3.12 Venv_Setup.py <directorypath> 
