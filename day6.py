with open('input/day6.txt') as f:
    data = f.read().strip()

# Part 1
marker_length = marker = 4
for i in range(marker, len(data)):
    if data[i] in data[i-marker_length:i] or len(set(data[i-marker_length:i])) < marker_length:
        continue
    else:
        marker = i + 1
        break
print(marker)

# Part 2
message = max(14, marker)
for i in range(message, len(data)):
    if data[i] in data[i-13:i] or len(set(data[i-13:i])) < 13:
        continue
    else:
        message = i + 1
        break
print(message)
