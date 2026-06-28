using System.Text.Json.Serialization;

namespace FlowPilot.Web.Models
{

    public class WorkflowExecutionResult
    {
        [JsonPropertyName("final_result")]
        public string FinalResult { get; set; } = "";

        [JsonPropertyName("steps")]
        public List<WorkflowStepResult> Steps { get; set; } = [];
    }
}
