# MediBlog
    TThis is a Meditech Blog Web App that allows developers to discuss certain topics.
    With MediBlog, you can write and describe any challenge you are facing.
    Colleagues and other users can comment and provide insight into your challenges.
    Although this is only a basic website, we want to improve it over time.


## How to Install and Run the Project
- On your machine, download and install git: https://desktop.github.com/
- Download and install Python3: https://www.python.org/downloads/
- Run this command to install dependencies: `pip install -r requirements.txt`
- If the above command fails, run: `python3 -m pip install -r requirements.txt`
- Download MediBlog, Open github and run: `git clone git@github.com:MEDITECH-SA/summit-demo.git` Check the next step if you don't have access.

## Generating SSH key for access
- Create ssh key: `ssh-keygen -t ed25519 -C "email@meditech.ac.za"`
- you will be promped to enter file in which to save the key eg -> (/c/Users/username/.ssh/id_ed25519): `just press enter for default`
- follow the steps, and press enter if you want it to be default
- Check if the agent is running: `eval "$(ssh-agent -s)"`
- If you have used the default file, run: `ssh-add ~/.ssh/id_ed25519`
- Copy your ssh public key and paste on on git: `https://github.com/settings/keys`
- Your keys should look like this" `SHA256:kjfDkLdlkHdlkslJdsdGWpP` 'Note this wont work'

## How to run the APP on windows OS
- set FLASK_APP=app
- flask run -p 5005 / pyhon3 -m flask run -p 5005

## How to run the APP on Linux OS
- export FLASK_APP=app
- flask run -p 5005
