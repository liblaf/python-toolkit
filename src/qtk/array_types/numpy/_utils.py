from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeGuard

import qtk.typing as qt

if TYPE_CHECKING:
    import numpy as np


def is_numpy(obj: Any) -> TypeGuard[np.ndarray]:
    return qt.is_instance_named_partial(obj, "numpy.ndarray")
