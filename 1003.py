'''
切義大利餅問題

Description
    電腦程式語言的架構中，遞迴函數可說是較特殊的一種，因函數可以呼叫函數本身自己。

    請設計一個程式，用遞迴函數解決下面兩小題(Problem 1003, Problem 1004)。
    
    設有一 16 吋義大利脆餅，今欲以刀切餅，每刀均以直線方式切於餅面，第一刀可將脆餅切成兩片，二刀
    至多可分成 4 片，三刀至多可分成 7 片，試問 n 刀至多可將脆餅切成幾片？令 f(n) 為 n 刀將脆
    餅分成的片數，則 f(0) = 1。

Input Format
    一個正整數 n (1 <= n <= 50)。
Output Format
    輸出f(n)之值。

Sample Input
    3
Sample Output
    7
'''

def f(n: int) -> int:
    if n == 0: return 1
    return f(n-1) + n

n = int(input())

print(f(n))