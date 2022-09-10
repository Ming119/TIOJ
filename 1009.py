'''
In No Time!

Description
    考試時間所剩不多，你能夠把握剩下時間完成所有題目嗎？給你現在時間以及考試終止時間，請你判斷還
    剩下多少時間可以做題目。

Input Format
    輸入有兩行，第一行表示現在時間，第二行表示考試終止時間。時間的格式為HH:MM:SS (時：分：秒)，
    終止時間永遠比現在時間晚，但兩者時間差不會超過一天(24小時)。(請注意：兩者的時間點不一定都在
    同一日。)
Output Format
    請輸出距離考試結束還有多久時間，以HH:MM:SS表示。

Sample Input
    14:00:00
    10:00:00
Sample Output
    20:00:00
'''

current_time = list(map(int, input().split(':')))
end_time     = list(map(int, input().split(':')))

second = end_time[2] - current_time[2]
if second < 0:
    second += 60
    end_time[1] -= 1

minute = end_time[1] - current_time[1]
if minute < 0:
    minute += 60
    end_time[0] -= 1

hour   = end_time[0] - current_time[0]
if hour < 0:
    hour += 24

print(f'{hour:02}:{minute:02}:{second:02}')