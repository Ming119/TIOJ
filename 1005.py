'''
圓周率問題

Description
    英國一個大學教授Robert A.J. Matthews根據夜空中劃過天際的星星的位置，讓人驚訝的推論出關於
    pi（圓周率）的準確度。當然，這牽扯到數論的理論及應用。在此，我們沒有夜空，但是我們要用相同的
    理論來估計 pi 的值：
    
    從一個數量龐大的數的集合中隨機的取2個數, 這2個數互質(就是沒有比1大的公因數)的機率是:
        6/pi^2
    
    例如：假設一個數的集合為{2,3,4,5,6}, 可以形成10對數。其中(2,3), (2,5), (3,4), (3,5),
    (4,5), (5,6)這6對數互質。所以我們可以推出:
        6/pi^2 ~= 6/10
            pi ~= 3.162
    
    在這個問題中, 給你一些數, 要請你估計出 pi 的值。

Input Format
    輸入包含多組測試資料。每組測試資料的第一列有一個正整數 N（1 < N < 50），代表集合中元素的個
    數。接下來的 N 列每列各有一個正整數，代表此集合中的數。這些數都大於0，並且小於32768。
    N = 0 代表輸入結束。請參考 Sample Input。
Output Format
    對每一組測試資料，輸出你所估計 pi 的值，四捨五入到小數點後6位。如果沒有任何一對數互質，請輸
    出 `No estimate for this data set.`
    請參考Sample Output。

Sample Input
    5
    2
    3
    4
    5
    6
    2
    13
    39
    0
Sample Output
    3.162278
    No estimate for this data set.
'''

def isCoprime(a: int, b: int) -> bool:
    if a == 1 or b == 1: return True
    if a == b: return False
    if a > b: a, b = b, a

    for i in range(2, a+1):
        if a % i == 0 and b % i == 0:
            return False
    return True

while True:
    N = int(input())
    if N == 0: break

    data = [int(input()) for _ in range(N)]
    count = 0
    for i in range(N-1):
        for j in range(i+1, N):
            count += 1 if isCoprime(data[i], data[j]) else 0

    if count == 0:
        print('No estimate for this data set.')
    else:
        print('{:.6f}'.format((6 * (N/2*(N-1)) / count) ** 0.5))