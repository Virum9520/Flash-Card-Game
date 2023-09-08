import tkinter as tk
import random

BACKGROUND_COLOR = "#B1DDC6"
BG_img = '#91c2af'
words = ['Press', 'Button']
# Defining functions


def next_word():
    global words, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(bg_card, state='hidden')
    canvas.itemconfig(fg_card, state='normal')
    with open('data/french_words.csv', 'r') as file:
        line = random.choice(file.readlines())
        words = line.split(',')
        fr_word.config(text=words[0], bg='white', fg='black')
        french.config(text='French', bg='white', fg='black')
        flip_timer = window.after(3000, flip_card)


def flip_card():
    french.config(text='English', bg=BG_img, fg='white')
    fr_word.config(text=words[1], bg=BG_img, fg='white')
    canvas.itemconfig(fg_card, state='hidden')
    canvas.itemconfig(bg_card, state='normal')


# Defining elements
window = tk.Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, background=BACKGROUND_COLOR, width=800, height=550)

canvas = tk.Canvas(width=800, height=550, highlightthickness=0)

french = tk.Label(text='French', bg='white', fg='black', font=('Ariel', 40, 'italic',))
fr_word = tk.Label(text='Word', bg='white', fg='black', font=('Ariel', 60, 'bold',))

f_image = tk.PhotoImage(file='images/card_front.png')
b_image = tk.PhotoImage(file='images/card_back.png')

fg_card = canvas.create_image(400, 263, image=f_image)
bg_card = canvas.create_image(400, 263, image=b_image,)
canvas.itemconfig(fg_card, state='normal')
canvas.itemconfig(bg_card, state='hidden')
canvas.config(background=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)


w_image = tk.PhotoImage(file="images/wrong.png")
w_button = tk.Button(image=w_image, width=50, height=50, highlightthickness=0, command=next_word)

r_image = tk.PhotoImage(file="images/right.png")
r_button = tk.Button(image=r_image, width=50, height=50, highlightthickness=0, command=next_word)

canvas.grid(row=0, column=0, columnspan=2, rowspan=2)

french.grid(row=0, column=0, columnspan=2)
fr_word.grid(row=1, column=0, columnspan=2)

w_button.grid(row=3, column=0)
r_button.grid(row=3, column=1)

next_word()

window.mainloop()
