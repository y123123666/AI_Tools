import os
import shutil

def combine_images(source_folders, target_folder):
    os.makedirs(target_folder, exist_ok=True)

    for folder in source_folders:
        if os.path.exists(folder):
            for filename in os.listdir(folder):
                if filename.endswith(('.jpg', '.jpeg', '.png')):  # 根据需要添加文件格式
                    source_path = os.path.join(folder, filename)
                    target_path = os.path.join(target_folder, filename)
                    
                    # 防止文件名冲突
                    if os.path.exists(target_path):
                        name, ext = os.path.splitext(filename)
                        target_path = os.path.join(target_folder, f"{name}_copy{ext}")
                    
                    shutil.copy2(source_path, target_path)

    print("合成完成！")

# 示例用法
source_folders = ["processed_imgs/2_video2images/sample_1", "processed_imgs/2_video2images/sample_2", "processed_imgs/2_video2images/sample_3"]  # 替换为你的文件夹路径
target_folder = "processed_imgs/3_sample_images/v1_dataset"
combine_images(source_folders, target_folder)
