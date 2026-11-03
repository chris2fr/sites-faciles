{
  description = "Dev environment for Sites Faciles (Django/Wagtail + Tailwind)";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.11";
  };

  outputs = { self, nixpkgs }:
    let
      systems = [ "x86_64-linux" "aarch64-linux" ];
      forAllSystems = nixpkgs.lib.genAttrs systems;
    in
    {
      devShells = forAllSystems (system:
        let
          pkgs = import nixpkgs { inherit system; };
          # Force Poetry (and the venvs it manages) onto Python 3.11, matching pyproject.toml.
          poetry = pkgs.poetry.override { python3 = pkgs.python311; };
        in
        {
          default = pkgs.mkShell {
            name = "sites-faciles";

            packages = [
              # Python toolchain
              poetry
              pkgs.python311
              # JS toolchain (Tailwind CSS / daisyui)
              pkgs.nodejs_20
              # Database (PostgreSQL server + client)
              pkgs.postgresql_16
              # Build essentials (needed to compile some wheels, e.g. libsass)
              pkgs.gcc
              pkgs.gnumake
              pkgs.pkg-config
              pkgs.zlib
              pkgs.libffi
              pkgs.openssl
              # Misc
              pkgs.git
              pkgs.curl
              pkgs.wget
              pkgs.jq
            ];

            shellHook = ''
              set -e
              export PYTHONPATH="$PWD"
              export POETRY_VIRTUALENVS_IN_PROJECT=true
              export POETRY_VIRTUALENVS_PROMPT="(sites-faciles)"

              # Drop any inherited/non-Nix virtualenv so Poetry uses the in-project
              # .venv (and thus the Python version pinned by this flake).
              unset VIRTUAL_ENV PYTHONHOME

              # Bootstrap .env from the sample if absent.
              if [ ! -f .env ]; then
                echo "→ Creating .env from sample"
                if [ -f .env.example ]; then
                  cp .env.example .env
                else
                  cp sample.env .env
                fi
              fi

              # Bootstrap dev defaults: SECRET_KEY (if empty) and a concrete DATABASE_URL.
              python3 - <<'PY'
from pathlib import Path
import re, secrets

p = Path(".env")
p.touch(exist_ok=True)
text = p.read_text()

def parse(text):
    d = {}
    for ln in text.splitlines():
        s = ln.strip()
        if s and not s.startswith("#") and "=" in s:
            k, _, v = s.partition("=")
            d[k.strip()] = v.strip()
    return d

out = text
env = parse(out)
changed = False
DOLLAR = "\x24"  # '$' -- written escaped so Nix does not interpolate it

if not re.search(r"^SECRET_KEY=.+", out, re.M):
    key = secrets.token_urlsafe(50)
    if re.search(r"^SECRET_KEY=$", out, re.M):
        out = re.sub(r"^SECRET_KEY=$", "SECRET_KEY=" + key, out, count=1, flags=re.M)
    else:
        out = out.rstrip("\n") + "\nSECRET_KEY=" + key + "\n"
    env["SECRET_KEY"] = key
    changed = True
    print("→ Generated a SECRET_KEY in .env")

url = env.get("DATABASE_URL", "")
for k in ("DATABASE_USER", "DATABASE_PASSWORD", "DATABASE_HOST", "DATABASE_PORT", "DATABASE_NAME"):
    url = url.replace(DOLLAR + "{" + k + "}", env.get(k, ""))
if not url.strip():
    url = "postgres://{u}:{p}@{h}:{pt}/{n}".format(
        u=env.get("DATABASE_USER", "dju"),
        p=env.get("DATABASE_PASSWORD", "djpwd"),
        h=env.get("DATABASE_HOST", "localhost"),
        pt=env.get("DATABASE_PORT", "5432"),
        n=env.get("DATABASE_NAME", "djdb"))
if url != env.get("DATABASE_URL", ""):
    if re.search(r"^DATABASE_URL=.*$", out, re.M):
        out = re.sub(r"^DATABASE_URL=.*$", "DATABASE_URL=" + url, out, count=1, flags=re.M)
    else:
        out = out.rstrip("\n") + "\nDATABASE_URL=" + url + "\n"
    changed = True
    print("→ Fixed DATABASE_URL in .env (expanded placeholders)")

if changed:
    p.write_text(out)
PY

              # Report which required variables are still unset.
              missing=""
              for v in DATABASE_URL SITE_NAME SECRET_KEY HOST_URL DEBUG; do
                if ! grep -qE "^$v=.+" .env; then missing="$missing $v"; fi
              done
              [ -n "$missing" ] && echo "⚠ Still unset in .env:$missing (see sample.env)"

              # Python virtualenv via Poetry (in-project .venv).
              if [ ! -x .venv/bin/python ]; then
                echo "→ Installing Python dependencies with Poetry (.venv)"
                poetry install --no-root
              fi

              # Node dependencies (Tailwind, daisyui).
              if [ ! -d node_modules ]; then
                echo "→ Installing Node dependencies with npm (node_modules)"
                npm ci
              fi

              # Compile gettext translations (French UI strings). Cheap when up-to-date.
              make -C django_village compilemessages >/dev/null 2>&1 \
                || echo "⚠ compilemessages skipped (run `make -C django_village compilemessages`)"

              echo "✔ sites-faciles shell ready — Python: $(poetry run python --version)"
              echo "  Use: make runserver | make test-unit | make tailwind-compile"
            '';
          };
        });
    };
}
