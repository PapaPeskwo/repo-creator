# Description

The repo-creator is a Python script that allows users to easily initialize, commit, and push a directory to GitHub directly from your terminal.

# Setup and Installation
1. Clone or download this repository to your local machine.
2. Navigate to the project directory.
3. Install the necessary packages:

```bash
pip install -r requirements.txt
```

4. Rename the provided .env.template file in the root directory to .env.

5. Open the .env file and replace `your_actual_token_here` with your GitHub Personal Access Token in the `YOUR_GITHUB_PERSONAL_ACCESS_TOKEN` field.

```env
YOUR_GITHUB_PERSONAL_ACCESS_TOKEN=your_actual_token_here
```
Ensure to select the "repo" scope when creating your token.

6. Save and close the .env file.

# Usage

## Alias Mode
To use the script as an alias from any directory, add the following line to your `.bashrc`, `.zshrc`, or equivalent shell configuration file:

```bash
alias <your_alias_name>='python3 /path/to/cloned/repo/repo_creator.py --alias'
```
Then, source your shell configuration file to activate the alias:

```bash
source ~/.bashrc
```
Now, you can navigate to any directory you wish to create a repository for and use your alias directly. Adding the `--alias` flag removes the step where the script asks you to enter the directory folder to be pushed to Github.

## Normal Usage
To use the script in interactive mode, navigate to the cloned repository and execute:

```bash
python3 repo_creator.py
```
Follow the prompts to initialize, commit, and push your directory to GitHub.

## GUI Mode
To use the GUI functionality provided by `tkinter`, run the script with the `--tk` flag:

```bash
python3 repo_creator.py --tk
```
A GUI window will open, allowing you to select the directory you want to commit and push to GitHub through a user-friendly interface.

# Dependencies

- `tkinter` for the GUI.
- `PyGithub` to interact with the GitHub API.
- `python-dotenv` to load environment variables from the .env file.
