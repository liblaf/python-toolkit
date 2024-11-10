import logging
from collections.abc import Callable
from typing import TypeVar

import qtk

_T = TypeVar("_T")


def run(
    log_level: int | str = logging.NOTSET,
) -> Callable[[Callable[[], _T]], Callable[[], _T]]:
    def decorator(fn: Callable[[], _T]) -> Callable[[], _T]:
        def wrapped() -> _T:
            qtk.logging.init(level=log_level, file="experiment.log")
            return fn()

        if fn.__module__ == "__main__":
            wrapped()
        return wrapped

    return decorator
