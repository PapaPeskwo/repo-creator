# This is meant to be added as an alias in your bash or zsh config.abs
# When you run the alias, it will create a repo from the directory you're in.abs

import os
import subprocess
from datetime import datetime
from github import Github
from dotenv import load_dotenv
import argparse
import webbrowser

load_dotenv()

def repo_exists(user, repo_name):
    try:
        user.get_repo(repo_name)
        return True
    except:
        return False

def git_commands(directory, commit_message, private, use_ssh):
    os.chdir(directory)

    if os.path.exists('.git'):
        print("A .git directory is already present in this directory.")
        try:
            upstream_url = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url'])
            upstream_url = upstream_url.decode('utf-8').strip()
            print(f"The .git in this directory points to the following upstream: {upstream_url}")
        except subprocess.CalledProcessError:
            print("Failed to retrieve upstream information.")
        exit()

    if not any(os.listdir(directory)) or os.listdir(directory) == ['..git']:
        readme_path = os.path.join(directory, 'README.md')
        project_name = os.path.basename(directory)
        with open(readme_path, 'w') as readme:
            readme.write(project_name)
        print("Created README.md in empty directory.")

    commands = [
        'git init',
        'git add .',
        f'git commit -m "{commit_message}"'
    ]
    
    for cmd in commands:
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        process.communicate()

    token = os.getenv('YOUR_GITHUB_PERSONAL_ACCESS_TOKEN')
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

def create_and_push_repo():
    try:
        directory = os.getcwd()
        token = os.getenv('YOUR_GITHUB_PERSONAL_ACCESS_TOKEN')
        github = Github(token)
        user = github.get_user()
        repo_name = os.path.basename(directory)

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

        open_in_browser = input("Do you want to open the repository in your browser? [Y/n]: ").strip().lower()
        if open_in_browser == 'y':
            repo_url = f'https://github.com/{user.login}/{repo_name}'
            webbrowser.open(repo_url)

    except KeyboardInterrupt:
        print("\nOperation interrupted by user. Exiting...")
        exit()

if __name__ == "__main__":
    create_and_push_repo()
