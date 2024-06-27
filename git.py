import subprocess

subprocess.run(["git", "init"])
subprocess.run(["git", "remote", "add", "origin", "https://dev.azure.com/slb-swt/psuite/_git/pts-deployment-manifes"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "checkout", "-b", "deployment_history"])
subprocess.run(["git", "commit", "-m", "Automated file transfer from Azure Blob Storage"])
subprocess.run(["git", "push", "-u", "origin", "deployment_history"])