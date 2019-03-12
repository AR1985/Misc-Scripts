#!/env/bin/usr/python3
import math

def isItPrime(n):
    """isPrime gets passed a number, and returns True if it is a prime, or False if it is not a prime"""

    iRoot_N = int(math.sqrt(n)) #Calculates the root of the number as an integer

    for i in range(2, iRoot_N):
        
        if (n%i == 0):
            return(False)   #If remainder is 0, number is not a prime

    return(True)   #If the loop completes, the number is a prime



def listOfPrimes(n):
    """listOfPrimes generates and returns a list of all the root numbers up to the number n"""

    lPrime_List = []

    for i in range(2, n):
        if isItPrime(i) == True:      #Check if i is a prime number, if it is, add to list
            lPrime_List.append(i)

    return(lPrime_List)             #Return list of prime numbers




def isItPrimeOptimized(n, listOfPrimes):
    """isPrimeOptimized gets passed a number and a list, and only tests using the digits in the list"""
    """Returns True if it is a prime, or False if it is not a prime"""

    ### <Error handling> ###
    
    listOfPrimes.sort()             #Sort list lowest to highest, just in case
    if max(listOfPrimes) < n*.8:    #If the largest number in the list of primes is less than 80% of the value of n, return error.
        return("Error: Insufficient range, in list of primes")
    
    ### </Error handling> ###    


    iRoot_N = int(math.sqrt(n)) #Calculates the root of the number as an integer, to act as the upper bound of numbers to test
    

    for element in listOfPrimes:
        if element > iRoot_N:   #If the loop has gone past the square root of the number, it is a prime
            return (True)
        
        if (n%element == 0):
            return(False)       #If remainder is 0, number is not a prime

    return(True)                #If the loop completes, the number is a prime
