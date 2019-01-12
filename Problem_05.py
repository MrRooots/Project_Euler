def smallest_multiple():
    number = 20
    flag = False
    while flag == False:
        if number % 2 == 0:
            if number % 3 == 0:
                if number % 5 == 0:
                    if number % 7 == 0:
                        if number % 9 == 0:
                            if number % 11 == 0:
                                if number % 13 == 0:
                                    if number % 14 == 0:
                                        if number % 16 == 0:
                                            if number % 17 == 0:
                                                if number % 19 == 0:
                                                    if number % 20 == 0:
                                                        flag = True
                                                        return number
                                                else:
                                                    number += 20
                                            else:
                                                number += 20
                                        else:
                                            number += 20
                                    else:
                                        number += 20
                                else:
                                    number += 20
                            else:
                                number += 20
                        else:
                            number += 20
                    else:
                        number += 20
                else:
                    number += 20
            else:
                number += 20
        else:
            number += 20


print(smallest_multiple())