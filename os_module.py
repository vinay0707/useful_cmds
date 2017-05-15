import os

# print module details
print(dir(os))

print(os.getcwd())

os.chdir('../')

print(os.getcwd())

# change dir
os.chdir('./handson')

# get current working dir
print(os.getcwd())

# walk - nested directory details
for dirpath, dirnames, filesnames in os.walk(os.getcwd()):
    print('Current Path : ', dirpath)
    print('Dir : ', dirnames)
    print('Files : ', filesnames)
    print()


# get the environment variable value
print(os.environ.get('HOME'))

# Print the complete file path
file_path = os.path.join(os.environ.get('HOME'),'test.txt')
print(file_path)

#print base file name
print(os.path.basename('/Users/Anvi/test.txt'))

# split path and filename
print(os.path.split('/Users/Anvi/test.txt'))

# split filename and extension
print(  os.path.splitext('test.txt'))


#check if file exists
print(os.path.exists('/Users/Anvi/test.txt'))

#check if it is a dir
print(os.path.isdir('/Users/Anvi/test.txt'))

#check if  it is a file
print(os.path.isfile('/Users/Anvi/test.txt'))


