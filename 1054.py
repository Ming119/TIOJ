'''
[入門]難度2.星期幾咧

Description
    「今天是星期一的話，那麼五天後是星期幾？」這個問題的答案很顯然是「星期六。」
    我們都知道星期的計算方式是星期日、一、二、三、四、五、六、日，然後再回到星期一…
    翻譯成英文就是 Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday.

    現在我們將這個問題推廣：
    「今天是 XXX 的話，那麼 N 天後是星期幾？」其中XXX是星期一到星期日當中的某一天，N是一個正整數。
    請你寫一個程式解決這個問題。

Input Format
    輸入包含兩行，第一行有一個英文單字(可能是星期一到星期日當中的某一個)。
    第二行有一個正整數 N (1<=N<=100,000)。
Output Format
    請你用英文回答N天後是星期幾。

Sample Input
    Sample Input #1:
        Monday
        5
    Sample Input #2:
        Friday
        7
Sample Output
    Sample Output #1:
        Saturday
    Sample Output #2:
        Friday
'''

week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

day = input()
N = int(input())

print(week[(week.index(day) + N) % 7])

