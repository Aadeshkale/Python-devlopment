import argparse


def sq(n):
    return n**2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('num',help="arg for to find square",type=int)
    parser.add_argument('-o','--output',help='to write result in output file',action="store_true")
    args = parser.parse_args()
    res = sq(args.num)
    print(res)
    if args.output:
        with open('output.txt','w') as f:
            f.write(str(res))


if __name__ == '__main__':
    main()