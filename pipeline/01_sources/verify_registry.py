# Pipeline Step 1: Verify source registry & licenses
import yaml
import os

def verify_sources(registry_path: str) -> bool:
    if not os.path.exists(registry_path):
        print(f"Registry not found: {registry_path}")
        return False

    with open(registry_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    sources = data.get("sources", [])
    print(f"Verified {len(sources)} registered sources:")
    for s in sources:
        print(f" - [{s['id']}] {s['name']} (License: {s['license']}, Status: {s['status']})")
        if s["status"] != "approved":
            return False
    return True

if __name__ == "__main__":
    reg = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "memory", "sources", "registry.yaml"))
    ok = verify_sources(reg)
    print("Source Verification:", "PASSED" if ok else "FAILED")
