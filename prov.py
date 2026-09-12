import yaml
import subprocess
import sys

from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

#calls the respective access script as a subfunction to grant access
def grantAccess(platform, email):
    result = subprocess.run(["python", platform + ".py", email], capture_output=True, text=True)
    print("Output:", result.stdout.strip())
    print("Error:", result.stderr.strip())
    print("Exit Code:", result.returncode)


#pull args from cmd
name: str = sys.argv[1]
email: str = sys.argv[2]
role: str = sys.argv[3]

#makes a file object called stream
stream = open("roles.yaml", 'r')

#loads what's in the yaml file into a dictionary called roleList
roleList: dict = yaml.safe_load(stream)

#print what user is going to be granted access to and provisions said access
print(name + " is about to receive access to:")
accessList: list = roleList.get(role)
for access in accessList:
    print(access)
    grantAccess(access, email)


