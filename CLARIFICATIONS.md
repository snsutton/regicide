# Rules Clarifications

Implementation interpretations for ambiguous rules and edge cases.

---

## Yielding

### Solo Play
Solo players **cannot yield**.

### 2+ Player Games
The yield restriction only checks the **immediately preceding turn(s)**. If Player A yields, Player B cannot yield. But on Player A's next turn, they may yield again since Player B did not yield.

---

## Jester and Enemy Immunity

### Spades Retroactivity
When a Jester is played against a Spades enemy, all Spades played **prior** to the Jester begin reducing the enemy's attack. This is a special retroactive exception.

### Clubs Non-Retroactivity
Clubs played prior to a Jester against a Clubs enemy do **not** retroactively count for double damage. Only Clubs played after the Jester benefit from the immunity removal.

### Hearts and Diamonds
The rules do not mention Hearts or Diamonds in this context. We interpret that they also do **not** apply retroactively (like Clubs).

---

## Animal Companions

### Same Suit Pairing
When an Animal Companion is paired with a card of the same suit, the suit power is applied once at the **combined attack value**. Example: A♥ + 8♥ = 9 attack, heal 9 cards.

---

## Combos

### Face Cards
Face cards **cannot** be used in combos. The rule requires "the combined total of the cards played equals 10 or less" - any single face card (J=10, Q=15, K=20) already meets or exceeds this limit.

Face cards **can** be paired with Animal Companions (this is not a combo, it's the Animal Companion pairing rule).

---

## Suit Power Resolution Order

When multiple suit powers activate together:

1. **Hearts** (heal from discard)
2. **Diamonds** (draw cards)
3. **Clubs** (double damage - applied in Step 3)
4. **Spades** (shield - applied in Step 4)

Clubs vs Spades order does not matter since they apply in different steps.

---

## Exact Damage (Tavern Recovery)

"Exact damage" is calculated using the **final damage value**, including Clubs doubling.

**Example:** Jack has 20 health, 10 damage already dealt. Playing 5♣ deals 10 damage (doubled). Total damage = 20, which exactly equals Jack's health. The Jack is placed facedown on top of the Tavern deck.

---

## Partial Effects

### Hearts (Small Discard Pile)
If the attack value exceeds the discard pile size, heal as many cards as possible. Partial healing is allowed.

### Diamonds (Small Tavern Deck)
If the attack value exceeds the Tavern deck size, draw as many cards as available. There is no penalty for failing to draw from an empty Tavern.

---
