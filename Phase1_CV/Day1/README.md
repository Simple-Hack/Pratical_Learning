# Day1：YOLOv8核心原理

## 学习目标
1. 理解目标检测基础知识
2. 掌握YOLO系列演进历程
3. 深入理解YOLOv8网络结构
4. 实践COCO预训练模型预测

## 详细内容

### 1. 目标检测基础
- 目标检测任务介绍
- 评价指标（mAP、IoU）
- 检测框表示方法
- 常见数据集介绍

### 2. YOLO系列演进
- YOLOv1-v7的技术发展
- 核心改进点分析
- 性能对比
- 应用场景

### 3. YOLOv8网络结构
- Backbone设计
- Neck结构
- Head设计
- Anchor-free机制
- 损失函数改进

### 4. 实战练习
- 环境配置
- COCO预训练模型下载
- 模型预测演示
- 结果可视化

## 代码结构
```
Day1/
├── code/                    # 代码目录
│   ├── demo.py             # 演示代码
│   └── utils.py            # 工具函数
├── docs/                    # 学习文档
│   ├── detection_basics.md # 检测基础
│   ├── yolo_evolution.md   # YOLO演进
│   └── yolov8_arch.md      # YOLOv8结构
└── README.md               # 说明文档
```

## 任务清单
- [ ] 完成目标检测基础知识学习
- [ ] 理解YOLO系列演进过程
- [ ] 掌握YOLOv8网络结构
- [ ] 运行COCO预训练模型示例
- [ ] 完成课后练习题

## 资源链接
- YOLOv8官方文档：https://docs.ultralytics.com/
- COCO数据集：https://cocodataset.org/
- 论文解读：YOLOv8 Technical Report

## 注意事项
1. 确保GPU环境配置正确
2. 预训练模型下载可能需要代理
3. 注意显存使用情况
4. 保存实验结果和记录 