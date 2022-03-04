from datetime import datetime

activity = {'A': '8:00 - 9:30', 
            'B': '8:00 - 10:00',
            'C': '9:30 - 11:00',
            'D': '11:00 - 12:00',
            'E': '13:00 - 14:00',
            'F': '10:00 - 11:00',
            'G': '11:00 - 15:00',
            'H': '15:00 - 17:00',
            'I': '14:00 - 16:00',
            'J': '15:00 - 16:00',
            'K': '16:00 - 17:00'}

ans = [] # store the result in an array

# store start time and end time of activities in the dictionary
start_time, end_time = {}, {}
for key, val in activity.items():
    start_time[key] = val.split(' - ')[0]
    end_time[key] = val.split(' - ')[1]
    
# sort end time in ascending order
end_time = sorted(end_time.items(), key=lambda item: datetime.strptime(item[1], '%H:%M').time())

# compare end time of activity i with start time of activity j
# end_time: type(list)
# start_time: type(dict)
e = end_time[0][1]
ans.append(end_time[0][0])
for i in range(1, len(start_time)):
    s = start_time[end_time[i][0]]
    if datetime.strptime(e, '%H:%M').time() <= datetime.strptime(s, '%H:%M').time():
        e = end_time[i][1]
        ans.append(end_time[i][0])
print(ans)
