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
import config


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
username  = "viktormatias"
try:
    #bot.upload_photo("myimg.jpg",caption)
    #bot.follow_followers(username)
    #follow-va vs hora koito dadeniqt username sledva
    bot.follow_following(username)
    #follow-va vs hora koito sledvat dadeniqt username
    #print( send( "<@&693878676785463297>" + " a new post has been uploaded to instagram via your script") )
except:
    pass
