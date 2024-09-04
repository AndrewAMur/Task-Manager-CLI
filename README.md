# Task Manager CLI

Task Manager CLI is a command-line tool for managing tasks efficiently, built using Python. It allows users to add, list, and remove tasks, with options for setting due dates and task repetition.

## Features

- **Add Tasks**: Create tasks with an optional due date and repetition frequency (Daily, Weekly, Monthly).
- **List Tasks**: View all your tasks, along with their status, due dates, and repetition settings.
- **Remove Tasks**: Easily delete tasks you no longer need.

## Installation

### Prerequisites

- Python 3.6 or higher
- Virtual environment (optional but recommended)

### Setup

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd task-manager-cli
   ```

2. **Create and activate a virtual environment** (optional):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the task manager**:

   ```bash
   python main.py
   ```

## Usage

Once the script is running, you can manage your tasks with the following options:

- **List tasks**: View your current tasks.
- **Add a task**: Create a new task with optional due date and repetition.
- **Remove a task**: Delete a task from your list.
- **Quit**: Exit the task manager.

## File Structure

- **LICENSE**: MIT License file.
- **main.py**: Main script for the task manager.
- **requirements.txt**: List of Python dependencies.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
