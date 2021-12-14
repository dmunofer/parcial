import os

def verticalRooks(r1, r2):
    or_exclusivo = 0
    for x, y in zip(r1, r2):
        or_exclusivo ^= (abs(x-y)-1)
    if or_exclusivo!=0:
        return 'Player 2'
    else:
        return 'Player 1'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        r1 = []
        for _ in range(n):
            r1_item = int(input().strip())
            r1.append(r1_item)
        r2 = []
        for _ in range(n):
            r2_item = int(input().strip())
            r2.append(r2_item)
        result = verticalRooks(r1, r2)
        fptr.write(result + '\n')
    fptr.close()
