def insertInterval(intervals, newInterval):
    result = []
    i = 0
    for i in intervals:
        if i[1] < newInterval[0]:
            result.append(i)
        elif i[0] > newInterval[1]:
            result.append(newInterval)
            newInterval = i
        else:
            newInterval = [min(i[0], newInterval[0]), max(i[1], newInterval[1])]

    result.append(newInterval)
    return result

intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(insertInterval(intervals, newInterval)) # [[1, 5], [6, 9]]