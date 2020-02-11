import sys
if __name__ == "__main__":
    curr = None
    menor = 0
    mayor = 0
    for i in sys.stdin:
        key, val = i.split("\t")
        val = float(val)
        if curr == None:
            curr = key
            menor = val
            mayor = val
        elif key == curr:
            mayor = max(val, mayor)
            menor = min(val, menor)
                     
        elif key != curr:
            sys.stdout.write("{}\t{}\t{}\n".format(curr, mayor, menor))   
            curr = key
            menor = val
            mayor = val
    sys.stdout.write("{}\t{}\t{}\n".format(curr, mayor, menor)) 
