# open/open modes
animals = open('animals.txt', 'r+')
# r  = open for read (default)
# w  = open for write, truncate
# r+ = open for read/write
# w+ = open for read/write, truncate
# a+ = open for read/append

# read
animals.seek(0)
text = animals.read()
print(text)

# write
animals.write('frog\n')
animals.write('elephant\n')

# reread and print the file
# without seek and read again below, we will need to run it twice to show the updated file
animals.seek(0)
text = animals.read()
print(text)

# close
animals.close()
