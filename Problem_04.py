def LargestPalindrome(number): # Функция проверяет является ли число палиалиндромом
    num = str(number)
    if len(num) % 2 == 0: # Если кол-во цифр числа четное
        s1 = num[0:int(len(num) / 2)] # То она просто берет одну его половину
        s2 = num[int(len(num) / 2):] # И вторую :)
    else:
        s1 = num[0:int(len(num) / 2)] # Иначе берет опять же половину (целое число)
        s2 = num[int((len(num) / 2)) + 1:] # Берет вторую половину, игнорируя цифру посередине
    return s1 == s2[::-1] # Возвращает True\ False, в зависимости от того, является ли число палиндромом

result = 0
multiple = 0
# Простейший цикл в цикле, - решение в лоб:
for init in range(100, 1000):
    for init_1 in range(100, 1000):
        multiple = init * init_1
        # Если при подставлении числа в ф-цию было получено True, и если это число больше предыдущих, то:
        if (LargestPalindrome(multiple)) and (multiple > result):
            result = multiple

print(result)
