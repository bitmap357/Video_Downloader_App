from tkinter import *
from tkinter import filedialog


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


root.mainloop()
