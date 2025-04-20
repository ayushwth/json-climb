import os
import subprocess
from datetime import datetime, timedelta

# Function to execute git commands
def execute_git_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode()}")

# Function to create a dummy change
def make_dummy_change():
    with open("dummy_file.txt", "a") as file:
        # Add a line with the current date to simulate a change
        file.write(f"Change made on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# Function to commit the change
def commit_changes():
    # Add the file changes
    execute_git_command("git add .")

    # Commit the changes
    commit_message = f"Dummy commit {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    execute_git_command(f'git commit -m "{commit_message}"')

    # Push the changes to the remote repository
    execute_git_command("git push origin main")

# Function to simulate a past commit (by adjusting the commit date)
def commit_in_past():
    # Generate a date 1-7 days ago to fill past squares
    past_date = datetime.now() - timedelta(days=7)
    commit_message = f"Commit from {past_date.strftime('%Y-%m-%d')}"

    # Make a dummy change
    make_dummy_change()

    # Amend commit with the past date
    # Using 'set' to set the environment variable on Windows
    set_env_command = f'set GIT_COMMITTER_DATE={past_date} && git add . && git commit --amend --no-edit --date "{past_date}"'

    # Execute the amended commit command
    execute_git_command(set_env_command)

    # Push the changes
    execute_git_command("git push origin main --force")

if __name__ == "__main__":
    # Optionally choose between committing normally or simulating past commits
    choice = input("Do you want to commit in the past (yes/no)? ").strip().lower()
    if choice == "yes":
        commit_in_past()
    else:
        make_dummy_change()
        commit_changes()
