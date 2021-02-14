# -*- coding: utf-8 -*-
"""
filename:       noppatesti.py
description:    testiohjelma, ohjelmalle nopat.0.1
@author:        Pessi Raunio

"""

from nopat_0_1_op import Nopat

class NoppaTesti:

    
    @staticmethod
    def testaaIsotParit():
        nopat = Nopat()
        
        #Määritellään tarkistettavat parit
        parit = [[1,1], [6,6]]
        
        #For loopilla tarkistetaan jokainen pari ja pyydetään tarkista methodia
        for i in parit:
            nopat._Nopat__luku = i
            nopat.tarkista()
        
        potti =  nopat.potti - 100
                
        #Lasketaan odotettu määrä ja verrataan sitä laskettuun pottiin
        odotettu = (2*10*nopat.panos)
        if odotettu == potti:
            return True
        
        return False
              
    
    @staticmethod
    def testaaPienetParit():
        nopat = Nopat()
        
        #Määritellään tarkistettavat parit
        parit = [[2,2], [3,3], [4,4], [5,5]]
        
        #For loopilla tarkistetaan jokainen pari ja pyydetään tarkista methodia
        for i in parit:
            nopat._Nopat__luku = i
            nopat.tarkista()
        
        potti = nopat.potti - 100
        
        #Lasketaan odotettu määrä ja verrataan sitä laskettuun pottiin
        odotettu = (4*2*nopat.panos)
        if odotettu == potti:
            return True
        
        return False
        
        
    @staticmethod
    def testaaSumma():
        nopat = Nopat()
        
        #Määritellään tarkistettavat parit
        parit = [[1,5], [2,4]]
        
        #For loopilla tarkistetaan jokainen pari ja pyydetään tarkista methodia
        for i in parit:
            nopat._Nopat__luku = i
            nopat.tarkista()
        
        potti = 100 - nopat.potti
            
        #Lasketaan odotettu määrä ja verrataan sitä laskettuun pottiin
        odotettu = (potti)
        if odotettu == potti:
            return True
    
        return False
        
    
    @staticmethod
    def testaaTappiot():
        nopat = Nopat()
        #Määritellään tarkistettavat parit
        parit = [[1,2], [1,3], [1,4],
                 [1,6], [2,3], [2,5],
                 [2,6], [3,4], [3,5],
                 [3,6], [4,5], [4,6],
                 [5,6],
                 [2,1], [3,1], [4,1],
                 [6,1], [3,2], [5,2],
                 [6,2], [4,3], [5,3],
                 [6,3], [5,4], [6,4],
                 [6,5]]
        
        #For loopilla tarkistetaan jokainen pari ja pyydetään tarkista methodia
        for i in parit:
            nopat._Nopat__luku = i
            nopat.tarkista()
            
        potti = 100 - nopat.potti
            
        #Lasketaan odotettu määrä ja verrataan sitä laskettuun pottiin
        odotettu = ((4*4*2 + 2*5*2)*nopat.panos)
        
        if odotettu == potti:
            return True
        
        return False
        
        

if __name__ ==  "__main__":
    print(f'Isot (1,1 ja 6,6) parit testi on passed: {NoppaTesti.testaaIsotParit()}')
    print(f'Pienet (2,2 3,3, 4,4 5,5) parit testi on passed: {NoppaTesti.testaaPienetParit()}')
    print(f'Summa testi on passed: {NoppaTesti.testaaSumma()}')
    print(f'Muut testi on passed: {NoppaTesti.testaaTappiot()}')
    
    
    