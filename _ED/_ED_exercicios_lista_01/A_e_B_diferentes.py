def analisa(var1, var2):

    var1, var2 = int(input()), int(input())

    if var1 == var2:
        print(f'{var1}\n{var2}\niguais')
    else:
        if var1 > var2:
            print(f'{var1}\n{var2}\ndiferentes')
        else:
            print(f'{var2}\n{var1}\ndiferentes')