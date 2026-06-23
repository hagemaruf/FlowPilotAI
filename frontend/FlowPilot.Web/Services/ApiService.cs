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

    public async Task CreateWorkflow(
    string name,
    string description,
    string prompt)
    {
        await _http.PostAsJsonAsync(
            "api/workflows",
            new
            {
                name,
                description,
                prompt
            });
    }

    public async Task DeleteWorkflow(
        string workflowId)
    {
        await _http.DeleteAsync(
            $"api/workflows/{workflowId}");
    }

    public async Task<string> RunWorkflow(
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

        var result =
            await response.Content
                .ReadFromJsonAsync<RunResponse>();

        return result?.Result ?? "";
    }
}