#!/usr/bin/python3
import os
import sys

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)

    import hidden_4

    names = [name for name in dir(hidden_4) if not name.startswith("__")]
    for name in sorted(names):
        print(name)
