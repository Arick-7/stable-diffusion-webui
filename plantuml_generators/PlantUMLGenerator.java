/**
 * PlantUML代码生成器 - Java版本
 * 支持生成各种类型的UML图表
 */

import java.util.*;
import java.io.*;
import java.nio.file.*;

public class PlantUMLGenerator {
    protected String theme;
    protected String title;
    protected List<Note> notes;
    
    public PlantUMLGenerator() {
        this.theme = "plain";
        this.title = "";
        this.notes = new ArrayList<>();
    }
    
    public PlantUMLGenerator setTheme(String theme) {
        this.theme = theme;
        return this;
    }
    
    public PlantUMLGenerator setTitle(String title) {
        this.title = title;
        return this;
    }
    
    public PlantUMLGenerator addNote(String content, String position) {
        this.notes.add(new Note(content, position));
        return this;
    }
    
    public String generateCode() {
        return "@startuml\n@enduml";
    }
    
    // 内部类定义
    static class Note {
        String content;
        String position;
        
        Note(String content, String position) {
            this.content = content;
            this.position = position;
        }
    }
    
    static class Activity {
        String name;
        String note;
        String notePosition;
        
        Activity(String name, String note, String notePosition) {
            this.name = name;
            this.note = note;
            this.notePosition = notePosition;
        }
    }
    
    static class Partition {
        String name;
        List<String> activities;
        String color;
        
        Partition(String name, List<String> activities, String color) {
            this.name = name;
            this.activities = activities;
            this.color = color;
        }
    }
    
    static class Decision {
        String question;
        String yesPath;
        String noPath;
        String yesNote;
        String noNote;
        
        Decision(String question, String yesPath, String noPath, String yesNote, String noNote) {
            this.question = question;
            this.yesPath = yesPath;
            this.noPath = noPath;
            this.yesNote = yesNote;
            this.noNote = noNote;
        }
    }
}

class ActivityDiagramGenerator extends PlantUMLGenerator {
    private List<Activity> activities;
    private List<Partition> partitions;
    private List<Decision> decisions;
    private List<List<String>> parallelBlocks;
    
    public ActivityDiagramGenerator() {
        super();
        this.activities = new ArrayList<>();
        this.partitions = new ArrayList<>();
        this.decisions = new ArrayList<>();
        this.parallelBlocks = new ArrayList<>();
    }
    
    public ActivityDiagramGenerator addActivity(String name, String note, String notePosition) {
        this.activities.add(new Activity(name, note, notePosition));
        return this;
    }
    
    public ActivityDiagramGenerator addActivity(String name) {
        return addActivity(name, "", "right");
    }
    
    public ActivityDiagramGenerator addPartition(String name, List<String> activities, String color) {
        this.partitions.add(new Partition(name, activities, color));
        return this;
    }
    
    public ActivityDiagramGenerator addPartition(String name, List<String> activities) {
        return addPartition(name, activities, "");
    }
    
    public ActivityDiagramGenerator addDecision(String question, String yesPath, String noPath, 
                                              String yesNote, String noNote) {
        this.decisions.add(new Decision(question, yesPath, noPath, yesNote, noNote));
        return this;
    }
    
    public ActivityDiagramGenerator addDecision(String question, String yesPath, String noPath) {
        return addDecision(question, yesPath, noPath, "", "");
    }
    
    public ActivityDiagramGenerator addParallelBlock(List<String> activities) {
        this.parallelBlocks.add(new ArrayList<>(activities));
        return this;
    }
    
    @Override
    public String generateCode() {
        StringBuilder code = new StringBuilder();
        
        code.append("@startuml\n");
        
        if (theme != null && !theme.isEmpty()) {
            code.append("!theme ").append(theme).append("\n");
        }
        
        if (title != null && !title.isEmpty()) {
            code.append("title ").append(title).append("\n");
        }
        
        // 添加样式定义
        code.append("\n' 样式定义\n");
        code.append("skinparam activity {\n");
        code.append("    BackgroundColor lightblue\n");
        code.append("    BorderColor black\n");
        code.append("    FontSize 12\n");
        code.append("}\n\n");
        
        code.append("skinparam activityDiamond {\n");
        code.append("    BackgroundColor lightyellow\n");
        code.append("    BorderColor black\n");
        code.append("}\n\n");
        
        code.append("skinparam note {\n");
        code.append("    BackgroundColor lightgreen\n");
        code.append("    BorderColor darkgreen\n");
        code.append("}\n\n");
        
        code.append("start\n\n");
        
        // 生成分区和活动
        for (Partition partition : partitions) {
            String colorAttr = partition.color.isEmpty() ? "" : " #" + partition.color;
            code.append("partition \"").append(partition.name).append("\"").append(colorAttr).append(" {\n");
            
            for (String activity : partition.activities) {
                code.append("    :").append(activity).append(";\n");
            }
            
            code.append("}\n\n");
        }
        
        // 添加单独的活动
        for (Activity activity : activities) {
            code.append(":").append(activity.name).append(";\n");
            if (!activity.note.isEmpty()) {
                code.append("note ").append(activity.notePosition).append(": ").append(activity.note).append("\n");
            }
            code.append("\n");
        }
        
        // 添加决策点
        for (Decision decision : decisions) {
            code.append("if (").append(decision.question).append(") then (是)\n");
            code.append("    :").append(decision.yesPath).append(";\n");
            if (!decision.yesNote.isEmpty()) {
                code.append("    note right: ").append(decision.yesNote).append("\n");
            }
            code.append("else (否)\n");
            code.append("    :").append(decision.noPath).append(";\n");
            if (!decision.noNote.isEmpty()) {
                code.append("    note right: ").append(decision.noNote).append("\n");
            }
            code.append("endif\n\n");
        }
        
        // 添加并行块
        for (List<String> parallel : parallelBlocks) {
            code.append("fork\n");
            for (int i = 0; i < parallel.size(); i++) {
                if (i > 0) {
                    code.append("fork again\n");
                }
                code.append("    :").append(parallel.get(i)).append(";\n");
            }
            code.append("end fork\n\n");
        }
        
        code.append("stop\n");
        
        // 添加注释
        for (Note note : notes) {
            code.append("note ").append(note.position).append("\n");
            code.append("    ").append(note.content).append("\n");
            code.append("end note\n");
        }
        
        code.append("@enduml");
        
        return code.toString();
    }
}

class SequenceDiagramGenerator extends PlantUMLGenerator {
    private List<Participant> participants;
    private List<Message> messages;
    
    public SequenceDiagramGenerator() {
        super();
        this.participants = new ArrayList<>();
        this.messages = new ArrayList<>();
    }
    
    public SequenceDiagramGenerator addParticipant(String name, String alias, String participantType) {
        this.participants.add(new Participant(name, alias, participantType));
        return this;
    }
    
    public SequenceDiagramGenerator addParticipant(String name) {
        return addParticipant(name, name, "participant");
    }
    
    public SequenceDiagramGenerator addMessage(String from, String to, String message, String arrowType) {
        this.messages.add(new Message(from, to, message, arrowType));
        return this;
    }
    
    public SequenceDiagramGenerator addMessage(String from, String to, String message) {
        return addMessage(from, to, message, "->");
    }
    
    @Override
    public String generateCode() {
        StringBuilder code = new StringBuilder();
        
        code.append("@startuml\n");
        
        if (theme != null && !theme.isEmpty()) {
            code.append("!theme ").append(theme).append("\n");
        }
        
        if (title != null && !title.isEmpty()) {
            code.append("title ").append(title).append("\n");
        }
        
        code.append("\n");
        
        // 添加参与者
        for (Participant participant : participants) {
            if (!participant.alias.equals(participant.name)) {
                code.append(participant.type).append(" \"").append(participant.name)
                    .append("\" as ").append(participant.alias).append("\n");
            } else {
                code.append(participant.type).append(" ").append(participant.name).append("\n");
            }
        }
        
        code.append("\n");
        
        // 添加消息
        for (Message msg : messages) {
            code.append(msg.from).append(" ").append(msg.arrow).append(" ")
                .append(msg.to).append(": ").append(msg.message).append("\n");
        }
        
        code.append("@enduml");
        
        return code.toString();
    }
    
    static class Participant {
        String name;
        String alias;
        String type;
        
        Participant(String name, String alias, String type) {
            this.name = name;
            this.alias = alias;
            this.type = type;
        }
    }
    
    static class Message {
        String from;
        String to;
        String message;
        String arrow;
        
        Message(String from, String to, String message, String arrow) {
            this.from = from;
            this.to = to;
            this.message = message;
            this.arrow = arrow;
        }
    }
}

// 主类和示例用法
public class PlantUMLGeneratorMain {
    
    public static String createBuildingAIWorkflow() {
        ActivityDiagramGenerator generator = new ActivityDiagramGenerator();
        
        generator.setTitle("建筑AI辅助策划与设计系统工作流程");
        
        // 添加分区和活动
        generator.addPartition("数据输入阶段", Arrays.asList(
            "收集既往建筑项目策划书",
            "收集项目任务书",
            "获取国家建设标准",
            "获取地方建设标准"
        ));
        
        generator.addPartition("AI分析处理阶段", Arrays.asList(
            "建筑大语言模型加载",
            "多源数据融合分析",
            "启动对话式交互"
        ));
        
        generator.addPartition("智能生成阶段", Arrays.asList(
            "快速生成策划书草案",
            "生成设计任务书",
            "识别关键性能指标",
            "明确项目目标和需求"
        ));
        
        generator.addPartition("输出优化阶段", Arrays.asList(
            "为设计师提供清晰方向",
            "识别技术挑战点",
            "生成针对性解决方案"
        ));
        
        generator.addPartition("价值实现阶段", Arrays.asList(
            "降低认知负荷",
            "提高工作效率",
            "优化设计质量"
        ));
        
        generator.addNote(
            "系统通过AI技术整合多源建筑信息，实现智能化的项目策划与设计辅助",
            "top"
        );
        
        return generator.generateCode();
    }
    
    public static void saveToFile(String content, String filePath) throws IOException {
        Files.write(Paths.get(filePath), content.getBytes("UTF-8"));
    }
    
    public static void main(String[] args) {
        System.out.println("🚀 PlantUML生成器 - Java版本");
        System.out.println("=".repeat(50));
        
        try {
            // 创建输出目录
            String outputDir = "/workspace/plantuml_generators/java_output";
            Files.createDirectories(Paths.get(outputDir));
            
            // 生成建筑AI工作流程图
            String workflowCode = createBuildingAIWorkflow();
            String workflowFile = outputDir + "/building_ai_workflow.puml";
            saveToFile(workflowCode, workflowFile);
            
            // 生成序列图示例
            SequenceDiagramGenerator seqGen = new SequenceDiagramGenerator();
            seqGen.setTitle("建筑AI系统交互序列图")
                  .addParticipant("用户", "User", "actor")
                  .addParticipant("AI系统", "AI", "participant")
                  .addParticipant("数据库", "DB", "database")
                  .addMessage("User", "AI", "上传项目信息")
                  .addMessage("AI", "DB", "查询历史数据")
                  .addMessage("AI", "User", "生成策划书");
            
            String sequenceCode = seqGen.generateCode();
            String sequenceFile = outputDir + "/sequence_diagram.puml";
            saveToFile(sequenceCode, sequenceFile);
            
            System.out.println("✅ 已生成以下文件：");
            System.out.println("   📄 工作流程图: " + workflowFile);
            System.out.println("   📄 序列图示例: " + sequenceFile);
            System.out.println("\n🎯 所有文件已保存到: " + outputDir);
            
        } catch (IOException e) {
            System.err.println("文件操作错误: " + e.getMessage());
        }
    }
}