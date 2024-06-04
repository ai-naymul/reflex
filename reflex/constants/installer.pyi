"""Stub file for reflex/constants/installer.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
import os
import platform
from types import SimpleNamespace
from .base import IS_WINDOWS, Dirs, Reflex

def get_fnm_name() -> str | None: ...

class Bun(SimpleNamespace):
    VERSION = "1.1.10"
    MIN_VERSION = "0.7.0"
    ROOT_PATH = os.path.join(Reflex.DIR, "bun")
    DEFAULT_PATH = os.path.join(
        ROOT_PATH, "bin", "bun" if not IS_WINDOWS else "bun.exe"
    )
    INSTALL_URL = "https://bun.sh/install"
    WINDOWS_INSTALL_URL = (
        "https://raw.githubusercontent.com/reflex-dev/reflex/main/scripts/install.ps1"
    )

class Fnm(SimpleNamespace):
    VERSION = "1.35.1"
    DIR = os.path.join(Reflex.DIR, "fnm")
    FILENAME = get_fnm_name()
    EXE = os.path.join(DIR, "fnm.exe" if IS_WINDOWS else "fnm")
    INSTALL_URL = (
        f"https://github.com/Schniz/fnm/releases/download/v{VERSION}/{FILENAME}.zip"
    )

class Node(SimpleNamespace):
    VERSION = "18.17.0"
    MIN_VERSION = "18.17.0"
    BIN_PATH = os.path.join(
        Fnm.DIR,
        "node-versions",
        f"v{VERSION}",
        "installation",
        "bin" if not IS_WINDOWS else "",
    )
    PATH = os.path.join(BIN_PATH, "node.exe" if IS_WINDOWS else "node")
    NPM_PATH = os.path.join(BIN_PATH, "npm")

class PackageJson(SimpleNamespace):
    class Commands(SimpleNamespace):
        DEV = "next dev"
        EXPORT = "next build"
        EXPORT_SITEMAP = "next build && next-sitemap"
        PROD = "next start"
    PATH = os.path.join(Dirs.WEB, "package.json")
    DEPENDENCIES = {
        "@emotion/react": "11.11.1",
        "axios": "1.6.0",
        "json5": "2.2.3",
        "next": "14.0.1",
        "next-sitemap": "4.1.8",
        "next-themes": "0.2.1",
        "react": "18.2.0",
        "react-dom": "18.2.0",
        "react-focus-lock": "2.11.3",
        "socket.io-client": "4.6.1",
        "universal-cookie": "4.0.4",
    }
    DEV_DEPENDENCIES = {
        "autoprefixer": "10.4.14",
        "postcss": "8.4.31",
        "postcss-import": "16.1.0",
    }
