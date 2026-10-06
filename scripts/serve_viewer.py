#!/usr/bin/env python3
"""Serve this folder so the viewer can read data/. Works from any working directory.

Usage: python3 scripts/serve_viewer.py [port]     (default 8000; tries the next ports if busy)
Then open the printed address. Stop with Ctrl-C.
"""
import functools
import http.server
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)
    for p in range(port, port + 20):
        try:
            httpd = http.server.ThreadingHTTPServer(("127.0.0.1", p), handler)
        except OSError:
            continue
        print(f"serving {ROOT}\nopen http://localhost:{p}/viewer/", flush=True)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        return
    raise SystemExit(f"no free port in {port}-{port + 19}")


if __name__ == "__main__":
    main()
