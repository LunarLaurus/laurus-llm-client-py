# laurus_llm_client/__init__.py
"""Top-level package for laurus-llm-client."""

from .llm_client import LocalLLMClient
from .llm_helpers import LLMWrapper
from .lauruslogger import LOG

__all__ = ["LocalLLMClient", "LLMWrapper", "LOG"]

# package version (keep in sync with pyproject.toml)
__version__ = "0.0.3"
