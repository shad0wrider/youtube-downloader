import os,time,json
import ytdownload
import ffmpeg as fpeg

vf = {}
print("===================================")
print("//Made with ❤️ by @ElectronPro")
print("===================================")

link = input("Enter youtube link: ")

namer = str(link.split("v=")[1])

check = ytdownload.downloader(link)

fg = open(check,"r")

reader = json.loads(fg.read())

fc = list(reader["video"].keys())

print("Video Format Avaliable",fc)

print("=======================")
print("Select Resolution to Download: ")
for i in range(len(fc)):
    vf[f"{i+1}."] = fc[i]

for keys,values in vf.items():
    print(keys,values)
print("========================")
resol = input("enter number to download: ")

selectedOption = vf[resol+"."]

if selectedOption =="720p":
    if "720p" in str(reader["audiovideo"]):
        finalink = str(reader["audiovideo"]["720p"]["url"])
        os.system("wget "+f'"{finalink}"'+" "+f"-O 720pvideo{namer}.mp4")

if selectedOption =="360p":
    if "360p" in str(reader["audiovideo"]):
        finalink = str(reader["audiovideo"]["360p"]["url"])
        os.system("wget "+f'"{finalink}"'+" "+f"-O 360pvideo{namer}.mp4")
else:
    if selectedOption in str(reader["audiovideo"]):
        finalink = str(reader["audiovideo"][f"{selectedOption}"]["url"])
        os.system("wget "+f'"{finalink}"'+" "+f"-O {selectedOption}final{namer}.mp4")
    else:
        if selectedOption in str(reader["video"]):
            videolink = str(reader["video"][f"{selectedOption}"]["url"])
            os.system("wget "+f'"{videolink}"'+" "+f"-O {selectedOption}video{namer}.mp4")
            print(f"Raw {selectedOption}video Downloaded")

            if "AUDIO_QUALITY_MEDIUM" in str(reader["audio"]):
                audiolink = str(reader["audio"]["AUDIO_QUALITY_MEDIUM"]["url"])
                os.system("wget "+f'"{audiolink}"'+" "+f"-O {selectedOption}audio{namer}.mp4")
                print("Raw Audio Downloaded")
                print("Merging Audio and Video files..")

            elif "AUDIO_QUALITY_LOW" in str(reader["audio"]):
                audiolink = str(reader["audio"]["AUDIO_QUALITY_LOW"]["url"])
                os.system("wget "+f'"{audiolink}"'+" "+f"-O {selectedOption}audio{namer}.mp4")
                print("Raw audio Downloaded")
                print("Merging Audio and videos files...")
            invideo = fpeg.input(f'{selectedOption}video{namer}.mp4')
            inaudio = fpeg.input(f'{selectedOption}audio{namer}.mp4')
            fpeg.concat(invideo,inaudio,a=1,v=1).output(f'{selectedOption}final{namer}.mp4')
        else:
            print(f"{selectedOption} not found in",reader["video"])    
        



