# request-forwarder
A lightweight Python application that forwards incoming GET requests to a specified target server and runs silently in the system tray.

## Installation
Install the required Python packages:

`pip install flask requests pystray pillow`

Replace _TARGET_SERVER_URL_ with the actual URL you want to forward requests to.

## Usage

`python request-forwarder.py`

> On Windows OS: use _pythonw.exe_ instead of _python_ for running without console window 

For example, if your TARGET_SERVER_URL is https://api.example.com/data and you make a request like:

`http://localhost:5000/forward?param1=value1&param2=value2p`

The application will forward a GET request to:

`https://api.example.com/data?param1=value1&param2=value2`

And return the response from https://api.example.com/data to your original request.
