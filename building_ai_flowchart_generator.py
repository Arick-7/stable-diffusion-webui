#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
建筑AI辅助设计系统工作流程图生成器
基于给定的文字描述生成PlantUML流程图
"""

import os
from datetime import datetime


class BuildingAIFlowchartGenerator:
    """建筑AI辅助设计系统流程图生成器"""
    
    def __init__(self):
        self.title = "建筑AI辅助策划与设计系统工作流程"
        self.description = """
        AI可以基于既往建筑项目的策划书、任务书，以及国家和地方对特定类型建筑项目的建设标准，
        利用建筑大语言模型。通过对话形式，快速产出策划与设计任务书，这有助于更迅速地明确项目目标和需求。
        同时可识别关键性能指标，例如能耗、可持续性、舒适度等，对设计师更好地理解项目的特点，
        为后续设计提供清晰的方向，有针对性的面对技术挑战提供了高效的协助功能，
        从这个角度看也能大幅度降低人在信息收集和初期处理阶段的认知负荷。
        """
    
    def generate_plantuml_flowchart(self):
        """生成PlantUML流程图代码"""
        
        plantuml_code = f"""@startuml
!theme plain
title {self.title}

' 定义颜色和样式
skinparam activity {{
    BackgroundColor lightblue
    BorderColor black
    FontSize 12
}}

skinparam activityDiamond {{
    BackgroundColor lightyellow
    BorderColor black
}}

skinparam note {{
    BackgroundColor lightgreen
    BorderColor darkgreen
}}

start

' 输入数据源
partition "数据输入阶段" {{
    :收集既往建筑项目策划书;
    note right: 历史项目经验数据
    
    :收集项目任务书;
    note right: 当前项目需求文档
    
    :获取国家建设标准;
    note right: 国家级规范要求
    
    :获取地方建设标准;
    note right: 地方性规范要求
}}

' AI处理阶段
partition "AI分析处理阶段" {{
    :建筑大语言模型加载;
    note right: 专业领域AI模型
    
    :多源数据融合分析;
    note right: 整合所有输入信息
    
    if (数据完整性检查) then (完整)
        :启动对话式交互;
        note right: 与用户进行智能对话
    else (不完整)
        :请求补充信息;
        note right: 提示缺失的关键信息
        stop
    endif
}}

' 核心功能执行
partition "智能生成阶段" {{
    :快速生成策划书草案;
    note right: 基于AI分析的初步方案
    
    :生成设计任务书;
    note right: 详细的设计指导文档
    
    :识别关键性能指标;
    note right: 能耗、可持续性、舒适度等
    
    :明确项目目标和需求;
    note right: 清晰的项目定位
}}

' 输出优化
partition "输出优化阶段" {{
    :为设计师提供清晰方向;
    note right: 可操作的设计指导
    
    :识别技术挑战点;
    note right: 预判可能的技术难点
    
    :生成针对性解决方案;
    note right: 具体的应对策略
}}

' 价值实现
partition "价值实现阶段" {{
    :降低认知负荷;
    note right: 减少信息收集工作量
    
    :提高工作效率;
    note right: 加速项目前期准备
    
    :优化设计质量;
    note right: 基于标准和经验的优化
}}

stop

' 添加注释说明
note top of start
    系统通过AI技术整合多源建筑信息，
    实现智能化的项目策划与设计辅助
end note

@enduml"""
        
        return plantuml_code
    
    def generate_detailed_workflow(self):
        """生成详细的工作流程PlantUML图"""
        
        detailed_plantuml = """@startuml
!theme plain
title 建筑AI辅助设计系统详细工作流程

' 样式定义
skinparam activity {
    BackgroundColor #E1F5FE
    BorderColor #0277BD
    FontSize 11
}

skinparam activityDiamond {
    BackgroundColor #FFF3E0
    BorderColor #F57C00
}

skinparam partition {
    BorderColor #424242
    FontSize 12
    FontStyle bold
}

start

' 数据准备阶段
partition "**数据准备与预处理**" #LIGHTBLUE {
    :用户上传项目基本信息;
    
    fork
        :加载既往策划书数据库;
        note right: 结构化存储的历史项目数据
    fork again
        :加载任务书模板库;
        note right: 标准化的任务书格式
    fork again
        :调用国家标准API;
        note right: 实时获取最新标准
    fork again
        :调用地方标准数据库;
        note right: 地区特定的建设要求
    end fork
    
    :数据预处理与标准化;
    note right: 统一数据格式，清洗无效信息
}

' AI模型处理
partition "**AI智能分析**" #LIGHTGREEN {
    :初始化建筑大语言模型;
    note right: 加载预训练的专业模型
    
    :项目类型识别与分类;
    if (项目类型明确?) then (是)
        :匹配相应的标准模板;
    else (否)
        :启动类型识别对话;
        :用户确认项目类型;
    endif
    
    :多维度需求分析;
    note right
        - 功能需求分析
        - 技术需求评估
        - 法规合规检查
        - 经济可行性预判
    end note
}

' 对话交互阶段
partition "**智能对话生成**" #LIGHTYELLOW {
    repeat
        :生成针对性问题;
        note right: 基于缺失信息生成问题
        
        :用户回答问题;
        
        :更新项目需求模型;
        
        if (信息完整度检查) then (>=80%)
            :确认进入生成阶段;
        else (<80%)
            :继续收集信息;
        endif
    repeat while (信息完整?) is (否)
}

' 文档生成阶段
partition "**文档智能生成**" #LIGHTCORAL {
    fork
        :生成项目策划书;
        note right
            - 项目背景与目标
            - 技术路线规划
            - 资源配置方案
            - 风险评估预案
        end note
    fork again
        :生成设计任务书;
        note right
            - 设计要求详述
            - 技术标准清单
            - 质量控制要点
            - 交付成果规范
        end note
    end fork
}

' 性能指标识别
partition "**关键指标识别**" #LIGHTSTEELBLUE {
    :能耗性能分析;
    note right: 建筑能效等级预测
    
    :可持续性评估;
    note right: 绿色建筑认证可行性
    
    :舒适度指标设定;
    note right: 室内环境质量标准
    
    :经济性指标计算;
    note right: 成本效益分析
    
    :安全性能要求;
    note right: 结构安全与消防安全
}

' 输出优化
partition "**输出优化与验证**" #LAVENDER {
    :技术挑战识别;
    note right: 预判设计难点和技术风险
    
    :解决方案推荐;
    note right: 基于经验库的解决策略
    
    :文档质量检查;
    if (质量达标?) then (是)
        :生成最终文档;
    else (否)
        :返回优化建议;
        backward :重新生成;
    endif
}

' 交付阶段
partition "**成果交付**" #LIGHTPINK {
    :生成项目策划书PDF;
    :生成设计任务书PDF;
    :生成关键指标清单;
    :生成技术挑战应对方案;
    
    :降低设计师认知负荷;
    note right
        - 减少信息搜集时间
        - 提供结构化指导
        - 预判技术风险
    end note
}

stop

' 系统价值说明
note bottom
    **系统核心价值：**
    1. 快速响应：通过AI对话快速明确需求
    2. 标准合规：确保符合国家和地方标准
    3. 经验复用：利用历史项目经验
    4. 智能预判：提前识别技术挑战
    5. 减负增效：降低认知负荷，提高效率
end note

@enduml"""
        
        return detailed_plantuml

    def save_plantuml_files(self):
        """保存PlantUML文件到工作空间"""
        
        # 创建输出目录
        output_dir = "/workspace/building_ai_flowcharts"
        os.makedirs(output_dir, exist_ok=True)
        
        # 生成基础流程图
        basic_flowchart = self.generate_plantuml_flowchart()
        basic_file_path = os.path.join(output_dir, "basic_workflow.puml")
        
        with open(basic_file_path, 'w', encoding='utf-8') as f:
            f.write(basic_flowchart)
        
        # 生成详细流程图
        detailed_flowchart = self.generate_detailed_workflow()
        detailed_file_path = os.path.join(output_dir, "detailed_workflow.puml")
        
        with open(detailed_file_path, 'w', encoding='utf-8') as f:
            f.write(detailed_flowchart)
        
        return basic_file_path, detailed_file_path
    
    def create_html_viewer(self):
        """创建HTML查看器，可以在线渲染PlantUML图表"""
        
        html_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>建筑AI工作流程图查看器</title>
    <style>
        body {
            font-family: 'Microsoft YaHei', Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        .description {
            background: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
            line-height: 1.6;
        }
        .workflow-section {
            margin: 30px 0;
        }
        .workflow-section h2 {
            color: #34495e;
            border-left: 4px solid #3498db;
            padding-left: 10px;
        }
        .plantuml-link {
            background: #3498db;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            display: inline-block;
            margin: 10px 5px;
        }
        .plantuml-link:hover {
            background: #2980b9;
        }
        .code-block {
            background: #2c3e50;
            color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            margin: 10px 0;
        }
        .analysis {
            background: #e8f6f3;
            border-left: 4px solid #1abc9c;
            padding: 15px;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏗️ 建筑AI辅助策划与设计系统工作流程图</h1>
        
        <div class="description">
            <h3>📋 原始需求描述：</h3>
            <p>AI可以基于既往建筑项目的策划书、任务书，以及国家和地方对特定类型建筑项目的建设标准，利用建筑大语言模型。通过对话形式，快速产出策划与设计任务书，这有助于更迅速地明确项目目标和需求。同时可识别关键性能指标，例如能耗、可持续性、舒适度等，对设计师更好地理解项目的特点，为后续设计提供清晰的方向，有针对性的面对技术挑战提供了高效的协助功能，从这个角度看也能大幅度降低人在信息收集和初期处理阶段的认知负荷。</p>
        </div>

        <div class="analysis">
            <h3>🔍 流程分析结果：</h3>
            <ul>
                <li><strong>输入源：</strong>既往策划书、任务书、国家标准、地方标准</li>
                <li><strong>核心技术：</strong>建筑大语言模型 + 对话式交互</li>
                <li><strong>主要功能：</strong>智能生成策划书和设计任务书</li>
                <li><strong>关键指标：</strong>能耗、可持续性、舒适度等性能参数</li>
                <li><strong>核心价值：</strong>降低认知负荷、提高效率、预判技术挑战</li>
            </ul>
        </div>

        <div class="workflow-section">
            <h2>📊 在线查看流程图</h2>
            <p>点击下面的链接在PlantUML在线编辑器中查看和编辑流程图：</p>
            
            <a href="http://www.plantuml.com/plantuml/uml/" target="_blank" class="plantuml-link">
                🌐 PlantUML在线编辑器
            </a>
            
            <a href="https://plantuml-editor.kkeisuke.com/" target="_blank" class="plantuml-link">
                ✏️ 替代在线编辑器
            </a>
        </div>

        <div class="workflow-section">
            <h2>📁 生成的文件</h2>
            <ul>
                <li><code>basic_workflow.puml</code> - 基础工作流程图</li>
                <li><code>detailed_workflow.puml</code> - 详细工作流程图</li>
                <li><code>workflow_viewer.html</code> - 本查看器文件</li>
            </ul>
        </div>

        <div class="workflow-section">
            <h2>🚀 使用说明</h2>
            <ol>
                <li>复制下方的PlantUML代码</li>
                <li>打开PlantUML在线编辑器</li>
                <li>粘贴代码并查看生成的流程图</li>
                <li>可以根据需要修改和定制流程图</li>
            </ol>
        </div>

        <div class="workflow-section">
            <h2>💡 扩展建议</h2>
            <ul>
                <li><strong>数据库集成：</strong>建立标准化的项目数据库</li>
                <li><strong>模型优化：</strong>针对建筑领域进行模型微调</li>
                <li><strong>用户界面：</strong>开发友好的Web界面</li>
                <li><strong>质量控制：</strong>添加专家审核环节</li>
                <li><strong>版本管理：</strong>支持文档版本控制</li>
            </ul>
        </div>
    </div>

    <script>
        // 添加一些交互功能
        document.addEventListener('DOMContentLoaded', function() {
            console.log('建筑AI工作流程图查看器已加载');
        });
    </script>
</body>
</html>"""
        
        return html_content
    
    def run(self):
        """运行流程图生成器"""
        print("🏗️ 建筑AI辅助设计系统流程图生成器")
        print("=" * 50)
        
        # 创建输出目录
        output_dir = "/workspace/building_ai_flowcharts"
        os.makedirs(output_dir, exist_ok=True)
        
        # 保存PlantUML文件
        basic_file, detailed_file = self.save_plantuml_files()
        
        # 创建HTML查看器
        html_content = self.create_html_viewer()
        html_file_path = os.path.join(output_dir, "workflow_viewer.html")
        
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ 已生成以下文件：")
        print(f"   📄 基础流程图: {basic_file}")
        print(f"   📄 详细流程图: {detailed_file}")
        print(f"   🌐 HTML查看器: {html_file_path}")
        
        print("\n📋 流程分析总结：")
        print("1. 数据输入：整合多源建筑信息")
        print("2. AI处理：大语言模型智能分析")
        print("3. 对话交互：明确项目需求")
        print("4. 文档生成：自动产出策划书和任务书")
        print("5. 指标识别：关键性能参数提取")
        print("6. 价值实现：降低认知负荷，提高效率")
        
        return output_dir


if __name__ == "__main__":
    generator = BuildingAIFlowchartGenerator()
    output_directory = generator.run()
    
    print(f"\n🎯 所有文件已保存到: {output_directory}")
    print("\n💡 使用提示：")
    print("1. 打开 workflow_viewer.html 查看完整说明")
    print("2. 复制 .puml 文件内容到 PlantUML 在线编辑器查看图表")
    print("3. 可以根据具体项目需求修改和定制流程图")