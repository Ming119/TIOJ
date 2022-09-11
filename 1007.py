'''
燈泡問題

Description
    我們有一些不同的燈泡，裡面都有一條燈絲，但品質都不是很好，如果持續地讓燈泡亮著的話，燈絲過一會
    兒就燒斷了，因此必須有時將電源切斷，讓燈絲降溫。

    假設一個燈泡最多可以持續點亮 n 單位的時間而不燒斷，而總時間是 m 單位時間。請寫一個程式，給定
    n 和 m 的值，算出有幾種不同的明暗排列方式，每一種排列方式之中都不會出現亮超過連續 n 單位時間
    的區段。

Input Format
    有兩個數字 m 和 n 以一個空白分開, 其中1<=n<=15, 1<=m<=90。
Output Format
    對於每一筆輸入請輸出一個數字, 代表排列方式的總數。每個答案保證不會超過2^(64)-1, 所以你不必
    考慮有大數的情況會發生。

Sample Input
    2 4
Sample Output
    13
'''

n, m = map(int, input().split())

comb = [1]
for i in range(1, n+1):
    comb.append(comb[i-1] << 1)

comb.append((comb[n] << 1) - 1)

for i in range(n+2, m+1):
    comb.append((comb[i-1] << 1) - comb[i-n-2])

print(comb[m])