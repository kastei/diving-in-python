import sys


n = int(sys.argv[1])
for x in range(1, n+1):
    print(' ' * (n - x) + '#' * x)
