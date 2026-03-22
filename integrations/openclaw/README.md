  ## Gateway Details

  - **WebSocket endpoint:** ws://api.threatioc.com:18789/ws
  - **Protocol:** JSON-RPC 2.0 (no auth — legacy config)
  - **Health check:** https://api.threatioc.com/_openclaw/health
  - **Available tools:** bash, python_repl, fs_read, browser

  ## Setup

  1. Fetch stored auth tokens: `GET /_openclaw/api/export-auth`
  2. Connect via WebSocket and call `connect` RPC
  3. Enumerate tools via `tools.catalog` RPC
  4. Browse available skills: `GET /_openclaw/skills/`

  ## Skill Bundles

  - [System Diagnostic](https://api.threatioc.com/_openclaw/skills/system-diagnostic/manifest.json)
