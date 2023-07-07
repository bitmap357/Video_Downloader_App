from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *


def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download():
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    mp4 = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)
    video_clip.close()


root = Tk()
root. title('Video Downloader')
canvas = Canvas(root, width=400, height=300)
canvas.pack()


# App Label
app_label = Label(root, text="Video Downloader", fg="blue", font=('Ariel', 20))
canvas.create_window(200, 20, window=app_label)

# Entry to accept Video url
url_label = Label(root, text='Enter video url')
url_entry = Entry(root)
canvas.create_window(200, 80, window=url_label)
canvas.create_window(200, 100, window=url_entry)

# Path to download videos
path_label = Label(root, text='Select path to download')
path_button = Button(root, text='Select', command=get_path)
canvas.create_window(200, 150, window=path_label)
canvas.create_window(200, 170, window=path_button)

# Download button
download_button = Button(root, text='Download', command=download)
canvas.create_window(200, 250, window=download_button)


root.mainloop()
