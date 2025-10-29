import subprocess

# Runs the command "netsh wlan show profiles" and returns the output
# text - converts the output from bytes to string
# capture_output - captures the output so it is not directly displayed in terminal so we can parse it (it is in output.stdout)
output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)
