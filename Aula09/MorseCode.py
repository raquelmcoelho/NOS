from tkinter import *
tela = Tk()
tela.title("morse code")
tela.geometry("300x200")
tela.configure(background='black')


frame1 = Frame(tela)
frame1.configure(bg="black")
frame1.pack()


def substitui():
    frame1.destroy()
    frame2 = Frame(tela)
    frame2.configure(bg="black")
    frame2.pack()

    def codigomorse(event):
        codigo = str(frase.get())
        morse = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": ".._.", "g": "--.", "h": "....",
                 "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                 "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                 "y": "-.--", "z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
                 "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", " ": "/"}
        frasecodificada = ""
        for caractere in codigo.lower():
            if set(caractere).issubset(set(morse)):
                frasecodificada += morse[caractere] + " "

        codificado = Label(frame2, fg="white", bg="black")
        codificado.configure(text="seu código: " + frasecodificada)
        codificado.grid(row=5)

    Label(frame2, text="Insira o seu texto:", bg="black", fg="white").grid(row=3, sticky=W, pady=50, padx=90)
    frase = Entry(frame2, width=50)
    frase.bind("<Return>", codigomorse)
    frase.grid()


Label(frame1, text="\nTransformador Código Morse\n☺♥\n", bg="#000000", fg="white", font=("Comic Sans MS", "15")).grid()
Button(frame1, text="Vamos começar", command=substitui, bg='#000000', fg="white").grid()
mainloop()
