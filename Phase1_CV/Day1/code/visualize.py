import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
import cv2
import pandas as pd

def plot_training_results(results_file):
    """可视化训练结果"""
    # 检查文件是否存在
    if not os.path.exists(results_file):
        print(f"结果文件不存在: {results_file}")
        return
    
    # 读取CSV结果文件
    try:
        results = pd.read_csv(results_file)
        
        # 提取训练数据
        epochs = results['epoch'].values
        box_loss = results['box_loss'].values
        cls_loss = results['cls_loss'].values
        dfl_loss = results['dfl_loss'].values
        
        # 创建图形
        plt.figure(figsize=(10, 6))
        plt.plot(epochs, box_loss, 'b-', label='Box Loss')
        plt.plot(epochs, cls_loss, 'r-', label='Class Loss')
        plt.plot(epochs, dfl_loss, 'g-', label='DFL Loss')
        
        plt.title('训练损失随轮次的变化')
        plt.xlabel('轮次 (Epoch)')
        plt.ylabel('损失值 (Loss)')
        plt.legend()
        plt.grid(True)
        
        # 保存图形
        save_path = os.path.join(os.path.dirname(results_file), 'training_loss.png')
        plt.savefig(save_path)
        plt.close()
        print(f"训练损失图已保存至: {save_path}")
    except Exception as e:
        print(f"处理训练结果时出错: {e}")

def plot_validation_metrics(results_file):
    """可视化验证指标"""
    # 检查文件是否存在
    if not os.path.exists(results_file):
        print(f"结果文件不存在: {results_file}")
        return
    
    # 读取CSV结果文件
    try:
        results = pd.read_csv(results_file)
        
        # 提取验证指标
        epochs = results['epoch'].values
        metrics = ['metrics/precision', 'metrics/recall', 'metrics/mAP50', 'metrics/mAP50-95']
        metric_names = ['Precision', 'Recall', 'mAP50', 'mAP50-95']
        
        # 创建图形
        plt.figure(figsize=(12, 6))
        for metric, name in zip(metrics, metric_names):
            if metric in results.columns:
                values = results[metric].values
                plt.plot(epochs, values, '-', label=name)
            else:
                print(f"警告: 未找到指标 {metric}")
        
        plt.title('验证指标随轮次的变化')
        plt.xlabel('轮次 (Epoch)')
        plt.ylabel('指标值')
        plt.legend()
        plt.grid(True)
        
        # 保存图形
        save_path = os.path.join(os.path.dirname(results_file), 'validation_metrics.png')
        plt.savefig(save_path)
        plt.close()
        print(f"验证指标图已保存至: {save_path}")
    except Exception as e:
        print(f"处理验证指标时出错: {e}")

def plot_detection_results(image_path, result_path):
    """可视化检测结果"""
    # 检查文件是否存在
    if not os.path.exists(image_path) or not os.path.exists(result_path):
        print(f"图片或结果文件不存在")
        return
    
    # 读取原始图片和结果图片
    img_original = cv2.imread(image_path)
    img_result = cv2.imread(result_path)
    
    if img_original is None or img_result is None:
        print("无法读取图片文件")
        return
    
    # 转换颜色空间从BGR到RGB
    img_original = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)
    img_result = cv2.cvtColor(img_result, cv2.COLOR_BGR2RGB)
    
    # 创建图形
    plt.figure(figsize=(15, 5))
    
    # 显示原始图片
    plt.subplot(1, 2, 1)
    plt.imshow(img_original)
    plt.title('原始图片')
    plt.axis('off')
    
    # 显示检测结果
    plt.subplot(1, 2, 2)
    plt.imshow(img_result)
    plt.title('检测结果')
    plt.axis('off')
    
    # 保存对比图
    save_path = os.path.join(os.path.dirname(result_path), 'detection_comparison.png')
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0.1)
    plt.close()
    print(f"检测结果对比图已保存至: {save_path}")

def main():
    """主函数"""
    print("=== YOLOv8 训练结果可视化 ===")
    
    # 列出所有训练运行
    runs_dir = "../runs/detect"
    train_runs = [d for d in os.listdir(runs_dir) if d.startswith('train')]
    train_runs.sort()  # 按名称排序
    
    print("\n可用的训练运行:")
    for i, run in enumerate(train_runs, 1):
        print(f"{i}. {run}")
    
    # 让用户选择要查看的训练运行
    try:
        choice = int(input("\n请选择要查看的训练运行 (输入序号): "))
        if 1 <= choice <= len(train_runs):
            selected_run = train_runs[choice - 1]
            print(f"\n选择的训练运行: {selected_run}")
            
            # 训练结果文件路径
            results_file = os.path.join(runs_dir, selected_run, "results.csv")
            
            # 可视化训练结果
            plot_training_results(results_file)
            
            # 可视化验证指标
            plot_validation_metrics(results_file)
            
            # 可视化检测结果
            image_path = "../res/aniya.jpg"
            result_path = "../res/aniya_result.jpg"
            plot_detection_results(image_path, result_path)
        else:
            print("无效的选择！")
    except ValueError:
        print("请输入有效的数字！")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    main() 