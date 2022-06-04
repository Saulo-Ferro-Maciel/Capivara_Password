# Test
import random as ram

s = str(input("Digite uma palavra que deseja incluir na senha: ")).rstrip(" ").lstrip(" ")
ss = int(float(len(s)))
print(ss)
dd = list()
while True:
    if ss != 0:
        if ss == 4:
            for i in range(0,4):
                a = ram.randint(0,9)
                d = a
                dd.append(d)
            print(dd)
        else:
            if ss ==3:
                for i in range(0,5):
                    a = ram.randint(0,9)
                    d = a
                    dd.append(d)
                print(dd)
            elif ss ==1:
                for i in range(0,7):
                    a = ram.randint(0,9)
                    d = a
                    dd.append(d)
                print(dd)
            elif ss ==2:
                for i in range(0,6):
                    a = ram.randint(0,9)
                    d = a
                    dd.append(d)
                print(dd)
        dd = ''.join(map(str,dd))
        senha = f'{s}{dd}'
        print(senha)
        break
    else:
        if ss == 0:
            s = str(input("Digite uma palavra que deseja incluir na senha: ")).rstrip(" ").lstrip(" ")