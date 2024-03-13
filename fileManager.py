import os
import re
import shutil
main_versions = ['0.4', '0.5', '0.6', '0.7', '0.8']
for root, dirs, files in os.walk(r"D:\pythona\contracts"):#合同地址
    for file in files:
        if file.endswith('.sol'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                match = re.search(r"pragma solidity \^(\d+\.\d+\.\d+);", content)
                if match:
                    version = match.group(1)[:3]
                    sub_version = match.group(1)
                    if version in main_versions:
                        dest_folder = os.path.join(r"D:\pythona", version, sub_version)#分类好需要存放的位置
                        if not os.path.exists(dest_folder):
                            os.makedirs(dest_folder)
                            print("Created target folder", dest_folder)
                        print("Copying", file, "to target folder", dest_folder)
                        shutil.copy(file_path, dest_folder)
