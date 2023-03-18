import requests
import os
import sys
from github import Github

# This script scans a github repos and saves the all the docker files from the repo to a dolder name docker_file

# Set your GitHub access token here or use an environment variable
access_token = os.environ.get("ACCESS_TOKEN")
if access_token is not None:
    access_token = access_token
else:
    print("Make sure to set and env ACCESS_TOKEN")
    sys.exit(0)

def save_into_file(repo,file_content):
     create_docker_files_folder("docker_files")
     if file_content.encoding == "base64":
        with open(f"docker_files/{file_content.name}-{repo.name}", "w") as f:
            print(f"Saving {file_content.name} From {repo.name}")
            f.write(file_content.decoded_content.decode("utf-8"))

def create_docker_files_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

g = Github(access_token)

for repo in g.get_user().get_repos():
    try:
        repo_content = repo.get_contents("")
        while repo_content:
            file_content = repo_content.pop(0)
            if file_content.type == "dir":
                repo_content.extend(repo.get_contents(file_content.path))
            else:
                file_name = file_content.name.lower()
                if "dockerfile" in file_name and file_name != ".dockerignore":
                    save_into_file(repo, file_content)
    except Exception as e:
            print(e)
            # usually it gets here beacuse the repository was empty
            print("Something else went wrong")



