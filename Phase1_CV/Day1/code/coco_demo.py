import os
import torch
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import requests
import zipfile
from tqdm import tqdm

def download_file(url, filename):
    """下载文件的函数，带进度条"""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    with open(filename, 'wb') as f, tqdm(
        desc=filename,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as pbar:
        for data in response.iter_content(chunk_size=1024):
            size = f.write(data)
            pbar.update(size)

def main():
    """主函数"""
    print("=== COCO数据集目标检测演示 ===")
    
    # 创建数据目录
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # 检查是否已下载数据集
    zip_path = os.path.join(data_dir, "val2017.zip")
    if not os.path.exists(zip_path):
        print("正在下载COCO验证集...")
        download_file("http://images.cocodataset.org/zips/val2017.zip", zip_path)
    
    # 检查是否已解压数据集
    val_dir = os.path.join(data_dir, "val2017")
    if not os.path.exists(val_dir):
        print("正在解压数据集...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(data_dir)
    
    # 加载模型
    print("正在加载YOLOv8模型...")
    model = YOLO('yolov8n.pt')
    
    # 选择一张测试图片
    img_path = os.path.join(val_dir, "000000000139.jpg")
    if not os.path.exists(img_path):
        print(f"测试图片不存在: {img_path}")
        return
    
    # 读取图片
    print("正在处理图片...")
    img = cv2.imread(img_path)
    if img is None:
        print("无法读取图片")
        return
    
    # 进行预测
    print("正在进行目标检测...")
    results = model(img)
    
    # 创建结果目录
    result_dir = "results"
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    
    # 保存原始预测结果
    result_img = results[0].plot()
    cv2.imwrite(os.path.join(result_dir, "detection_result.jpg"), result_img)
    
    # 使用Matplotlib显示结果
    plt.figure(figsize=(15, 5))
    
    # 显示原始图片
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('原始图片')
    plt.axis('off')
    
    # 显示检测结果
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB))
    plt.title('检测结果')
    plt.axis('off')
    
    # 保存对比图
    plt.savefig(os.path.join(result_dir, "detection_comparison.png"), bbox_inches='tight', pad_inches=0.1)
    plt.close()
    
    # 打印检测结果
    print("\n检测结果:")
    for r in results:
        print(f"检测到 {len(r.boxes)} 个目标")
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            print(f"类别: {r.names[cls]}, 置信度: {conf:.2f}")
    
    print(f"\n结果已保存至 {result_dir} 目录")

if __name__ == "__main__":
    main() 