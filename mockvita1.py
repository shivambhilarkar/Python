# n = int(input())
# b = input()
# g = input()

# i = 0
# while i<n:
#     d = g.find(b[0])
#     if d<0:
#         break
#     g = g[d+1:]+g[:d]
#     b = b[1:]
#     i = i + 1
# print(len(b))


def swaym(x,y):
    rem_m=(abs((x.count('m')) - (y.count('m'))))
    rem_r=(abs((x.count('r'))-(y.count('r'))))
    return(int(rem_m)+int(rem_r))
t=int(input())
x,y=map(str,input().split())
x=str(x)
y=str(y)
print(swaym(x,y))








