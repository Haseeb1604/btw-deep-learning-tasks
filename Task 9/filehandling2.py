import os

# create a directory to store our files
try:
    os.mkdir('my_files')
except FileExistsError:
    print('Directory already exists.')

# create a list of file names
file_names = ['file1.txt', 'file2.txt', 'file3.txt']

# iterate over the list of file names and write some text to each file
for name in file_names:
    try:
        with open(f'my_files/{name}', 'w') as f:
            f.write(f'This is some text for {name}.\n')
            f.write('And another line for good measure.\n')
            f.write('Bytewise Task for filehandling')
    except IOError:
        print(f'An error occurred while writing to {name}.')

# iterate over the list of file names and read the contents of each file
for name in file_names:
    try:
        with open(f'my_files/{name}', 'r') as f:
            contents = f.read()
            print(f'Contents of {name}:')
            print(contents)
    except IOError:
        print(f'An error occurred while reading from {name}.')
