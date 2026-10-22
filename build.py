"""Build protected production; keep human-readable source untouched.

One-time tooling setup: python tools/production/bootstrap.py
Rebuild: python build.py
"""
from tools.production.protected_build import build

if __name__ == '__main__':
    build()
