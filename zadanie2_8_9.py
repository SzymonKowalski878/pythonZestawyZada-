from file_manager import FileManager

test = FileManager('tekst.txt')
print(test.read_file())
test.update_file('ppies')
print(test.read_file())
test.update_file('dsadsadsa')
print(test.read_file())
