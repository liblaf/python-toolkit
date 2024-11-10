import logging
from collections.abc import Callable
from typing import Any, TypeVar

import qtk
import qtk.typing as tp

_T = TypeVar("_T")


def run(
    *,
    exp_name: str | None = None,
    log_level: int | str = logging.NOTSET,
    log_file: tp.StrPath | None = "exp.log",
    tags: list[str] | None = None,
    parameters: dict[str, Any] | None = None,
) -> Callable[[Callable[[], _T]], Callable[[], _T]]:
    def decorator(fn: Callable[[], _T]) -> Callable[[], _T]:
        def wrapped() -> _T:
            exp: qtk.Experiment = qtk.start(name=exp_name, tags=tags)
            if parameters is not None:
                exp.log_parameters(parameters)
            qtk.logging.init(level=log_level, fpath=log_file)
            result: _T = fn()
            if log_file:
                exp.log_asset(log_file)
            return result

        if fn.__module__ == "__main__":
            wrapped()
        return wrapped

    return decorator
