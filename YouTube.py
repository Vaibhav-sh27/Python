from pytube import YouTube  
import os

def Video():
	print("""\t\t\t Video Downloader \t\t\t\n""")
	h=yt.streams.filter(progressive=True)
	print("The available resolutions of video are: \n")
	for k in h:
		print(k)
	g=int(input("\nChoose the resolution of video --> "))
	
	try:
		h[g-1].download(SAVE_PATH)
		print("\nVideo downloaded !!")
	except:
		print("Some Error!")  

def Audio():
	print("""\t\t\t Audio Downloader \t\t\t\n""")
	h=yt.streams.filter(only_audio=True)
	print("The available bitrate of audio file are: \n")
	for k in h:
		print(k)
	g=int(input("\nChoose the bitrate of audio file --> "))
	
	try:
		file =h[g-1].download(SAVE_PATH)
		base, ext = os.path.splitext(file)
		new_file = base + '.mp3'
		os.rename(file, new_file)
		print("\nAudio file Downloaded!!")
	except:
		print("Some Error!")  

SAVE_PATH = "YouTube" 

link=input("Enter the link of YouTube Video--> ")

try:
	yt = YouTube(link)  
except:
	print("Connection Error") 

choice=input("""What action do you want to be done?
\t\t---> Download Video(V)
\t\t---> Download Audio(A)
\t\t---> Download Both(B)
----> """).upper()

if choice =="V":
	Video()
elif choice=="A":
	Audio()
elif choice=="B":
	Video()
	Audio()
else:
	print("invalid choice")

print('\nTask Completed!') 