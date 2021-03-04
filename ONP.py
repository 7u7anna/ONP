#Napisz algorytm , ktory wyznaczy wartosc wyrazenia zapisanego w ONP

s = str(input())
T = []
def algorytmONP(T, s):
    n = len(s)
    for i in range(n):
        if s[i].isdigit():
           T.append(s[i])
        else:
            if s[i] == '+':
                y = T[-2]
                x = T[-1]
                count = int(T[-2]) + int(T[-1])
                T.remove(x)
                T.remove(y)
                T.append(count)
            if s[i] == '-':
                y = T[-2]
                x = T[-1]
                count1 = int(T[-2]) - int(T[-1])
                T.remove(x)
                T.remove(y)
                T.append(count1)
            if s[i] == '*':
                y = T[-2]
                x = T[-1]
                count2 = int(T[-2]) * int(T[-1])
                T.remove(x)
                T.remove(y)
                T.append(count2)
            if s[i] == '/':
                y = T[-2]
                x = T[-1]
                count3 = int(T[-2]) / int(T[-1])
                T.remove(x)
                T.remove(y)
                T.append(count3)             
algorytmONP(T, s)
print(T)
