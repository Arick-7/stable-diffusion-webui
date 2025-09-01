#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PlantUML生成器使用示例 - Python版本
展示各种图表类型的生成方法
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from plantuml_generator import (
    ActivityDiagramGenerator, 
    SequenceDiagramGenerator, 
    ClassDiagramGenerator,
    PlantUMLRenderer
)

def example_1_simple_activity():
    """示例1：简单活动图"""
    generator = ActivityDiagramGenerator()
    
    generator.set_title("简单工作流程")
    
    # 添加简单活动序列
    generator.add_activity("开始工作", "准备阶段")
    generator.add_activity("执行任务", "核心工作")
    generator.add_activity("检查结果", "质量控制")
    generator.add_activity("完成工作", "结束阶段")
    
    return generator.generate_code()

def example_2_complex_workflow():
    """示例2：复杂工作流程（建筑AI系统）"""
    generator = ActivityDiagramGenerator()
    
    generator.set_title("建筑AI辅助设计完整流程")
    
    # 数据输入阶段
    generator.add_partition("数据输入阶段", [
        "收集既往建筑项目策划书",
        "收集项目任务书",
        "获取国家建设标准", 
        "获取地方建设标准"
    ], "LIGHTBLUE")
    
    # AI处理阶段
    generator.add_partition("AI分析处理阶段", [
        "建筑大语言模型加载",
        "多源数据融合分析"
    ], "LIGHTGREEN")
    
    # 添加决策点
    generator.add_decision(
        "数据完整性检查",
        "启动对话式交互",
        "请求补充信息",
        "数据充足，可以继续",
        "缺少关键信息"
    )
    
    # 智能生成阶段
    generator.add_partition("智能生成阶段", [
        "快速生成策划书草案",
        "生成设计任务书",
        "识别关键性能指标",
        "明确项目目标和需求"
    ], "LIGHTYELLOW")
    
    # 并行处理关键指标
    generator.add_parallel_block([
        "能耗性能分析",
        "可持续性评估", 
        "舒适度指标设定",
        "经济性指标计算"
    ])
    
    # 输出优化阶段
    generator.add_partition("输出优化阶段", [
        "为设计师提供清晰方向",
        "识别技术挑战点",
        "生成针对性解决方案"
    ], "LIGHTCORAL")
    
    # 最终决策
    generator.add_decision(
        "质量检查通过？",
        "生成最终文档",
        "返回优化建议",
        "达到质量标准",
        "需要进一步改进"
    )
    
    # 价值实现阶段
    generator.add_partition("价值实现阶段", [
        "降低认知负荷",
        "提高工作效率", 
        "优化设计质量"
    ], "LIGHTPINK")
    
    # 添加系统说明
    generator.add_note(
        "系统通过AI技术整合多源建筑信息，实现智能化的项目策划与设计辅助。\n" +
        "核心价值：快速响应、标准合规、经验复用、智能预判、减负增效",
        "top"
    )
    
    return generator.generate_code()

def example_3_sequence_diagram():
    """示例3：序列图"""
    generator = SequenceDiagramGenerator()
    
    generator.set_title("建筑AI系统交互序列图")
    
    # 添加参与者
    generator.add_participant("建筑师", "Architect", "actor")
    generator.add_participant("AI系统", "AI", "participant")
    generator.add_participant("项目数据库", "ProjectDB", "database")
    generator.add_participant("标准API", "StandardAPI", "participant")
    generator.add_participant("文档生成器", "DocGen", "participant")
    
    # 添加交互消息
    generator.add_message("Architect", "AI", "上传项目基本信息")
    generator.add_message("AI", "ProjectDB", "查询相似历史项目")
    generator.add_message("ProjectDB", "AI", "返回项目数据")
    generator.add_message("AI", "StandardAPI", "获取适用建设标准")
    generator.add_message("StandardAPI", "AI", "返回标准规范")
    generator.add_message("AI", "Architect", "生成初步问题清单")
    generator.add_message("Architect", "AI", "回答项目需求问题")
    generator.add_message("AI", "AI", "分析需求和约束条件")
    generator.add_message("AI", "DocGen", "请求生成策划书")
    generator.add_message("DocGen", "AI", "返回策划书草案")
    generator.add_message("AI", "Architect", "提供完整策划方案")
    
    return generator.generate_code()

def example_4_class_diagram():
    """示例4：类图"""
    generator = ClassDiagramGenerator()
    
    generator.set_title("建筑AI系统架构类图")
    
    # 添加核心类
    generator.add_class(
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
    )
    
    generator.add_class(
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
    )
    
    generator.add_class(
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
    )
    
    generator.add_class(
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
    )
    
    # 添加关系
    generator.add_relationship("BuildingAISystem", "Project", "-->", "processes")
    generator.add_relationship("BuildingAISystem", "Plan", "-->", "generates")
    generator.add_relationship("Project", "Plan", "-->", "creates")
    generator.add_relationship("Plan", "KPI", "o--", "contains")
    
    return generator.generate_code()

def example_5_use_case_diagram():
    """示例5：用例图（手动生成）"""
    return """@startuml
!theme plain
title 建筑AI系统用例图

left to right direction

actor "建筑师" as Architect
actor "项目经理" as PM
actor "业主" as Owner

rectangle "建筑AI辅助设计系统" {
    usecase "上传项目信息" as UC1
    usecase "生成策划书" as UC2  
    usecase "生成任务书" as UC3
    usecase "识别关键指标" as UC4
    usecase "技术挑战分析" as UC5
    usecase "导出文档" as UC6
    usecase "查看历史项目" as UC7
    usecase "标准合规检查" as UC8
}

' 用例关系
Architect --> UC1
Architect --> UC2
Architect --> UC3
PM --> UC4
PM --> UC5
Owner --> UC6
Architect --> UC7
Architect --> UC8

' 包含关系
UC2 .> UC4 : <<include>>
UC3 .> UC4 : <<include>>
UC2 .> UC8 : <<include>>
UC3 .> UC8 : <<include>>

' 扩展关系
UC5 .> UC2 : <<extend>>

note right of UC4
    关键指标包括：
    - 能耗性能
    - 可持续性
    - 舒适度
    - 经济性
end note

@enduml"""

def run_all_examples():
    """运行所有示例"""
    print("🎨 PlantUML生成器使用示例")
    print("=" * 60)
    
    # 创建输出目录
    output_dir = "/workspace/plantuml_generators/examples/output"
    os.makedirs(output_dir, exist_ok=True)
    
    renderer = PlantUMLRenderer()
    
    examples = [
        ("简单活动图", example_1_simple_activity()),
        ("复杂工作流程", example_2_complex_workflow()),
        ("序列图", example_3_sequence_diagram()),
        ("类图", example_4_class_diagram()),
        ("用例图", example_5_use_case_diagram())
    ]
    
    for name, code in examples:
        print(f"\n📊 生成 {name}...")
        
        # 保存PlantUML文件
        filename = name.replace(" ", "_").lower()
        puml_file = os.path.join(output_dir, f"{filename}.puml")
        renderer.save_to_file(code, puml_file)
        
        # 创建HTML查看器
        html_content = renderer.create_html_viewer(code, name)
        html_file = os.path.join(output_dir, f"{filename}.html")
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"   ✅ PlantUML文件: {puml_file}")
        print(f"   🌐 HTML查看器: {html_file}")
    
    print(f"\n🎯 所有示例文件已保存到: {output_dir}")
    print("\n💡 使用提示：")
    print("1. 打开任意HTML文件查看对应的流程图")
    print("2. 复制PlantUML代码到在线编辑器查看")
    print("3. 可以基于这些示例创建自己的流程图")

if __name__ == "__main__":
    run_all_examples()