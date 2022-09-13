'''
[入門]難度1.除法練習

Description
    給你兩個正整數P,Q，請你判斷比較大的數是否能夠被比較小的數整除？

Input Format
    兩個正整數P,Q(1<=P,Q<=10,000)。
Output Format
    如果P,Q當中較小者可以整除較大者的話請輸出'Y'，否則請輸出'N'。

Sample Input
    Sample Input #1:
        3 5
    Sample Input #2:
        10 2
Sample Output
    Sample Output #1:
        N
    Sample Output #2:
        Y
'''

P, Q = map(int, input().split())

if P > Q:
    P, Q = Q, P

if Q % P == 0:
    print('Y')
else:
    print('N')
