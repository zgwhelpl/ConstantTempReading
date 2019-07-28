from sense_hat import SenseHat
import os

sense = SenseHat()
sense.set_rotation(90)

isBright= 'Low'  

from time import sleep

def toggleBrightness():
    global isBright
    if (isBright == 'High'):
        isBright = 'Low'
    elif (isBright == 'Low'):
        isBright = 'Off'
    elif (isBright == 'Off'):
        isBright = 'High'

def tempRangeText(tempF):
    color = [255, 255, 255]
    if (tempF >=80):
        color = [255, 0, 0]
    if (tempF <= 70):
        color = [106, 189, 255]
    '''if (tempF <= 65):
        color = [0, 0, 255]'''
    return color

def tempRangeBL(tempF):
    color = [0,0,0]
    if (tempF >= 85):
        color = [100, 0, 0]
    if (tempF <= 65):
        color = [0, 0, 255]
    return color



while(True):
    temp = sense.temp
    tempF = (temp*9/5) + 32
    
    #Dimmed Text, No back light
    if (isBright == 'Low'):
        x = 48 #Dimmest level of white visible on actual hat
        #x = 150 #For Sense Hat Emulator visibility
        textColor = [x, x, x]
        backColor = [0, 0, 0]
    #Dynamic Text and Backlight colors
    elif (isBright == 'High'):
        textColor = tempRangeText(tempF)
        backColor = tempRangeBL(tempF)
    #No Color, no Light
    elif (isBright == 'Off'):
        textColor = backColor = [0, 0, 0]
    
    sense.show_message("%.1f F" % tempF, .1, textColor, backColor)
    print("%.1f F" %tempF)
    for event in sense.stick.get_events():
        if (event.direction == 'middle' and event.action == 'pressed'):
            toggleBrightness()
            sense.show_message("%s" %isBright, .1, textColor, backColor)
