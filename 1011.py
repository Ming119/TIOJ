'''
Edit Distance In Numbers

Description
    對於字串來說，Edit Distance是一個著名的DP問題。現在我們把這個問題弄得簡單一點，例如：把字
    串換成數字。對於一個數字 A，我們想要藉由某些操作換成數字 B。而對於整數 K 的一個合法的操作包
    括以下三種情形：
        乘以 2 加 1，即 K = 2K + 1
        乘以 2，即 K = 2K
        除以 2，即 K = floor(K/2)
    給定整數 A 和 B，請你求出最小的操作次數 N 使得從 A 開始操作 N 次可以換成 B。

Input Format
    包含兩個數字 A，B (0 <= A，B <= 2^(31))。
Output Format
    請輸出最小操作次數N。

Sample Input
    17
    15
Sample Output
    7
'''

A = int(input())
B = int(input())

total = 0
while A != B:
    if A > B: A //= 2
    else: B //= 2
    total += 1

print(total)
