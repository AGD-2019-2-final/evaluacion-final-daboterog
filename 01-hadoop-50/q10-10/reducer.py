import sys
if __name__ == '__main__':
    
    letra_actual = None
    numeros = 0

    for line in sys.stdin:

        letra, num = line.split("\t")
        num = int(num)

        if letra == letra_actual:
            numeros = str(numeros) + ',' + str(num) 
        else:
            if letra_actual is not None:
                if letra_actual !=',':
                    sys.stdout.write("{}\t{}\n".format(letra_actual, numeros))

            letra_actual = letra
            numeros =  int(num)

    sys.stdout.write("{}\t{}\n".format(letra_actual, numeros))
