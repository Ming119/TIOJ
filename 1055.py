'''
[入門]難度3.好多星星

Description
    給你一個數字，請你參考範例輸入輸出的形式畫出星星。

Input Format
    兩個正整數A,B(1<=A,B<=100, |A-B|<=20)
Output Format
    請參考範例輸出。

Sample Input
    Sample Input #1:
        4 7
    Sample Input #2:
        10 1
Sample Output
    Sample Output #1:
        ****
        *****
        ******
        *******

    Sample Output #2:
        **********
        *********
        ********
        *******
        ******
        *****
        ****
        ***
        **
        *
'''

A, B = map(int, input().split())

if A < B:
    for i in range(A, B+1):
        print('*' * i)

else:
    for i in range(A, B-1, -1):
        print('*' * i)
