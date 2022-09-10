'''
Prefix and Postfix

Description
    我們說字串 A 是字串 B 的Prefix(前綴字串)，若且唯若字串 B 的前 len(A) 個字母與 A 完全相
    同，其中 len(A) 指的是字串 A 的長度。例如： “Exam”和 “Example”都是 “Example”的
    Prefix，但是 “Ample”和 “Exapple”都不是 “Example”的 Prefix。同樣的，當 B 的後
    len(A) 個字母與 A 完全相同的時候，我們稱 A 是 B 的 Suffix (後綴字串)。給定兩個字串 P，
    Q，請你找出最長的字串 S 使得 S 是 P 的Prefix，同時也是 Q 的 Suffix。

Input Format
    兩個字串 P，Q 各佔一行，只包含小寫英文字母，長度皆不超過1000字元。
Output Format
    輸出最長的字串 S 的長度 len(S)。

Sample Input
    example
    exam
Sample Output
    4
'''

P = input()
Q = input()

len = min(len(P), len(Q))
for i in range(len, 0, -1):
    if P[:i] == Q[-i:]:
        print(i)
        break
else: print(0)