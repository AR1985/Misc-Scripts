#! python3

import random
import time

tempList = []
tempTuple = ()
tempSet = {5}
tempDic = {1:1}

def generateDataTypes():
    """Generates the temporary list, tuple, set, and dictionary, which will be used for calculations"""
    
    #Generate the temporary list
    for i in range(1000000):
        tempList.append(random.randint(1,5000000))

    print('Done generating the list')



    #Generate the temporary tuple (just copy the list since tuples are immutable and can't be appended using a loop)
    tempTuple = tuple(tempList)
    print('Done generating the tuple')


    #Generate the temporary set	
    tempSet = {5}
    while(len(tempSet) < 1000000):
        tempSet.add(random.randint(1,5000000))

    print('Done generating the set')



    #Generate the temporary dictionary
    tempDic = {1:1}
    for j in range(999999):
        tempDic[i]=random.randint(1,5000000)

    print('Done generating the dictionary \n')

    return(tempTuple)


def calculateLookupResults(tempTuple, loops):
    """Generates a lookup value, and queries the list/tuple/set/dictionary the number of times as defined by the variable loops.  Outputs results to screen"""
  
    lookupValue = random.randint(1,5000000)         #Generate a random number, that will be used to search the loops
    listValue = int(loops/1000)                      #Loops and tuples are slow, so will be calculated by looping 1000 times less, and multiplying the reuslts by 1000 after


    #Query the list by iterating through the elements, and calculate the time required.  Multiply by any factor required, to reduce program runtime since lists are slow.
    startTime = time.time()

    for k in range(1,listValue):
        lookupValue in tempList

    print(f"Time to check {loops} values in a list by calling 'Value' in 'List' is {round((time.time() - startTime) * 1000, 3)} seconds")



    #Query the tuple by iterating through the items, and calculate the time required.
    startTime = time.time()

    for m in range(1,listValue):
        lookupValue in tempTuple

    print(f'Time to check {loops} values in a tuple is {round((time.time() - startTime) * 1000, 3)} seconds')



    #Query the set, and calculate the time required
    startTime = time.time()

    for n in range(1,loops):
        lookupValue in tempSet

    print(f'Time to check {loops} values in a set is {round(time.time() - startTime, 3)} seconds')


    #Query the dictionary, and calculate the time required
    startTime = time.time()

    for p in range(1,loops):
        lookupValue in tempDic

    print(f'Time to check {loops} values in a dictionary is {round(time.time() - startTime, 3)} seconds')



def main():

    (tempTuple) = generateDataTypes()               #Generate the lists/tuples/sets/dictionaries.  tempTuple has to be returned to avoid resetting to zero.

    calculateLookupResults(tempTuple, 1000000)      #Calculate and display the results.  tempTuple has to be passed, or else will be interpreted as zero.



main()                  #Call main function
