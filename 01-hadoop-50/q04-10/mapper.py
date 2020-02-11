import sys

if __name__ == "__main__":
    for i in sys.stdin:
        a = i.split()
        sys.stdout.write("{}\t1\n".format(a[0]))
