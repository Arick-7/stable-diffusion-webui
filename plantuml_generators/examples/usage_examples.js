/**
 * PlantUML生成器使用示例 - JavaScript版本
 * 展示各种图表类型的生成方法
 */

// 引入生成器类（如果在Node.js环境中）
// const { ActivityDiagramGenerator, SequenceDiagramGenerator, ClassDiagramGenerator } = require('../plantuml_generator.js');

function example1SimpleActivity() {
    /**
     * 示例1：简单活动图
     */
    const generator = new ActivityDiagramGenerator();
    
    generator.setTitle("简单工作流程");
    
    // 添加简单活动序列
    generator.addActivity("开始工作", "准备阶段");
    generator.addActivity("执行任务", "核心工作");  
    generator.addActivity("检查结果", "质量控制");
    generator.addActivity("完成工作", "结束阶段");
    
    return generator.generateCode();
}

function example2ComplexWorkflow() {
    /**
     * 示例2：复杂工作流程（建筑AI系统）
     */
    const generator = new ActivityDiagramGenerator();
    
    generator.setTitle("建筑AI辅助设计完整流程");
    
    // 数据输入阶段
    generator.addPartition("数据输入阶段", [
        "收集既往建筑项目策划书",
        "收集项目任务书",
        "获取国家建设标准",
        "获取地方建设标准"
    ], "LIGHTBLUE");
    
    // AI处理阶段
    generator.addPartition("AI分析处理阶段", [
        "建筑大语言模型加载",
        "多源数据融合分析"
    ], "LIGHTGREEN");
    
    // 添加决策点
    generator.addDecision(
        "数据完整性检查",
        "启动对话式交互",
        "请求补充信息",
        "数据充足，可以继续",
        "缺少关键信息"
    );
    
    // 智能生成阶段
    generator.addPartition("智能生成阶段", [
        "快速生成策划书草案",
        "生成设计任务书",
        "识别关键性能指标",
        "明确项目目标和需求"
    ], "LIGHTYELLOW");
    
    // 并行处理关键指标
    generator.addParallelBlock([
        "能耗性能分析",
        "可持续性评估",
        "舒适度指标设定",
        "经济性指标计算"
    ]);
    
    // 输出优化阶段
    generator.addPartition("输出优化阶段", [
        "为设计师提供清晰方向",
        "识别技术挑战点",
        "生成针对性解决方案"
    ], "LIGHTCORAL");
    
    // 最终决策
    generator.addDecision(
        "质量检查通过？",
        "生成最终文档",
        "返回优化建议",
        "达到质量标准",
        "需要进一步改进"
    );
    
    // 价值实现阶段
    generator.addPartition("价值实现阶段", [
        "降低认知负荷",
        "提高工作效率",
        "优化设计质量"
    ], "LIGHTPINK");
    
    // 添加系统说明
    generator.addNote(
        "系统通过AI技术整合多源建筑信息，实现智能化的项目策划与设计辅助。\\n" +
        "核心价值：快速响应、标准合规、经验复用、智能预判、减负增效",
        "top"
    );
    
    return generator.generateCode();
}

function example3SequenceDiagram() {
    /**
     * 示例3：序列图
     */
    const generator = new SequenceDiagramGenerator();
    
    generator.setTitle("建筑AI系统交互序列图");
    
    // 添加参与者
    generator.addParticipant("建筑师", "Architect", "actor");
    generator.addParticipant("AI系统", "AI", "participant");
    generator.addParticipant("项目数据库", "ProjectDB", "database");
    generator.addParticipant("标准API", "StandardAPI", "participant");
    generator.addParticipant("文档生成器", "DocGen", "participant");
    
    // 添加交互消息
    generator.addMessage("Architect", "AI", "上传项目基本信息");
    generator.addMessage("AI", "ProjectDB", "查询相似历史项目");
    generator.addMessage("ProjectDB", "AI", "返回项目数据");
    generator.addMessage("AI", "StandardAPI", "获取适用建设标准");
    generator.addMessage("StandardAPI", "AI", "返回标准规范");
    generator.addMessage("AI", "Architect", "生成初步问题清单");
    generator.addMessage("Architect", "AI", "回答项目需求问题");
    generator.addMessage("AI", "AI", "分析需求和约束条件");
    generator.addMessage("AI", "DocGen", "请求生成策划书");
    generator.addMessage("DocGen", "AI", "返回策划书草案");
    generator.addMessage("AI", "Architect", "提供完整策划方案");
    
    return generator.generateCode();
}

function example4ClassDiagram() {
    /**
     * 示例4：类图
     */
    const generator = new ClassDiagramGenerator();
    
    generator.setTitle("建筑AI系统架构类图");
    
    // 添加核心类
    generator.addClass(
        "BuildingAISystem",
        [
            "- llmModel: LanguageModel",
            "- projectDatabase: ProjectDatabase",
            "- standardsAPI: StandardsAPI",
            "- documentGenerator: DocumentGenerator"
        ],
        [
            "+ generatePlan(project: Project): Plan",
            "+ analyzeRequirements(input: String): Requirements", 
            "+ identifyKPIs(project: Project): List<KPI>",
            "+ generateTaskDocument(plan: Plan): Document"
        ]
    );
    
    generator.addClass(
        "Project",
        [
            "- id: String",
            "- type: BuildingType",
            "- location: String",
            "- requirements: List<String>",
            "- constraints: List<String>"
        ],
        [
            "+ validate(): Boolean",
            "+ getType(): BuildingType",
            "+ addRequirement(req: String): void",
            "+ getConstraints(): List<String>"
        ]
    );
    
    generator.addClass(
        "Plan",
        [
            "- content: String",
            "- kpis: List<KPI>",
            "- challenges: List<Challenge>",
            "- timeline: Timeline",
            "- budget: Budget"
        ],
        [
            "+ exportToPDF(): PDF",
            "+ validate(): Boolean",
            "+ addKPI(kpi: KPI): void",
            "+ identifyChallenges(): List<Challenge>"
        ]
    );
    
    generator.addClass(
        "KPI",
        [
            "- name: String",
            "- type: KPIType",
            "- targetValue: Double",
            "- unit: String"
        ],
        [
            "+ calculate(): Double",
            "+ isAchievable(): Boolean", 
            "+ getDescription(): String"
        ]
    );
    
    // 添加关系
    generator.addRelationship("BuildingAISystem", "Project", "-->", "processes");
    generator.addRelationship("BuildingAISystem", "Plan", "-->", "generates");
    generator.addRelationship("Project", "Plan", "-->", "creates");
    generator.addRelationship("Plan", "KPI", "o--", "contains");
    
    return generator.generateCode();
}

function createHTMLViewer(examples) {
    /**
     * 创建HTML查看器
     */
    const htmlContent = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PlantUML示例集合</title>
    <style>
        body {
            font-family: 'Microsoft YaHei', Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        .example-section {
            margin: 30px 0;
            border: 1px solid #bdc3c7;
            border-radius: 10px;
            overflow: hidden;
        }
        .example-header {
            background: #34495e;
            color: white;
            padding: 15px;
            font-size: 18px;
            font-weight: bold;
        }
        .example-content {
            padding: 20px;
        }
        .code-block {
            background: #2c3e50;
            color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
            font-size: 12px;
            line-height: 1.4;
            max-height: 300px;
            overflow-y: auto;
        }
        .btn {
            background: #3498db;
            color: white;
            padding: 8px 16px;
            text-decoration: none;
            border-radius: 5px;
            display: inline-block;
            margin: 5px;
            border: none;
            cursor: pointer;
        }
        .btn:hover {
            background: #2980b9;
        }
        .btn-copy {
            background: #27ae60;
        }
        .btn-copy:hover {
            background: #219a52;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 PlantUML生成器示例集合</h1>
        
        <div style="text-align: center; margin: 30px 0;">
            <a href="http://www.plantuml.com/plantuml/uml/" target="_blank" class="btn">
                🌐 PlantUML在线编辑器
            </a>
        </div>
        
        ${examples.map((example, index) => `
        <div class="example-section">
            <div class="example-header">
                📈 示例${index + 1}：${example.name}
            </div>
            <div class="example-content">
                <button class="btn btn-copy" onclick="copyToClipboard('code-${index}')">
                    📋 复制代码
                </button>
                <div class="code-block" id="code-${index}">${example.code}</div>
            </div>
        </div>
        `).join('')}
    </div>

    <script>
        function copyToClipboard(elementId) {
            const codeElement = document.getElementById(elementId);
            const text = codeElement.textContent;
            
            navigator.clipboard.writeText(text).then(function() {
                alert('代码已复制到剪贴板！');
            }, function(err) {
                console.error('复制失败: ', err);
                // 备用复制方法
                const textArea = document.createElement('textarea');
                textArea.value = text;
                document.body.appendChild(textArea);
                textArea.select();
                document.execCommand('copy');
                document.body.removeChild(textArea);
                alert('代码已复制到剪贴板！');
            });
        }
    </script>
</body>
</html>`;
    
    return htmlContent;
}

function runAllExamples() {
    /**
     * 运行所有示例
     */
    console.log("🎨 PlantUML生成器使用示例 - JavaScript版本");
    console.log("=".repeat(60));
    
    const examples = [
        { name: "简单活动图", code: example1SimpleActivity() },
        { name: "复杂工作流程", code: example2ComplexWorkflow() },
        { name: "序列图", code: example3SequenceDiagram() },
        { name: "类图", code: example4ClassDiagram() }
    ];
    
    examples.forEach((example, index) => {
        console.log(`\n📊 示例${index + 1}：${example.name}`);
        console.log("代码长度:", example.code.length, "字符");
        console.log("前100字符预览:", example.code.substring(0, 100) + "...");
    });
    
    // 生成HTML查看器
    const htmlContent = createHTMLViewer(examples);
    
    // 如果在Node.js环境中，保存文件
    if (typeof require !== 'undefined') {
        const fs = require('fs');
        const path = require('path');
        
        const outputDir = "/workspace/plantuml_generators/examples/js_output";
        
        // 创建目录（同步方式）
        try {
            fs.mkdirSync(outputDir, { recursive: true });
        } catch (err) {
            // 目录可能已存在
        }
        
        // 保存HTML文件
        const htmlFile = path.join(outputDir, "examples_viewer.html");
        fs.writeFileSync(htmlFile, htmlContent, 'utf8');
        
        // 保存各个示例的PlantUML文件
        examples.forEach((example, index) => {
            const filename = example.name.replace(/\s+/g, '_').toLowerCase();
            const pumlFile = path.join(outputDir, `${filename}.puml`);
            fs.writeFileSync(pumlFile, example.code, 'utf8');
            console.log(`✅ 已保存: ${pumlFile}`);
        });
        
        console.log(`\n🌐 HTML查看器已保存: ${htmlFile}`);
        console.log(`🎯 所有文件已保存到: ${outputDir}`);
    }
    
    return examples;
}

// Node.js环境下运行
if (typeof require !== 'undefined' && require.main === module) {
    runAllExamples();
}

// 浏览器环境下的全局暴露
if (typeof window !== 'undefined') {
    window.PlantUMLExamples = {
        example1SimpleActivity,
        example2ComplexWorkflow,
        example3SequenceDiagram,
        example4ClassDiagram,
        runAllExamples
    };
}