import sys
if __name__ == "__main__":
    
    for line in sys.stdin:
        
        numero = int(line.split('\t')[0])
        numero1 = "{:03.0f}".format(numero)

        letra = line.split('\t')[1]
        letras = letra.rstrip('\r\n')

        for i in range(len(letras)):
            sys.stdout.write("{}\t{}\n".format(str(letras[i]),numero1))
