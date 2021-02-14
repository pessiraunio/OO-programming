# -*- coding: utf-8 -*-
"""
arrangenumbers_0_3.py
@author: Pessi Raunio
modules:random

"""
import random

print("Title --  Number arranging game \n")

#Creating a number list and filling it with numbers using for loop 
#And adding empty space to the end of the list
numbers = []
for i in range(9):
    numbers.append(i+1)
numbers[-1] = '_'


#Copying number list to a tuple called check_numbers
check_numbers = tuple(numbers)


#swapping 4 times number[i] with a random number
random_number = random.randint(1, 7)
for i in range(4):
    numbers[i], numbers[random_number] = numbers[random_number], numbers[i]
    
#Calculating the number of inversions
inversions = 0
    
for i in range(8):
    for k in range(i+1, 8):
        if check_numbers.index(numbers[i]) > check_numbers.index(numbers[k]):
            inversions = inversions + 1

#Breaking the loop if number of inversions is odd
while inversions % 2 != 0:
    print("puzzle not solvable")
    print("numbers of inversions:", inversions)
    for i, var in enumerate(numbers):
        print(var) if (i+1)%3==0 else print(var, end=' ')
    break
else:
    #Continuing this loop if inversions is even.
    while tuple(numbers) != check_numbers:

        for i, var in enumerate(numbers):
            print(var) if (i+1)%3==0 else print(var, end=' ')
        
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
            if tuple(numbers) == check_numbers:
                print("You won! the numbers are in a correct order!")
                for i, var in enumerate(numbers):
                    print(var) if (i+1)%3==0 else print(var, end=' ')
                break
        #Giving an error if given number is invalid
        except ValueError:
            print("Give an integer from 1 to 8")
            continue
    
    


