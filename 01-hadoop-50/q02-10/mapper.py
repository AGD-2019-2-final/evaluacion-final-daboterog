import sys
if __name__ == "__main__":
    for line in sys.stdin:
        splits = line.split(",")
        proposito = splits[3]
        monto = splits[4]
        print(proposito + ',' + monto)
        #sys.stdout.write("{}\1n".format(ch))
