import os
import signal

def stop_app():
    try:
        # Read PID from the file
        with open("flask_pid.txt", "r") as f:
            pid = int(f.read().strip())

        # Kill the Flask process
        os.kill(pid, signal.SIGTERM)
        print(f"Stopped Flask app running at PID: {pid}")

        # Remove the PID file
        os.remove("flask_pid.txt")

    except FileNotFoundError:
        print("Error: PID file not found. Is the Flask app running?")
    except ValueError:
        print("Error: Invalid PID in file.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    stop_app()
