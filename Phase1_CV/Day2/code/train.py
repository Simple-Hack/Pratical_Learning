from ultralytics import YOLO
from torch.utils.tensorboard import SummaryWriter
import os
import torch

def train_with_tensorboard():
    """使用TensorBoard监控训练过程"""
    # 创建TensorBoard日志目录
    log_dir = os.path.join('runs', 'tensorboard')
    writer = SummaryWriter(log_dir)

    # 加载模型
    model = YOLO('yolov8n.pt')

    # 自动检测设备
    device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
    print(f"使用设备: {device}")

    # 设置训练参数，包括数据增强
    results = model.train(
        data='coco8.yaml',
        epochs=30,
        imgsz=640,
        batch=16,
        name='yolo_augmented',
        # 数据增强参数
        augment=True,
        mosaic=1.0,  # mosaic增强概率
        mixup=0.5,   # mixup增强概率
        # 其他训练参数
        save_period=1,
        device=device,  # 使用自动检测的设备
        # TensorBoard相关
        project='runs/detect',
        exist_ok=True
    )

    # 记录训练指标到TensorBoard
    for epoch, metrics in enumerate(results.metrics):
        writer.add_scalar('Loss/train', metrics['train/box_loss'], epoch)
        writer.add_scalar('mAP50', metrics['metrics/mAP50(B)'], epoch)
        writer.add_scalar('Precision', metrics['metrics/precision(B)'], epoch)
        writer.add_scalar('Recall', metrics['metrics/recall(B)'], epoch)

    writer.close()

def main():
    """主函数"""
    print("=== YOLOv8训练与数据增强实验 ===")
    train_with_tensorboard()

if __name__ == "__main__":
    main()
