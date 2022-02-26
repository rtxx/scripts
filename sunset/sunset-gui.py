#!/usr/bin/python
# baby 1st python script
# needs pip install pystray

import os
import sys
import json
import pystray
from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image

PROGDIR=os.path.dirname(os.path.realpath(__file__))
PROGCONFIGDIR= PROGDIR + '/config'
PROGCONFIGFILE= PROGCONFIGDIR + '/gui-config.json'

def lightTheme(_):

  # loads config.json into f
  with open(PROGCONFIGFILE, 'r') as f:
    configs = json.load(f)

  # loads json values into vars
  sunsetLocation = configs['sunsetLocation']
  lightThemeName = configs['lightTheme']
  lightThemeSetting = configs['lightThemeSetting']

  # sends info to sunset
  os.system("bash "+ sunsetLocation + " " + lightThemeSetting  + " " + lightThemeName)
  #os.system("notify-send -t 2000 'sunset' 'Light Theme: '" + lightThemeName)

  # closes config.json
  f.close()

def darkTheme(_):

  # loads config.json into f
  with open(PROGCONFIGFILE, 'r') as f:
    configs = json.load(f)

  # loads json values into vars
  sunsetLocation = configs['sunsetLocation']
  darkThemeName = configs['darkTheme']
  darkThemeSetting = configs['darkThemeSetting']

  os.system("bash "+ sunsetLocation + " " + darkThemeSetting + " " + darkThemeName)
  #os.system("notify-send -t 2000 'sunset' 'Dark Theme: '" + darkThemeName)

  # closes config.json
  f.close()

def editConfig():
  os.system("kitty nano " + PROGCONFIGFILE)

def quit():
  print('Quitting...')
  exit()

def test():
  print("yee")

image = Image.open(PROGCONFIGDIR + "/icon.png")
menu = (item('Light theme', lightTheme),
        item('Dark Theme', darkTheme),
        item('More...', menu(
          item('Edit config',editConfig),
          item('Exit',quit))))

icon = pystray.Icon("sunset", image, "sunset", menu)
icon.run()
