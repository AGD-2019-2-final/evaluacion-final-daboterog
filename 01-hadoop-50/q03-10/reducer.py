import sys
if __name__ == "__main__":
    
    for i in sys.stdin:
        clave, valor = i.split("#")
        sys.stdout.write("{}\n".format(valor.rstrip())) 
 
