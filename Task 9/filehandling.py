# open a file for writing
try:
    with open('my_file.txt', 'w') as f:
        # write some data to the file
        f.write('Hello, world!\n')
        f.write('This is some more text.\n')
        f.write('And another line for good measure.\n')
except IOError:
    print('An error occurred while writing to the file.')

# open the same file for reading
try:
    with open('my_file.txt', 'r') as f:
        # read the contents of the file into a variable
        contents = f.read()
        # print the contents to the console
        print(contents)
except IOError:
    print('An error occurred while reading from the file.')
