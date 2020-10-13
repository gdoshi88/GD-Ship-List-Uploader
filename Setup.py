# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:14:24 2017

@author: tastetf
"""

"""Fichier d'installation script """

import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

# On appelle la fonction setup
setup(
    name = "Shipping list loader",
    version = "0.1",
    description = "Loading ship list",
    executables = [Executable("ShipListLoader.py", base="Win32GUI")],
)