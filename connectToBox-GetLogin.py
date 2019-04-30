################################################################################################
################################################################################################
########
########        Title:   	Connect to Box - Get login
########		Author:		Henry Steele - Library Technology Services - Tufts University
########		Date:		February 2019
########    
########    This work is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License. 
########    To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/4.0/ 
########    or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
########
########	Purpose:
########		Connect to the Box API using previsouly defined public and
########		private keys from a Box developers app, and create a user on
########		behalf of this app
########
########		Only need to run this script once to set up user.
########
########    Input:
########        - argument to command:  path of config file containing public and private key
######## 			+ e.g. "python connectToBox-GetLogin.py config/config.json"
########
########	Requirements:
########		- A Box developer's account for your institution
########		- Box app in dev console, with public and private key
########		- Box admin to approve app
########		- a folder you want to write to in Box.  Could be a shared folder
########		- a directory structure containing the following in the same
########		  directory as this script:
########			+config (public and private key)
########		- extra libraries
########			+ pip install boxsdk[jwt]
########
########	Output:
########		- outputs credentials for non-human user that can write and
########		  read on behalf of your Box developer app
########

import requests
import json
import os
import glob

from boxsdk import JWTAuth
from boxsdk import Client


config = str(sys.argv[1])

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

######################################################################
######################################################################
########	Enter a name for the app user.  This should match the
########	name of the app in the script is using from the
########	Box dev console

new_app_user = client.create_user('<name of app user>', login=None)

print(str(new_app_user) +"\n\n")



print("Current user login: " + str(new_app_user.login) + "\n\n")

print("Current user id:" + str(new_app_user.id) + "\n\n")

output_file = open("New App user login info.txt", "w+")

output_file.write("User credentials for accessing Box folders.  Add this user by email as a collaborator in the Box folder you want your app to have access to\n")

output_file.write("App user login: " + str(new_app_user.login) + "\n")

output_file.write("App user id:" + str(new_app_user.id) + "\n")

output_file.close()
