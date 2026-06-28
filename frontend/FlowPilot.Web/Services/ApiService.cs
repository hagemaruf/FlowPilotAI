using System.Net.Http.Json;
using FlowPilot.Web.Models;

namespace FlowPilot.Web.Services;

public class ApiService
{
    private readonly HttpClient _http;

    public ApiService(HttpClient http)
    {
        _http = http;
    }

    public async Task<List<Workflow>> GetWorkflows()
    {
        return await _http.GetFromJsonAsync<List<Workflow>>(
            "api/workflows"
        ) ?? new List<Workflow>();
    }

    public async Task CreateWorkflow(CreateWorkflowRequest request)
    {
        await _http.PostAsJsonAsync(
            "api/workflows",
            request);
    }

    public async Task DeleteWorkflow(
        string workflowId)
    {
        await _http.DeleteAsync(
            $"api/workflows/{workflowId}");
    }

    public async Task<WorkflowExecutionResult?> RunWorkflow(
    string workflowId,
    string userInput)
    {
        var response =
            await _http.PostAsJsonAsync(
                "api/runs",
                new
                {
                    workflow_id = workflowId,
                    user_input = userInput
                });

        response.EnsureSuccessStatusCode();

        return await response.Content
            .ReadFromJsonAsync<WorkflowExecutionResult>();
    }

    public async Task<List<RunHistory>> GetHistory()
    {
        return await _http.GetFromJsonAsync<List<RunHistory>>(
            "api/history")
            ?? new();
    }

    public async Task<List<WorkflowTemplate>> GetTemplates()
    {
        return await _http.GetFromJsonAsync<List<WorkflowTemplate>>(
            "api/templates")
            ?? new();
    }
}