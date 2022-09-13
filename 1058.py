'''
[入門]難度5.兩個數字

Description
    給你兩個數字，請你輸出比較大的那個。

Input Format
    兩個數字A,B(1<=A,B<=1000,A不等於B)。
Output Format
    請完整地輸出A與B中比較大的那個數。

Sample Input
    Sample Input #1:
        3 5
    Sample Input #2:
        10.1 12.3
Sample Output
    Sample Input #1:
        5
    Sample Input #2:
        12.3
'''

A, B = input().split()

a , b = A, B

indexOfDotA = a.find('.')
indexOfDotB = b.find('.')

if indexOfDotA == -1:
    a += '.'
    indexOfDotA = a.find('.')

if indexOfDotB == -1:
    b += '.'
    indexOfDotB = b.find('.')

a = '0'*(indexOfDotB-indexOfDotA) + a + '0'*(indexOfDotA-indexOfDotB)
b = '0'*(indexOfDotA-indexOfDotB) + b + '0'*(indexOfDotB-indexOfDotA)

bigger = max(a, b)

if bigger == a: print(A)
else: print(B)
