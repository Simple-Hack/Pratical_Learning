# Day4：边缘设备部署实战

## 学习目标
1. 理解TensorRT加速原理
2. 掌握ONNX模型导出方法
3. 配置Jetson Nano环境
4. 实现实时目标检测

## 详细内容

### 1. TensorRT基础
- TensorRT框架介绍
- 计算图优化原理
- 量化加速方法
- 支持算子分析

### 2. 模型转换与优化
- PyTorch到ONNX转换
- ONNX到TensorRT转换
- FP16/INT8量化
- 性能优化技巧

### 3. Jetson Nano环境
- 系统镜像烧录
- CUDA环境配置
- 依赖库安装
- 开发环境搭建

### 4. 部署实战
- 实时视频检测
- 多线程优化
- 性能监控
- 结果可视化

## 代码结构
```
Day4/
├── code/                    # 代码目录
│   ├── export.py           # 模型导出
│   ├── detect.py           # 检测程序
│   └── utils/              # 工具函数
├── models/                  # 模型目录
│   ├── yolov8.onnx        # ONNX模型
│   └── yolov8.engine      # TensorRT引擎
├── docs/                    # 文档
│   ├── tensorrt.md         # TensorRT教程
│   └── deployment.md       # 部署指南
└── README.md               # 说明文档
```

## 任务清单
- [ ] 学习TensorRT原理
- [ ] 完成模型转换
- [ ] 配置开发环境
- [ ] 实现实时检测
- [ ] 优化运行性能

## 资源链接
- TensorRT文档：https://developer.nvidia.com/tensorrt
- Jetson Nano教程：https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit
- YOLOv8部署指南：https://docs.ultralytics.com/modes/export/

## 注意事项
1. 注意显存管理
2. 监控设备温度
3. 做好性能测试
4. 优化推理速度
5. 记录部署过程

## 性能优化提示
1. 使用FP16量化
2. 开启动态Batch
3. 优化输入尺寸
4. 使用CUDA Graph
5. 开启多线程处理 