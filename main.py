import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import urllib.request
import os
import threading
import time
from instabot import Bot
from datetime import datetime
import http.client
import sys
import config
#import config
from flask import request, redirect, render_template
from flask import Flask, Response

uname = "qwerty"

class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        #while True:
            # Do something
            #print('Doing something imporant in the background')
        follow(uname)
        time.sleep(self.interval)


app = Flask(__name__)



@app.route('/')

def index():
    return render_template('index.html')

@app.route('/signup', methods = ['POST'])
def signup():
    username = request.form['username']
    uname = username
    print(uname)
    #follow(uname)
    example = ThreadingExample(uname)

    return  redirect('/')



bot = Bot()
bot.login(username = config.username, password = config.password)
'''
def send( message ):

    # your webhook URL
    webhookurl = config.webhookurl

    # compile the form data (BOUNDARY can be anything)
    formdata = "------:::BOUNDARY:::\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\n" + message + "\r\n------:::BOUNDARY:::--"

    # get the connection and make the request
    connection = http.client.HTTPSConnection("discordapp.com")
    connection.request("POST", webhookurl, formdata, {
        'content-type': "multipart/form-data; boundary=----:::BOUNDARY:::",
        'cache-control': "no-cache",
        })

    # get the response
    response = connection.getresponse()
    result = response.read()

    # return back to the calling function with the result
    return result.decode("utf-8")
'''



def follow(uname):
    try:
        #bot.upload_photo("myimg.jpg",caption)
        #bot.follow_followers(username)
        #follow-va vs hora koito dadeniqt username sledva
        print("asdf")
        print(uname)
        bot.follow_following(uname)
        #follow-va vs hora koito sledvat dadeniqt username
        #print( send( "<@&693878676785463297>" + " a new post has been uploaded to instagram via your script") )
    except:
        pass
