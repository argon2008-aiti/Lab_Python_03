

number = 1       #initialize variable from which number samples would be collected

prime_Counter = 0 #variable to count the number of prime numbers

while prime_Counter < 50:  # iterate until number of primes = 50

    divisors = 0           # variable to sum divisors
    
    for digit in range(1,number+1): # test if number is prime
        if number % digit == 0:
            divisors += 1

    if divisors == 2:               # print number if it is prime
        print number,
        prime_Counter += 1

        if prime_Counter % 10 == 0: #go to next line if prime numbers is 10
            print

        

    number += 1                    #get next integer in the sequence
        
        

        
