
from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__, template_folder='.') # Assuming index.html is in the same directory

# Specify the directory where you want to save the downloaded files
VIDEODOWNLOAD_DIR = 'c:/Users/princ/Videos'
MP3DOWNLOAD_DIR = 'c:/Users/princ/Music'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    yt_url = request.form['youtube_url']
    action = request.form.get('action') # Get the selected action (audio or video)

    if not yt_url:
        return "Error: YouTube URL is required.", 400

    try:
        if action == 'audio':
            download_audio(yt_url)
            return "Successfully extracted audio"
        elif action == 'video':
            download_video(yt_url)
            return "Successfully downloaded video"
        else:
            return "Error: Please select an action (audio or video).", 400
    except Exception as e:
        print(f"Error during download: {e}")
        return f"An error occurred: {e}", 500

def download_audio(yt_url):
    yt = YouTube(yt_url)
    stream = yt.streams.get_audio_only()
    # Ensure the directory exists
    os.makedirs(MP3DOWNLOAD_DIR, exist_ok=True)
    stream.download(output_path=MP3DOWNLOAD_DIR)
    print(f"Successfully extracted audio to {MP3DOWNLOAD_DIR}")

def download_video(yt_url):
    yt = YouTube(yt_url)
    stream = yt.streams.get_highest_resolution()
    # Ensure the directory exists
    os.makedirs(VIDEODOWNLOAD_DIR, exist_ok=True)
    stream.download(output_path=VIDEODOWNLOAD_DIR)
    print(f"Successfully downloaded video to {VIDEODOWNLOAD_DIR}")

if __name__ == '__main__':
    app.run(debug=True)