import sys
sys.stdin = open('input.txt', encoding='UTF-8')

#Man1 = M1
#Man2 = M2

Man1 = input()
Man2 = input()

if Man1 == '바위' and Man2 == '가위':
    print('Result : Man1 Win!')

elif Man1 == '가위' and Man2 == '바위':
    print('Result : Man2 Win!')