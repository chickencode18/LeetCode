import math


def solve():
   n,q = map(int,input().split())
   a = list(map(int,input().split()))
   for _ in range(q):
        l,r,k = map(int,input().split())
        sum = 0
        for i in range(n):
            if i>=l-1 and i<=r-1:
                sum+=k
            else:
                sum+=a[i]
        if sum%2!=0:
            print('YES','\n')
        else:
            print('NO','\n')
        
            

def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
