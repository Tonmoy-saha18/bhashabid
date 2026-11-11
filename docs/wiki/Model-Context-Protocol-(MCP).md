# Model Context Protocol (MCP) Integration

Bhashabid includes a fully compliant **Model Context Protocol (MCP)** server, allowing AI coding assistants like **Cursor, Claude Desktop, Windsurf, and Zed** to call deterministic Bengali tools directly.

---

## 🛠️ Exposed MCP Tools

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| `convert_number` | `number` (int), `format` (words/grouped) | Converts digits to standard Bengali cardinal words and South Asian grouped formatting (`১২,৩৪,৫৬৭`). |
| `normalize_text` | `text` (str), `profile` (bd_standard/wb_standard) | Canonicalizes Unicode NFC, Dari (`।`) punctuation, and Bangla Academy orthography. |
| `lint_text` | `text` (str) | Detects Guru-chandali, honorific mismatches, and English calques, returning line/column diagnostics and suggestions. |
| `prosody_scan` | `text` (str), `metre`, `verify_payar` (bool) | Scans verse lines for Dalabritta, Matrabritta, or Aksharbritta; verifies 14-akshar Payar couplets. |
| `generate_writ_prayer` | `remedy`, `subject`, `authority` | Formulates Article 102 High Court constitutional writ prayers in statutory judicial Bengali. |

---

## ⚙️ Configuration Setup

### Claude Desktop (`claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "bhashabid": {
      "command": "python",
      "args": ["-m", "tools.mcp_server"],
      "cwd": "C:/path/to/bhashabid"
    }
  }
}
```

### Cursor MCP Settings
1. Open Cursor Settings -> Features -> MCP.
2. Click **+ Add New MCP Server**.
3. Name: `bhashabid`
4. Type: `command`
5. Command: `python -m tools.mcp_server`
6. Working Directory: `/path/to/bhashabid`
