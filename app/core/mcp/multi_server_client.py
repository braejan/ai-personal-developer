from langchain_mcp_adapters.client import MultiServerMCPClient


def get_mcp_client():
    return MultiServerMCPClient({
        "time": {
            "command": "python",
            "args": ["app/core/mcp/time/server.py"],
            "transport": "stdio",
        }
    })
