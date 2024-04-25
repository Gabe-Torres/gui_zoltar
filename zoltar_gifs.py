from PIL import Image, ImageTk, ImageSequence
import tkinter as tk
# from zoltar_teller_gui import app, bg_color

zoltar_gif = Image.open("/Users/gabrieltorres/Desktop/zoltar/zoltar.gif")
frames_zoltar = [frame.copy() for frame in ImageSequence.Iterator(zoltar_gif)]
zoltar_gif_label = tk.Label(app, bg=bg_color)

# image_label = tk.Label(app, bg=bg_color)
zoltar_gif_label.pack()

current_frame = 0

def update_zoltar_gif():
  from zoltar_teller_gui import app, zoltar_gif_label
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