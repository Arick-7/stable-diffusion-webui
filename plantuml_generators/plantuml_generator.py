#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PlantUML代码生成器 - Python版本
支持生成各种类型的UML图表
"""

import os
import json
from datetime import datetime
from typing import List, Dict, Any, Optional
from enum import Enum


class DiagramType(Enum):
    """图表类型枚举"""
    ACTIVITY = "activity"
    SEQUENCE = "sequence"
    CLASS = "class"
    USE_CASE = "usecase"
    COMPONENT = "component"
    STATE = "state"
    DEPLOYMENT = "deployment"


class PlantUMLGenerator:
    """PlantUML代码生成器主类"""
    
    def __init__(self):
        self.theme = "plain"
        self.title = ""
        self.notes = []
        self.elements = []
        
    def set_theme(self, theme: str = "plain"):
        """设置主题"""
        self.theme = theme
        return self
    
    def set_title(self, title: str):
        """设置图表标题"""
        self.title = title
        return self
    
    def add_note(self, content: str, position: str = "bottom"):
        """添加注释"""
        self.notes.append({"content": content, "position": position})
        return self


class ActivityDiagramGenerator(PlantUMLGenerator):
    """活动图生成器"""
    
    def __init__(self):
        super().__init__()
        self.activities = []
        self.partitions = []
        self.decisions = []
        self.parallel_blocks = []
    
    def add_activity(self, name: str, note: str = "", note_position: str = "right"):
        """添加活动"""
        activity = {
            "type": "activity",
            "name": name,
            "note": note,
            "note_position": note_position
        }
        self.activities.append(activity)
        return self
    
    def add_partition(self, name: str, activities: List[str], color: str = ""):
        """添加分区"""
        partition = {
            "name": name,
            "activities": activities,
            "color": color
        }
        self.partitions.append(partition)
        return self
    
    def add_decision(self, question: str, yes_path: str, no_path: str, 
                    yes_note: str = "", no_note: str = ""):
        """添加决策点"""
        decision = {
            "question": question,
            "yes_path": yes_path,
            "no_path": no_path,
            "yes_note": yes_note,
            "no_note": no_note
        }
        self.decisions.append(decision)
        return self
    
    def add_parallel_block(self, activities: List[str]):
        """添加并行执行块"""
        self.parallel_blocks.append(activities)
        return self
    
    def generate_code(self) -> str:
        """生成PlantUML活动图代码"""
        code = ["@startuml"]
        
        if self.theme:
            code.append(f"!theme {self.theme}")
        
        if self.title:
            code.append(f"title {self.title}")
        
        # 添加样式定义
        code.extend([
            "",
            "' 样式定义",
            "skinparam activity {",
            "    BackgroundColor lightblue",
            "    BorderColor black",
            "    FontSize 12",
            "}",
            "",
            "skinparam activityDiamond {",
            "    BackgroundColor lightyellow",
            "    BorderColor black",
            "}",
            "",
            "skinparam note {",
            "    BackgroundColor lightgreen",
            "    BorderColor darkgreen",
            "}",
            "",
            "start",
            ""
        ])
        
        # 生成分区和活动
        for partition in self.partitions:
            color_attr = f" #{partition['color']}" if partition['color'] else ""
            code.append(f"partition \"{partition['name']}\"{color_attr} {{")
            
            for activity in partition['activities']:
                code.append(f"    :{activity};")
            
            code.append("}")
            code.append("")
        
        # 添加单独的活动
        for activity in self.activities:
            code.append(f":{activity['name']};")
            if activity['note']:
                code.append(f"note {activity['note_position']}: {activity['note']}")
            code.append("")
        
        # 添加决策点
        for decision in self.decisions:
            code.append(f"if ({decision['question']}) then (是)")
            code.append(f"    :{decision['yes_path']};")
            if decision['yes_note']:
                code.append(f"    note right: {decision['yes_note']}")
            code.append("else (否)")
            code.append(f"    :{decision['no_path']};")
            if decision['no_note']:
                code.append(f"    note right: {decision['no_note']}")
            code.append("endif")
            code.append("")
        
        # 添加并行块
        for parallel in self.parallel_blocks:
            code.append("fork")
            for i, activity in enumerate(parallel):
                if i > 0:
                    code.append("fork again")
                code.append(f"    :{activity};")
            code.append("end fork")
            code.append("")
        
        code.append("stop")
        
        # 添加注释
        for note in self.notes:
            code.append(f"note {note['position']}")
            code.append(f"    {note['content']}")
            code.append("end note")
        
        code.append("@enduml")
        
        return "\n".join(code)


class SequenceDiagramGenerator(PlantUMLGenerator):
    """序列图生成器"""
    
    def __init__(self):
        super().__init__()
        self.participants = []
        self.messages = []
        self.activations = []
    
    def add_participant(self, name: str, alias: str = "", participant_type: str = "participant"):
        """添加参与者"""
        participant = {
            "name": name,
            "alias": alias or name,
            "type": participant_type
        }
        self.participants.append(participant)
        return self
    
    def add_message(self, from_participant: str, to_participant: str, 
                   message: str, arrow_type: str = "->"):
        """添加消息"""
        msg = {
            "from": from_participant,
            "to": to_participant,
            "message": message,
            "arrow": arrow_type
        }
        self.messages.append(msg)
        return self
    
    def add_activation(self, participant: str, start_msg: str, end_msg: str = ""):
        """添加激活框"""
        activation = {
            "participant": participant,
            "start": start_msg,
            "end": end_msg
        }
        self.activations.append(activation)
        return self
    
    def generate_code(self) -> str:
        """生成PlantUML序列图代码"""
        code = ["@startuml"]
        
        if self.theme:
            code.append(f"!theme {self.theme}")
        
        if self.title:
            code.append(f"title {self.title}")
        
        code.append("")
        
        # 添加参与者
        for participant in self.participants:
            if participant['alias'] != participant['name']:
                code.append(f"{participant['type']} \"{participant['name']}\" as {participant['alias']}")
            else:
                code.append(f"{participant['type']} {participant['name']}")
        
        code.append("")
        
        # 添加消息
        for msg in self.messages:
            code.append(f"{msg['from']} {msg['arrow']} {msg['to']}: {msg['message']}")
        
        code.append("@enduml")
        
        return "\n".join(code)


class ClassDiagramGenerator(PlantUMLGenerator):
    """类图生成器"""
    
    def __init__(self):
        super().__init__()
        self.classes = []
        self.relationships = []
    
    def add_class(self, name: str, attributes: List[str] = None, 
                 methods: List[str] = None, stereotype: str = ""):
        """添加类"""
        class_def = {
            "name": name,
            "attributes": attributes or [],
            "methods": methods or [],
            "stereotype": stereotype
        }
        self.classes.append(class_def)
        return self
    
    def add_relationship(self, from_class: str, to_class: str, 
                        relationship_type: str = "-->", label: str = ""):
        """添加关系"""
        rel = {
            "from": from_class,
            "to": to_class,
            "type": relationship_type,
            "label": label
        }
        self.relationships.append(rel)
        return self
    
    def generate_code(self) -> str:
        """生成PlantUML类图代码"""
        code = ["@startuml"]
        
        if self.theme:
            code.append(f"!theme {self.theme}")
        
        if self.title:
            code.append(f"title {self.title}")
        
        code.append("")
        
        # 添加类定义
        for cls in self.classes:
            if cls['stereotype']:
                code.append(f"class {cls['name']} <<{cls['stereotype']}>> {{")
            else:
                code.append(f"class {cls['name']} {{")
            
            # 添加属性
            for attr in cls['attributes']:
                code.append(f"    {attr}")
            
            if cls['attributes'] and cls['methods']:
                code.append("    --")
            
            # 添加方法
            for method in cls['methods']:
                code.append(f"    {method}")
            
            code.append("}")
            code.append("")
        
        # 添加关系
        for rel in self.relationships:
            if rel['label']:
                code.append(f"{rel['from']} {rel['type']} {rel['to']} : {rel['label']}")
            else:
                code.append(f"{rel['from']} {rel['type']} {rel['to']}")
        
        code.append("@enduml")
        
        return "\n".join(code)


class PlantUMLFactory:
    """PlantUML工厂类，用于创建不同类型的图表生成器"""
    
    @staticmethod
    def create_generator(diagram_type: DiagramType):
        """根据图表类型创建对应的生成器"""
        if diagram_type == DiagramType.ACTIVITY:
            return ActivityDiagramGenerator()
        elif diagram_type == DiagramType.SEQUENCE:
            return SequenceDiagramGenerator()
        elif diagram_type == DiagramType.CLASS:
            return ClassDiagramGenerator()
        else:
            return PlantUMLGenerator()


class PlantUMLRenderer:
    """PlantUML渲染器，用于将代码转换为图片或HTML"""
    
    def __init__(self):
        self.base_url = "http://www.plantuml.com/plantuml"
    
    def generate_url(self, plantuml_code: str, format_type: str = "svg") -> str:
        """生成PlantUML在线查看URL"""
        import base64
        import zlib
        
        # 压缩代码
        compressed = zlib.compress(plantuml_code.encode('utf-8'))
        encoded = base64.b64encode(compressed).decode('ascii')
        
        return f"{self.base_url}/{format_type}/{encoded}"
    
    def save_to_file(self, plantuml_code: str, file_path: str):
        """保存PlantUML代码到文件"""
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(plantuml_code)
    
    def create_html_viewer(self, plantuml_code: str, title: str = "PlantUML图表") -> str:
        """创建HTML查看器"""
        html_template = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: 'Microsoft YaHei', Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}
        h1 {{
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }}
        .code-section {{
            margin: 20px 0;
        }}
        .code-block {{
            background: #2c3e50;
            color: #ecf0f1;
            padding: 20px;
            border-radius: 10px;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            line-height: 1.4;
            max-height: 500px;
            overflow-y: auto;
        }}
        .btn {{
            background: #3498db;
            color: white;
            padding: 12px 24px;
            text-decoration: none;
            border-radius: 25px;
            display: inline-block;
            margin: 10px;
            font-size: 16px;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
        }}
        .btn:hover {{
            background: #2980b9;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }}
        .btn-copy {{
            background: #27ae60;
        }}
        .btn-copy:hover {{
            background: #219a52;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 {title}</h1>
        
        <div style="text-align: center; margin: 30px 0;">
            <a href="http://www.plantuml.com/plantuml/uml/" target="_blank" class="btn">
                🌐 PlantUML在线编辑器
            </a>
            <button class="btn btn-copy" onclick="copyToClipboard()">
                📋 复制代码
            </button>
        </div>
        
        <div class="code-section">
            <h3>PlantUML代码：</h3>
            <div class="code-block" id="plantuml-code">{plantuml_code}</div>
        </div>
        
        <div style="margin-top: 30px;">
            <h3>使用说明：</h3>
            <ol>
                <li>点击"复制代码"按钮复制PlantUML代码</li>
                <li>打开PlantUML在线编辑器</li>
                <li>粘贴代码并查看生成的图表</li>
                <li>可以导出为PNG、SVG等格式</li>
            </ol>
        </div>
    </div>

    <script>
        function copyToClipboard() {{
            const codeElement = document.getElementById('plantuml-code');
            const text = codeElement.textContent;
            
            navigator.clipboard.writeText(text).then(function() {{
                alert('代码已复制到剪贴板！');
            }}, function(err) {{
                console.error('复制失败: ', err);
                // 备用复制方法
                const textArea = document.createElement('textarea');
                textArea.value = text;
                document.body.appendChild(textArea);
                textArea.select();
                document.execCommand('copy');
                document.body.removeChild(textArea);
                alert('代码已复制到剪贴板！');
            }});
        }}
    </script>
</body>
</html>"""
        return html_template


def create_building_ai_workflow():
    """创建建筑AI工作流程图"""
    generator = ActivityDiagramGenerator()
    
    generator.set_title("建筑AI辅助策划与设计系统工作流程")
    
    # 添加分区和活动
    generator.add_partition("数据输入阶段", [
        "收集既往建筑项目策划书",
        "收集项目任务书", 
        "获取国家建设标准",
        "获取地方建设标准"
    ])
    
    generator.add_partition("AI分析处理阶段", [
        "建筑大语言模型加载",
        "多源数据融合分析",
        "启动对话式交互"
    ])
    
    generator.add_partition("智能生成阶段", [
        "快速生成策划书草案",
        "生成设计任务书",
        "识别关键性能指标",
        "明确项目目标和需求"
    ])
    
    generator.add_partition("输出优化阶段", [
        "为设计师提供清晰方向",
        "识别技术挑战点", 
        "生成针对性解决方案"
    ])
    
    generator.add_partition("价值实现阶段", [
        "降低认知负荷",
        "提高工作效率",
        "优化设计质量"
    ])
    
    generator.add_note(
        "系统通过AI技术整合多源建筑信息，实现智能化的项目策划与设计辅助",
        "top"
    )
    
    return generator.generate_code()


def create_sequence_diagram_example():
    """创建序列图示例"""
    generator = SequenceDiagramGenerator()
    
    generator.set_title("建筑AI系统交互序列图")
    
    # 添加参与者
    generator.add_participant("用户", "User", "actor")
    generator.add_participant("AI系统", "AI", "participant")
    generator.add_participant("数据库", "DB", "database")
    generator.add_participant("标准API", "API", "participant")
    
    # 添加消息交互
    generator.add_message("User", "AI", "上传项目信息")
    generator.add_message("AI", "DB", "查询历史项目数据")
    generator.add_message("AI", "API", "获取建设标准")
    generator.add_message("AI", "User", "生成对话问题")
    generator.add_message("User", "AI", "回答问题")
    generator.add_message("AI", "AI", "分析需求")
    generator.add_message("AI", "User", "生成策划书")
    
    return generator.generate_code()


def create_class_diagram_example():
    """创建类图示例"""
    generator = ClassDiagramGenerator()
    
    generator.set_title("建筑AI系统类图")
    
    # 添加类
    generator.add_class(
        "BuildingAISystem",
        ["- llm_model: LanguageModel", "- database: ProjectDatabase", "- standards: StandardsAPI"],
        ["+ generatePlan(project: Project): Plan", "+ analyzeRequirements(input: String): Requirements"]
    )
    
    generator.add_class(
        "Project",
        ["- id: String", "- type: String", "- requirements: List<String>"],
        ["+ validate(): Boolean", "+ getType(): String"]
    )
    
    generator.add_class(
        "Plan",
        ["- content: String", "- kpis: List<KPI>", "- challenges: List<Challenge>"],
        ["+ export(): PDF", "+ validate(): Boolean"]
    )
    
    # 添加关系
    generator.add_relationship("BuildingAISystem", "Project", "-->", "processes")
    generator.add_relationship("BuildingAISystem", "Plan", "-->", "generates")
    generator.add_relationship("Project", "Plan", "-->", "creates")
    
    return generator.generate_code()


if __name__ == "__main__":
    print("🚀 PlantUML生成器 - Python版本")
    print("=" * 50)
    
    # 创建输出目录
    output_dir = "/workspace/plantuml_generators/output"
    os.makedirs(output_dir, exist_ok=True)
    
    renderer = PlantUMLRenderer()
    
    # 1. 生成建筑AI工作流程图
    workflow_code = create_building_ai_workflow()
    workflow_file = os.path.join(output_dir, "building_ai_workflow.puml")
    renderer.save_to_file(workflow_code, workflow_file)
    
    # 创建HTML查看器
    html_content = renderer.create_html_viewer(workflow_code, "建筑AI工作流程图")
    html_file = os.path.join(output_dir, "building_ai_workflow.html")
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # 2. 生成序列图示例
    sequence_code = create_sequence_diagram_example()
    sequence_file = os.path.join(output_dir, "sequence_diagram.puml")
    renderer.save_to_file(sequence_code, sequence_file)
    
    # 3. 生成类图示例
    class_code = create_class_diagram_example()
    class_file = os.path.join(output_dir, "class_diagram.puml")
    renderer.save_to_file(class_code, class_file)
    
    print("✅ 已生成以下文件：")
    print(f"   📄 工作流程图: {workflow_file}")
    print(f"   🌐 HTML查看器: {html_file}")
    print(f"   📄 序列图示例: {sequence_file}")
    print(f"   📄 类图示例: {class_file}")
    
    print(f"\n🎯 所有文件已保存到: {output_dir}")