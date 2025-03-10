# Day5：LLM基础与农业知识库构建

## 学习目标
1. 掌握Prompt Engineering技巧
2. 理解RAG架构设计原理
3. 完成农业语料数据清洗
4. 构建本地知识库系统

## 详细内容

### 1. Prompt Engineering
- Prompt设计原则
- Few-shot学习方法
- Chain-of-Thought提示
- 提示词优化技巧

### 2. RAG架构设计
- 检索增强生成原理
- 向量数据库选择
- 文本嵌入方法
- 相似度计算策略

### 3. 农业语料处理
- 数据源获取
- 文本预处理
- 数据清洗流程
- 质量控制方法

### 4. 知识库构建
- LangChain框架使用
- 文档加载与处理
- 向量存储配置
- 检索系统实现

## 代码结构
```
Day5/
├── code/                    # 代码目录
│   ├── process.py          # 数据处理
│   ├── embed.py            # 文本嵌入
│   └── retrieve.py         # 检索系统
├── data/                    # 数据目录
│   ├── raw/                # 原始数据
│   ├── processed/          # 处理后数据
│   └── vectors/            # 向量数据
├── docs/                    # 文档
│   ├── prompt.md           # 提示工程
│   └── rag.md              # RAG架构
└── README.md               # 说明文档
```

## 任务清单
- [ ] 学习Prompt设计
- [ ] 理解RAG架构
- [ ] 处理农业数据
- [ ] 构建知识库
- [ ] 测试检索效果

## 资源链接
- LangChain文档：https://python.langchain.com/
- 农业政策数据：http://www.moa.gov.cn/
- Prompt工程指南：https://www.promptingguide.ai/

## 注意事项
1. 数据质量控制
2. 向量存储选择
3. 检索性能优化
4. 内存资源管理
5. 定期备份数据

## 扩展阅读
1. RAG论文解读
2. 向量数据库对比
3. 文本嵌入模型
4. 相似度算法
5. 农业领域知识 