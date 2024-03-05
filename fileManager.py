#合同分类器
import os
import re
import shutil
versions = ['0.4', '0.5', '0.6', '0.7', '0.8']
for version in versions:
    os.makedirs(os.path.join(r"D:\pythona", version), exist_ok=True)#在此输入你保存分类文件的地址
for root, dirs, files in os.walk(r"D:\pythona\contracts"):#在此输入你的合同地址
    for file in files:
        if file.endswith('.sol'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                match = re.search(r"pragma solidity \^(\d+\.\d+\.\d+);", content)
                if match:
                    version = match.group(1)[:3]
                    print(version)
                    if version in versions:
                        dest_folder = os.path.join(r"D:\pythona", version)
                        print("Copying", file, "to target folder", dest_folder)
                        shutil.copy(file_path, dest_folder)
