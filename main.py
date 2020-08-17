import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import urllib.request
import os
import time
from instabot import Bot
from datetime import datetime
import http.client
import sys
#import config
from flask import request, redirect, render_template
from flask import Flask

app = Flask(__name__)

uname = "qwerty"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods = ['POST'])
def signup():
    username = request.form['username']
    uname = username
    print(uname)
    follow(uname)

    #print("The email address is '" + email + "'")

    return  '{} {}'.format(uname, redirect('/'))



bot = Bot()
bot.login(username = os.environ['config.username'], password = os.environ['config.password'])
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
def follow(uname){
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

}
