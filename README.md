# Description

The GitHub Repo Upstreamer is a Python script that allows users to easily initialize, commit, and push a directory to GitHub, all with the convenience of a GUI interface. The script makes use of the tkinter library to present a simple GUI for the user to select a folder, and then decide whether the repository should be public or private.

# Setup and Installation
1. Clone or download this repository to your local machine.
2. Navigate to the project directory.
3. Install the necessary packages:

```bash
pip install tkinter pygithub python-dotenv
```

4. There is a .env.template file provided in the root directory. Rename this file to .env.

5. Open the .env file and replace your_actual_token_here with your GitHub Personal Access Token in the YOUR_GITHUB_PERSONAL_ACCESS_TOKEN field.

```env
YOUR_GITHUB_PERSONAL_ACCESS_TOKEN=your_actual_token_here
```
Note: Make sure you have sufficient permissions enabled in the GitHub token, especially repo-related scopes.

6. Save and close the .env file.

# Usage

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

# Caution

Handle your personal access token with care. It provides access to your GitHub account, and leaking it can compromise your repositories. Always store it in a secure place and avoid committing it to any public repository. Ensure that the .env file is added to your .gitignore to prevent unintentional pushes.

# Contribute

Feel free to fork this repository, make changes, and submit pull requests. Feedback and contributions are always welcome!
