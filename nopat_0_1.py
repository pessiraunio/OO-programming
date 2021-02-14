"""
Author: Pessi Raunio
Description: Tupla tai kuitti peli
Filename: nopat_0_1.py
Modules: random

"""
import random
#Luodaan luokka nopat parametreillä potti, panos ja maara
class Nopat:
    def __init__(self, potti, panos, maara):
        self.potti = potti
        self.panos = panos
        self.maara = maara
        
    #Alustetaan potti
    @property
    def potti(self):
        return self.__potti
    
    #Tarkistetaan potin arvo
    @potti.setter
    def potti(self, potti):
        if potti <= 0:
            raise ValueError("potti ei voi olla negatiivinen")
        else:
            self.__potti = potti
            
    #Alustetaan panos
    @property
    def panos(self):
        return self.__panos
    
    #Tarkistetaan panoksen määärä arvo
    @panos.setter
    def panos(self, panos):
        for i in range(1):
            if (panos == 0):
                print("Minimi panos on 1, panokseksi asetettu 1")
            else:
                break
        while (panos):
            if int(panos) > int(self.__potti):
                print("Panos ei voi olla enemmän kuin potti")
                self.__panos = panos
                break
            
            elif (panos) < 0:
                print("Minimi panos on 1, panokseksi asetettu 1")
                self.__panos = 1
                break
            else:
                self.__panos = panos
                break
        
    #Alustetaan maara attribuutti
    @property
    def maara(self):
        return self.__maara
    #Tarkistaan maara 
    @maara.setter
    def maara(self, maara):
        if maara < 0:
            maara = 1
        self.__maara = maara
        self.__luku = [0]*self.maara
            
            
            
    def heita(self):
         try:
             for i in range(self.maara):
                 self.__luku[i] = random.randint(1, 6)
             print("Noppien silmäluvut ovat", self.__luku[0], "ja", self.__luku[1])
         except:
             print("Eimihinkään")
             
    def tarkista(self, maara):
        if maara != 2:
            raise ValueError("Väärä peli, tämä on kahden nopan tupla-tai-kuitti")
        else:
            for i in self.__luku:
                if self.__luku[0] == self.__luku[1]:
                    if self.__luku[0] == 6 or self.__luku[0] == 1:
                        print("Voitit panoksesi kymmenkertaisena.")
                        self.__potti = int(self.__potti) + int(self.__panos) * 10
                        print("potti on nyt", int(self.__potti))
                        break
                    
                    elif self.__luku[0] == 2 or self.__luku[0] == 3 or self.__luku[0] == 4 or self.__luku[0] == 5:
                        self.__potti = int(self.__potti) + (int(self.__panos) * 2)
                        print("Voitit panoksesi kaksinkertaisena.")
                        print("potti on nyt", int(self.__potti))
                        break
                
                elif (self.__luku[0] + self.__luku[1] == 6) or self.__luku[0] != self.__luku[1]:
                        self.__potti = int(self.__potti) - int(self.__panos)
                        if self.__potti < 0:
                            self.__potti = 0
                        print("Hävisit panoksesi, potti on nyt", self.__potti)
                        break
                else:
                    print("ei tuplaa")
                    self._potti = self.__potti - (2*int(self.__panos))
                        
            
            
def main():
    
    
    print("Tupla-tai-kuitti peli - alkupotti 100\n")
    print("Minimipanos 1\n")
    

    
    
    peli = Nopat(100, 1, 2)
        
    while (peli.potti > 0):
        while (peli.panos):
            try:
                peli.panos = int(input("Aseta panoksesi: "))
                if (int(peli.panos) > int(peli.potti)):
                    print("panos:", (peli.panos))
                    print("potti", (peli.potti))
                    continue
                else:
                    break
            except ValueError:
                print("Panos ei voi olla tyhjä")
                
        peli.heita()
        peli.tarkista(peli.maara)
    print("\n---Potti kulutettiin, peli on päättynyt---")

if __name__ == '__main__':
    main()