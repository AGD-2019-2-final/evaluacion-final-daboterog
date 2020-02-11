import sys
if __name__ == "__main__":
    for line in sys.stdin:
        splits = line.split(",")
        ch = splits[2]
        print(ch + '\t' + "1")
        #sys.stdout.write("{}\1n".format(ch))
