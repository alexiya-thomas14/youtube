import pytube
link = "https://youtu.be/ZdA1Il2CRTc"
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()