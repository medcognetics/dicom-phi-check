from .anonymize import anonymize

try:
    from .version import __version__
except ImportError:
    __version__ = "Unknown"

__all__ = [
    "__version__",
    "anonymize",
]
