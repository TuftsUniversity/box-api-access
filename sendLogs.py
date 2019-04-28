################################################################################################
################################################################################################
########
########        Title:   	Send Logs
########		Author:		Henry Steele - Library Technology Services - Tufts University
########		Date:		February 2019
########
########	Purpose:
########		Connect to Box through a Box developers app and write to a target
########        directory on behalf of the previsouly created Box dev app user
########
########
########    Edit script:
########
########    change the parameters in the commented sections below
########        - add user ID for non-human Box API user created with connectToBox-GetLogin.py
########        - add target folder ID from Box for folder you're writing to
########
########    Input:
########        - 1st argument to command:  file you want to send to Box, with relative path
########            + e.g. "python sendLogs.py input/input.out"
########        - 2nd argument to command:  path of config file containing public and private key
########            + e.g. "python connectToBox-GetLogin.py config/config.json"
########
########
########	Requirements:
########		- A Box developer's account for your institution
########		- Box app in dev console, with public and private key
########		- Box admin to approve app
########		- a folder you want to write to in Box.  Could be a shared folder
########		- a directory structure containing the following in the same
########		  directory as this script:
########			+config (public and private key)
########        - user ID of the non-human app user created in  connectToBox-GetLogin.py
########        - target Box folderID, to which the user created in connectToBox-GetLogin.py
########          has been added as an editor or collaborator.  Add user by email.
########          Target folder ID is the end of the URL when you are inside that folder
########          in the Box interface
########
########    Output:
########        - input file writes to specified Box directory
########        - see comments in code below to enter folder ID of this folder
########
import json
import glob
import os
import sys

from boxsdk import JWTAuth
from boxsdk import Client


filename = str(sys.argv[1])

config = str(sys.argv[2])

filename.replace('\r\n', '')

config_file = open(config, "r")

resultString = config_file.read().replace('\n', '')
result = json.loads(resultString, strict=False)

app_auth = result['boxAppSettings']['appAuth']

box_settings = result['boxAppSettings']

print("\n\n\n" + json.dumps(result) + "\n\n\n")

sdk = JWTAuth(
    client_id = box_settings['clientID'],
    client_secret = box_settings['clientSecret'],
    enterprise_id = result['enterpriseID'],
	jwt_key_id = app_auth['publicKeyID'],
    rsa_private_key_data = app_auth['privateKey'],
    rsa_private_key_passphrase = app_auth['passphrase']
)

client = Client(sdk)

print("Client: " + str(client) + "\n")

current_user = client.user().get()


print ("Current user: " + str(current_user) + "\n")

##############################################################
##############################################################
########        Enter user ID of non-human app user here
########        (At end of URL in interface)
########

user = client.user(user_id='<ID of non-human app user>').get()

print("App user: " + str(user) + "\n")
app_user_sdk = JWTAuth(
    client_id = box_settings['clientID'],
    client_secret = box_settings['clientSecret'],
	enterprise_id = result['enterpriseID'],
	user = user,   #this is the app user I create one time in previous script
	jwt_key_id = app_auth['publicKeyID'],
    rsa_private_key_data = app_auth['privateKey'],
    rsa_private_key_passphrase = app_auth['passphrase']
)

app_user_sdk.authenticate_user()

client = Client(app_user_sdk)

##############################################################
##############################################################
########        Enter Box ID of target folder here
########        (At end of URL in interface)
########
parent_id = <ID of target Box folder>

uploaded_file = client.folder(folder_id=parent_id).upload(filename)


print("\n\n\n" + str(uploaded_file) + "\n\n\n")

sys.exit()
