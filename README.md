# box-api-access
<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.


Use the Box API to manage files in Box
**Title:**      Send Logs

**Author:** Henry Steele - Library Technology Services - Tufts University

**Date:**    February 2019

**Requirements:**

- A Box developer&#39;s account for your institution
- Box app in dev console, with public and private key
- Box admin to approve app
- a folder you want to write to in Box.  Could be a shared folder
- config (public and private key)
- see word document for how to set this up



**Steps:**

**1 - Create Box admin user:**

  Only need to run this script once to set up user.

  **Edit script:**

  change the parameters in the commented sections below

  - add a username for the Box Dev app user.  This can be the same as the app name from the Box dev console

  **Command:**

  - **Before** you run this the first time, you can install the requirements by running the following pip command:
    - pip install –r requirements.txt
  - 1st argument to command is the location of the JSON config file from the Box app.  You would have downloaded this from the Box dev console within your app
    - python connectToBox-GetLogin.py \<config/config.json\>

  **Output:**

   - outputs credentials for non-human user that can write and
   - read on behalf of your Box developer app

**2-send files**

  **Edit script:**

  change the parameters in the commented sections below

  - add user ID for non-human Box API user created with connectToBox-GetLogin.py  
  - add target folder ID from Box for folder you&#39;re writing to

 **Command:**

   - 1st argument to command:  file you want to send to Box, with relative path
   - 2nd argument to command:  path of config file containing public and private key
   - python sendLogs.py input/input.out config/config.json

   **Requirements:**

   - A Box developer&#39;s account for your institution
   - Box app in dev console, with public and private key
   - Box admin to approve app
   - a folder you want to write to in Box.  Could be a shared folder
   - config file with public and private key from your app in Box developer cons (public and private key)
   - user ID of the non-human app user created in  connectToBox-GetLogin.py
   - target Box folderID, to which the user created in connectToBox-GetLogin.py has been added as an editor or collaborator.  Add user by email.
   - Target folder ID is the end of the URL when you are inside that folder in the Box interface

**CRON and shell script:**

- I've provided an example of a shell script you can wrap the (second) Python script in, so this can be invoked with a CRON job, although this setup is beyond the scope of this document.

   **Output:**

   - input file writes to specified Box directory
   - see comments in code below to enter folder ID of this folder
   - see comments in code below to enter folder ID of this folder

