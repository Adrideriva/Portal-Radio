import tkinter as tk
from PIL import Image, ImageTk
import pygame

#ventana del TK
root = tk.Tk()
root.geometry("300x400")
root.config(bg="black")
root.title("Radio")
root.resizable(False, False)
#definir la imagen
img = Image.open("assets/radio.png")
img = img.resize((200, 300))
imagen = ImageTk.PhotoImage(img)

#cargar la imagen XD
label1 = tk.Label(root, image=imagen)
label1.config(bg="black")
label1.pack()

#definir el audio
radio = ("assets/Radioloop.mp3")

#reproducir audio

pygame.mixer.init()
pygame.mixer.music.load(radio)
pygame.mixer.music.play(loops=-1)

def mute():
    if pygame.mixer.music.get_busy():

        pygame.mixer.music.pause()
        boton.config(text="Unmute")
    else:
        pygame.mixer.music.unpause()
        boton.config(text="Mute")
    

#boton para mutear volumen
boton = tk.Button(root, command=mute, text="Mute")
boton.place(x=130, y=350)


root.mainloop()