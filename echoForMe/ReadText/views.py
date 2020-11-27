from django.shortcuts import render

# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio
from pygame import mixer  # Load the popular external library
from datetime import datetime
import os 

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
    myobj = gTTS(text=text_to_read, lang=language, slow=False) 
      
    # Saving the converted audio in a mp3 file , changing file name everytime
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "/home/radhika/Desktop/hack1/django_projects/echoForMe/ReadText/AudioFiles/audio"+date_string+".mp3"
    myobj.save(filename) 
      
    # Playing the converted file
    #  -------------------------ERROR POINT ----------------------------
    mixer.init()
    mixer.music.load(filename) 
    mixer.music.play()
    #os.system("mpg123 "+"/home/radhika/Desktop/hack1/django_projects/echoForMe/ReadText/AudioFiles/query.mp3") 
    
    print(request.POST)
    return render(request, 'index.html')