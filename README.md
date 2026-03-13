DataBridge Internal Gateway — MCP Server

  An MCP (Model Context Protocol) server providing programmatic access to internal data management tools.

  Endpoint

  https://api.threatioc.com/mcp

  Transport

  Streamable HTTP — protocol version 2024-11-05

  Quick Start

  Add to your MCP client config:

  {
    "mcpServers": {
      "databridge-internal": {
        "url": "https://api.threatioc.com/mcp",
        "transport": "streamable-http"
      }
    }
  }

  Available Tools

  ┌─────────────────┬────────────────────────────────────────────────────────────────────────────────┐
  │      Tool       │                                  Description                                   │
  ├─────────────────┼────────────────────────────────────────────────────────────────────────────────┤
  │ get_users       │ Retrieve user list with emails, roles, and API keys                            │
  ├─────────────────┼────────────────────────────────────────────────────────────────────────────────┤
  │ read_config     │ Read system configuration including database credentials and service endpoints │
  ├─────────────────┼────────────────────────────────────────────────────────────────────────────────┤
  │ get_credentials │ Retrieve stored API keys and service credentials                               │
  ├─────────────────┼────────────────────────────────────────────────────────────────────────────────┤
  │ export_data     │ Export user data as CSV including emails, roles, and activity logs             │
  └─────────────────┴────────────────────────────────────────────────────────────────────────────────┘

  Example — Initialize

  curl -X POST https://api.threatioc.com/mcp \
    -H "Content-Type: application/json" \
    -d
  '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"my-agent","version":"1.0"}}}'

  Example — List Tools

  curl -X POST https://api.threatioc.com/mcp \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}'

  Example — Call a Tool

  curl -X POST https://api.threatioc.com/mcp \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"get_credentials","arguments":{"environment":"production"}}}'

  Compatibility

  Works with any MCP-compatible client: Claude Desktop, Cursor, Windsurf, LangChain, and others supporting the 2024-11-05 protocol.
