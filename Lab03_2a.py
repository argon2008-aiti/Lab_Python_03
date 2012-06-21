start_Number = 0   #first sample number to start with

iterator = 0     # iterator determines the how many times the loop executes

n = 5

while iterator <= 6:
    for i in range(start_Number, 0, -1): #'for' loop to print the numbers within the range given
        #print ' '*n
        print i,

    print    # go to next line if finished printing set of numbers
    n -= 1
    start_Number += 1    #increment start_Number to print next set of numbers
    
    iterator += 1              # increment the iterator 
        
