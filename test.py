import math


def solve():
    n = int(input())
    a = list(map(int,input().split()))

    total = sum(a)
    if total%3==0:
        print(0,'\n')
    else:
        print(3*(total//3 + 1) - total,'\n' )
         
            

def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
