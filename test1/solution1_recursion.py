from datetime import datetime
       
def createMatrix(event):
    
    matrix = [[0 for col in range(len(event))] for row in range(len(event))]
    
    for i in range(len(event)):
        for j in range(len(event)):
            if i >= j:
                matrix[i][j] = 0
            else:
                activity_1 = event[chr(i+65)] # convert number to letter with ascii
                activity_2 = event[chr(j+65)] # convert number to letter with ascii
                
                time_activity_1 = [elem for elem in activity_1.split(' - ')]
                time_activity_2 = [elem for elem in activity_2.split(' - ')]
              
                if datetime.strptime(time_activity_1[1], '%H:%M').time() <= datetime.strptime(time_activity_2[0], '%H:%M').time():
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 0
    return matrix

    
def recursion(track, matrix, row):
    global metmoi
    
    if sum(matrix[row]) == 0:
        metmoi.append(track)
        return
    
    else:
        for col in range(len(event)):
    
            if matrix[row][col] == 1:
                track.append(col)
                return recursion(track, matrix, col)
                track.pop()
        
    

event = {'A': '8:00 - 9:30', 
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
        
matrix = createMatrix(event)

track = []
metmoi = []

for row in range(len(event)):
    track.append(row)
    recursion(track, matrix, row)
    track = []
    
ans, largest = [], 0
for elem in metmoi:
    if len(elem) > largest:
        largest = len(elem)
        ans = elem
    
print([chr(i+65) for i in ans])


    
