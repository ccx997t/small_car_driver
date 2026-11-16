#!/usr/bin/env bash
set -euo pipefail
project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
freecad_runner='/home/yanght/codex_pro/warmroom/apps/freecad/squashfs-root/AppRun'
# Desktop display may be absent in IDE/agent shells. This machine uses X0.
export DISPLAY="${DISPLAY:-:0}"
export XAUTHORITY="${XAUTHORITY:-/home/yanght/.Xauthority}"
export XDG_CONFIG_HOME="$project_dir/.freecad-profile/config"
export XDG_DATA_HOME="$project_dir/.freecad-profile/data"
export XDG_CACHE_HOME="$project_dir/.freecad-profile/cache"
mkdir -p "$XDG_CONFIG_HOME" "$XDG_DATA_HOME" "$XDG_CACHE_HOME"
exec "$freecad_runner" --safe-mode \
  --user-cfg "$project_dir/.freecad-profile/user.cfg" \
  --system-cfg "$project_dir/.freecad-profile/system.cfg" \
  --log-file "$project_dir/.freecad-profile/FreeCAD-r02.log" \
  "$project_dir/models/round-02/显示配色.FCMacro"
