from tkinter import *
from tkinter import filedialog , ttk
from pytube import YouTube

folder_name = ""

def openLocation():
    global folder_name
    folder_name = filedialog.askdirectory()
    if(len(folder_name)>1):
        locationError.config(text=folder_name,fg="blue")
    else:
        locationError.config(text="Please Choose Your Folder",fg="red")

def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()
    if (len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)
        
        if(choice==choices[0]):
            select = yt.streams.filter(progressive=True).first()
        elif (choice == choices [1]):
            select = yt.sreams.filter(progressive=True,file_extension='mp4').first()
        elif (choice == choices [2]):
             select = yt.sreams.filter(only_audio=True).first()
        else:
            ytdError.config(text="Put Your Link",fg="red")
    select.download(folder_name)
    ytdError.config(text="done donwload")

root =Tk()
ytdError = Label(root, text="",fg="red",font=("Tajawal",10))
root.title("Videos Downloader")
root.geometry("650x250+300+10")
root.resizable(False,False)
root.columnconfigure(0,weight=1)
f1=Frame(root,width=580,height=100,bg='whitesmoke',bd=3,relief=GROOVE)
# f1.place(x=30,y=230)
f2=Frame(root,width=580,height=55,bg='whitesmoke',bd=3,relief=GROOVE)
# f2.place(x=30,y=250)
# t = Label(root,text='Videos Downloader',bg='red',fg='white',font=("Tajawal",15,'bold'))
# t.pack(fill=X)
ytdLabel= Label(root,text='Put Your Link',font=("Tajawal",15,'bold'))
ytdLabel.pack()

ytdEntryVar =StringVar()
ytdEntry = Entry(root,width=70,justify='center',font=("Tajawal",15),fg='blue',textvariable=ytdEntryVar)
ytdEntry.pack()

saveLabel = Label(root,text="Choose Your Folder",bg="whitesmoke",font=('Tajawal',15,"bold"))
saveLabel.place(x=220,y=90)

saveEntry = Button(root,width=20,font=("Tajawal",12),bg="red",fg="white",text="path",command=openLocation)
saveEntry.place(x=220,y=120)

locationError =Label(root,text=" You Did Not Choose The Path ",bg="whitesmoke",font=('Tajawal',15,"bold"))
locationError.place(x=180,y=160)

# ytdquality = Label(root,text=" choose quality",bg="whitesmoke",font=('Tajawal',15,"bold"))
# ytdquality.place(x=430,y=255)

choices = ["720p","144p","only audio"]
ytdchoices = ttk.Combobox(root,values=choices)
# ytdchoices.place(x=260,y=200)

downloadbtn = Button(root,text="start downloading",width=20,font=("Tajawal",12),bg='red',fg="white",command=DownloadVideo)
downloadbtn.place(x=220,y=200)

root.mainloop()

