namespace FlowPilot.Web.Models
{
    public class WorkflowStep
    {
        public int Order { get; set; }

        public string Name { get; set; } = "";

        public string Prompt { get; set; } = "";
    }
}
