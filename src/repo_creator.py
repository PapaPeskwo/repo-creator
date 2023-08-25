import os
import subprocess
from datetime import datetime
from github import Github
from dotenv import load_dotenv
import argparse

# Load environment variables from .env
load_dotenv()

def repo_exists(user, repo_name):
    try:
        user.get_repo(repo_name)
        return True
    except:
        return False

def git_commands(directory, commit_message, private, use_ssh):
    os.chdir(directory)
    commands = [
        'git init',
        'git add .',
        f'git commit -m "{commit_message}"'
    ]
    
    for cmd in commands:
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        process.communicate()

    # Use PyGithub to create a repo on GitHub
    token = os.getenv('YOUR_GITHUB_PERSONAL_ACCESS_TOKEN')  # Retrieve token from environment variable
    if not token:
        raise ValueError("GitHub token not found in .env file")
    github = Github(token)
    user = github.get_user()

    repo_name = os.path.basename(directory)
    repo = user.create_repo(repo_name, private=private)
    
    if use_ssh:
        remote_url = f'git@github.com:{user.login}/{repo_name}.git'
    else:
        remote_url = f'https://github.com/{user.login}/{repo_name}.git'
    
    commands_after_repo_creation = [
        f'git remote add origin {remote_url}',
        'git branch -M master',
        'git push -u origin master'
    ]

    for cmd in commands_after_repo_creation:
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        process.communicate()

def create_and_push_repo(use_tk):
    try:
        directory = None
        if use_tk:
            import tkinter as tk
            from tkinter import filedialog
            root = tk.Tk()
            root.withdraw()  # Hide the root window
            directory = filedialog.askdirectory(title="Select Folder")
            root.quit()  # Terminate the Tkinter main loop
        else:
            directory = os.path.normpath(input("Please enter the path to the folder: "))

        if not directory:
            return

        token = os.getenv('YOUR_GITHUB_PERSONAL_ACCESS_TOKEN')
        github = Github(token)
        user = github.get_user()
        repo_name = os.path.basename(directory)

        # Check if repo already exists
        if repo_exists(user, repo_name):
            print(f"Repository '{repo_name}' already exists on GitHub. Exiting...")
            exit()

        public_response = input("Do you want the repository to be public? [y/N]: ").strip() or "n"
        public = public_response.lower() == 'y'

        ssh_response = input("Do you want to use SSH (instead of HTTPS) to push to GitHub? [y/N]: ").strip() or "n"
        use_ssh = ssh_response.lower() == 'y'

        commit_message = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        git_commands(directory, commit_message, private=not public, use_ssh=use_ssh)
        print("Repository created and pushed!")

    except KeyboardInterrupt:
        print("\nOperation interrupted by user. Exiting...")
        exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GitHub Repo Upstreamer")
    parser.add_argument("-tk", action="store_true", help="Use tkinter for file dialog")

    args = parser.parse_args()
    create_and_push_repo(args.tk)