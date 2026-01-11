from flask import Flask, render_template, request, jsonify
import datetime
import webbrowser
import os

app = Flask(__name__)

def process_command(command):
    command = command.lower()

    if "time" in command:
        return datetime.datetime.now().strftime("The time is %I:%M %p")

    elif "date" in command:
        return datetime.datetime.now().strftime("Today is %d %B %Y")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    elif "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad"

    elif "hello" in command:
        return "Hello! How can I help you?"

    elif "stop" in command or "exit" in command:
        return "Goodbye!"

    else:
        return "Sorry, I don't understand that command."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/command", methods=["POST"])
def command():
    data = request.json
    user_command = data.get("command", "")
    response = process_command(user_command)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
