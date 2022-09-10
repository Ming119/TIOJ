'''
Rails

Description
    現在火車從A方向來，預定從B方向離開。火車共有N節車廂，並且各車廂依次以1到N來編號。你可以假設
    各車廂在進站之前可以單獨與其他車廂分離，也可以單獨離開車站到往B方向的鐵軌或是車站北方的「維修
    鐵路」上。維修鐵路是一小段至多只能容納M節車廂的鐵軌，可以從車站依照順序將車廂移至維修鐵路，或
    者將車廂從維修鐵路（如果有的話）駛進車站，但是在把車廂從A開進車站的時候，維修鐵路不能有任何車
    廂。你可以假設在任何時間火車站都可以容納所有的車廂。但是一旦一節車廂進站後，就不能再回到A方向
    的鐵軌上了，並且一旦離開車站往B方向後，也不能再回到車站。
    現在你的任務是寫一個程式，判斷火車能否以一特定的排列方式在B方向的鐵軌上。

Input Format
    第一行有兩個正整數N，M。(1<=N<=1000，0<=M<=9)
    第二行有 N 個正整數，為1,2,...,N的一個排列。
Output Format
    若能在B鐵軌上排出特定排列，請輸出yes，否則請輸出no。

Sample Input
    5 1
    3 2 5 1 4
Sample Output
    yes
'''

N, M = map(int, input().split())
train = list(map(int, input().split()))

station_track  = []
maintain_track = []

index = 0
for i in range(1, N+1):
    station_track.append(i)

    while station_track and station_track[-1] == train[index]:
        station_track.pop()
        index += 1
    
    if station_track and train[index] in station_track and train[index] not in station_track[~M:]:
        print('no')
        break
    
    if station_track and train[index] in station_track[~M:]:
        while station_track[-1] != train[index]:
            maintain_track.append(station_track.pop())
        station_track.pop()
        index += 1

        while maintain_track:
            station_track.append(maintain_track.pop())
else:
    print('yes')