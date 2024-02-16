import os
#Explain what you want to do first! Perhaps with the Finder?

#checking PATH
print(os.getcwd())

#Create New Folder (Directory)
foldername = "Python_FileIO"
if not os.path.exists(foldername):
    os.makedirs(foldername)

#Check if new folder is created
dirlist = os.listdir()
if foldername in dirlist:
    print("Folder successfully created")
else:
    print("New folder unsuccessful")

#Change Current Directory/PATH
os.chdir(foldername)

#check PATH
print(os.getcwd())

#Create New File
filename = "example_file.txt"
file = open(filename, 'w')
file.write("In the beginning God created the heavens and the earth.")
file.close()

#Read File
file = open(filename, 'r')
content = file.read()
print(content)
file.close()

#Update File
file = open(filename, 'w')
file.write("In the beginning God created the heavens and the earth. (Gen 1:1)")
file.close()

#Check Changed File by Reading File
file = open(filename, 'r')
content = file.read()
print(content)
file.close()

#Delete File
os.remove(filename)

#Go back to previous directory/PATH
os.chdir("../")

#Remove Directory
os.rmdir("Python_FileIO")

#Check if the folder is deleted
dirlist = os.listdir()
if foldername not in dirlist:
    print("Folder successfully deleted")
else:
    print("Deletion Unsuccessful")
