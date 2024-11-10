import logging
from collections.abc import Callable
from typing import Any, TypeVar, get_type_hints

import qtk
import qtk.typing as tp

_T = TypeVar("_T")
_C = TypeVar("_C", bound=qtk.BaseConfig)


def run(
    *,
    exp_name: str | None = None,
    log_level: int | str = logging.NOTSET,
    log_file: tp.StrPath | None = "exp.log",
    tags: list[str] | None = None,
    parameters: dict[str, Any] | None = None,
) -> Callable[[Callable[[_C], _T]], Callable[[_C], _T]]:
    def decorator(fn: Callable[[_C], _T]) -> Callable[[_C], _T]:
        def wrapped(cfg: _C) -> _T:
            qtk.logging.init(level=log_level, fpath=log_file)
            exp: qtk.Experiment = qtk.start(name=exp_name, tags=tags)
            exp.log_parameters(cfg.model_dump())
            result: _T = fn(cfg)
            if log_file:
                exp.log_asset(log_file)
            return result

        if fn.__module__ == "__main__":
            cls: type[_C] = get_type_hints(fn)["cfg"]
            cfg: _C = cls(**(parameters or {}))
            wrapped(cfg)
        return wrapped

    return decorator
