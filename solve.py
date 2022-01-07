import sys

def main(a, b):
    print(-b/a)

if __name__ == '__main__':
    exit(main(float(sys.argv[1]), float(sys.argv[2])))
