from abc import ABC


class AppAtlasPlugin(ABC):
    @classmethod
    def __subclasshook__(cls, __subclass: type) -> bool:
        return hasattr(__subclass, "register_plugin") and callable(
            __subclass.register_plugin
        )


__all__ = ["AppAtlasPlugin"]
