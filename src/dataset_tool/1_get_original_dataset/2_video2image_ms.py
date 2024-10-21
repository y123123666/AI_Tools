import cv2
import os

def extract_frames(video_path, output_folder, interval):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)  # 获取视频的帧率
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"总帧数: {total_frames}, 帧率: {fps} FPS")

    # 计算每隔多少帧提取一帧
    frame_interval = int(fps * interval)

    for frame_count in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            break
        
        # 仅在每隔 frame_interval 帧时保存图像
        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            
        # 显示进度
        progress = (frame_count + 1) / total_frames * 100
        print(f"转换进度: {progress:.2f}%，当前帧: {frame_count + 1}/{total_frames}")

    cap.release()
    print("提取完成！")


# 输入视频文件路径、输出文件夹和时间间隔（秒）
video_path = "origin_data/video/elements/6.mp4"
output_folder = "origin_data/images/elements_6"
interval = 0.1  # 每隔0.1秒提取一帧
extract_frames(video_path, output_folder, interval)
