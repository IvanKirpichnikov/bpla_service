from abc import abstractmethod
from typing import Protocol


class Provider[ObjT](Protocol):
    @abstractmethod
    async def get(self) -> ObjT:
        raise NotImplementedError
