namespace FlowPilot.Web.Models;

public class CreateWorkflowRequest
{
    public string Name { get; set; } = "";

    public string Description { get; set; } = "";

    public List<WorkflowStep> Steps { get; set; } = [];
}