from bs4 import BeautifulSoup
import re
import json
import time
import os
import requests as rq
import random
import secrets


def newuuid():
  randomuid = str(secrets.token_hex(12))
  return str(randomuid)


headers = {

"Host": "www.youtube.com",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "none",
"DNT": "1",
"Sec-GPC": "1",
"Connection":"keep-alive",
"Cookie": "GPS=1; YSC=qY3wFam-DV4; VISITOR_INFO1_LIVE=CthXQ4wxYdU; VISITOR_PRIVACY_METADATA=CgJJThICGgA%3D; PREF=f6=40000000&tz=Asia.Kolkata&f7=100",
"Upgrade-Insecure-Requests": "1",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "none",
"Sec-Fetch-User": "?1",
"TE": "trailers",

}


def downloader(linker):

    info = {"video":{},"audiovideo":{},"audio":{}}
  
    link = linker

    videoid = str(link.split("v=")[1])
    
    file = rq.get(link,headers=headers)

    mc = str(file.text).replace('\\u0026','&')

    filer = open("src.html","w")
    filer.write(mc)
    filer.close()

    with open("src.html", "r", encoding="utf-8") as file:
        html_content = file.read()


    pattern = re.compile(r'ytInitialPlayerResponse = ({.*?});', re.DOTALL)
    match = pattern.search(html_content)

    if match:
        json_data = match.group(1)

        fc = json.loads(json_data)["streamingData"]["adaptiveFormats"]
        for i in range(len(fc)):
            if "qualityLabel" in str(fc[i]):
                if "audio" in str(fc[i]):
                    info["audio"][fc[i]["qualityLabel"]] = {"url":fc[i]["url"],"itag":fc[i]["itag"]}
                else:
                    info["video"][fc[i]["qualityLabel"]] = {"url":fc[i]["url"],"itag":fc[i]["itag"]}
            
            elif "audio" in str(fc[i]["mimeType"]):
                info["audio"][fc[i]["audioQuality"]] = {"url":fc[i]["url"],"itag":fc[i]["itag"]}

        dc = json.loads(json_data)["streamingData"]["formats"]
        for i in range(len(dc)):
            info["audiovideo"][dc[i]["qualityLabel"]] = {"url":dc[i]["url"],"audioQuality":dc[i]["audioQuality"]}


            
        saveuuid = newuuid()
        open(f"{saveuuid}data{videoid}.json","w").write(json.dumps(info))
        sendpath = os.path.abspath(f"{saveuuid}data{videoid}.json")
        return sendpath
    else:
        print("Pattern not found in the HTML file.")

