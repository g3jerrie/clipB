import os
import platform
import subprocess
import webbrowser
import time
import socket

def start_app():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Set up virtual environment
    subprocess.run(["python", "-m", "venv", "venv"])
    
    if platform.system() == "Windows":
        subprocess.run(["venv\\Scripts\\activate"], shell=True)
    else:
        subprocess.run(["source", "venv/bin/activate"], shell=True)

    subprocess.run(["pip", "install", "-r", "requirements.txt"])

    # Start the Flask app and store PID
    process = subprocess.Popen(["python", "clipB.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    with open("flask_pid.txt", "w") as f:
        f.write(str(process.pid))

    print(f"Flask app started with PID: {process.pid}")

    # Wait a moment to ensure the server starts
    time.sleep(3)

    # Open the web browser
    local_ip = socket.gethostbyname(socket.gethostname())
    url = f"http://{local_ip}:5000"
    webbrowser.open(url)

if __name__ == "__main__":
    start_app()
