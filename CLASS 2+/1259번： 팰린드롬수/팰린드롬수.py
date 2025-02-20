import sys

def input():
  return sys.stdin.readline().rstrip()

check = input()

while(int(check) != 0):
    for i in range(len(check)//2):
        if check[i] != check[-1-i]:
          print('no')
          break
    else:
       print('yes')
    
    check = input()

