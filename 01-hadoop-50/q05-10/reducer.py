import sys
if __name__ == "__main__":
    curr = None
    numero = 0
    for i in sys.stdin:
        key, val = i.split(",")
        val = int(val)
        if curr == None:
            curr = key
            numero = val
        elif key == curr:
            numero = numero + 1
                     
        elif key != curr:
            sys.stdout.write("{}\t{}\n".format(curr, numero))   
            curr = key
            numero = val  
    sys.stdout.write("{}\t{}\n".format(curr, numero)) 
