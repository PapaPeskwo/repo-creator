import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
from datetime import datetime
from github import Github
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def git_commands(directory, commit_message, private):
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
    
    commands_after_repo_creation = [
        f'git remote add origin git@github.com:{user.login}/{repo_name}.git',
        'git branch -M master',
        'git push -u origin master'
    ]

    for cmd in commands_after_repo_creation:
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        process.communicate()

def create_and_push_repo():
    root.withdraw()  # Hide the root window
    directory = filedialog.askdirectory(title="Select Folder")

    if not directory:
        root.deiconify()  # Show the main window again
        return


    public = messagebox.askyesno("Repository Setting", "Do you want the repository to be public?")
    commit_message = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    git_commands(directory, commit_message, private=not public)
    messagebox.showinfo("Info", "Repository created and pushed!")
    root.quit()  # Terminate the Tkinter main loop

root = tk.Tk()
root.title("GitHub Repo Upstreamer")
root.geometry("300x150")

frame = tk.Frame(root)
frame.pack(pady=50)

btn = tk.Button(frame, text="Create & Push Repository", command=create_and_push_repo)
btn.pack()

root.mainloop()
