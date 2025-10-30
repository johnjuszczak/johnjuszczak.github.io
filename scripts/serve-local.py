import argparse, os, shutil, subprocess, sys, time, socket, webbrowser
from pathlib import Path

def find_bundle():
    for name in ("bundle", "bundle.cmd", "bundle.bat", "bundle.exe"):
        p = shutil.which(name)
        if p:
            return p
    return "bundle"

def wait_port(host, port, timeout=120):
    start = time.time()
    while time.time() - start < timeout:
        try:
            with socket.create_connection((host, int(port)), timeout=1):
                return True
        except OSError:
            time.sleep(0.25)
    return False

def main():
    ap = argparse.ArgumentParser(
        description=("Serve a Jekyll site locally via Bundler. Pass the site directory."),
        epilog=("Examples:\n"
                "  py scripts/serve-local.py .\n"
                "  py scripts/serve-local.py . --no-livereload\n"
                "  py scripts/serve-local.py . --config _alt.yml --config foo.yml\n"
                "  py scripts/serve-local.py . --preview-baseurl /pr-preview/pr-4\n"
                "  py scripts/serve-local.py . -a"),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    ap.add_argument("site_dir", nargs="?", help="Path to the Jekyll site directory")
    ap.add_argument("--config", action="append", default=[])
    ap.add_argument("--no-local", action="store_true")
    ap.add_argument("--preview-baseurl", default="")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", default="4000")
    ap.add_argument("--no-livereload", action="store_true")
    ap.add_argument("-a", "--auto", action="store_true")
    args = ap.parse_args()

    if not args.site_dir:
        ap.print_help()
        sys.exit(1)

    repo = Path(args.site_dir).expanduser().resolve()
    if not repo.is_dir():
        print(f"Not a directory: {repo}", file=sys.stderr)
        sys.exit(2)

    os.chdir(repo)

    cfgs = []
    if (repo / "_config.yml").exists():
        cfgs.append("_config.yml")
    local_cfg = repo / "_config.local.yml"
    if not args.no_local and local_cfg.exists():
        cfgs.append("_config.local.yml")
    if args.config:
        cfgs.extend(args.config)
    if not cfgs:
        print("No config files found. Expected at least _config.yml", file=sys.stderr)
        sys.exit(3)

    cmd = [find_bundle(), "exec", "jekyll", "serve",
           "--host", args.host, "--port", str(args.port),
           "--config", ",".join(cfgs)]
    if not args.no_livereload:
        cmd.append("--livereload")
    if args.preview_baseurl:
        cmd.extend(["--baseurl", args.preview_baseurl])

    url_base = f"http://{args.host}:{args.port}"
    baseurl = args.preview_baseurl if args.preview_baseurl else ""
    if baseurl and not baseurl.startswith("/"):
        baseurl = "/" + baseurl
    url = url_base + baseurl

    if args.auto:
        proc = subprocess.Popen(cmd)
        try:
            if wait_port(args.host, args.port, timeout=10):
                webbrowser.open(url, new=1, autoraise=True)
            proc.wait()
            sys.exit(proc.returncode)
        except KeyboardInterrupt:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
            sys.exit(130)
    else:
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            sys.exit(e.returncode)

if __name__ == "__main__":
    main()
