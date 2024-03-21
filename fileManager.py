import os
import re
import shutil
#
#过滤出来的基本都是可运行的合约，但是还有一些合约是工具类，这个很难分辨，得手动过滤
#然后仔细看看有没有address相同的合约，如果有，那就可以都删了
#（因为这个版本会把import去掉，你很难找到带有import的那个主合约来进行合并
#
main_versions = ['0.5', '0.4','0.6', '0.7', '0.8']
done_versions = ['0.5.0','0.5.16','0.5.17','0.5.2','0.5.00','0.5.7'] #已经收集够的合约版本
for root, dirs, files in os.walk(r"E:\Desktop\大创\smartbugs-wild-master.1.1\smartbugs-wild-master\contracts"):#合同地址 （可以直接mainnet文件夹
    for file in files:
        if file.endswith('.sol'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                match = re.search(r"pragma solidity \^(\d+\.\d+\.\d+);", content)
                if match:
                    version = match.group(1)[:3]
                    sub_version = match.group(1)
                    if version in main_versions and sub_version not in done_versions:
                        match_import = re.search(r"import", content)
                        dest_folder = os.path.join(r"E:\Desktop\大创\0.5.0^", version, sub_version)#分类好需要存放的位置
                        if match_import:
                            continue
                        if not os.path.exists(dest_folder):
                            os.makedirs(dest_folder)
                            print("Created target folder", dest_folder)
                        print("Copying", file, "to target folder", dest_folder)
                        shutil.copy(file_path, dest_folder)
