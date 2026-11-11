# tools/skill_installer.py
# One-Click Global Skill & Reference Installer for AI IDEs & Agents
import os
import sys
import shutil
import json
from pathlib import Path
from typing import Dict, Any, List

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def get_source_skill_dir() -> Path:
    p = Path(REPO_ROOT) / "skills" / "bangla-expert"
    if p.exists() and (p / "SKILL.md").exists():
        return p
    import importlib.util
    spec = importlib.util.find_spec("skills")
    if spec and spec.submodule_search_locations:
        p_pkg = Path(spec.submodule_search_locations[0]) / "bangla-expert"
        if p_pkg.exists():
            return p_pkg
    raise FileNotFoundError("Could not locate source 'skills/bangla-expert' directory.")

def detect_environments() -> Dict[str, Dict[str, Any]]:
    """
    Auto-detects which AI IDEs / Agent environments exist on this machine.
    """
    home = Path.home()
    appdata = Path(os.environ.get("APPDATA", "")) if os.environ.get("APPDATA") else None

    # 1. Cursor
    cursor_found = False
    cursor_hint = ""
    if (home / ".cursor").exists():
        cursor_found = True
        cursor_hint = str(home / ".cursor")
    elif appdata and (appdata / "Cursor").exists():
        cursor_found = True
        cursor_hint = str(appdata / "Cursor")
    elif shutil.which("cursor") is not None:
        cursor_found = True
        cursor_hint = "cursor on PATH"

    # 2. Antigravity
    ag_found = False
    ag_hint = ""
    if (home / ".gemini").exists():
        ag_found = True
        ag_hint = str(home / ".gemini")
    elif shutil.which("agy") is not None or shutil.which("antigravity") is not None:
        ag_found = True
        ag_hint = "agy CLI on PATH"

    # 3. Claude (Desktop / Code)
    claude_found = False
    claude_hint = ""
    claude_cfg = None
    if sys.platform == "win32" and appdata:
        claude_cfg = appdata / "Claude" / "claude_desktop_config.json"
    elif sys.platform == "darwin":
        claude_cfg = home / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    else:
        claude_cfg = home / ".config" / "Claude" / "claude_desktop_config.json"

    if (home / ".claude").exists():
        claude_found = True
        claude_hint = str(home / ".claude")
    elif claude_cfg and claude_cfg.parent.exists():
        claude_found = True
        claude_hint = str(claude_cfg.parent)
    elif shutil.which("claude") is not None:
        claude_found = True
        claude_hint = "claude CLI on PATH"

    return {
        "cursor": {"detected": cursor_found, "hint": cursor_hint},
        "antigravity": {"detected": ag_found, "hint": ag_hint},
        "claude": {"detected": claude_found, "hint": claude_hint, "config": claude_cfg}
    }

def get_claude_desktop_config_path() -> Path:
    home = Path.home()
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA")
        return Path(appdata) / "Claude" / "claude_desktop_config.json" if appdata else home / ".config" / "Claude" / "claude_desktop_config.json"
    elif sys.platform == "darwin":
        return home / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    return home / ".config" / "Claude" / "claude_desktop_config.json"

def install_mcp(target: str = "all", workspace_dir: str = None) -> str:
    """
    Installs Bhashabid MCP server configuration globally for detected environments.
    """
    home = Path.home()
    repo_path = str(Path(REPO_ROOT).resolve()).replace("\\", "/")
    python_exe = sys.executable.replace("\\", "/")
    env_info = detect_environments()

    mcp_entry = {
        "command": python_exe,
        "args": ["-m", "tools.mcp_server"],
        "cwd": repo_path
    }

    configured = []
    skipped = []

    # 1. Cursor Global MCP (~/.cursor/mcp.json)
    if target in ["cursor", "all"]:
        if target == "cursor" or env_info["cursor"]["detected"]:
            mcp_file = home / ".cursor" / "mcp.json"
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
            configured.append(f"Cursor: {mcp_file}")
        else:
            skipped.append("Cursor (Not detected)")

    # 2. Antigravity Global MCP (~/.gemini/antigravity/mcp_servers.json)
    if target in ["antigravity", "all"]:
        if target == "antigravity" or env_info["antigravity"]["detected"]:
            ag_mcp = home / ".gemini" / "antigravity" / "mcp_servers.json"
            os.makedirs(ag_mcp.parent, exist_ok=True)
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
            configured.append(f"Antigravity: {ag_mcp}")
        else:
            skipped.append("Antigravity (Not detected)")

    # 3. Claude Desktop MCP
    if target in ["claude", "all"]:
        claude_cfg = get_claude_desktop_config_path()
        if target == "claude" or (claude_cfg and claude_cfg.parent.exists()) or env_info["claude"]["detected"]:
            os.makedirs(claude_cfg.parent, exist_ok=True)
            data = {"mcpServers": {}}
            if claude_cfg.exists():
                try:
                    with open(claude_cfg, "r", encoding="utf-8") as f:
                        data = json.load(f)
                except Exception:
                    data = {"mcpServers": {}}
            if "mcpServers" not in data:
                data["mcpServers"] = {}
            data["mcpServers"]["bhashabid"] = mcp_entry
            with open(claude_cfg, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            configured.append(f"Claude Desktop: {claude_cfg}")
        else:
            skipped.append("Claude Desktop (Not detected)")

    # Workspace MCP (only if explicitly requested)
    if workspace_dir:
        ws_path = Path(workspace_dir)
        ws_mcp = ws_path / ".cursor" / "mcp.json"
        os.makedirs(ws_mcp.parent, exist_ok=True)
        data = {"mcpServers": {}}
        if ws_mcp.exists():
            try:
                with open(ws_mcp, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                data = {"mcpServers": {}}
        if "mcpServers" not in data:
            data["mcpServers"] = {}
        data["mcpServers"]["bhashabid"] = mcp_entry
        with open(ws_mcp, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        configured.append(f"Workspace: {ws_mcp}")

    msg = "✓ Bhashabid MCP server configuration successfully installed to:\n"
    for c in configured:
        msg += f"  - {c}\n"
    if skipped:
        msg += "Notice: Skipped environments not installed on this machine:\n"
        for s in skipped:
            msg += f"  - {s}\n"
    return msg

def install_skill(target: str = "all", workspace_dir: str = None, with_mcp: bool = True) -> str:
    """
    Installs Bhashabid skill files and reference guides globally for detected environments.
    """
    src_dir = get_source_skill_dir()
    home = Path.home()
    env_info = detect_environments()
    dest_paths = []
    skipped = []

    # 1. Cursor Global Rules (~/.cursor/rules/bangla-expert.mdc and ~/.cursor/bangla-references)
    if target in ["cursor", "all"]:
        if target == "cursor" or env_info["cursor"]["detected"]:
            cur_global_rules = home / ".cursor" / "rules"
            os.makedirs(cur_global_rules, exist_ok=True)
            src_rule = Path(REPO_ROOT) / "adapters" / "cursor" / ".cursorrules"
            if src_rule.exists():
                shutil.copy(src_rule, cur_global_rules / "bangla-expert.mdc")

            cur_global_refs = home / ".cursor" / "bangla-references"
            os.makedirs(cur_global_refs, exist_ok=True)
            shutil.copytree(src_dir / "references", cur_global_refs, dirs_exist_ok=True)

            dest_paths.append(f"Cursor (Global Rule): {cur_global_rules / 'bangla-expert.mdc'}")
            dest_paths.append(f"Cursor (References):  {cur_global_refs}")
        else:
            skipped.append("Cursor (Not detected)")

    # 2. Antigravity Global Skills (~/.gemini/antigravity/skills/bangla-expert)
    if target in ["antigravity", "all"]:
        if target == "antigravity" or env_info["antigravity"]["detected"]:
            ag_global = home / ".gemini" / "antigravity" / "skills" / "bangla-expert"
            os.makedirs(ag_global, exist_ok=True)
            shutil.copytree(src_dir, ag_global, dirs_exist_ok=True)
            dest_paths.append(f"Antigravity (Global Skill): {ag_global}")
        else:
            skipped.append("Antigravity (Not detected)")

    # 3. Claude Global Skills (~/.claude/skills/bangla-expert)
    if target in ["claude", "all"]:
        if target == "claude" or env_info["claude"]["detected"]:
            cl_global = home / ".claude" / "skills" / "bangla-expert"
            os.makedirs(cl_global, exist_ok=True)
            shutil.copytree(src_dir, cl_global, dirs_exist_ok=True)
            dest_paths.append(f"Claude (Global Skill): {cl_global}")
        else:
            skipped.append("Claude (Not detected)")

    # 4. Optional Workspace Directory (Only if explicitly passed via --workspace)
    if workspace_dir:
        ws = Path(workspace_dir)
        cur_rules = ws / ".cursor" / "rules"
        os.makedirs(cur_rules, exist_ok=True)
        src_rule = Path(REPO_ROOT) / "adapters" / "cursor" / ".cursorrules"
        if src_rule.exists():
            shutil.copy(src_rule, ws / ".cursorrules")
            shutil.copy(src_rule, cur_rules / "bangla-expert.mdc")
        shutil.copytree(src_dir / "references", ws / ".cursor" / "bangla-references", dirs_exist_ok=True)
        dest_paths.append(f"Workspace ({ws.name}): {cur_rules / 'bangla-expert.mdc'}")
        dest_paths.append(f"Workspace ({ws.name}): {ws / '.cursorrules'}")

    msg = f"✓ Bhashabid skill and all {len(list((src_dir / 'references').glob('*.md')))} reference guides successfully installed to:\n"
    for dp in dest_paths:
        msg += f"  - {dp}\n"

    if skipped:
        msg += "Notice: Skipped environments not installed on this machine:\n"
        for s in skipped:
            msg += f"  - {s}\n"

    if with_mcp:
        mcp_msg = install_mcp(target=target, workspace_dir=workspace_dir)
        msg += f"\n{mcp_msg}"

    return msg

def uninstall_mcp(target: str = "all", workspace_dir: str = None) -> str:
    """
    Removes Bhashabid MCP server configuration after scanning detected environments.
    """
    home = Path.home()
    env_info = detect_environments()
    removed_from = []
    skipped = []

    # 1. Cursor Global MCP (~/.cursor/mcp.json)
    if target in ["cursor", "all"]:
        if target == "cursor" or env_info["cursor"]["detected"]:
            targets = [home / ".cursor" / "mcp.json"]
            if workspace_dir:
                targets.append(Path(workspace_dir) / ".cursor" / "mcp.json")
            else:
                targets.append(Path.cwd() / ".cursor" / "mcp.json")

            for mcp_file in targets:
                if mcp_file.exists():
                    try:
                        with open(mcp_file, "r", encoding="utf-8") as f:
                            data = json.load(f)
                        if "mcpServers" in data and "bhashabid" in data["mcpServers"]:
                            del data["mcpServers"]["bhashabid"]
                            with open(mcp_file, "w", encoding="utf-8") as f:
                                json.dump(data, f, indent=2, ensure_ascii=False)
                            removed_from.append(f"Cursor MCP: {mcp_file}")
                    except Exception:
                        pass
        else:
            skipped.append("Cursor (Not detected)")

    # 2. Claude Desktop config
    if target in ["claude", "all"]:
        claude_cfg = get_claude_desktop_config_path()
        if target == "claude" or (claude_cfg and claude_cfg.exists()) or env_info["claude"]["detected"]:
            if claude_cfg and claude_cfg.exists():
                try:
                    with open(claude_cfg, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    if "mcpServers" in data and "bhashabid" in data["mcpServers"]:
                        del data["mcpServers"]["bhashabid"]
                        with open(claude_cfg, "w", encoding="utf-8") as f:
                            json.dump(data, f, indent=2, ensure_ascii=False)
                        removed_from.append(f"Claude Desktop MCP: {claude_cfg}")
                except Exception:
                    pass
        else:
            skipped.append("Claude Desktop (Not detected)")

    # 3. Antigravity MCP (~/.gemini/antigravity/mcp_servers.json)
    if target in ["antigravity", "all"]:
        if target == "antigravity" or env_info["antigravity"]["detected"]:
            ag_mcp = home / ".gemini" / "antigravity" / "mcp_servers.json"
            if ag_mcp.exists():
                try:
                    with open(ag_mcp, "r", encoding="utf-8") as f:
                        ag_data = json.load(f)
                    if "mcpServers" in ag_data and "bhashabid" in ag_data["mcpServers"]:
                        del ag_data["mcpServers"]["bhashabid"]
                        with open(ag_mcp, "w", encoding="utf-8") as f:
                            json.dump(ag_data, f, indent=2, ensure_ascii=False)
                        removed_from.append(f"Antigravity MCP: {ag_mcp}")
                except Exception:
                    pass
        else:
            skipped.append("Antigravity (Not detected)")

    msg = ""
    if removed_from:
        msg += "✓ Bhashabid MCP server configuration successfully removed from:\n"
        for rf in removed_from:
            msg += f"  - {rf}\n"
    else:
        msg += "Notice: No active Bhashabid MCP server entries found for the specified target.\n"

    if skipped:
        msg += "Notice: Skipped environments not installed on this machine:\n"
        for s in skipped:
            msg += f"  - {s}\n"

    return msg

def uninstall_skill(target: str = "all", workspace_dir: str = None, with_mcp: bool = True) -> str:
    """
    Uninstalls Bhashabid skill files and reference guides after scanning detected environments.
    """
    home = Path.home()
    workspace = Path(workspace_dir) if workspace_dir else Path.cwd()
    env_info = detect_environments()
    removed_paths = []
    skipped = []

    # 1. Cursor
    if target in ["cursor", "all"]:
        if target == "cursor" or env_info["cursor"]["detected"]:
            cur_global_mdc = home / ".cursor" / "rules" / "bangla-expert.mdc"
            if cur_global_mdc.exists():
                cur_global_mdc.unlink(missing_ok=True)
                removed_paths.append(f"Cursor (Global Rule): {cur_global_mdc}")

            cur_global_refs = home / ".cursor" / "bangla-references"
            if cur_global_refs.exists():
                shutil.rmtree(cur_global_refs, ignore_errors=True)
                removed_paths.append(f"Cursor (References):  {cur_global_refs}")

            # Check home ~/.cursorrules
            if (home / ".cursorrules").exists():
                try:
                    c = (home / ".cursorrules").read_text(encoding="utf-8")
                    if "Bangla Academy" in c or "bhashabid" in c:
                        (home / ".cursorrules").unlink(missing_ok=True)
                        removed_paths.append(f"Cursor (~/.cursorrules): {home / '.cursorrules'}")
                except Exception:
                    pass
        else:
            skipped.append("Cursor (Not detected)")

    # 2. Antigravity
    if target in ["antigravity", "all"]:
        if target == "antigravity" or env_info["antigravity"]["detected"]:
            ag_global = home / ".gemini" / "antigravity" / "skills" / "bangla-expert"
            if ag_global.exists():
                shutil.rmtree(ag_global, ignore_errors=True)
                removed_paths.append(f"Antigravity (Global Skill): {ag_global}")
        else:
            skipped.append("Antigravity (Not detected)")

    # 3. Claude
    if target in ["claude", "all"]:
        if target == "claude" or env_info["claude"]["detected"]:
            cl_global = home / ".claude" / "skills" / "bangla-expert"
            if cl_global.exists():
                shutil.rmtree(cl_global, ignore_errors=True)
                removed_paths.append(f"Claude (Global Skill): {cl_global}")
        else:
            skipped.append("Claude (Not detected)")

    # 4. Workspace Cleanups (if any legacy files exist in workspace)
    for p in [workspace / ".cursorrules", workspace / ".cursor" / "rules" / "bangla-expert.mdc"]:
        if p.exists():
            try:
                p.unlink(missing_ok=True)
                removed_paths.append(f"Workspace Rule: {p}")
            except Exception:
                pass
    if (workspace / ".cursor" / "bangla-references").exists():
        shutil.rmtree(workspace / ".cursor" / "bangla-references", ignore_errors=True)
        removed_paths.append(f"Workspace References: {workspace / '.cursor' / 'bangla-references'}")

    msg = ""
    if removed_paths:
        msg = f"✓ Bhashabid skill and references successfully removed from:\n"
        for rp in removed_paths:
            msg += f"  - {rp}\n"
    else:
        msg = "Notice: No installed Bhashabid skill files were found for the specified target.\n"

    if skipped:
        msg += "Notice: Skipped environments not installed on this machine:\n"
        for s in skipped:
            msg += f"  - {s}\n"

    if with_mcp:
        mcp_msg = uninstall_mcp(target=target, workspace_dir=str(workspace))
        msg += f"\n{mcp_msg}"

    return msg

def verify_installation() -> Dict[str, Any]:
    """
    Verifies that Bhashabid is properly installed and active across detected environments.
    """
    home = Path.home()
    env_info = detect_environments()
    status = {}

    # Cursor
    cursor_active = False
    cursor_details = []
    if env_info["cursor"]["detected"]:
        cur_rule = home / ".cursor" / "rules" / "bangla-expert.mdc"
        cur_refs = home / ".cursor" / "bangla-references"
        cur_mcp = home / ".cursor" / "mcp.json"

        has_rule = cur_rule.exists()
        has_refs = cur_refs.exists() and len(list(cur_refs.glob("*.md"))) > 0
        has_mcp = False
        if cur_mcp.exists():
            try:
                data = json.load(open(cur_mcp, "r", encoding="utf-8"))
                has_mcp = "bhashabid" in data.get("mcpServers", {})
            except Exception:
                pass

        cursor_active = has_rule and has_refs
        cursor_details.append(f"Global Rules: {'✓' if has_rule else '✗'}")
        cursor_details.append(f"References ({len(list(cur_refs.glob('*.md'))) if has_refs else 0} guides): {'✓' if has_refs else '✗'}")
        cursor_details.append(f"MCP Server: {'✓' if has_mcp else '✗'}")

    status["cursor"] = {
        "detected": env_info["cursor"]["detected"],
        "active": cursor_active,
        "details": cursor_details
    }

    # Antigravity
    ag_active = False
    ag_details = []
    if env_info["antigravity"]["detected"]:
        ag_skill = home / ".gemini" / "antigravity" / "skills" / "bangla-expert" / "SKILL.md"
        ag_mcp = home / ".gemini" / "antigravity" / "mcp_servers.json"
        has_skill = ag_skill.exists()
        has_mcp = False
        if ag_mcp.exists():
            try:
                data = json.load(open(ag_mcp, "r", encoding="utf-8"))
                has_mcp = "bhashabid" in data.get("mcpServers", {})
            except Exception:
                pass
        ag_active = has_skill
        ag_details.append(f"Global Skill: {'✓' if has_skill else '✗'}")
        ag_details.append(f"MCP Server: {'✓' if has_mcp else '✗'}")

    status["antigravity"] = {
        "detected": env_info["antigravity"]["detected"],
        "active": ag_active,
        "details": ag_details
    }

    # Claude
    claude_active = False
    claude_details = []
    if env_info["claude"]["detected"]:
        cl_skill = home / ".claude" / "skills" / "bangla-expert" / "SKILL.md"
        claude_cfg = get_claude_desktop_config_path()
        has_skill = cl_skill.exists()
        has_mcp = False
        if claude_cfg and claude_cfg.exists():
            try:
                data = json.load(open(claude_cfg, "r", encoding="utf-8"))
                has_mcp = "bhashabid" in data.get("mcpServers", {})
            except Exception:
                pass
        claude_active = has_skill
        claude_details.append(f"Global Skill: {'✓' if has_skill else '✗'}")
        claude_details.append(f"Desktop MCP: {'✓' if has_mcp else '✗'}")

    status["claude"] = {
        "detected": env_info["claude"]["detected"],
        "active": claude_active,
        "details": claude_details
    }

    return status

def format_status_report() -> str:
    st = verify_installation()
    lines = ["=" * 65, "BHASHABID SYSTEM INSTALLATION & HEALTH STATUS", "=" * 65]
    for env, data in st.items():
        name = env.capitalize()
        if not data["detected"]:
            lines.append(f"[-] {name:15} : Not detected on this machine")
        else:
            state = "ACTIVE (Verified)" if data["active"] else "INACTIVE / NOT INSTALLED"
            icon = "[✓]" if data["active"] else "[!]"
            lines.append(f"{icon} {name:15} : {state}")
            for d in data["details"]:
                lines.append(f"     • {d}")
    lines.append("=" * 65)
    return "\n".join(lines)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Install, Uninstall, or Verify Bhashabid Global Skill & MCP")
    parser.add_argument("--action", choices=["install", "uninstall", "status"], default="install")
    parser.add_argument("--target", choices=["antigravity", "claude", "cursor", "all"], default="all")
    parser.add_argument("--workspace", default=None, help="Target workspace path (optional; default is purely global)")
    parser.add_argument("--no-mcp", action="store_true", help="Skip MCP server configuration")
    args = parser.parse_args()
    if args.action == "status":
        print(format_status_report())
    elif args.action == "uninstall":
        print(uninstall_skill(args.target, args.workspace, with_mcp=not args.no_mcp))
    else:
        print(install_skill(args.target, args.workspace, with_mcp=not args.no_mcp))
