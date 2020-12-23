import re
from typing import Any, Callable, Dict, Final, Optional, Tuple

import pydicom

Dataset = pydicom.dataset.Dataset


class Handler:
    def __init__(self, handler: Callable[[Any], Any]) -> None:
        self.handler = handler

    def __call__(self, dataset: Dataset, tag: int) -> Any:
        element = dataset.get(tag)
        if element is not None:
            element.value = self.handler(element.value)


def str_to_first_int(s: str) -> Optional[int]:
    x = re.findall(r"\d+", s)
    if len(x) > 0:
        return int(x[0])


def age_to_anonymized_age(age_str: str) -> str:
    """So few people live into their 90s that an age greater than 89 is considered to be identifying information."""
    age: Optional[int] = str_to_first_int(age_str)
    if age is None:
        return "----"
    elif age > 89:
        return "90Y+"
    else:
        return f"{age:03}Y"


rules: Final[Dict[Tuple[int, int], Callable[[Dataset, int], Any]]] = {
    (0x0010, 0x1010): Handler(age_to_anonymized_age),
}
