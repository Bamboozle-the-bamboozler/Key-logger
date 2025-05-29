# Python Educational Keylogger

**WARNING: This keylogger is for educational purposes only.  
Please don't use this software on any computer you do not own or do not have explicit permission to monitor.  
Unauthorized use is illegal and unethical.**

## What does this do?

This Python script logs keystrokes on your own computer and saves them to a text file (`keylog.txt`).  
It's designed for personal learning about how keyloggers work, and should only be run in a controlled, private environment.

## How to use

### Download the latest Python version (preferably as 3.10+)  

### 1. Install the module

This script uses the `pynput` library. Install it with: 

```
pip install pynput
```

### 2. Run the script
- Open up PowerShell and write:
```PowerShell
cd "C:\Users\*your username*\downloads" 

# press "enter" (\downloads if that's where your downloads go)

# after pressing "enter" write:

python keylogger.py
```

- The script will start logging keyboard input.
- Keystrokes are written to `keylog.txt`, which will eventually be auto-created in your downloads (or based on where your notepad usually saves). The keystrokes are logged every 10 seconds.


## **Ethics and Legality**

- **Never** use on someone else’s computer or without explicit consent.
- **Deleting or hiding** the presence of this script may be illegal and is not recommended.
- Use this code only for learning on your own machine.

## How does it work?

- Listens for key presses with `pynput`.
- Buffers the keystrokes and writes them to `keylog.txt` periodically.

## If it doesn't work:
- Make sure you downloaded Python with the option of enabling "PATH"; if you're unsure of whether you did or not, try to uninstall Python and reinstall it, in the setup, there's an option to add the download to the PATH.
- Upgrade pips and modules, and check if you're using the latest Python patch

## Deleting/stopping the script

 I haven't found a way to stop the script manually without deleting the files, so the only option I can give out for stopping the script would be deleting the files downloaded, and uninstalling the module downloaded (`pynput`):

```powershell
pip uninstall pynput
```
### !If the code is still running and logging your keys, check the Task Manager to see if python.exe is running. If it is, just kill the process to stop the script from running.

## Disclaimer

### You are solely responsible for any use or misuse of this code.
### !!I HAVE NOTHING TO DO WITH ANY MISUSE OR ANY DOWNSIDES DONE FROM EDITING THE .PY!!! 
### !!!THIS IS FOR EDUCATIONAL USE ONLY!!!
