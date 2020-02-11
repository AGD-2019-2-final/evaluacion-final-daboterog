import sys
if __name__ == "__main__":
    curatr = None
    total = 0
    for i in sys.stdin:
        key, val = i.split("\t")
        val = int(val)
        if key == curatr:
            curatr= key
            total += val
        else:
            if curatr is not None:
                sys.stdout.write("{}\t{}\n".format(curatr, total))

            curatr = key
            total = val

    sys.stdout.write("{}\t{}\n".format(curatr, total))
