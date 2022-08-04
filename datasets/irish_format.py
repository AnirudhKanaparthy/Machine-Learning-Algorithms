rawfile = open('iris.data')

wrt_str = ''

for line in rawfile:
    line = line.strip()
    data = line.split(',')
    if data[-1] == 'Iris-setosa':
        wrt_str += ','.join(data[:-1]) + ',0\n'
    elif data[-1] == 'Iris-versicolor':
        wrt_str += ','.join(data[:-1]) + ',1\n'
    elif data[-1] == 'Iris-virginica':
        pass
rawfile.close()


wrt_file = open('iris.csv', 'w')
wrt_file.write(wrt_str)

wrt_file.close()
print('Formatting Done!')