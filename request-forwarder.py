import os
import sys
import threading
import requests
from flask import Flask, request
from pystray import Icon, MenuItem
from PIL import Image, ImageDraw

# Initialize Flask app
app = Flask(__name__)

# The URL of the server to which we will forward the GET request
TARGET_SERVER_URL = "https://httpbin.org/get"  # Replace with the target URL

# Flask route to handle incoming GET requests
@app.route("/forward", methods=["GET"])
def forward_request():
    # Get the query parameters from the incoming GET request
    params = request.args
    
    # Forward the parameters to another server (TARGET_SERVER_URL)
    response = requests.get(TARGET_SERVER_URL, params=params)
    
    # Return the response from the target server
    return response.text, response.status_code

# Function to create a system tray icon
def create_tray_icon():
    # Create a simple image for the tray icon
    image = Image.new("RGB", (64, 64), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.rectangle([0, 0, 64, 64], fill="#b20000")
    
    # Define the tray icon menu actions
    def on_quit(icon, item):
        icon.stop()  # Stop the tray icon

    # Define the tray icon menu
    menu = (MenuItem("Quit", on_quit),)
    
    # Create the icon
    icon = Icon("test_icon", image, menu=menu)
    icon.run()

# Function to start Flask in a separate thread
def start_flask():
    app.run(host="localhost", port=5000)

# Main function
def main():
    # Start Flask server in a separate thread
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Start the system tray icon
    create_tray_icon()

if __name__ == "__main__":
    main()
