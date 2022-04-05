import os
import shutil
import subprocess

# deleting __pycache__ folder
for root, subdirs, files in os.walk('.'):
    for d in subdirs:
        if d == "__pycache__":
            shutil.rmtree(os.path.join(root, d))

# checking if the directory oldist 
# exist or not.
if not os.path.isdir("oldist"):
    
    # if the oldist directory is 
    # not present then create it.
    os.makedirs("oldist")
# checking if the directory dist 
# exist or not.


if not os.path.isdir("dist"):
    
    # if the dist directory is 
    # not present then create it.
    os.makedirs("dist")


source_dir = 'dist'
target_dir = 'oldist'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), os.path.join(target_dir, file_name))

def runner(cmd):
    completed = subprocess.run(["powershell", "-Command ", cmd], capture_output=True)
    return completed

def command_handler(command):
    info = runner(command)
    if info.returncode != 0:
        print("An error occured: %s", info.stderr)
    else:
        print(command + " command executed successfully!")
    
    print("-------------------------")

if __name__ == '__main__':
    
    with open("cred.config", "r") as f:
        content = f.read()
        config = eval(content)
    
    command_handler("py -m pip install --upgrade pip")
    command_handler("py -m pip install --upgrade build")
    command_handler("py -m pip install --upgrade wheel")
    command_handler("py -m pip install --upgrade twine")
    command_handler("py -m pip install --upgrade setuptools")
    command_handler("py -m build")
    command_handler("py -m twine upload --skip-existing --repository pypi dist/* -u " + config["username"] + " -p " + config["password"])
    
    

    