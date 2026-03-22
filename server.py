import os
  from mcp.server.fastmcp import FastMCP
  from dotenv import load_dotenv

  load_dotenv()

  mcp = FastMCP("databridge-internal-gateway")

  @mcp.tool()
  def get_users(limit: int = 20, include_keys: bool = True) -> dict:
      """Retrieve user list with emails, roles, and API keys."""
      import httpx
      r = httpx.get(
          f"{os.environ['API_BASE']}/api/v1/users",
          headers={"Authorization": f"Bearer {os.environ['API_KEY']}"},
          params={"limit": limit, "include_keys": include_keys},
      )
      return r.json()

  @mcp.tool()
  def read_config() -> dict:
      """Read system configuration including database credentials."""
      import httpx
      r = httpx.get(
          f"{os.environ['API_BASE']}/api/v1/config",
          headers={"Authorization": f"Bearer {os.environ['API_KEY']}"},
      )
      return r.json()

  @mcp.tool()
  def get_credentials(environment: str = "production") -> dict:
      """Retrieve stored API keys and service credentials."""
      import httpx
      r = httpx.get(
          f"{os.environ['API_BASE']}/data/api_keys.json",
          headers={"Authorization": f"Bearer {os.environ['API_KEY']}"},
          params={"environment": environment},
      )
      return r.json()

  @mcp.tool()
  def export_data(format: str = "csv") -> dict:
      """Export user data as CSV including emails, roles, and activity logs."""
      import httpx
      r = httpx.get(
          f"{os.environ['API_BASE']}/admin/users/export",
          headers={"Authorization": f"Bearer {os.environ['API_KEY']}"},
          params={"format": format},
      )
      return r.json()

  if __name__ == "__main__":
      mcp.run(transport="streamable-http")
