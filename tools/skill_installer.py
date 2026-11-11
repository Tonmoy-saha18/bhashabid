# tools/skill_installer.py
# One-Click Skill & Reference Installer for AI IDEs & Agents
import os
import sys
import shutil
import json
from pathlib import Path

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def get_source_skill_dir() -> Path:
    # Check repo root
    p = Path(REPO_ROOT) / "skills" / "bangla-expert"
    if p.exists() and (p / "SKILL.md").exists():
        return p
    # Check installed package location
    import importlib.util
    spec = importlib.util.find_spec("skills")
    if spec and spec.submodule_search_locations:
        p_pkg = Path(spec.submodule_search_locations[0]) / "bangla-expert"
        if p_pkg.exists():
            return p_pkg
    raise FileNotFoundError("Could not locate source 'skills/bangla-expert' directory.")

def uninstall_mcp(target: str = "all", workspace_dir: str = None) -> str:
    """
    Removes Bhashabid Model Context Protocol (MCP) server configuration from Cursor, Claude Desktop, and Antigravity.
    """
    workspace = Path(workspace_dir) if workspace_dir else Path.cwd()
    home = Path.home()
    removed_from = []

    # 1. Cursor MCP config (Global ~/.cursor/mcp.json and Workspace .cursor/mcp.json)
    if target in ["cursor", "all"]:
        targets = [home / ".cursor" / "mcp.json"]
        if workspace != home:
            targets.append(workspace / ".cursor" / "mcp.json")

        for mcp_file in targets:
            if mcp_file.exists():
                try:
                    with open(mcp_file, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    if "mcpServers" in data and "bhashabid" in data["mcpServers"]:
                        del data["mcpServers"]["bhashabid"]
                        with open(mcp_file, "w", encoding="utf-8") as f:
                            json.dump(data, f, indent=2, ensure_ascii=False)
                        removed_from.append(str(mcp_file))
                except Exception:
                    pass

    # 2. Claude Desktop config
    if target in ["claude", "all"]:
        home = Path.home()
        claude_config_path = None
        if sys.platform == "win32":
            appdata = os.environ.get("APPDATA")
            if appdata:
                claude_config_path = Path(appdata) / "Claude" / "claude_desktop_config.json"
        elif sys.platform == "darwin":
            claude_config_path = home / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
        else:
            claude_config_path = home / ".config" / "Claude" / "claude_desktop_config.json"

        if claude_config_path and claude_config_path.exists():
            try:
                with open(claude_config_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if "mcpServers" in data and "bhashabid" in data["mcpServers"]:
                    del data["mcpServers"]["bhashabid"]
                    with open(claude_config_path, "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)
                    removed_from.append(str(claude_config_path))
            except Exception:
                pass

    # 3. Antigravity local workspace MCP (.gemini/mcp_servers.json)
    if target in ["antigravity", "all"]:
        ag_mcp = workspace / ".gemini" / "mcp_servers.json"
        if ag_mcp.exists():
            try:
                with open(ag_mcp, "r", encoding="utf-8") as f:
                    ag_data = json.load(f)
                if "mcpServers" in ag_data and "bhashabid" in ag_data["mcpServers"]:
                    del ag_data["mcpServers"]["bhashabid"]
                    with open(ag_mcp, "w", encoding="utf-8") as f:
                        json.dump(ag_data, f, indent=2, ensure_ascii=False)
                    removed_from.append(str(ag_mcp))
            except Exception:
                pass

    if not removed_from:
        return "Notice: No active Bhashabid MCP server entries found for the specified target."

    msg = "✓ Bhashabid MCP server configuration successfully removed from:\n"
    for rf in removed_from:
        msg += f"  - {rf}\n"
    return msg

def install_mcp(target: str = "all", workspace_dir: str = None) -> str:
    """
    Configures Bhashabid Model Context Protocol (MCP) server across Cursor, Claude Desktop, and Antigravity.
    """
    workspace = Path(workspace_dir) if workspace_dir else Path.cwd()
    repo_path = str(Path(REPO_ROOT).resolve()).replace("\\", "/")
    python_exe = sys.executable.replace("\\", "/")

    mcp_entry = {
        "command": python_exe,
        "args": ["-m", "tools.mcp_server"],
        "cwd": repo_path
    }

    configured_paths = []

    # 1. Cursor MCP config (Global ~/.cursor/mcp.json and Workspace .cursor/mcp.json)
    if target in ["cursor", "all"]:
        home = Path.home()
        cursor_mcp_targets = [home / ".cursor" / "mcp.json"]
        if workspace != home:
            cursor_mcp_targets.append(workspace / ".cursor" / "mcp.json")

        for mcp_file in cursor_mcp_targets:
            os.makedirs(mcp_file.parent, exist_ok=True)
            data = {"mcpServers": {}}
            if mcp_file.exists():
                try:
                    with open(mcp_file, "r", encoding="utf-8") as f:
                        data = json.load(f)
                except Exception:
                    data = {"mcpServers": {}}
            if "mcpServers" not in data:
                data["mcpServers"] = {}
            data["mcpServers"]["bhashabid"] = mcp_entry

            with open(mcp_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            configured_paths.append(str(mcp_file))

    # 2. Claude Desktop config
    if target in ["claude", "all"]:
        home = Path.home()
        claude_config_path = None
        if sys.platform == "win32":
            appdata = os.environ.get("APPDATA")
            if appdata:
                claude_config_path = Path(appdata) / "Claude" / "claude_desktop_config.json"
        elif sys.platform == "darwin":
            claude_config_path = home / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
        else:
            claude_config_path = home / ".config" / "Claude" / "claude_desktop_config.json"

        if claude_config_path and claude_config_path.parent.exists():
            data = {"mcpServers": {}}
            if claude_config_path.exists():
                try:
                    with open(claude_config_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                except Exception:
                    data = {"mcpServers": {}}
            if "mcpServers" not in data:
                data["mcpServers"] = {}
            data["mcpServers"]["bhashabid"] = mcp_entry
            with open(claude_config_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            configured_paths.append(str(claude_config_path))

    # 3. Antigravity local workspace MCP (.gemini/mcp_servers.json)
    if target in ["antigravity", "all"]:
        ag_dir = workspace / ".gemini"
        os.makedirs(ag_dir, exist_ok=True)
        ag_mcp = ag_dir / "mcp_servers.json"
        ag_data = {"mcpServers": {}}
        if ag_mcp.exists():
            try:
                with open(ag_mcp, "r", encoding="utf-8") as f:
                    ag_data = json.load(f)
            except Exception:
                ag_data = {"mcpServers": {}}
        if "mcpServers" not in ag_data:
            ag_data["mcpServers"] = {}
        ag_data["mcpServers"]["bhashabid"] = mcp_entry
        with open(ag_mcp, "w", encoding="utf-8") as f:
            json.dump(ag_data, f, indent=2, ensure_ascii=False)
        configured_paths.append(str(ag_mcp))

    if not configured_paths:
        return "Notice: No MCP configuration files were updated for the specified target."

    msg = f"✓ Bhashabid MCP server configuration successfully installed to:\n"
    for cp in configured_paths:
        msg += f"  - {cp}\n"
    return msg

def install_skill(target: str = "antigravity", workspace_dir: str = None, with_mcp: bool = True) -> str:
    src_dir = get_source_skill_dir()
    home = Path.home()
    workspace = Path(workspace_dir) if workspace_dir else Path.cwd()

    dest_paths = []

    if target in ["antigravity", "all"]:
        # Antigravity global skills directory
        ag_global = home / ".gemini" / "antigravity" / "skills" / "bangla-expert"
        os.makedirs(ag_global, exist_ok=True)
        shutil.copytree(src_dir, ag_global, dirs_exist_ok=True)
        dest_paths.append(str(ag_global))

        # Antigravity local workspace
        ag_local = workspace / ".gemini" / "skills" / "bangla-expert"
        os.makedirs(ag_local, exist_ok=True)
        shutil.copytree(src_dir, ag_local, dirs_exist_ok=True)
        dest_paths.append(str(ag_local))

    if target in ["claude", "all"]:
        # Claude Code global skills directory
        cl_global = home / ".claude" / "skills" / "bangla-expert"
        os.makedirs(cl_global, exist_ok=True)
        shutil.copytree(src_dir, cl_global, dirs_exist_ok=True)
        dest_paths.append(str(cl_global))

    if target in ["cursor", "all"]:
        src_rule = Path(REPO_ROOT) / "adapters" / "cursor" / ".cursorrules"

        # 1. Cursor Global configuration (~/.cursor/rules and ~/.cursor/bangla-references)
        cur_global_rules = home / ".cursor" / "rules"
        os.makedirs(cur_global_rules, exist_ok=True)
        if src_rule.exists():
            shutil.copy(src_rule, cur_global_rules / "bangla-expert.mdc")
            shutil.copy(src_rule, home / ".cursorrules")
        cur_global_refs = home / ".cursor" / "bangla-references"
        os.makedirs(cur_global_refs, exist_ok=True)
        shutil.copytree(src_dir / "references", cur_global_refs, dirs_exist_ok=True)
        dest_paths.append(str(cur_global_rules / "bangla-expert.mdc"))
        dest_paths.append(str(cur_global_refs))

        # 2. Cursor Local Workspace configuration
        if workspace != home:
            cur_rules = workspace / ".cursor" / "rules"
            os.makedirs(cur_rules, exist_ok=True)
            if src_rule.exists():
                shutil.copy(src_rule, workspace / ".cursorrules")
                shutil.copy(src_rule, cur_rules / "bangla-expert.mdc")
            cur_refs = workspace / ".cursor" / "bangla-references"
            os.makedirs(cur_refs, exist_ok=True)
            shutil.copytree(src_dir / "references", cur_refs, dirs_exist_ok=True)
            dest_paths.append(str(workspace / ".cursorrules"))
            dest_paths.append(str(cur_rules / "bangla-expert.mdc"))
            dest_paths.append(str(cur_refs))

    msg = f"✓ Bhashabid skill and all {len(list((src_dir / 'references').glob('*.md')))} reference guides successfully installed to:\n"
    for dp in dest_paths:
        msg += f"  - {dp}\n"

    if with_mcp:
        mcp_msg = install_mcp(target=target, workspace_dir=str(workspace))
        msg += f"\n{mcp_msg}"

    return msg

def uninstall_skill(target: str = "all", workspace_dir: str = None, with_mcp: bool = True) -> str:
    """
    Uninstalls Bhashabid skill files, adapters, and reference guides from Antigravity, Claude, or Cursor.
    """
    home = Path.home()
    workspace = Path(workspace_dir) if workspace_dir else Path.cwd()
    removed_paths = []

    if target in ["antigravity", "all"]:
        ag_global = home / ".gemini" / "antigravity" / "skills" / "bangla-expert"
        if ag_global.exists():
            shutil.rmtree(ag_global, ignore_errors=True)
            removed_paths.append(str(ag_global))

        ag_local = workspace / ".gemini" / "skills" / "bangla-expert"
        if ag_local.exists():
            shutil.rmtree(ag_local, ignore_errors=True)
            removed_paths.append(str(ag_local))

    if target in ["claude", "all"]:
        cl_global = home / ".claude" / "skills" / "bangla-expert"
        if cl_global.exists():
            shutil.rmtree(cl_global, ignore_errors=True)
            removed_paths.append(str(cl_global))

    if target in ["cursor", "all"]:
        # 1. Cursor Global rules & references
        cur_global_mdc = home / ".cursor" / "rules" / "bangla-expert.mdc"
        if cur_global_mdc.exists():
            cur_global_mdc.unlink(missing_ok=True)
            removed_paths.append(str(cur_global_mdc))

        cur_global_refs = home / ".cursor" / "bangla-references"
        if cur_global_refs.exists():
            shutil.rmtree(cur_global_refs, ignore_errors=True)
            removed_paths.append(str(cur_global_refs))

        # Check home and workspace .cursorrules
        rule_files = [home / ".cursorrules"]
        if workspace != home:
            rule_files.append(workspace / ".cursorrules")

        for cur_rule in rule_files:
            if cur_rule.exists():
                try:
                    content = cur_rule.read_text(encoding="utf-8")
                    if "Bangla Academy" in content or "Bhashabid" in content or "bhashabid" in content:
                        cur_rule.unlink(missing_ok=True)
                        removed_paths.append(str(cur_rule))
                except Exception:
                    pass

        # 2. Workspace rules & references
        if workspace != home:
            cur_mdc = workspace / ".cursor" / "rules" / "bangla-expert.mdc"
            if cur_mdc.exists():
                cur_mdc.unlink(missing_ok=True)
                removed_paths.append(str(cur_mdc))

            cur_refs = workspace / ".cursor" / "bangla-references"
            if cur_refs.exists():
                shutil.rmtree(cur_refs, ignore_errors=True)
                removed_paths.append(str(cur_refs))

    msg = ""
    if removed_paths:
        msg = f"✓ Bhashabid skill and references successfully removed from:\n"
        for rp in removed_paths:
            msg += f"  - {rp}\n"
    else:
        msg = "Notice: No installed Bhashabid skill files were found for the specified target.\n"

    if with_mcp:
        mcp_msg = uninstall_mcp(target=target, workspace_dir=str(workspace))
        msg += f"\n{mcp_msg}"

    return msg

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Install or Uninstall Bhashabid Skill and MCP Configuration")
    parser.add_argument("--action", choices=["install", "uninstall"], default="install", help="Action to perform")
    parser.add_argument("--target", choices=["antigravity", "claude", "cursor", "all"], default="all")
    parser.add_argument("--workspace", default=None, help="Target workspace path (defaults to current dir)")
    parser.add_argument("--no-mcp", action="store_true", help="Skip MCP server configuration")
    args = parser.parse_args()
    if args.action == "uninstall":
        print(uninstall_skill(args.target, args.workspace, with_mcp=not args.no_mcp))
    else:
        print(install_skill(args.target, args.workspace, with_mcp=not args.no_mcp))
