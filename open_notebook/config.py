import os
import sys

# ROOT DATA FOLDER
# Patched in-place to fix Pressingly/foss-bundle PR #9 regression: wrapper
# spawns Python with cwd at read-only resourcesPath, so upstream
# `DATA_FOLDER = "./data"` crashes at import. Selects a per-user writable
# directory per OS, matching Electron `app.getPath("userData")` intent.
_APP = "Open Notebook"
if sys.platform == "darwin":
    DATA_FOLDER = os.path.expanduser(f"~/Library/Application Support/{_APP}/data")
elif sys.platform == "win32":
    DATA_FOLDER = os.path.join(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")), _APP, "data")
else:
    DATA_FOLDER = os.path.expanduser(f"~/.local/share/{_APP}/data")

# LANGGRAPH CHECKPOINT FILE
sqlite_folder = f"{DATA_FOLDER}/sqlite-db"
os.makedirs(sqlite_folder, exist_ok=True)
LANGGRAPH_CHECKPOINT_FILE = f"{sqlite_folder}/checkpoints.sqlite"

# UPLOADS FOLDER
UPLOADS_FOLDER = f"{DATA_FOLDER}/uploads"
os.makedirs(UPLOADS_FOLDER, exist_ok=True)

# TIKTOKEN CACHE FOLDER
# Reads TIKTOKEN_CACHE_DIR from the environment so Docker can redirect the cache
# to a path outside /data/ (which is typically volume-mounted and would hide the
# pre-baked encoding baked into the image at build time).
TIKTOKEN_CACHE_DIR = os.environ.get("TIKTOKEN_CACHE_DIR", "").strip() or f"{DATA_FOLDER}/tiktoken-cache"
os.makedirs(TIKTOKEN_CACHE_DIR, exist_ok=True)
