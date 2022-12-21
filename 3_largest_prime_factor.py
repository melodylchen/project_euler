#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?


#find prime factors of the number

#find the largest prime factor

def largest_prime_factor(integer):
    i = 2
    multiples = []
    while i < integer:
        if integer%i == 0:
            multiples.append(i)
        i += 1
    
    num_factors = array(len(multiples))
    j = 0
    k = 0
    counter = 0

    while j < len(multiples):
        
        while k < len(multiples):
            if (multiples[j])%(multiples[k]) == 0:
                counter += 1
            k +=1 
        num_factors[j]= counter
        j += 1
        counter = 0
    return multiples, num_factors

print(largest_prime_factor(24))

    
    
#print(largest_prime_factor(13195))

