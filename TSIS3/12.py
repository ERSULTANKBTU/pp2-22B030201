def histogram(x):
    for i in range(max(x)):
        line = ''
        for j in range(len(x)):
            if x[j] >= (i + 1):
                line += '*'
            else:
                line += ' '
        print(line)
s = list(map(int, input().split()))
print(histogram(s))
        