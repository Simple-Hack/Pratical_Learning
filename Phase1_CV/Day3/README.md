# Day3：注意力机制与模型优化

## 学习目标
1. 理解CBAM注意力模块原理
2. 掌握模型剪枝与量化方法
3. 在YOLOv8中添加CBAM
4. 评估改进模型效果

## 详细内容

### 1. CBAM注意力机制
- 通道注意力机制
- 空间注意力机制
- CBAM工作原理
- 注意力可视化

### 2. 模型优化基础
- 模型剪枝原理
- 权重量化方法
- 知识蒸馏技术
- 模型压缩策略

### 3. YOLOv8改进实践
- CBAM模块实现
- 网络结构修改
- 模型训练调优
- 性能对比分析

### 4. 小目标检测优化
- 特征增强策略
- 多尺度检测
- 注意力机制应用
- 实验结果分析

## 代码结构
```
Day3/
├── code/                    # 代码目录
│   ├── cbam.py             # CBAM实现
│   ├── train_cbam.py       # 训练脚本
│   └── visualize.py        # 可视化工具
├── models/                  # 模型目录
│   ├── yolov8_cbam.yaml    # 改进模型配置
│   └── weights/            # 模型权重
├── docs/                    # 文档
│   ├── attention.md        # 注意力机制
│   └── optimization.md     # 优化方法
└── README.md               # 说明文档
```

## 任务清单
- [ ] 学习CBAM原理
- [ ] 实现CBAM模块
- [ ] 修改YOLOv8网络
- [ ] 训练改进模型
- [ ] 进行效果对比

## 资源链接
- CBAM论文：https://arxiv.org/abs/1807.06521
- YOLOv8源码：https://github.com/ultralytics/ultralytics
- Grad-CAM可视化：https://github.com/jacobgil/pytorch-grad-cam

## 注意事项
1. 改进前后要做好对照实验
2. 保存原始模型结果
3. 记录改进过程
4. 分析性能瓶颈
5. 总结优化经验 