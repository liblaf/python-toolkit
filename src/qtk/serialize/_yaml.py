from pathlib import Path
from typing import Any

from ruamel.yaml import YAML

import qtk.typing as qt


def load_yaml(fpath: qt.StrPath) -> Any:
    fpath: Path = Path(fpath)
    yaml = YAML()
    with fpath.open() as fp:
        return yaml.load(fp)


def save_yaml(fpath: qt.StrPath, data: Any) -> None:
    fpath: Path = Path(fpath)
    yaml = YAML()
    with fpath.open("w") as fp:
        yaml.dump(data, fp)
