from pathlib import Path
from typing import Any

import tomlkit

import qtk.typing as qt


def load_toml(fpath: qt.StrPath) -> tomlkit.TOMLDocument:
    fpath: Path = Path(fpath)
    with fpath.open() as fp:
        return tomlkit.load(fp)


def save_toml(fpath: qt.StrPath, data: Any, *, sort_keys: bool = False) -> None:
    fpath: Path = Path(fpath)
    with fpath.open("w") as fp:
        tomlkit.dump(data, fp, sort_keys=sort_keys)
