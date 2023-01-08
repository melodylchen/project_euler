#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?


#find prime factors of the number

#find the largest prime factor


# This is a really terrible solution but it kind of works. For some reason the answer is before the
# last element of the array output - will debug later
def largest_prime_factor(integer):
    largest_prime_factor = 1 #Default 1 for the number 1
    list_of_factors = [1]
    # Find list of factors.
    max_factor = round(integer/3) #won't be larger than a 3rd of the value

    for i in range(2, max_factor):
        time_to_break = False
        if integer % i == 0:
            for x in list_of_factors:
                if i % x == 0 and x != 1 and i>x:
                    time_to_break = True
                    break
                elif i not in list_of_factors: 
                    list_of_factors.append(i)
        if time_to_break:
            break
                
                
            
            
        
    """
    for i in range(2, max_factor):
        if integer % i == 0:
            list_of_factors.append(i)

    """
        
    """for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
    """

    """
    # is this also inefficient. Refactor

    while True:
        for i in range(1, round(integer/2)):
            if integer % i == 0:
                list_of_factors.append(i)
                
        break
    """
    
    # Find list of primes
    # Count the number of divisible integers, remove ones that are divisible by more integers than 1
   
    """
    while True:
        excess = []
        for j in list_of_factors:
            # This is inefficient, try again
            for k in list_of_factors:
                if j>k>1 and j%k == 0:
                    excess.append(j)
                    break
                
                    
        break
    difference = [x for x in list_of_factors if x not in excess]
    """
    return list_of_factors
    #return list_of_factors, excess, max(difference)

print(largest_prime_factor(13195))
print(largest_prime_factor(600851475143))
