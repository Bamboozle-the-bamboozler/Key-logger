# Python Educational Keylogger

**WARNING: This keylogger is for educational purposes only.  
Please don't use this software on any computer you do not own or do not have explicit permission to monitor.  
Unauthorized use is illegal and unethical.**

## What does this do?

This Python script logs keystrokes on your own computer and saves them to a text file (`keylog.txt`).  
It's designed for personal learning about how keyloggers work, and should only be run in a controlled, private environment.

## How to use

### 1. Install the module

This script uses the `pynput` library. Install it with:

```
pip install pynput
```

### 2. Run the script
- Open up PowerShell and write:
```powershell
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

## Disclaimer

You are solely responsible for any use or misuse of this code.
!!I HAVE NOTHING TO DO WITH ANY MISUSE OR ANY DOWNSIDES DONE FROM EDITING THE .PY!!! 
!!!THIS IS FOR EDUCATIONAL USE ONLY!!!
