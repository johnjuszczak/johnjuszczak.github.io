import argparse, os, shutil, subprocess, sys
from pathlib import Path

def find_bundle():
    for name in ("bundle", "bundle.cmd", "bundle.bat", "bundle.exe"):
        p = shutil.which(name)
        if p:
            return p
    return "bundle"

def main():
    ap = argparse.ArgumentParser(
        description=("Serve a Jekyll site locally via Bundler.\n"
                     "Optionally simulate a preview baseurl and enable live reload."),
        epilog=("Examples:\n"
                "  python serve_local.py\n"
                "  python serve_local.py --no-livereload\n"
                "  python serve_local.py --config _alt.yml --config foo.yml\n"
                "  python serve_local.py --preview-baseurl /pr-preview/pr-4\n"
                "  python serve_local.py --host 0.0.0.0 --port 4001"),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    ap.add_argument("--config", action="append", default=[])
    ap.add_argument("--no-local", action="store_true")
    ap.add_argument("--preview-baseurl", default="")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", default="4000")
    ap.add_argument("--no-livereload", action="store_true")
    args = ap.parse_args()

    repo = Path(__file__).resolve().parent
    os.chdir(repo)

    cfgs = ["_config.yml"]
    local_cfg = repo / "_config.local.yml"
    if not args.no_local and local_cfg.exists():
        cfgs.append("_config.local.yml")
    if args.config:
        cfgs.extend(args.config)

    cmd = [find_bundle(), "exec", "jekyll", "serve",
           "--host", args.host, "--port", args.port,
           "--config", ",".join(cfgs)]
    if not args.no_livereload:
        cmd.append("--livereload")
    if args.preview_baseurl:
        cmd.extend(["--baseurl", args.preview_baseurl])

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)

if __name__ == "__main__":
    main()
