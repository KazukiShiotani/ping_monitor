#!/usr/bin/env python

from flask import *
from datetime import datetime

app = Flask(__name__, static_folder="static")
import subprocess


f = open('ip_table.txt')
a = f.readlines()

ip = []
name = []


for line in a:
    l = line.split()
    ip.append(l[0])
    name.append(l[1])



@app.route('/')
def ping_monitor():
    ping = []
    stable = []
    now = datetime.utcnow()
    date = now.strftime("%Y-%m-%d %H:%M:%S")
    for i in range(len(ip)):
        p = subprocess.call(['ping','-c','1','-W','1',ip[i]])
        ping.append(p)
        if p == 0:
            stable.append('Connection OK!!!!!')
        else :
            stable.append('No Connection!!!!!!')
    return render_template('index.html',PING = zip(ip, name, stable), date = date)
        
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=9888, threaded = True)
                
                                                                            
