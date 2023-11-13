import subprocess
from os import environ
def check_sudo():
    return 'SUDP_USER' in environ
def install(command):
    try:
        subprocess.check_call(command,shell=True)
    except:
        print(f"couldn't install the package command:[{command}]")
if __name__ == "__main__":
    commands=["apt-get install -y nmap","go install https://github.com/tomnomnom/waybackurls@latest","apt-get install whatweb"]
    for command in commands:
        install(command)

