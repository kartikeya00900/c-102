import os
import shutil


from_dir="C:/Users/karti/Downloads"

to_dir="C:/Users/karti/OneDrive/Pictures"
list_of_files=os.listdir(from_dir)
#print(list_of_files)

#Move All Image Files From Download Folder To Another Folder
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == "":
        continue
    if extension in [".gif",".png",".jpg",".jpeg",".jfif"]:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "image_files"
        path3= to_dir + "/" + "image_files" + "/" + file_name
        #print("Path1 ",path1)
        #print("path3",path3)
        

        #Check If Folder / Directory Path exists before moving
        #else make a new folder / direstory then move

        if os.path.exists(path2):
            print("moving" + file_name + ".....")

            #Move From path1 ---> path3
            shutil.move(path1,path3)

        else:
            os.mkdir(path2)
            print("moving" + file_name + ".....")
            shutil.move(path1,path3)