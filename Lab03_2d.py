start_Number = 7   #first sample number to start with

iterator = 0     # iterator determines the how many times the loop executes

n = 0

while iterator <= 6:
    print '  '*n,
    for i in range(1,start_Number): #'for' loop to print the numbers within the range given
        print i,

    print    # go to next line if finished printing set of numbers

    n += 1
    
    start_Number -= 1    #increment start_Number to print next set of numbers
    
    iterator += 1              # increment the iterator 
        
