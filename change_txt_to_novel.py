import os
import re

def process_txt_files(src_folder_path, dest_folder_path):
    if not os.path.exists(dest_folder_path):
        os.makedirs(dest_folder_path)

    for file_name in os.listdir(src_folder_path):
        if file_name.endswith('.txt'):
            src_file_path = os.path.join(src_folder_path, file_name)
            dest_file_path = os.path.join(dest_folder_path, file_name[:-4] + '_changed.txt')

            with open(src_file_path, 'r', encoding='utf-8') as file:
                content = file.readlines()

            new_content = []
            for line in content:
                if line.strip() != '':
                    new_content.append(line.rstrip() + ' ')
                else:
                    new_content.append(line)

            with open(dest_file_path, 'w', encoding='utf-8') as file:
                file.writelines(new_content)

if __name__ == "__main__":
    src_folder_path = "B:/train_MEGA/MarxEngelsGesamtausgabe"  # 请将这里的字符串替换为你需要处理的源文件夹路径
    dest_folder_path = "B:/train_MEGA/MEGA_novel"  # 请将这里的字符串替换为你需要将处理后的文件保存到的目标文件夹路径
    process_txt_files(src_folder_path, dest_folder_path)
