#!/usr/bin/env python3

import game
import card
import player

def main():
    g = game.game()
    print(g.players[0].hand)

    return 0

if __name__ == "__main__":
    main()