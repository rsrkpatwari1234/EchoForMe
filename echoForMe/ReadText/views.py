from django.shortcuts import render

# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio
from datetime import datetime
import os 
import vlc

#web scraping libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# For time lag between Heading and Content
import time

# Create your views here.
# from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

def textToAudio(request):
    # Language in which you want to convert 
    language = 'en'
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    alldata = request.POST
    text_to_read = alldata.get("text_to_read")
    print(type(text_to_read))
    myobj = gTTS(text=text_to_read, lang=language, slow=False) 
      
    # Saving the converted audio in a mp3 file , changing file name everytime
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "/home/vidit/EchoForMe/echoForMe/ReadText/AudioFiles/audio"+date_string+".mp3"
    myobj.save(filename) 
      
    # Playing the converted file
    #  -------------------------ERROR POINT ---------------------------- 
    p = vlc.MediaPlayer(filename)
    p.play()
    print(request.POST)
    return render(request, 'index.html')

def texttoAudioNews(request):
    language = 'en'
    opts=webdriver.ChromeOptions()
    opts.headless=True
    driver = webdriver.Chrome(ChromeDriverManager().install() ,options=opts)
    headings=[] #List to store heading of the news
    contents=[] #List to store content of the news
    driver.get("https://timesofindia.indiatimes.com/videos/business/gdp-contracts-7-5-in-july-september-india-enters-recession/videoshow/79450419.cms")

    content = driver.page_source
    soup = BeautifulSoup(content,features="html.parser")

    for a in soup.findAll('div',attrs={'class':'_2GHni'}):
        heading=a.find('h1')
        content=a.find('p',attrs={'class':'_159Jb'})

    myobjHeading = gTTS(text=heading.text, lang=language, slow=False)
    myobjContent = gTTS(text=content.text, lang=language, slow=False)

    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    filename1 = "/home/vidit/EchoForMe/echoForMe/ReadText/AudioFiles/heading"+date_string+".mp3"
    filename2 = "/home/vidit/EchoForMe/echoForMe/ReadText/AudioFiles/content"+date_string+".mp3"
    myobjHeading.save(filename1)
    myobjContent.save(filename2)

    headingMp3 = "/home/vidit/EchoForMe/echoForMe/ReadText/AudioFiles/heading.mp3"
    contentMp3 = "/home/vidit/EchoForMe/echoForMe/ReadText/AudioFiles/content.mp3"

    # Playing the converted file
    #  -------------------------ERROR POINT ---------------------------- 
    # Playing the title Heading
    p = vlc.MediaPlayer(headingMp3)
    p.play()
    time.sleep(2)
    p = vlc.MediaPlayer(filename1)
    p.play()

    # 10 sec time lag between heading and content 
    time.sleep(8)
    p = vlc.MediaPlayer(contentMp3)
    p.play()
    time.sleep(2)
    # Playing News Content
    g = vlc.MediaPlayer(filename2)
    g.play()
    
    return render(request, 'index.html')
