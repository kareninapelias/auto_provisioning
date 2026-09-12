# auto_provisioning
when you're tired of giving people access manually

After cloning the repo for use:
- Configure roles.yaml with your roles and the accesses provisioned per role. "general" accesses will be provisioned to all users; roles after that will be provisioned depending on the role.
- Create your own .env file! You can refer to .env.example to see formatting for GitHub example.
- Make your own respective .py scripts for each platform that allows API invite requests.
- Syntax for calling prov.py: ./prov.py "name" "email" "role"