# -*- coding: utf-8 -*-
'''Koodi tehty "nopat_0_1.py" mallivastauksen pohjalle.
    Author Pessi Raunio
    Filename nopat_1_0.py'''

import random
import tkinter as tk
from tkinter import messagebox


class Nopat(tk.Tk, tk.Label):
    
    #Luodaan ohjelma-ikkuna, määritetään Nopan muuttjille attribuutit
    #Super initillä peritään Nopan yläluokasta "tk.Tk", metodi "master"
    def __init__(self, maara = 2, potti = 100, panos = 1, master=None) :
        super().__init__(master)
        self.title("Tupla-tai-kuitti-peli")
        self.master = master
        self.geometry("400x400")
        self.potti = potti
        self.panos = panos
        self.maara = maara
        
        self.luoLayout()
        
    #Asetellaan napit ja tekstikentät ikkunaan sekä määritellään niiden attribuutit.    
    def luoLayout(self):
        labelTervetuloa = tk.Label(self, text="Tervetuloa pelaamaan tupla tai kuitti peliä", font="Modern")
        labelTervetuloa.pack(pady=5)
        labelPanos = tk.Label(self, text="Aseta panoksesi", font="Modern 15")
        labelPanos.pack(pady=5)
        
        
        labelAlkuPotti = tk.Label(self, text=f"Aloituspotti {self.potti}", font="Helvetica 10")
        labelAlkuPotti.pack(pady=5)
        
        global entryPanos
        entryPanos = tk.Entry(self)
        entryPanos.pack(pady=5)
        
        buttonHeita = tk.Button(self, text="Heitä", command=self.tarkistaTulos)
        buttonHeita.pack(pady=5)

        buttonTalleta = tk.Button(self, text="Lunasta voitot", command=self.lunastaVoitot)
        buttonTalleta.pack(pady=5)
    

    def lunastaVoitot(self):
        if (self.potti > 0):
            tk.messagebox.showinfo(title="Lunastus", message=f"Lunastit {self.potti}, peli päättyi")
            exit()
        else:
            tk.messagebox.showinfo(title="Lunastus", message=f"Ei lunastettavaa, potti on {self.potti}")
            raise ValueError
            
    #Metodi jolla peli pelataan
    def tarkistaTulos(self):
        labelPaattyi = tk.Label(self, text='').pack()
        self.heita()
        self.tarkista()

        
    @property
    def potti(self):
        return self.__potti
    
    @potti.setter
    def potti(self, potti):

        self.__potti = potti
        if self.__potti < 0 : self.__potti = 0
    
    @property
    def panos(self):
        return self.__panos
    
    @panos.setter
    def panos(self, panos):
        
        if panos >= 1 and panos <= self.potti:
            self.__panos = panos
        else :
            tk.messagebox.showerror(title="Virhe", message="Panoksen oltava 1 tai pienempi kuin potti")
            raise ValueError
   
    @property
    def maara(self):
        return self.__maara
    
    @maara.setter
    def maara(self, maara):

        if maara < 0:
            maara = 1
        self.__maara = maara
        self.__luku = [0]*self.maara
        
    
    def heita(self) :
        for i in range(self.maara) :
            self.__luku[i] = random.randint(1, 6)
                
    
    def tarkista(self):
        
        #Asetetaan layouttiin tekstikentät joihin tulostetaan pelin tulos noppien mukaisesti.
        
        inputPanos = entryPanos.get()

        text_nopat = f'Noppien luvut: {self.__luku[0]} ja {self.__luku[1]}'

        labelTulos = tk.Label(self, text='', bd=1, relief="sunken")
        labelTulos.place(x=170, y=250)
        labelNopat = tk.Label(self, text='', bd=1, relief="sunken")
        labelNopat.place(x=150, y=280)
        labelPottiTulos = tk.Label(self, text='', bd=1, relief="sunken")
        labelPottiTulos.place(x=170, y=310)

        try:
            self.panos = int(inputPanos)
        except ValueError:
            tk.messagebox.showerror(title="Panos puuttuu", message="Aseta panos!")
            raise ValueError
            
        
        if self.maara != 2 :
            raise ValueError('Väärä peli, tupla-tai-kuitti on kahden nopan peli')
        else :
            if self.__luku[0] == self.__luku[1] :
                if self.__luku[0] == 1 or self.__luku[0] == 6 :
                    labelTulos.config(text=f"    Voitit 10 x {self.panos}    ")
                    labelNopat.config(text=text_nopat)
                    
                    coeff = 10
                else :
                    labelNopat.config(text=text_nopat)
                    labelTulos.config(text=f"    Voitit 2 x {self.panos}    ")
                    
                    coeff = 2
            elif sum(self.__luku) == 6 :
                labelNopat.config(text=text_nopat)
                labelTulos.config(text=f"    Menetit {self.panos}    ")
    
                coeff = -1
            else :
                labelNopat.config(text=text_nopat)
                labelTulos.config(text=f"Menetit 2 x {self.panos}")
            
                coeff = -2
                
            self.potti += self.panos * coeff
            
        if self.potti <= 0:
            msqbox = tk.messagebox.askyesno(title="Peli päättyi", message="Potti kulutettu, haluatko aloittaa uuden pelin?.")
            if msqbox == True:
                restart()
            else:
                exit()

        return labelPottiTulos.config(text=f"Potti nyt: {self.potti}")
        

    
if __name__ == '__main__' :

    #Aloittaa uuden pelin uudessa ikkunassa
    def restart():
        root = Nopat()
        root.mainloop()

        

    root = Nopat()
    root.mainloop()

