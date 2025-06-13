"""YADE Python bindings wrapper package."""

import importlib.util
import sys
from pathlib import Path


def _find_yade_py_path() -> str:
    """YADEのPythonバインディングパスを自動で解決する。."""
    _yade_py = Path(__file__).parent / "install" / "lib" / "x86_64-linux-gnu"
    _yade_builds = [d for d in _yade_py.iterdir() if d.name.startswith("yade-")]
    if not _yade_builds:
        msg = "No yade build found in install/lib/x86_64-linux-gnu"
        raise ImportError(msg)
    return str(_yade_builds[0] / "py")


_yade_py_path = _find_yade_py_path()
if _yade_py_path not in sys.path:
    sys.path.insert(0, _yade_py_path)

_yade = importlib.import_module("yade")
Matrix3 = _yade.Matrix3
O = _yade.O  # noqa: E741
# 必要に応じて他のシンボルもここでwrap
