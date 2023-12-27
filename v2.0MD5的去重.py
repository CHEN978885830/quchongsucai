import hashlib
import os
from datetime import datetime

def md5_of_file(file_path):
    """计算文件的 MD5 哈希值"""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def generate_md5_for_folder(folder_path):
    """为指定文件夹中的 MP4 和 DOCX 文件生成 MD5 哈希值，并记录文件创建时间"""
    md5_dict = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and (filename.lower().endswith('.mp4') or filename.lower().endswith('.docx')):
            file_md5 = md5_of_file(file_path)
            creation_time = os.path.getctime(file_path)
            md5_dict[file_md5] = (file_path, creation_time)
    return md5_dict

def remove_duplicates(folder1, folder2):
    """找出并删除两个文件夹中重复的 MP4 和 DOCX 文件，删除最新创建的文件"""
    md5_folder1 = generate_md5_for_folder(folder1)
    md5_folder2 = generate_md5_for_folder(folder2)

    for md5 in md5_folder1:
        if md5 in md5_folder2:
            file1, creation_time1 = md5_folder1[md5]
            file2, creation_time2 = md5_folder2[md5]
            file_to_delete = file1 if creation_time1 > creation_time2 else file2

            os.remove(file_to_delete)
            print(f"Deleted: {file_to_delete}")

# 文件夹路径
folder1_path = r"C:\Users\chenliqi\Desktop\MD5测试\第一次\ʚ💩ɞ(史门）\视频作品"
folder2_path = r"C:\Users\chenliqi\Desktop\MD5测试\第二次\史门视频作品"

# 删除重复文件
remove_duplicates(folder1_path, folder2_path)
