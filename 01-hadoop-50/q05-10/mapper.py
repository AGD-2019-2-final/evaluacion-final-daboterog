import sys
if __name__ == "__main__":
    for i in sys.stdin:
        a = i.split("-")
        ##print(a[1])
        sys.stdout.write("{},{}\n".format(a[1],1))
