def freq(data):
    biggest = 0
    num = data[0]
    for i in data:
        curr_frequency = data.count(i)
        if (curr_frequency > biggest) or ((curr_frequency == biggest) and (i > num)):
            biggest = curr_frequency
            num = i

    return num
