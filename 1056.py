'''
[入門]難度4.圈圈叉叉

Description
    大家應該都有玩過「井字遊戲」吧？
    在這個遊戲中，先手是O，後手是X。兩人輪流在一個井字形狀的棋盤中的一個空格畫上O或X，一旦出現同
    樣的O(或X)連成一條線(直的、橫的或對角線)，那麼遊戲終止，且先手(或後手)獲勝。如果九個格子都被
    填滿，還沒有人獲勝，那麼遊戲也終止，且兩個人平手。
    我們用3x3的字元陣列代表一個盤面，例如：
        ...
        .O.
        OXX
    其中'.'代表空格，'O'以及'X'分別代表先手和後手所放置的符號。
    喔當然，裡面不能出現其它字元的。
    現在給你一個盤面，請你判斷這個盤面是否為遊戲過程、或遊戲終止時可能的盤面？

Input Format
    總共有3列，每列3個字元，總共九個字元。
Output Format
    如果這個盤面是遊戲過程或遊戲終止時可能的盤面，請你輸出"POSSIBLE"，否則輸出"IMPOSSIBLE"。

Sample Input
    Sample Input #1:
        ...
        ...
        ...
    Sample Input #2:
        ..O
        .O.
        OXX
    Sample Input #3:
        ..O
        .O.
        O..
    Sample Input #4:
        XOX
        OOX
        OXO
    Sample Input #5:
        ORZ
        ...
        ...
Sample Output
    Sample Output #1:
        POSSIBLE
    Sample Output #2:
        POSSIBLE
    Sample Output #3:
        IMPOSSIBLE
    Sample Output #4:
        POSSIBLE
    Sample Output #5:
        IMPOSSIBLE
'''

def isPossible(board: list[str]) -> bool:
    countO = 0
    countX = 0

    for row in board:
        for char in row:
            if char != '.' and char != 'O' and char != 'X': return False
            if char == 'O': countO += 1
            elif char == 'X': countX += 1
    if countO > countX + 1 or countX > countO: return False
    if isWin(board, 'O') and isWin(board, 'X'): return False
    if isWin(board, 'O') and countO != countX + 1: return False
    if isWin(board, 'X') and countO != countX: return False
    
    return True

def isWin(board: list[str], char: str) -> bool:
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == char: return True
        if board[0][i] == board[1][i] == board[2][i] == char: return True
    if board[0][0] == board[1][1] == board[2][2] == char: return True
    if board[0][2] == board[1][1] == board[2][0] == char: return True
    return False

board = list(input() for i in range(3))

print('POSSIBLE' if isPossible(board) else 'IMPOSSIBLE')
