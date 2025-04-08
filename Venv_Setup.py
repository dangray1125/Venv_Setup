import os
import subprocess
import sys

def create_virtualenv(project_path):
    """Create a virtual environment in the specified project directory."""
    venv_path = os.path.join(project_path, "venv")
    if not os.path.exists(venv_path):
        print(f"Creating virtual environment in {venv_path}...")
        subprocess.check_call([sys.executable, "-m", "venv", venv_path])
        print(f"Virtual environment '{venv_path}' created successfully.")
    else:
        print(f"Virtual environment already exists at {venv_path}.")

def install_requirements(project_path, requirements_file):
    """Install the required packages from the requirements.txt file into the virtual environment."""
    venv_path = os.path.join(project_path, "venv", "bin", "pip")
    
    if os.path.exists(requirements_file):
        print(f"Installing packages from {requirements_file}...")
        subprocess.check_call([venv_path, "install", "-r", requirements_file])
        print("Packages installed successfully.")
    else:
        print(f"Warning: {requirements_file} not found. Skipping package installation.")

def main():
    # Ensure that the project path is provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python setup_venv.py <project_path>")
        sys.exit(1)

    project_path = sys.argv[1]
    requirements_file = os.path.join(project_path, "requirements.txt")

    # Step 1: Create the virtual environment in the project directory
    create_virtualenv(project_path)

    # Step 2: Install packages from requirements.txt if it exists
    install_requirements(project_path, requirements_file)

    print(f"Setup complete. You can activate the virtual environment by running:\nsource {os.path.join(project_path, 'venv', 'bin', 'activate')}")

if __name__ == "__main__":
    main()
