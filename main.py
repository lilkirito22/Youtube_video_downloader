import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.filter(progressive=True, file_extension="mp4")
        video.get_highest_resolution().download()
    except Exception as e:
        finishedLabel.config(text="An error occurred")

    finishedLabel.config(text="Download finished")



# System settings

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#Our app frame

app= customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading

finishedLabel = customtkinter.CTkLabel(app, text="")
finishedLabel.pack(pady=10)


# Download button

download = customtkinter.CTkButton(app, text="Download", command=startDownload) 
download.pack(pady=10)

# Run app 
app.mainloop()