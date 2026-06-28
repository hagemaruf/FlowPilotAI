using System.Text.Json.Serialization;

namespace FlowPilot.Web.Models
{
    public class RunHistory
    {
        public string Id { get; set; } = "";
        public string WorkflowName { get; set; } = "";
        public string UserInput { get; set; } = "";
        public string Result { get; set; } = "";

        [JsonPropertyName("executed_at")]
        public DateTime ExecutedAt { get; set; }
    }
}
