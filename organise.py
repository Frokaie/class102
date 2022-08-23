import os
import shutil

from_dir="Folder1"
to_dir="Folder2"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,extention=os.path.splitext(file_name)
    print(extention)
    print(name)
    if extention=="":
        continue
    if extention in [".gif",".png",".jpg",".jpeg",".jfif",".txt"]:
        path1=from_dir+"/"+file_name
        path2=to_dir+"/"+extention
        path3=to_dir+"/"+extention+"/"+file_name
        print("path1",path1)
        print("path3",path3)
        
        if os.path.exists(path2):
            print("moving"+file_name+"...")
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("moving"+file_name+"...")
            shutil.move(path1,path3)
    