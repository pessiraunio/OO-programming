# -*- coding: utf-8 -*-
"""
arrangenumbers_0_4.py
@author: Pessi Raunio
Number arranging game with functions
modules used: random

"""

import random


def create():
        numbers = []
        for i in range(9):
            numbers.append(i+1)
        numbers[-1] = '_'
        return numbers

def suffle(numbers):
        random.shuffle(numbers)
        return numbers
    
def isSolvable(numbers, check):
        inversions = 0
        for i in range(8):
            for k in range(i+1, 8):
                if check.index(numbers[i]) > check.index(numbers[k]):
                    inversions = inversions + 1
        if inversions % 2 == 0:
            return True
        else:
            return False

def isReady(numbers, check):
    if numbers == check:
        return 

def move(numbers):
        while True:
            try:
                empty = '_'
                empty_place = numbers.index(empty)
                user_input = int(input("Number to move: "))
                input_index = numbers.index(user_input)
                #Checking if the move is allowed, no prompt if move is not allowed just repeating the question to keep it simple
                if numbers[0] == '_' and (numbers[input_index] == numbers[3] or numbers[input_index] == numbers[1]):
                    numbers[empty_place], numbers[input_index] = numbers[input_index], numbers[empty_place]
                
                elif numbers[1] == '_' and (numbers[input_index] == numbers[0] or numbers[input_index] == numbers[2] or numbers[input_index] == numbers[4]):
                    numbers[empty_place], numbers[input_index] = numbers[input_index], numbers[empty_place]
                
                elif numbers[2] == '_' and (numbers[input_index] == numbers[1] or numbers[input_index] == numbers[5]):
                    numbers[empty_place], numbers[input_index] = numbers[input_index], numbers[empty_place]
                
                elif numbers[3] == '_' and (numbers[input_index] == numbers[6] or numbers[input_index] == numbers[4] or numbers[input_index] == numbers[0]):
                    numbers[empty_place], numbers[input_index] = numbers[input_index], numbers[empty_place]
                
                elif numbers[4] == '_' and (numbers[input_index] == numbers[1] or numbers[input_index] == numbers[3] or numbers[input_index] == numbers[5] or numbers[input_index] == numbers[7]):
                    numbers[empty_place], numbers[input_index] = numbers[input_index], numbers[empty_place]
                
                elif numbers[5] == '_' and (numbers[input_index] == numbers[2] or numbers[input_index] == numbers[4] or numbers[input_index] == numbers[8]):
                    numbers[empty_place], numbers[input_index] = numbers[input_index], numbers[empty_place]
                
                elif numbers[6] == '_' and (numbers[input_index] == numbers[3] or numbers[input_index] == numbers[7]):
                    numbers[empty_place], numbers[input_index] = numbers[input_index], numbers[empty_place]
                
                elif numbers[7] == '_' and (numbers[input_index] == numbers[4] or numbers[input_index] == numbers[6] or numbers[input_index] == numbers[8]):
                    numbers[empty_place], numbers[input_index] = numbers[input_index], numbers[empty_place]
                
                elif numbers[-1] == '_' and (numbers[input_index] == numbers[5] or numbers[input_index] == numbers[7]):
                    numbers[empty_place], numbers[input_index] = numbers[input_index], numbers[empty_place]
                    
                #Checking if the order is correct and printing it out with a message
                
            except ValueError:
                print("Give an integer from 1 to 8")
                continue
            return user_input
                
def printBoard(numbers):
        for i, var in enumerate(numbers):
            print(var) if (i+1)%3==0 else print(var, end=' ')




def main():
    
    #create a list of numbers, suffle the order and add an empty string to the end
    numbers = create()
    check = tuple(numbers)        
    #preparation loop
    while True:    
        suffle(numbers)
        if isSolvable(numbers, check):
            break
    print('8 puzzle - arrange the numbers by swapping them with the empty place')
    #the main loop
    while True:
        printBoard(numbers)
        if isReady(numbers, check) == True:
            print('Good work!')
            break
        else:
            move(numbers)


    
if __name__ == "__main__":
    main()




