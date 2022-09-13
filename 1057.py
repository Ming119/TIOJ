'''
[入門]難度5.過河拆橋

Description
    你有一塊長M公尺的輕便可攜式木橋，正準備渡過一條寬P公尺的河流。這條河流上總共有N個木樁，這些木
    樁的排列方式恰好形成一條垂直於河流流向的直線。你是否能夠利用這塊可攜式木橋達到過河的任務呢？如
    果可以過河，至少要拆幾次橋呢？
    你可以假設木樁只是一個點，不具有任何長度或寬度。

Input Format
    輸入包含兩列，第一列有三個正整數M,P,N (1<=M,P<=231-1, 1<=N<=100)
    第二列包含N個嚴格遞增的正整數S1,S2,...,SN (1<=Si<P)。
    你要從河岸標記為0公尺的位置渡到標記為P公尺的對岸。
Output Format
    如果可以過河，請輸出拆橋的次數。否則請輸出"IMPOSSIBLE"。

Sample Input
    Sample Input #1:
        8 50 10
        2 6 14 22 30 38 46 47 48 49
    Sample Input #2:
        10 8 1
        5
    Sample Input #3:
        1 100 1
        50
Sample Output
    Sample Output #1:
        6
    Sample Output #2:
        0
    Sample Output #3:
        IMPOSSIBLE
'''

M, P, N = map(int, input().split())

S = list(map(int, input().split()))

if M >= P:
    print(0)
    exit()

count = 0
current_point = 0
for i in S:
    if i > M: break
    current_point = i

while current_point < P:
    if current_point + M >= P:
        print(count+1)
        break

    for i in range(current_point + M, current_point, -1):
        if i in S:
            current_point = i
            count += 1
            break
    else:
        print('IMPOSSIBLE')
        break