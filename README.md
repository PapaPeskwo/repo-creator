# Description

The repo-creator is a Python script that allows users to easily initialize, commit, and push a directory to GitHub directly from your terminal.

# Setup and Installation
1. Clone or download this repository to your local machine.
2. Navigate to the project directory.
3. Install the necessary packages:

```bash
pip install -r requirements.txt
```

4. There is a .env.template file provided in the root directory. Rename this file to .env.

5. Open the .env file and replace your_actual_token_here with your GitHub Personal Access Token in the YOUR_GITHUB_PERSONAL_ACCESS_TOKEN field.

```env
YOUR_GITHUB_PERSONAL_ACCESS_TOKEN=your_actual_token_here
```
Select the "repo" scope.

6. Save and close the .env file.

# Usage

## Alias
You can now run the code with an alias in your terminal. In your .bashrc or .zshrc (or wherever you store your aliases) add a line like this:
```bash
alias <your_alias_name>='python3 /path/to/cloned/repo/src/alias_repo_creator.py
```
Then source the location you added your alias to, for this example we'll use .bashrc:
```bash
source ~/.bashrc
```
Now you can cd into whichever directory you want and use your alias.

## Normal usage
1. Write:
```bash
python src/repo_creator.py -tk
```
2. Follow the steps. If you're on windows, you'll most likely want to push with HTTPS. Mac and Linux users use SSH.

## Use with a GUI

1. To use the GUI functionality provided by `tkinter`, run the script with the `-tk` flag:

```bash
python src/repo_creator.py -tk
```
1. A GUI window will appear with a button labeled "Create & Push Repository". Click on it.
2. A file dialog will appear, allowing you to select the directory you want to commit and push to GitHub.
3. After selecting a directory, a messagebox will prompt you to decide whether the repository should be public or private.
4. Click "Yes" for a public repository or "No" for a private one.
5. The script will then initialize a Git repository in the directory, commit its contents, create a new repository on GitHub, and then push the directory to that repository.
6. A confirmation messagebox will appear once the process is complete.

# Dependencies

- `tkinter` for the GUI
- `PyGithub` to interact with the GitHub API
- `python-dotenv` to load environment variables from the .env file

# Contribute

Feel free to fork this repository, make changes, and submit pull requests. Feedback and contributions are always welcome!
