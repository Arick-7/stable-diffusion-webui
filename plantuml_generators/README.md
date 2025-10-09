# PlantUML生成器套件

🚀 一套完整的PlantUML代码生成程序，支持多种编程语言实现

## 📁 文件结构

```
plantuml_generators/
├── plantuml_generator.py      # Python版本
├── plantuml_generator.js      # JavaScript版本  
├── plantuml_generator.ts      # TypeScript版本
├── PlantUMLGenerator.java     # Java版本
├── PlantUMLGenerator.cs       # C#版本
├── README.md                  # 说明文档
├── examples/                  # 使用示例
└── output/                    # 生成的文件输出目录
```

## 🎯 功能特性

### 支持的图表类型
- ✅ **活动图 (Activity Diagram)** - 工作流程图
- ✅ **序列图 (Sequence Diagram)** - 交互时序图  
- ✅ **类图 (Class Diagram)** - 系统架构图
- 🔄 **用例图 (Use Case Diagram)** - 功能需求图
- 🔄 **组件图 (Component Diagram)** - 系统组件图
- 🔄 **状态图 (State Diagram)** - 状态转换图

### 核心功能
- 🎨 **样式自定义** - 支持主题和颜色配置
- 📝 **注释支持** - 添加详细的说明注释
- 🔄 **决策节点** - 支持条件分支逻辑
- ⚡ **并行处理** - 支持并行执行块
- 📊 **分区管理** - 逻辑分组和可视化分区
- 🌐 **在线查看** - 生成在线查看链接

## 🚀 快速开始

### Python版本使用示例

```python
from plantuml_generator import ActivityDiagramGenerator

# 创建活动图生成器
generator = ActivityDiagramGenerator()

# 设置基本信息
generator.setTitle("我的工作流程")

# 添加分区和活动
generator.addPartition("准备阶段", [
    "收集需求",
    "分析数据",
    "制定计划"
])

generator.addPartition("执行阶段", [
    "开始实施",
    "监控进度",
    "调整策略"
])

# 添加决策点
generator.addDecision(
    "质量检查通过？",
    "进入下一阶段", 
    "返回修改",
    "符合标准",
    "需要改进"
)

# 生成PlantUML代码
plantuml_code = generator.generateCode()
print(plantuml_code)
```

### JavaScript版本使用示例

```javascript
// 创建活动图生成器
const generator = new ActivityDiagramGenerator();

// 设置基本信息
generator.setTitle("我的工作流程");

// 添加分区和活动
generator.addPartition("准备阶段", [
    "收集需求",
    "分析数据", 
    "制定计划"
]);

// 生成代码
const plantumlCode = generator.generateCode();
console.log(plantumlCode);
```

### Java版本使用示例

```java
// 创建活动图生成器
ActivityDiagramGenerator generator = new ActivityDiagramGenerator();

// 设置基本信息
generator.setTitle("我的工作流程");

// 添加分区和活动
generator.addPartition("准备阶段", Arrays.asList(
    "收集需求",
    "分析数据",
    "制定计划"
));

// 生成代码
String plantumlCode = generator.generateCode();
System.out.println(plantumlCode);
```

## 📊 建筑AI系统示例

所有版本都包含了基于您提供文字的建筑AI辅助设计系统流程图生成功能：

```python
# Python版本
workflow_code = create_building_ai_workflow()

# JavaScript版本  
const workflowCode = createBuildingAIWorkflow();

# Java版本
String workflowCode = createBuildingAIWorkflow();
```

## 🌐 在线查看

生成的PlantUML代码可以在以下在线编辑器中查看：

- [PlantUML官方在线编辑器](http://www.plantuml.com/plantuml/uml/)
- [PlantUML Editor](https://plantuml-editor.kkeisuke.com/)
- [PlantText](https://www.planttext.com/)

## 🛠️ 安装和运行

### Python版本
```bash
# 直接运行
python3 plantuml_generator.py

# 或作为模块导入
from plantuml_generator import ActivityDiagramGenerator
```

### JavaScript版本
```bash
# Node.js环境
node plantuml_generator.js

# 浏览器环境
<script src="plantuml_generator.js"></script>
```

### Java版本
```bash
# 编译
javac PlantUMLGenerator.java

# 运行
java PlantUMLGeneratorMain
```

### TypeScript版本
```bash
# 安装依赖
npm install -g typescript

# 编译
tsc plantuml_generator.ts

# 运行
node plantuml_generator.js
```

### C#版本
```bash
# 编译
csc PlantUMLGenerator.cs

# 运行
./PlantUMLGenerator.exe
```

## 📋 API参考

### 基础方法
- `setTitle(title)` - 设置图表标题
- `setTheme(theme)` - 设置主题样式
- `addNote(content, position)` - 添加注释

### 活动图专用方法
- `addActivity(name, note, position)` - 添加单个活动
- `addPartition(name, activities, color)` - 添加分区
- `addDecision(question, yesPath, noPath)` - 添加决策点
- `addParallelBlock(activities)` - 添加并行执行块

### 序列图专用方法
- `addParticipant(name, alias, type)` - 添加参与者
- `addMessage(from, to, message, arrow)` - 添加消息交互

### 类图专用方法
- `addClass(name, attributes, methods)` - 添加类定义
- `addRelationship(from, to, type, label)` - 添加类关系

## 🎨 样式自定义

所有生成器都支持PlantUML的样式自定义：

```plantuml
skinparam activity {
    BackgroundColor lightblue
    BorderColor black
    FontSize 12
}
```

## 📈 扩展功能

### 1. 自定义主题
```python
generator.setTheme("aws-orange")  # AWS主题
generator.setTheme("blueprint")   # 蓝图主题
```

### 2. 颜色配置
```python
generator.addPartition("重要阶段", activities, "red")
```

### 3. 多种箭头类型
```python
generator.addMessage("A", "B", "同步调用", "->")
generator.addMessage("A", "B", "异步调用", "->>")
```

## 🔧 高级用法

### 复杂流程图示例
```python
generator = ActivityDiagramGenerator()
generator.setTitle("复杂业务流程")

# 并行处理
generator.addParallelBlock([
    "数据收集",
    "标准检查", 
    "风险评估"
])

# 条件分支
generator.addDecision(
    "所有检查通过？",
    "进入设计阶段",
    "返回修改",
    "满足所有条件",
    "存在问题需要解决"
)
```

## 🐛 故障排除

### 常见问题
1. **中文字符显示问题** - 确保文件编码为UTF-8
2. **在线编辑器无法加载** - 检查网络连接或使用备用编辑器
3. **代码格式错误** - 检查PlantUML语法是否正确

### 调试技巧
- 使用在线编辑器验证生成的代码
- 检查分区和活动的括号匹配
- 确保决策节点的条件语法正确

## 📚 参考资源

- [PlantUML官方文档](https://plantuml.com/)
- [PlantUML活动图语法](https://plantuml.com/activity-diagram-beta)
- [PlantUML序列图语法](https://plantuml.com/sequence-diagram)
- [PlantUML类图语法](https://plantuml.com/class-diagram)

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个工具套件！

## 📄 许可证

MIT License - 自由使用和修改