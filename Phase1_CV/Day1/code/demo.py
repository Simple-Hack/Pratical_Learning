import cv2
import numpy as np
from ultralytics import YOLO
import torch

def check_gpu():
    """检查GPU是否可用"""
    print(f"CUDA是否可用: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"当前GPU: {torch.cuda.get_device_name(0)}")
        print(f"GPU显存: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f}GB")

def load_model():
    """加载YOLOv8预训练模型"""
    try:
        model = YOLO('yolov8n.pt')  # 加载nano版本模型
        print("模型加载成功！")
        return model
    except Exception as e:
        print(f"模型加载失败: {e}")
        return None

def predict_image(model, image_path):
    """对单张图片进行预测"""
    try:
        # 进行预测
        results = model(image_path)
        
        # 获取原始图片
        img = cv2.imread(image_path)
        
        # 在图片上绘制检测结果
        for result in results:
            boxes = result.boxes
            for box in boxes:
                # 获取边界框坐标
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                # 获取置信度
                conf = box.conf[0].cpu().numpy()
                # 获取类别
                cls = int(box.cls[0].cpu().numpy())
                
                # 绘制边界框
                cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                # 添加标签
                label = f"{result.names[cls]} {conf:.2f}"
                cv2.putText(img, label, (int(x1), int(y1)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # 保存结果
        output_path = image_path.replace('.jpg', '_result.jpg')
        cv2.imwrite(output_path, img)
        print(f"结果已保存至: {output_path}")
        
    except Exception as e:
        print(f"预测过程出错: {e}")

def main():
    """主函数"""
    print("=== YOLOv8 目标检测演示 ===")
    
    # 检查GPU
    check_gpu()
    
    # 加载模型
    model = load_model()
    if model is None:
        return
    
    # 测试图片路径
    image_path = "test.jpg"  # 请替换为实际的测试图片路径
    
    # 进行预测
    predict_image(model, image_path)

if __name__ == "__main__":
    main() 