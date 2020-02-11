import sys
if __name__ == "__main__":
    curr = None
    ma = 0
    for i in sys.stdin:
        key, val = i.split(",")
        val = int(val)
        if curr == None:
            curr = key
            ma = val
        elif key == curr:
            if val > ma:
                ma = val
         
        elif key != curr:
            sys.stdout.write("{}\t{}\n".format(curr, ma))   
            curr = key
            ma = val  
    sys.stdout.write("{}\t{}\n".format(curr, ma)) 
