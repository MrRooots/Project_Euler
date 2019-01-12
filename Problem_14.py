def Collatz_sequence():
    ex_number = 1
    chain_length = 0
    max_chain_length = 0
    while ex_number < 1000000:
        number = ex_number
        while number > 1:
            if number % 2 == 0:
                number //= 2
                chain_length += 1
            else:
                number = 3 * number + 1
                chain_length += 1
        if chain_length > max_chain_length:
            max_chain_length = chain_length
            result = ex_number
        ex_number += 1
        chain_length = 0
    return max_chain_length, result

print(Collatz_sequence())