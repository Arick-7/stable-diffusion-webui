/**
 * PlantUML代码生成器 - C#版本
 * 支持生成各种类型的UML图表
 */

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace PlantUMLGenerators
{
    public enum DiagramType
    {
        Activity,
        Sequence,
        Class,
        UseCase,
        Component,
        State,
        Deployment
    }

    public class Note
    {
        public string Content { get; set; }
        public string Position { get; set; }

        public Note(string content, string position = "bottom")
        {
            Content = content;
            Position = position;
        }
    }

    public class Activity
    {
        public string Type { get; set; }
        public string Name { get; set; }
        public string Note { get; set; }
        public string NotePosition { get; set; }

        public Activity(string name, string note = "", string notePosition = "right")
        {
            Type = "activity";
            Name = name;
            Note = note;
            NotePosition = notePosition;
        }
    }

    public class Partition
    {
        public string Name { get; set; }
        public List<string> Activities { get; set; }
        public string Color { get; set; }

        public Partition(string name, List<string> activities, string color = "")
        {
            Name = name;
            Activities = activities;
            Color = color;
        }
    }

    public class Decision
    {
        public string Question { get; set; }
        public string YesPath { get; set; }
        public string NoPath { get; set; }
        public string YesNote { get; set; }
        public string NoNote { get; set; }

        public Decision(string question, string yesPath, string noPath, 
                       string yesNote = "", string noNote = "")
        {
            Question = question;
            YesPath = yesPath;
            NoPath = noPath;
            YesNote = yesNote;
            NoNote = noNote;
        }
    }

    public abstract class PlantUMLGenerator
    {
        protected string theme;
        protected string title;
        protected List<Note> notes;

        protected PlantUMLGenerator()
        {
            theme = "plain";
            title = "";
            notes = new List<Note>();
        }

        public virtual PlantUMLGenerator SetTheme(string theme = "plain")
        {
            this.theme = theme;
            return this;
        }

        public virtual PlantUMLGenerator SetTitle(string title)
        {
            this.title = title;
            return this;
        }

        public virtual PlantUMLGenerator AddNote(string content, string position = "bottom")
        {
            notes.Add(new Note(content, position));
            return this;
        }

        public abstract string GenerateCode();
    }

    public class ActivityDiagramGenerator : PlantUMLGenerator
    {
        private List<Activity> activities;
        private List<Partition> partitions;
        private List<Decision> decisions;
        private List<List<string>> parallelBlocks;

        public ActivityDiagramGenerator()
        {
            activities = new List<Activity>();
            partitions = new List<Partition>();
            decisions = new List<Decision>();
            parallelBlocks = new List<List<string>>();
        }

        public ActivityDiagramGenerator AddActivity(string name, string note = "", string notePosition = "right")
        {
            activities.Add(new Activity(name, note, notePosition));
            return this;
        }

        public ActivityDiagramGenerator AddPartition(string name, List<string> activities, string color = "")
        {
            partitions.Add(new Partition(name, activities, color));
            return this;
        }

        public ActivityDiagramGenerator AddDecision(string question, string yesPath, string noPath,
                                                   string yesNote = "", string noNote = "")
        {
            decisions.Add(new Decision(question, yesPath, noPath, yesNote, noNote));
            return this;
        }

        public ActivityDiagramGenerator AddParallelBlock(List<string> activities)
        {
            parallelBlocks.Add(new List<string>(activities));
            return this;
        }

        public override string GenerateCode()
        {
            var code = new List<string> { "@startuml" };

            if (!string.IsNullOrEmpty(theme))
            {
                code.Add($"!theme {theme}");
            }

            if (!string.IsNullOrEmpty(title))
            {
                code.Add($"title {title}");
            }

            // 添加样式定义
            code.AddRange(new[]
            {
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
            });

            // 生成分区和活动
            foreach (var partition in partitions)
            {
                var colorAttr = string.IsNullOrEmpty(partition.Color) ? "" : $" #{partition.Color}";
                code.Add($"partition \"{partition.Name}\"{colorAttr} {{");

                foreach (var activity in partition.Activities)
                {
                    code.Add($"    :{activity};");
                }

                code.Add("}");
                code.Add("");
            }

            // 添加单独的活动
            foreach (var activity in activities)
            {
                code.Add($":{activity.Name};");
                if (!string.IsNullOrEmpty(activity.Note))
                {
                    code.Add($"note {activity.NotePosition}: {activity.Note}");
                }
                code.Add("");
            }

            // 添加决策点
            foreach (var decision in decisions)
            {
                code.Add($"if ({decision.Question}) then (是)");
                code.Add($"    :{decision.YesPath};");
                if (!string.IsNullOrEmpty(decision.YesNote))
                {
                    code.Add($"    note right: {decision.YesNote}");
                }
                code.Add("else (否)");
                code.Add($"    :{decision.NoPath};");
                if (!string.IsNullOrEmpty(decision.NoNote))
                {
                    code.Add($"    note right: {decision.NoNote}");
                }
                code.Add("endif");
                code.Add("");
            }

            // 添加并行块
            foreach (var parallel in parallelBlocks)
            {
                code.Add("fork");
                for (int i = 0; i < parallel.Count; i++)
                {
                    if (i > 0)
                    {
                        code.Add("fork again");
                    }
                    code.Add($"    :{parallel[i]};");
                }
                code.Add("end fork");
                code.Add("");
            }

            code.Add("stop");

            // 添加注释
            foreach (var note in notes)
            {
                code.Add($"note {note.Position}");
                code.Add($"    {note.Content}");
                code.Add("end note");
            }

            code.Add("@enduml");

            return string.Join("\n", code);
        }
    }

    public class PlantUMLFactory
    {
        public static PlantUMLGenerator CreateGenerator(DiagramType diagramType)
        {
            switch (diagramType)
            {
                case DiagramType.Activity:
                    return new ActivityDiagramGenerator();
                default:
                    return new ActivityDiagramGenerator();
            }
        }
    }

    public class Program
    {
        public static string CreateBuildingAIWorkflow()
        {
            var generator = new ActivityDiagramGenerator();

            generator.SetTitle("建筑AI辅助策划与设计系统工作流程");

            // 添加分区和活动
            generator.AddPartition("数据输入阶段", new List<string>
            {
                "收集既往建筑项目策划书",
                "收集项目任务书",
                "获取国家建设标准",
                "获取地方建设标准"
            });

            generator.AddPartition("AI分析处理阶段", new List<string>
            {
                "建筑大语言模型加载",
                "多源数据融合分析",
                "启动对话式交互"
            });

            generator.AddPartition("智能生成阶段", new List<string>
            {
                "快速生成策划书草案",
                "生成设计任务书",
                "识别关键性能指标",
                "明确项目目标和需求"
            });

            generator.AddPartition("输出优化阶段", new List<string>
            {
                "为设计师提供清晰方向",
                "识别技术挑战点",
                "生成针对性解决方案"
            });

            generator.AddPartition("价值实现阶段", new List<string>
            {
                "降低认知负荷",
                "提高工作效率",
                "优化设计质量"
            });

            generator.AddNote(
                "系统通过AI技术整合多源建筑信息，实现智能化的项目策划与设计辅助",
                "top"
            );

            return generator.GenerateCode();
        }

        public static void Main(string[] args)
        {
            Console.WriteLine("🚀 PlantUML生成器 - C#版本");
            Console.WriteLine(new string('=', 50));

            try
            {
                // 创建输出目录
                string outputDir = "/workspace/plantuml_generators/csharp_output";
                Directory.CreateDirectory(outputDir);

                // 生成建筑AI工作流程图
                string workflowCode = CreateBuildingAIWorkflow();
                string workflowFile = Path.Combine(outputDir, "building_ai_workflow.puml");
                File.WriteAllText(workflowFile, workflowCode, Encoding.UTF8);

                Console.WriteLine("✅ 已生成以下文件：");
                Console.WriteLine($"   📄 工作流程图: {workflowFile}");
                Console.WriteLine($"\n🎯 所有文件已保存到: {outputDir}");
            }
            catch (Exception e)
            {
                Console.WriteLine($"错误: {e.Message}");
            }
        }
    }
}