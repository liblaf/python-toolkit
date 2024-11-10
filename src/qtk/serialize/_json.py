import json
from pathlib import Path
from typing import Any

import qtk.typing as qt


def load_json(fpath: qt.StrPath) -> Any:
    fpath: Path = Path(fpath)
    with fpath.open() as fp:
        return json.load(fp)


def save_json(fpath: qt.StrPath, data: Any) -> None:
    fpath: Path = Path(fpath)
    with fpath.open("w") as fp:
        json.dump(data, fp)
