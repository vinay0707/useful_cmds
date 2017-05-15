from sys import argv

script, filename = argv

txt = open(filename)

print "flilename: %r" %filename

print txt.read()

print "type the filename again:"
file_again = raw_input("> ")
txt = open(file_again)

print txt.read()


