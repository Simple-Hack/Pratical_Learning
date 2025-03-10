# Day2：数据标注与模型训练

## 学习目标
1. 掌握LabelImg标注工具使用
2. 学会构建YOLO格式数据集
3. 理解数据增强策略
4. 完成病虫害检测模型训练

## 详细内容

### 1. 数据标注
- LabelImg工具安装与使用
- YOLO格式标注规范
- 标注质量控制
- 数据集划分策略

### 2. YOLO格式数据集构建
- 数据集组织结构
- 标签格式转换
- 配置文件编写
- 数据集验证

### 3. 数据增强策略
- Mosaic增强
- Mixup增强
- 随机裁剪与旋转
- 光照与噪声增强

### 4. 模型训练实战
- 训练参数配置
- TensorBoard使用
- 训练过程监控
- 模型评估与选择

## 代码结构
```
Day2/
├── code/                    # 代码目录
│   ├── train.py            # 训练脚本
│   ├── augment.py          # 数据增强
│   └── utils.py            # 工具函数
├── data/                    # 数据目录
│   ├── images/             # 图片
│   ├── labels/             # 标签
│   └── dataset.yaml        # 数据集配置
├── docs/                    # 文档
│   ├── labeling_guide.md   # 标注指南
│   └── training_guide.md   # 训练指南
└── README.md               # 说明文档
```

## 任务清单
- [ ] 完成数据标注工具学习
- [ ] 构建病虫害数据集
- [ ] 实现数据增强
- [ ] 完成模型训练
- [ ] 评估模型性能

## 资源链接
- LabelImg工具：https://github.com/tzutalin/labelImg
- Kaggle叶子病害数据集：https://www.kaggle.com/datasets/
- YOLOv8训练指南：https://docs.ultralytics.com/modes/train/

## 注意事项
1. 标注数据要保证质量
2. 定期备份标注结果
3. 监控训练过程
4. 保存最佳模型
5. 记录实验结果 