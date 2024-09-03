# Frontend Stack Automation

This project automates the setup of frontend projects using popular tech stacks: MERN, MEVN, and MEAN. It helps developers quickly scaffold a full-stack web application by generating both server and client components tailored to the selected stack.

## Features

- **MERN Stack:** MongoDB, Express.js, React.js, Node.js
- **MEVN Stack:** MongoDB, Express.js, Vue.js, Node.js
- **MEAN Stack:** MongoDB, Express.js, Angular, Node.js
- Automated project setup with customizable configurations
- Installs dependencies and sets up basic project structure

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- Node.js and npm
- `npx` (included with npm)
- Angular CLI (for MEAN stack)

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/frontend-stack-automation.git
cd frontend-stack-automation
```

### Create Virtual Environment (Mac)

```bash
cd /path/to/frontend-stack-automation
python3 -m venv env
source env/bin/activate
```

### Install Python Dependencies (if any are required)

```bash
pip install -r requirements.txt
```

## Usage

To generate a new project, run the main.py script with the desired stack and project name:

```bash
python3 main.py [STACK] [PROJECT_NAME]
```

Replace [STACK] with one of the following:

MERN for MongoDB, Express.js, React.js, Node.js
MEVN for MongoDB, Express.js, Vue.js, Node.js
MEAN for MongoDB, Express.js, Angular, Node.js
Replace [PROJECT_NAME] with your desired project name.

### Example

To create a new MERN stack project named my-mern-app:


```bash
python3 main.py MERN my-mern-app
```

This command will create a project structure with a server and client directory, install the necessary dependencies, and set up the project for you.

## Project Structure

After running the script, your project will have the following structure:

```bash
my-mern-app/
│
├── client/      # Frontend application (React, Vue, or Angular)
│
├── server/      # Backend application (Express.js)
│
└── package.json # Root package.json with start script
```

## Running the Project

Once the project is set up, you can start both the client and server with a single command:

```bash
cd my-mern-app
npm start
```

This will run the frontend and backend concurrently.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.