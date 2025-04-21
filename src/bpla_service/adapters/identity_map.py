from typing import Any, Hashable


class IdentityMap[ValueT]:
    _map: dict[Hashable, ValueT]
    
    def __init__(self) -> None:
        self._map = {}
    
    def get(self, model: Hashable, key: Hashable) -> ValueT | None:
        return self._map.get((key, model))
    
    def set(self, model: Hashable, key: Hashable, value: ValueT) -> None:
        self._map[(key, model)] = value
