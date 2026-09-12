import yaml
import subprocess

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

#calls the respective access script as a subfunction to grant access
def grantAccess(platform, email):
    result = subprocess.run(["python", platform + ".py", email], capture_output=True, text=True)
    print("Output:", result.stdout.strip())
    print("Exit Code:", result.returncode)

if __name__ == '__main__':
    #starting with hardcoded values for now
    name: str = "Joe Schmoe"
    email: str = "joe.schmoe@email.com"
    role: str = "general"
    platform: str = "github"

    #makes a file object called stream
    stream = open("roles.yaml", 'r')

    #loads what's in the yaml file into a dictionary called roleList
    roleList: dict = yaml.safe_load(stream)

    #print what roleList contains
    for key, value in roleList.items():
        #prints role : [list with respective accesses in string format]
        print (key + " : " + str(value))

    grantAccess(platform, email)


