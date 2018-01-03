from tkinter import*
window = Tk()
window.title('Alien')
c = Canvas(window, height=300, width=400)
c.pack()
body = c.create_oval(100, 150, 300, 250, fill='green')
eye = c.create_oval(170, 70, 230, 130, fill='white')
eyeball = c.create_oval(190, 90, 210, 110, fill='purple')
mouth = c.create_oval(150, 220, 250, 240, fill='red')
neck = c.create_line(200, 150, 200, 130)
hat = c.create_polygon(180, 75, 220, 75, 200, 20, fill='darkblue')
def mouth_open():
    c.itemconfig(mouth, fill='black')
def mouth_close():
    c.itemconfig(mouth, fill='red')
def blink():
    c.itemconfig(eye, fill='green')
    c.itemconfig(eyeball, state=HIDDEN)
def unblink():
    c.itemconfig(eye, fill='white')
    c.itemconfig(eyeball, state=NORMAL)
words = c.create_text(200, 280, text='I am an alien.')
def steal_hat():
    c.itemconfig(hat, state=HIDDEN)
    c.itemconfig(words, text='Give me my hat back!')
def give_hat():
    c.itemconfig(hat, state=NORMAL)
    c.itemconfig(words, text='Thank you!')
def how_are_you():
    c.itemconfig(words, text='I am great!')
def hello():
    c.itemconfig(words, text='Hello, I am an alien')
def add(x,y):
    z = x + y
    t='The answer is ' + str(z)
    c.itemconfig(words, text=t)
def subtract(x,y):
    z = x - y
    t='The answer is ' + str(z)
    c.itemconfig(words, text=t)
def exponent(x,y):
    z =  pow(x,y) 
    t='The answer is ' + str(z)
    c.itemconfig(words, text=t)
def divide(x,y):
    z = x / y
    t='The answer is ' + str(z)
    c.itemconfig(words, text=t)
def multiply(x,y):
    z = x * y
    t='The answer is ' + str(z)
    c.itemconfig(words, text=t)

def howisAditi():
    c.itemconfig(words, text='Don\'t add aditi to the Whatsapp group')
