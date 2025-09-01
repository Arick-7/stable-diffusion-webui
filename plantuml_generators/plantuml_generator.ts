/**
 * PlantUML代码生成器 - TypeScript版本
 * 支持生成各种类型的UML图表
 */

interface Note {
    content: string;
    position: string;
}

interface Activity {
    type: string;
    name: string;
    note: string;
    notePosition: string;
}

interface Partition {
    name: string;
    activities: string[];
    color: string;
}

interface Decision {
    question: string;
    yesPath: string;
    noPath: string;
    yesNote: string;
    noNote: string;
}

interface Participant {
    name: string;
    alias: string;
    type: string;
}

interface Message {
    from: string;
    to: string;
    message: string;
    arrow: string;
}

interface ClassDefinition {
    name: string;
    attributes: string[];
    methods: string[];
    stereotype: string;
}

interface Relationship {
    from: string;
    to: string;
    type: string;
    label: string;
}

enum DiagramType {
    ACTIVITY = "activity",
    SEQUENCE = "sequence",
    CLASS = "class",
    USE_CASE = "usecase",
    COMPONENT = "component",
    STATE = "state",
    DEPLOYMENT = "deployment"
}

abstract class PlantUMLGenerator {
    protected theme: string;
    protected title: string;
    protected notes: Note[];
    
    constructor() {
        this.theme = "plain";
        this.title = "";
        this.notes = [];
    }
    
    setTheme(theme: string = "plain"): this {
        this.theme = theme;
        return this;
    }
    
    setTitle(title: string): this {
        this.title = title;
        return this;
    }
    
    addNote(content: string, position: string = "bottom"): this {
        this.notes.push({ content, position });
        return this;
    }
    
    abstract generateCode(): string;
}

class ActivityDiagramGenerator extends PlantUMLGenerator {
    private activities: Activity[];
    private partitions: Partition[];
    private decisions: Decision[];
    private parallelBlocks: string[][];
    
    constructor() {
        super();
        this.activities = [];
        this.partitions = [];
        this.decisions = [];
        this.parallelBlocks = [];
    }
    
    addActivity(name: string, note: string = "", notePosition: string = "right"): this {
        const activity: Activity = {
            type: "activity",
            name,
            note,
            notePosition
        };
        this.activities.push(activity);
        return this;
    }
    
    addPartition(name: string, activities: string[], color: string = ""): this {
        const partition: Partition = {
            name,
            activities,
            color
        };
        this.partitions.push(partition);
        return this;
    }
    
    addDecision(question: string, yesPath: string, noPath: string, 
               yesNote: string = "", noNote: string = ""): this {
        const decision: Decision = {
            question,
            yesPath,
            noPath,
            yesNote,
            noNote
        };
        this.decisions.push(decision);
        return this;
    }
    
    addParallelBlock(activities: string[]): this {
        this.parallelBlocks.push([...activities]);
        return this;
    }
    
    generateCode(): string {
        const code: string[] = ["@startuml"];
        
        if (this.theme) {
            code.push(`!theme ${this.theme}`);
        }
        
        if (this.title) {
            code.push(`title ${this.title}`);
        }
        
        // 添加样式定义
        code.push(
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
        );
        
        // 生成分区和活动
        this.partitions.forEach(partition => {
            const colorAttr = partition.color ? ` #${partition.color}` : "";
            code.push(`partition "${partition.name}"${colorAttr} {`);
            
            partition.activities.forEach(activity => {
                code.push(`    :${activity};`);
            });
            
            code.push("}", "");
        });
        
        // 添加单独的活动
        this.activities.forEach(activity => {
            code.push(`:${activity.name};`);
            if (activity.note) {
                code.push(`note ${activity.notePosition}: ${activity.note}`);
            }
            code.push("");
        });
        
        // 添加决策点
        this.decisions.forEach(decision => {
            code.push(`if (${decision.question}) then (是)`);
            code.push(`    :${decision.yesPath};`);
            if (decision.yesNote) {
                code.push(`    note right: ${decision.yesNote}`);
            }
            code.push("else (否)");
            code.push(`    :${decision.noPath};`);
            if (decision.noNote) {
                code.push(`    note right: ${decision.noNote}`);
            }
            code.push("endif", "");
        });
        
        // 添加并行块
        this.parallelBlocks.forEach(parallel => {
            code.push("fork");
            parallel.forEach((activity, index) => {
                if (index > 0) {
                    code.push("fork again");
                }
                code.push(`    :${activity};`);
            });
            code.push("end fork", "");
        });
        
        code.push("stop");
        
        // 添加注释
        this.notes.forEach(note => {
            code.push(`note ${note.position}`);
            code.push(`    ${note.content}`);
            code.push("end note");
        });
        
        code.push("@enduml");
        
        return code.join("\n");
    }
}

class SequenceDiagramGenerator extends PlantUMLGenerator {
    private participants: Participant[];
    private messages: Message[];
    
    constructor() {
        super();
        this.participants = [];
        this.messages = [];
    }
    
    addParticipant(name: string, alias: string = "", participantType: string = "participant"): this {
        const participant: Participant = {
            name,
            alias: alias || name,
            type: participantType
        };
        this.participants.push(participant);
        return this;
    }
    
    addMessage(fromParticipant: string, toParticipant: string, 
              message: string, arrowType: string = "->"): this {
        const msg: Message = {
            from: fromParticipant,
            to: toParticipant,
            message,
            arrow: arrowType
        };
        this.messages.push(msg);
        return this;
    }
    
    generateCode(): string {
        const code: string[] = ["@startuml"];
        
        if (this.theme) {
            code.push(`!theme ${this.theme}`);
        }
        
        if (this.title) {
            code.push(`title ${this.title}`);
        }
        
        code.push("");
        
        // 添加参与者
        this.participants.forEach(participant => {
            if (participant.alias !== participant.name) {
                code.push(`${participant.type} "${participant.name}" as ${participant.alias}`);
            } else {
                code.push(`${participant.type} ${participant.name}`);
            }
        });
        
        code.push("");
        
        // 添加消息
        this.messages.forEach(msg => {
            code.push(`${msg.from} ${msg.arrow} ${msg.to}: ${msg.message}`);
        });
        
        code.push("@enduml");
        
        return code.join("\n");
    }
}

class ClassDiagramGenerator extends PlantUMLGenerator {
    private classes: ClassDefinition[];
    private relationships: Relationship[];
    
    constructor() {
        super();
        this.classes = [];
        this.relationships = [];
    }
    
    addClass(name: string, attributes: string[] = [], methods: string[] = [], stereotype: string = ""): this {
        const classDef: ClassDefinition = {
            name,
            attributes,
            methods,
            stereotype
        };
        this.classes.push(classDef);
        return this;
    }
    
    addRelationship(fromClass: string, toClass: string, 
                   relationshipType: string = "-->", label: string = ""): this {
        const rel: Relationship = {
            from: fromClass,
            to: toClass,
            type: relationshipType,
            label
        };
        this.relationships.push(rel);
        return this;
    }
    
    generateCode(): string {
        const code: string[] = ["@startuml"];
        
        if (this.theme) {
            code.push(`!theme ${this.theme}`);
        }
        
        if (this.title) {
            code.push(`title ${this.title}`);
        }
        
        code.push("");
        
        // 添加类定义
        this.classes.forEach(cls => {
            if (cls.stereotype) {
                code.push(`class ${cls.name} <<${cls.stereotype}>> {`);
            } else {
                code.push(`class ${cls.name} {`);
            }
            
            // 添加属性
            cls.attributes.forEach(attr => {
                code.push(`    ${attr}`);
            });
            
            if (cls.attributes.length > 0 && cls.methods.length > 0) {
                code.push("    --");
            }
            
            // 添加方法
            cls.methods.forEach(method => {
                code.push(`    ${method}`);
            });
            
            code.push("}", "");
        });
        
        // 添加关系
        this.relationships.forEach(rel => {
            if (rel.label) {
                code.push(`${rel.from} ${rel.type} ${rel.to} : ${rel.label}`);
            } else {
                code.push(`${rel.from} ${rel.type} ${rel.to}`);
            }
        });
        
        code.push("@enduml");
        
        return code.join("\n");
    }
}

class PlantUMLFactory {
    static createGenerator(diagramType: DiagramType): PlantUMLGenerator {
        switch (diagramType) {
            case DiagramType.ACTIVITY:
                return new ActivityDiagramGenerator();
            case DiagramType.SEQUENCE:
                return new SequenceDiagramGenerator();
            case DiagramType.CLASS:
                return new ClassDiagramGenerator();
            default:
                return new ActivityDiagramGenerator();
        }
    }
}

// 工具函数
function createBuildingAIWorkflow(): string {
    const generator = new ActivityDiagramGenerator();
    
    generator.setTitle("建筑AI辅助策划与设计系统工作流程");
    
    // 添加分区和活动
    generator.addPartition("数据输入阶段", [
        "收集既往建筑项目策划书",
        "收集项目任务书",
        "获取国家建设标准",
        "获取地方建设标准"
    ]);
    
    generator.addPartition("AI分析处理阶段", [
        "建筑大语言模型加载",
        "多源数据融合分析",
        "启动对话式交互"
    ]);
    
    generator.addPartition("智能生成阶段", [
        "快速生成策划书草案",
        "生成设计任务书",
        "识别关键性能指标",
        "明确项目目标和需求"
    ]);
    
    generator.addPartition("输出优化阶段", [
        "为设计师提供清晰方向",
        "识别技术挑战点",
        "生成针对性解决方案"
    ]);
    
    generator.addPartition("价值实现阶段", [
        "降低认知负荷",
        "提高工作效率",
        "优化设计质量"
    ]);
    
    generator.addNote(
        "系统通过AI技术整合多源建筑信息，实现智能化的项目策划与设计辅助",
        "top"
    );
    
    return generator.generateCode();
}

// 导出模块
export {
    PlantUMLGenerator,
    ActivityDiagramGenerator,
    SequenceDiagramGenerator,
    ClassDiagramGenerator,
    PlantUMLFactory,
    DiagramType,
    createBuildingAIWorkflow
};

// Node.js环境下的使用示例
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        PlantUMLGenerator,
        ActivityDiagramGenerator,
        SequenceDiagramGenerator,
        ClassDiagramGenerator,
        PlantUMLFactory,
        DiagramType,
        createBuildingAIWorkflow
    };
}