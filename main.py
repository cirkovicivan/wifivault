#!/usr/bin/env python3

import subprocess

print("wifi-password-extractor \n")

# Runs the command "netsh wlan show profiles" and returns the output
# text - converts the output from bytes to string
# capture_output - captures the output so it is not directly displayed in terminal so we can parse it (it is in output.stdout)
output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)

SSID = []

# Splits the output into lines and from each line extracts the SSID
for line in output.stdout.splitlines():
    if "All User Profile" in line:
        SSID.append(line.split(":")[1].strip())

details = [] 

# get the details for each SSID
for name in SSID:
    details.append(subprocess.run(["netsh", "wlan", "show", "profile", "name=" + name, "key=clear"], capture_output=True, text=True))

# Extract the password from the output and display it to user
# enumerate - pairs each item in the list with its index 
for index, item in enumerate(details):
    for line in item.stdout.splitlines():
        if "Key Content" in line:
            print("SSID: " + SSID[index] + "\nPassword: " + line.split(":")[1].strip()+"\n")

input("Press enter to exit...")