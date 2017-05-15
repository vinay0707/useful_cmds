# File objects

# f = open('test.txt','r')
#
# print(f.name, f.mode)

# f.close()

# file opening with Context manager
with open('test.txt', 'r') as f:
    # print(f.mode)
    print(f.read())         # reads entire content of a file

# print(f.closed) # file is already closed
# print(f.read()) # error


with open('test.txt', 'r') as f:
    # print(f.mode)
    print(f.readlines())  # reads all lines

with open('test.txt', 'r') as f:
    # print(f.mode)
    print(f.readline())  # read only 1 line

with open('test.txt', 'r') as f:
    for line in f:          # ready line by line
        print(line)

with open('test.txt','r') as f:
    f_contents = f.read(50)            # read 50 bytes only
    print(f_contents)

    print "---"
    f_contents = f.read(50)            # reads next 50 bytes only
    print(f_contents)

with open('test.txt','r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents + '-')
        print(f.tell())             # file current position in the file
        f_contents = f.read(size_to_read)


with open('test.txt','r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents)
    f.seek(0)                       # mover file cursor to begining of the file
    f_contents = f.read(size_to_read)
    print(f_contents)

## Writing a new file

with open('test2.txt','w') as f:        # 'w' overwrite if file exists, 'a' append to existing file
    f.write('test1')
    f.write('test2')

with open('test.txt','r') as rf:            # reads ASCII file
    with open('test_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)

with open('canon.jpg','rb') as rf:            # reads BINARY file
    with open('canon_cpy.jpg','wb') as wf:
        for line in rf:
            wf.write(line)