# YouTube Downloader
This is a simple web application that I built using Flask and Pytube
to easily download YouTube videos or extract their audio.
for this we need only to paste or write link of our downloading or video/audio.
for this project i used vs code to run this project, i used live server extension 
for running this project on server. this project contains two files 
1) html file for front end
2) python or app file for backend
firstly we need to install putube and flask
for that type in command prompt:pip install Flask pytube

# how to download video
Paste the YouTube video URL into the input field.

Select either "Download Audio Only" or "Download Video".

Click the "Start Download" button.

# some main code explaination or working

firstly we need to import our libraries such as
from flask import Flask, render_template, request
from pytube import YouTube
import os

from flask import Flask, render_template, request: These lines import necessary modules from the Flask framework.

Flask: The main class to create your web application instance.
render_template: Used to render HTML files (like index.html) and send them as responses.
request: An object that holds data about the incoming request, such as form data submitted by the user.
from pytube import YouTube: This imports the YouTube class from the Pytube library, which is used to interact with YouTube videos.

import os: This imports the os module, providing functions for interacting with the operating system, particularly for creating directories.

app = Flask(__name__, template_folder='.'): This creates an instance of the Flask application. template_folder='.' 
tells Flask to look for HTML templates in the same directory as app.py.

@app.route('/'): This is a Flask decorator that associates the index() function with the root URL (/) of your application.

def download():: This function handles the actual download logic.

yt_url = request.form['youtube_url']: Retrieves the YouTube URL that the user entered into the text input field on the index.html form.

def download_audio(yt_url)::

yt = YouTube(yt_url): Creates a Pytube YouTube object from the provided URL.
stream = yt.streams.get_audio_only(): Gets the audio-only stream for the video.



