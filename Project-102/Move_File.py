import os
import shutil

from_dir = "/Users/sadhakshinde/WhiteHatJR/Python/Project-102"
to_dir = "/Users/sadhakshinde/WhiteHatJR/Python/Project-102/Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for x in list_of_files:
    name,extention = os.path.splitext(x)
    if extention == "":
        continue
    if extention in [".txt",".docx",".pptx",".pdf"]:
        path1 = from_dir + '/' + x
        path2 = to_dir
        path3 = to_dir + '/' + x
        if os.path.exists(path2):
            print("Moving the file",x)
            shutil.move(path1,path3)
        else:
            print("Making a new directory")
            os.mkdir(path2)
            shutil.move(path1,path3)
            