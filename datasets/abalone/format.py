raw_file = open('abalone.data')

write_str = ""

for line in raw_file:
    if line[0] == 'M':
        write_str += '0'+line[1:]
    elif line[0] == 'F':
        write_str += '1'+line[1:]

write_file = open('abalone.csv', 'w')
write_file.write(write_str)

raw_file.close()
write_file.close()

print("Formatting done!")