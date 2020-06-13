from abc import ABC, abstractmethod
from typing import List, Optional


class Pack(ABC):
    @abstractmethod
    def command_name(self) -> Optional[str]:
        pass

    @abstractmethod
    def depends_on(self) -> List['Pack']:
        pass

    @abstractmethod
    def install(self):
        pass

    @abstractmethod
    def configure(self, configs_dir):
        pass
