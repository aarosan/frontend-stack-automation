import sys
import os
import subprocess
import json
import shutil

def initialize_root_package_json(destination):
    try:
        # Initialize package.json
        subprocess.run(["npm", "init", "-y"], cwd=destination, check=True)
        print(f"Initialized package.json in '{destination}' successfully.")
        
        #Install concurrently
        subprocess.run(["npm", "install", "concurrently", "--save-dev"], cwd=destination, check=True)
        print(f"Installed concurrently in '{destination}' successfully.")

        # Modify package.json to add start script
        package_json_path = os.path.join(destination, "package.json")
        with open(package_json_path, "r") as file:
            package_json = json.load(file)

        # Ensure the scripts field exists
        if "scripts" not in package_json:
            package_json["scripts"] = {}
        
        package_json["scripts"]["start"] = "concurrently \"cd server && npm start\" \"cd client && npm start\""
        
        with open(package_json_path, "w") as file:
            json.dump(package_json, file, indent=2)
        
        print("Added start script to package.json successfully.")

    except Exception as e:
        print(f"An error occurred while initializing or updating package.json: {e}")

def create_server(source, destination):
    # Create the server directory path
    server_destination = os.path.join(destination, "server")

    if not os.path.exists(source):
        print(f"Source directory '{source}' does not exist.")
        return

    # Create the server directory
    os.makedirs(server_destination, exist_ok=True)

    try:
        shutil.copytree(source, server_destination, dirs_exist_ok=True)
        print(f"Copied directory from '{source}' to '{server_destination}' successfully.")
    except Exception as e:
        print(f"An error occurred while copying: {e}")
        return

    try:
        subprocess.run(["npm", "init", "-y"], cwd=server_destination, check=True)
        print(f"Initialized package.json in '{server_destination}' successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while initializing package.json in server: {e}")

    try:
        subprocess.run(["npm", "install"], cwd=server_destination, check=True)
        print(f"Ran 'npm install' successfully in '{server_destination}'.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running 'npm install': {e}")

def create_client(destination):
    client_destination = os.path.join(destination, "client")

    # Create React App
    try:
        subprocess.run(["npx", "create-react-app", client_destination], check=True)
        print(f"Created React app successfully in '{client_destination}'.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while creating the React app: {e}")
        return

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 mern.py [project_name] [source_directory]")
        sys.exit(1)
    
    project_name = sys.argv[1]
    source = sys.argv[2]

    # Define where the project will be created
    # os.getcwd() returns the current working directory
    # os.path.join() joins the current working directory with the project name
    destination_dir = os.path.join(os.getcwd(), project_name)

    # Create the project directory
    os.makedirs(destination_dir, exist_ok=True)

    initialize_root_package_json(destination_dir)
    create_server(source, destination_dir)
    create_client(destination_dir)