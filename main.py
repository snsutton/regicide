#!/usr/bin/env python3

import subprocess
import platform

from game import Game

def open_terminal():
    if platform.system() == "Windows":
        subprocess.call("start cmd", shell=True)
    else:
        raise NotImplementedError("Your OS is not supported.")

def main():
    g = Game()
    open_terminal()
    print(g)

    return 0

if __name__ == "__main__":
    main()