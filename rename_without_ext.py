import os

root_dir = "./test/"

for idx,file_name in enumerate(os.listdir(root_dir)):
    base_path, ext = os.path.splitext(os.path.join(root_dir, file_name))
    os.rename(base_path + ext,root_dir+str(idx) + ext)
    print(root_dir+str(idx) + ext)