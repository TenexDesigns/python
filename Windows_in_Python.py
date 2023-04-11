We use the  tkinter libray , which comes with python , to make windows and widgets



widgets = GUI elements such as buttons, textboxes , labels and images
windows = serves as a cotainer to hold these widgets


To display a window , This is the syntax

from tkinter import *


window_name = Tk()  # This will instanciate an instance of a window


window.mainloop() # places a window on the coputer screen it also listens for events.






To customise our window

TO CHAGE THE SIZE
window_name.geormetry("420x 420") // We use this to set the size of the window

TO CHANE THE TITLE

window_name.title("George New Window Title")

TO CHANGE THE WINDOW ICON

custom_icon = PhototImage(file='C://logo.png')  // Here we convert our image into a photo image that tkinter can understand , and we  strore it in a variable
window_name.iconPhoto(True,custom_icon)// Here we use the convetred phot image to chage our windows icon



TO CHNAGE THE BACKGROUND COLOR

window_name.config(background ="black") // You can put any color you want ,even hexagonl values , but they have to start with # e.g #eeeeff











































































































..
