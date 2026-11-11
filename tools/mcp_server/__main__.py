# tools/mcp_server/__main__.py
import sys
from .server import main

if __name__ == "__main__":
    sys.exit(main() or 0)
