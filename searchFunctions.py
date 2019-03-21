#print('Please enter the max value: ',end="")
#max = int(input())

print('Please enter the answer: ',end="")
answer = int(input())

min = 0


def binarySearch(answer, list):
    """Performs a binary search for the answer, within the min and max range.
    Returns list with index[0] of True if number is found, False if number is not found
    Returns list with index[1] of the number of guesses."""

    print(list)                 #Debug value
    list.sort()
    print(list)                 #Debug value
    
    guesses = 0
    found = False
    indexLength = len(list)
    min = 0                     #Represents the array position
    max = indexLength-1         #Represents the array position

    
    while True:
        mid = int((min + max)/2)                    #Recalculate midpoint
        guesses += 1 

        if list[max] < list[min]:                               #If the min and max values have crossed, the number is not in the subset
            print(f'Error! Answer not in subset')
            break

        if answer > list[mid]:                            #If the answer is above the midpoint, set the midpoint as the new minimum
            min = int(mid + 1)

        if answer < list[mid]:                            #If the answer is below the midpoint, set the midpoint as the new maximum
            max = int(mid - 1)

        if answer == list[mid]:                           #If the answer is the midpoint, bitch you found it!
            print(f'Answer found! Answer is {list[mid]}, Took {guesses} guesses to find')
            found = True
            break


    return([found, guesses])                        #Return True/False for whether the number was found, and the number of guesses it took



list = [0,2,4,3,8,7,1,13,24,6,18,23,5,14,16]
#print(binarySearch(min, max, answer, list))
print(binarySearch(answer, list))
