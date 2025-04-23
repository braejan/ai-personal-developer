from mcp.server.fastmcp import FastMCP
from datetime import datetime, timezone
import logging


logger = logging.getLogger()

mcp = FastMCP(
    name="DateTime",
    description="Allow to give the current time and formatted dates",
    host="0.0.0.0",
    port=8050,
)


@mcp.tool()
async def get_current_date_iso():
    """Returns the current date in ISO format (YYYY-MM-DD)"""
    return datetime.now().strftime("%Y-%m-%d")


@mcp.tool()
async def get_current_date_time_with_tz():
    """Returns the current date and time with timezone in ISO format (YYYY-MM-DDTHH:MM:SS+HH:MM)"""
    return datetime.now(timezone.utc).isoformat()


# Run the server

if __name__ == "__main__":
    logger.info(f"Running server {mcp.name} at stdio transport")
    mcp.run("stdio")
