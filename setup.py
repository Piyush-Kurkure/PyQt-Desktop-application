import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "interface" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("interface.py", base = base)])
