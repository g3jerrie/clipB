# 
#   clipB
#
#   @g3jerrie
#

from flask import Flask, request, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/", methods=["GET", "POST"])
def clipboard():
    global clipboard_content
    clipboard_content = ""  # Ensure this variable is initialized
    if request.method == "POST":
        clipboard_content = request.form["content"]
        socketio.emit("update", clipboard_content)  # Send real-time update
    return render_template("index.html", content=clipboard_content)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
