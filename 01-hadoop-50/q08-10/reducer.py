import sys
if __name__ == "__main__":
    curr = None
    suma = 0
    cuenta = 1
    promedio = 0
    for i in sys.stdin:
        key, val = i.split("\t")
        val = float(val)
        if curr == None:
            curr = key
            suma = suma + val
            promedio = suma/cuenta
        elif key == curr:
            suma = suma + val
            cuenta = cuenta + 1
            promedio = suma/cuenta                     
        elif key != curr:
            sys.stdout.write("{}\t{}\t{}\n".format(curr, suma, promedio)) 
            curr = key
            suma = val
            cuenta = 1
            promedio = val
    sys.stdout.write("{}\t{}\t{}\n".format(curr, suma, promedio)) 
