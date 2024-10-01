import os

#making a folder
# if(not os.path.exists("data")):
#     os.mkdir("data")

# making a file inside a folder
# file_name = 'example.txt' 
# file_path = os.path.join("data", file_name) 
# with open(file_path, 'w') as f: 
#     f.write('This is an example file.')

#removing a file inside a folder
# os.remove(file_path)

#removind a directory
# os.rmdir("data")

#rename file type
# files= os.listdir("data")
# count=0
# for i in files:
#     if i.endswith(".png"):
#         os.rename(f'data/{i}',f"data/{count}.png")
#         count+=1