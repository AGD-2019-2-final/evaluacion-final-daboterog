import sys
if __name__ == "__main__":
    curr = None
    cuenta = 0
    for i in sys.stdin:
        key, val = i.split("\t")
        val = int(val)
        if curr == None:
            curr = key
            cuenta = cuenta + 1
            
        elif key == curr:
            cuenta = cuenta + 1
                     
        elif key != curr:
            sys.stdout.write("{},{}\n".format(curr, cuenta))   
            curr = key
            cuenta = 1
            
    sys.stdout.write("{},{}\n".format(curr, cuenta)) 
