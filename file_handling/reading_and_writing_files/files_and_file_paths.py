print("Variables store data when a program is running")
print("Files persist data after a program has stopped running")
print("File's content - Think of it as a single string value potentially gigabytes in size")

print('' * 99)

print("A file has two key properties:")
print("1. filename - this is the name of the file (usually written as one word) - Additionally (optional in some OS like Linux) the part of the filename after the last period character is called the file's extension and tells you the file's type i.e what kind of file it is e.g .py specifies it is a python file")
print("2. path - This specifies the location of a file on the computer")

print('' * 99)

print("Operating systems differ on how they handle filenames and paths as shown below:")
print("This is a file named hello.py located on the Desktop of different OS under a folder called programs")
print(r"Windows - C:\Users\mutwiri-2\Desktop\programs\hello.py")
print(r"Linux - /home/mutwiri-2/Desktop/programs/hello.py")
print(r"MacOs - /Users/mutwiri-2/Desktop/programs/hello.py")

print('' * 99)

print(r"On Windows, the path begins from C:\ which is called the root folder i.e the folder that contains all other folders.")
print("Users, mutwiri-2, Desktop and programs are all folders (or directories) and hello.py is the name of the file. That means hello.py is a file located inside the programs folder which is itself located inside the Desktop folder located inside mutwiri-2 folder which is located inside the Users folder which is then located in the root folder.")

print('' * 99)

print("On Linux and MacOs, path begins from / (root folder) as shown above")

print('' * 99)

print("Additional volumes like USB flash drives will appear differently on various OS")
print(r"Windows - Appear as new lettered root drives e.g D:\ or F:\ ")
print(r"MacOs - Appear as new folders under the /Volumes folder")
print(r"Linux - Appear as new folders under the /mnt ('mount') folder")

print('' * 99)

print("Windows paths are written using backslashes as the separator between folders names. Linux and MacOs use forward slashes as the path separator between folder names")
print("For your program to work on all operating systems, write your Python scripts to handle both cases")

print('' * 99)

print("The Path() function in the pathlib module when passed string values of individual file and folder names in a path will return a string with a file path using the correct path separators")
from pathlib import Path
print(Path('Desktop', 'Programs', 'hello.py'))
print(type(Path('Desktop', 'Programs', 'hello.py')))

print('' * 99)
