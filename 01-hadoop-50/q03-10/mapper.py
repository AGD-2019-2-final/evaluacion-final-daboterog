import sys
if __name__ == "__main__":
    for i in sys.stdin:
        datos = i.rstrip().split(',')
        sys.stdout.write("{}#{}\n".format(datos[1],i.rstrip()))
