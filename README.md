# Repo Docker File Scanner Script

this python script scans a github repositry and returns all of the docker file
inside  this list

# Configuration
1. Create access token for github to access it api
2. Set the token as env using the command
```
export ACCESS_TOKEN=<your acces token>
```
3. Install the requirments with
```
pip install -r requirements.txt
```

## Ideas to improve this tool
- Make find all sort of files by extenstion (.yaml,.tf,providers.tf ...etc)
- Make it a cli instead of a script
- create a docker image for running this tool (benfit is no need to install dependencies locally)