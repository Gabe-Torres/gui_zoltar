import tkinter as tk
import random
from PIL import Image, ImageTk, ImageSequence
from gtts import gTTS
import subprocess
import threading


bg_color = "#0000FF"

user_happy = False

app = tk.Tk()
app.title("ZOLTAR")
app.configure(bg=bg_color)

top_image_logo = Image.open("/Users/gabrieltorres/Desktop/zoltar/zoltar.png.webp")
top_photo_logo = ImageTk.PhotoImage(top_image_logo)

top_image_label_logo = tk.Label(app, image=top_photo_logo, bg=bg_color)
top_image_label_logo.image = top_photo_logo
top_image_label_logo.pack()

zoltar_gif = Image.open("/Users/gabrieltorres/Desktop/zoltar/zoltar.gif")
frames_zoltar = [frame.copy() for frame in ImageSequence.Iterator(zoltar_gif)]
zoltar_gif_label = tk.Label(app, bg=bg_color)

# image_label = tk.Label(app, bg=bg_color)
zoltar_gif_label.pack()

current_frame = 0

def update_zoltar_gif():
  global current_frame
  if current_frame < len(frames_zoltar):
        frame = frames_zoltar[current_frame]
        photo = ImageTk.PhotoImage(frame)
        zoltar_gif_label.config(image=photo)
        zoltar_gif_label.image = photo
        current_frame += 1
        app.after(100, update_zoltar_gif)
  else: 
    current_frame = 0
    app.after(100, update_zoltar_gif)

user_clicked = tk.BooleanVar()

zoltar = [
  "If you hear an onion ring, answer it.",
"Conscience is what hurts when everything else feels so good.",
"Be kind to unkind people – they need it the most.",
"Always borrow money from a pessimist; they don’t expect to be paid back!",
"There is nothing better than a friend, unless it is a friend with chocolate!",
"If Cinderella’s slipper fitted perfectly, why did it fall off?",
"With great power there comes an even greater electricity bill!",
"No matter how smart you are, you will never convince someone stupid that they are stupid.",
"A goal without a plan is just a wish!",
"Do not miss out on something that is great just because it could be difficult!",
"There is nothing better than a friend, unless it is a friend with chocolate!",
"If PLAN A fails all is not lost, there are 25 more letters in the alphabet!",
"Expecting the unexpected makes the unexpected expected!",
"Remember this, a true friend is the one that walks in when the rest of the world walks out.",
"All easy problems have already been solved!",
"Be kind to unkind people; they need it most.",
"A person that aims at nothing is sure to hit it.",
"If you always do what you have always done, you will always get what you always had.",
"A bus is a vehicle that runs twice as fast when you are wanting to catch it, than when you are riding in it.",
"There will come a point in your life when you realise who REALLY matters, who NEVER did, and who ALWAYS will.",
"Remember, cats have 32 muscles in each ear; this is to help them ignore you!",
"You do not realize what you have until it has gone; toilet paper is the best example!",
"Better late than never, but never late is better!",
"Those who live in the past limit their future!"
]

gifs_and_messages = [
  ("/Users/gabrieltorres/Desktop/zoltar/exit1.gif", "Something Weird is Happening"),
  ("/Users/gabrieltorres/Desktop/zoltar/exit2.gif", "Zoltar is upset"),
  ("/Users/gabrieltorres/Desktop/zoltar/exit3.gif", "Zoltar is very upset"),
  ("/Users/gabrieltorres/Desktop/zoltar/exit4.gif", "Zoltar is very very upset"),
  ("/Users/gabrieltorres/Desktop/zoltar/exit5.gif", "Zoltar is very very very upset"),
  ("/Users/gabrieltorres/Desktop/zoltar/dont-run.gif", "You cant run from Zoltar"),
  ("/Users/gabrieltorres/Desktop/zoltar/transition1.gif", "Zoltar stares within your soul"),
  ("/Users/gabrieltorres/Desktop/zoltar/transition2.gif", "Zoltar is not pleased"),
  ("/Users/gabrieltorres/Desktop/zoltar/transition3.gif", "Zoltar sees within your soul")
]
def transition_through_gifs(gifs_and_messages):
  top_image_label_logo.pack_forget()
  zoltar_gif_label.pack_forget()

  def gif_thread():
    for gif_path, message in gifs_and_messages:
      zoltar_label.config(text=message)

      gif = Image.open(gif_path)
      frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]

      for frame in frames:
        photo = ImageTk.PhotoImage(frame)
        image_label.config(image=photo)
        image_label.image = photo
        app.update_idletasks()
        app.after(100)

        app.wait_variable(user_clicked)

        zoltar_label.config(text="Zoltar ask again - are you pleased? Do you wish to leave?")

        if user_happy:
          final_gif_path = Image.open("/Users/gabrieltorres/Desktop/zoltar/youre-free.gif")
          final_message = "You are free to go!"
          display_final_happy_gif(final_gif_path, final_message)
        else: 
          lost_soul = Image.open("/Users/gabrieltorres/Desktop/zoltar/lost-souls.gif")
          lost_soul_message = "You are a lost soul... You joined Zoltar's army of lost souls!"
          display_final_lost_gif(lost_soul, lost_soul_message)

  gif_thread = threading.Thread(target=gif_thread)
  gif_thread.start()

whatever_button_clicks = 0

def handle_whatever_button_click():
  zoltar_label.config(text="You must make Zoltar happy first!")

  global whatever_button_clicks
  whatever_button_clicks += 1

  if whatever_button_clicks == 5:
    whatever_button_clicks = 0
    user_clicked.set(True)
    transition_through_gifs(gifs_and_messages)

    
def get_random_zoltar():
  quote = random.choice(zoltar)
  return quote

def get_random_zoltar_audio():
  quote = get_random_zoltar()
  zoltar_label.config(text=quote)
  tts = gTTS(text=quote, lang='en-us')
  tts.save("zoltar_quote.mp3")
  subprocess.run(["afplay", "zoltar_quote.mp3"])

def make_user_happy():
    global user_happy
    user_happy = True
    whatever_button_clicks = 0

def confirm_exit():
  global user_happy

  if user_happy:
    app.quit()
  else:
    zoltar_label.config(text="You must make Zoltar happy first!")


def show_confirmation_buttons():
  Happy_button.pack()
  whatever_button.pack()

zoltar_label = tk.Label(app, text="", wraplength=300, font=("Gotham", 20, "italic"), bg=bg_color, fg="white")
zoltar_label.pack(pady=20)

zoltar_button = tk.Button(app, text="Zoltar Saids Make Your Wish!", command=get_random_zoltar_audio)
zoltar_button.pack()

Happy_button = tk.Button(app, text="Yeah Sure I'm Happy...?", command=make_user_happy, bg="green")
Happy_button.pack()
Happy_button.pack_forget()

exit_button = tk.Button(app, text="LEAVING SO SOON? ARE YOU NOT PLEASED WITH ZOLTAR?", command=show_confirmation_buttons)
exit_button.pack()

whatever_button = tk.Button(app, text="Fuck you, Zoltar. Bitch ass", command=handle_whatever_button_click, bg="red")
whatever_button.pack()
whatever_button.pack_forget()

app.after(0, update_zoltar_gif)

app.mainloop()