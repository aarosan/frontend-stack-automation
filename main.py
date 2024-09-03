import sys
import os
import subprocess

#Replace with the full direct path to the server template
source_dir = "/frontend-stack-automation/templates/server"

def run_script(script_name, project_name, source):
    try:
        subprocess.run(["python3", script_name, project_name, source], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 main.py [MERN/MEVN/MEAN] [project_name]")
        sys.exit(1)
    
    stack = sys.argv[1].upper()
    project_name = sys.argv[2]
    
    scripts = {
        "MERN": "mern.py",
        "MEVN": "mevn.py",
        "MEAN": "mean.py"
    }

    script_name = scripts.get(stack)

    if script_name:
        run_script(script_name, project_name, source_dir)
    else:
        print("Invalid stack name. Please choose MERN, MEVN or MEAN.")
        sys.exit(1)

if __name__ == "__main__":
    main()
    