import sys
import requests

#take platform and email from passed args
platform: str = sys.argv[0].removesuffix(".py")
email: str = sys.argv[1]

#initialize variables
token: str = ""
userrepo: str = ""
targetUser: str = ""


#loads .env and finds relevant token and repo
with open(".env", 'r') as envTokens:
    for line in envTokens:
        current: str = line.strip()
        if current.startswith(platform + "="):
            token = current.removeprefix(platform + "=")
        if current.startswith("github_userrepo"):
            userrepo = current.removeprefix("github_userrepo=")


#find targetUser based on email, returns login
def findUser(email):

    headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2026-03-10',
    }

    #gets the response from GitHub as a json
    response = requests.get('https://api.github.com/search/users?q=' + email, headers=headers).json()

    #items from response has login nested in a list and then another dict
    targetUser = response.get("items")[0].get("login")

    return targetUser

#send request to add to repo
def addUser(targetUser):
    #adds the token to the Auth Bearer header
    concatTokenBearer: str = "Bearer " + token 

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': concatTokenBearer,
        'X-GitHub-Api-Version': '2026-03-10',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = '{"permission":"triage"}'

    #gets the response from GitHub as a json
    response = requests.put('https://api.github.com/repos/' +
                            userrepo +
                            '/collaborators/' +
                            targetUser, headers=headers, data=data).json()

    return response

#main actions
targetUser = findUser(email)
result = addUser(targetUser)
print(result)

