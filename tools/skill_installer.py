# tools/skill_installer.py
# One-Click Skill & Reference Installer for AI IDEs & Agents
import os
import sys
import shutil
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

def install_skill(target: str = "antigravity", workspace_dir: str = None) -> str:
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
        # Cursor rules directory in workspace
        cur_rules = workspace / ".cursor" / "rules"
        os.makedirs(cur_rules, exist_ok=True)
        # Copy rule file to both .cursorrules (workspace root) and .cursor/rules/bangla-expert.mdc
        src_rule = Path(REPO_ROOT) / "adapters" / "cursor" / ".cursorrules"
        if src_rule.exists():
            shutil.copy(src_rule, workspace / ".cursorrules")
            shutil.copy(src_rule, cur_rules / "bangla-expert.mdc")
        # Also copy references into .cursor/bangla-references/ so Cursor AI can read them
        cur_refs = workspace / ".cursor" / "bangla-references"
        os.makedirs(cur_refs, exist_ok=True)
        shutil.copytree(src_dir / "references", cur_refs, dirs_exist_ok=True)
        dest_paths.append(str(workspace / ".cursorrules"))
        dest_paths.append(str(cur_rules / "bangla-expert.mdc"))

    msg = f"✓ Bhashabid skill and all {len(list((src_dir / 'references').glob('*.md')))} reference guides successfully installed to:\n"
    for dp in dest_paths:
        msg += f"  - {dp}\n"
    return msg

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Install Bhashabid Skill with all References")
    parser.add_argument("--target", choices=["antigravity", "claude", "cursor", "all"], default="all")
    parser.add_argument("--workspace", default=None, help="Target workspace path (defaults to current dir)")
    args = parser.parse_args()
    print(install_skill(args.target, args.workspace))
