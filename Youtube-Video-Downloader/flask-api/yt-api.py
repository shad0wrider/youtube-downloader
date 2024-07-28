import os
import time
from flask import Flask , url_for , render_template , render_template_string , request
import json , requests
import ytdownload as ytloader
from markupsafe import escape


cwd = os.getcwd()+"/"

def finder(idval):
    listing = os.listdir(os.getcwd())
    for m in listing:
        if idval in m:
            return str(os.path.abspath(m))
            
    else:
            return False



def jsondataloader(path):
     jsonfile = open(path,"r")
     jsondata = json.loads(jsonfile.read())
     return jsondata


app = Flask("yt")

@app.route("/help")
def help():
    return render_template('help.html')

@app.route('/data')
def datafinder():
    link = request.args.get('link')
    idval = str(link.split("v=")[1])
    if len(idval) != 11:
         return "The video ID is not valid :("

    
    else:
        
        finaldataload = finder(idval)
        if finaldataload == False:
            mc =  ytloader.downloader(link)
            return jsondataloader(mc)
        else:
             return jsondataloader(finaldataload)
    

def runner():
    app.run(host="0.0.0.0",port=2341)

def starter():
    fire = Thread(target=runner)
    fire.run()

starter()





def runner():
     app.run(host="0.0.0.0",port=2341)

def starter():
     fire = Thread(target=runner)
     fire.start()

starter()






