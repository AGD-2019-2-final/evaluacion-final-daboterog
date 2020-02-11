import sys
if __name__ == "__main__":
    aux=[]
    for i in sys.stdin:
        letra, fecha, numero = i.split("\t")
        numero = int(numero)
        aux.append([letra, fecha, numero])
    aux = sorted(aux, key=lambda x: (x[0], x[2]))
    for k in aux:
        sys.stdout.write("{}\t{}\t{}\n".format(k[0], k[1], k[2]))
