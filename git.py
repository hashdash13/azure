import subprocess

subprocess.run(["git", "init"])
subprocess.run(["git", "remote", "add", "origin", "https://github.com/hashdash13/azure.git"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "config", "--global", "credential.helper", "store"])
subprocess.run(["git", "checkout", "-b", "branch_name"])
subprocess.run(["git", "commit", "-m", "Automated file transfer from Azure Blob Storage"])
subprocess.run(["git", "push", "-u", "origin", "branch_name"])