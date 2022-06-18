from pytube import YouTube

link = input("Link: ")
directory = input("Kaydedilecek Dosya: ")
import os

try:
    yt = YouTube(link)
except:
    print("Link geçersiz!")
    exit()

mp3 = yt.streams.filter(only_audio=True).first()

print("İndiriliyor...")

output = mp3.download(directory)

base, ext = os.path.splitext(output)
to_mp3 = base + ".mp3"
os.rename(output, to_mp3)

print("İndirme başarıyla tamamlandı Sametcim!")
