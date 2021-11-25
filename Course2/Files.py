import shutil
import os
text = "Hello\nThis is me,\nMario!"

try:
    with open("New_File.txt","w") as file:
        file.write(text)
finally:
    print("File Created.")
append = "\nAnd I am Luiggi!"
with open("New_File.txt","a") as file:
        file.write(append)

shutil.copyfile("New_File.txt", "C:\\Users\\joaopaulo\\Google Drive\\Phyton\\New_File_Copy.txt")
#Moving a file
source = "text.txt"
destination = "C:\\Users\\joaopaulo\\Google Drive\\Phyton\\text.txt"
source_folder = "Files"
destination_folder = "C:\\Users\\joaopaulo\\Google Drive\\Phyton\\Files"
#move the file
try:
    if os.path.exists(destination):
        print("There is already a file there.")
    else:
        os.replace(source,destination)
        print("{} was moved.".format(source))

except FileNotFoundError as e:
    print(e)
    print("{} was not found.".format(source))

#move the folder
try:
    if os.path.exists(destination_folder):
        print("There is already a folder there.")
    else:
        os.replace(source_folder,destination_folder)
        print("{} was moved.".format(source_folder))

except FileNotFoundError as e:
    print(e)
    print("{} was not found.".format(source_folder))
#Deleting a file
delete = "delete.txt"
delete_folder = "Delete"
try:
    os.remove(delete)
except FileNotFoundError as B:
    print(B)
    print("{} file not found.".format(delete))
#Deletinga Folder
try:
    #os.rmdir(delete_folder)
    shutil.rmtree(delete_folder)
except FileNotFoundError as a:
    print(a)
    print("{} folder not found.".format(delete_folder))
except OSError as c:
    print(c)
    print("{} folder is not empty.".format(delete_folder))
except PermissionError as B:
    print(B)
    print("{} folder not found.".format(delete_folder))