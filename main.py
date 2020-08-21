import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import json
import urllib.request
import os
import threading
import time
from instabot import Bot
from datetime import datetime
import http.client
import sys
import config
from instaloader import Instaloader, Profile
from flask import request, redirect, render_template
from flask import Flask, Response

uname = ""
delay_to_follow = 60
estimated_time = 0

L = Instaloader()

app = Flask(__name__)

bot = Bot(follow_delay = delay_to_follow)
bot.login(username = config.username, password = config.password)



@app.route('/')
def index():
    return render_template('index.html', estimated_time = estimated_time)

@app.route('/signup', methods = ['POST'])
def signup():
    username = request.form['username']
    uname = username
    print(uname)
    followerz = followers(uname)
    print(followerz)
    estimated_time = followerz*delay_to_follow/60

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

            #follow(uname)
            print("guza mi")
            print( send( "<@&694256156549316699>" + "followed " + uname) )
            time.sleep(self.interval)


    example = ThreadingExample()
    return   render_template('index.html', estimated_time = estimated_time)



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


def followers (uname):
    profile = Profile.from_username(L.context, uname)
    #print(profile.followers)
    return profile.followers

def follow(uname):
    try:
        print(uname)
        bot.follow_following(uname)
    except:
        pass
