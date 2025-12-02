# Regicide Development Roadmap

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Game Engine (Core)                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌───────────┐   │
│  │    Rules    │  │    State    │  │   Actions   │  │ Validator │   │
│  │   Engine    │  │   Manager   │  │   Handler   │  │           │   │
│  └─────────────┘  └─────────────┘  └─────────────┘  └───────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                              ▲
                              │ Game Interface (Abstract)
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│  Local Solo   │    │  LAN Server   │    │ Remote Server │
│   Adapter     │    │   Adapter     │    │   Adapter     │
└───────────────┘    └───────────────┘    └───────────────┘
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│  Textual TUI  │    │textual serve  │    │ Web Deploy    │
│  (Terminal)   │    │  (Browser)    │    │  (Hosted)     │
└───────────────┘    └───────────────┘    └───────────────┘
```

## Design Principles

1. **Separation of Concerns** - Game logic completely independent of UI/networking
2. **Authoritative Server** - All game state changes validated server-side
3. **Stateless Protocol** - Client sends actions, server sends full state
4. **Portable Core** - Engine can run anywhere Python runs

---

## Phase 1: Core Game Engine

**Goal**: Complete, tested game logic with no UI dependencies

Each step follows TDD: write tests first, then implement to pass.

### 1.1 Card and Deck
- [ ] **Tests**: Card creation, rank/suit values, attack values (A=1, 2-10=face, J=10, Q=15, K=20)
- [ ] **Tests**: Deck operations (shuffle, draw, add, peek, length, empty check)
- [ ] **Implement**: `Card`, `Deck` classes

### 1.2 Hand and Player
- [ ] **Tests**: Hand limits by player count, add/remove cards, value calculation for discarding
- [ ] **Tests**: Player state, hand ownership
- [ ] **Implement**: `Hand`, `Player` classes

### 1.3 Enemy and Combat
- [ ] **Tests**: Enemy stats (J=10/20, Q=15/30, K=20/40), damage tracking, defeat conditions
- [ ] **Tests**: Exact damage detection (for Tavern recovery)
- [ ] **Tests**: Shield accumulation and attack reduction
- [ ] **Implement**: `Enemy` class, damage logic

### 1.4 Setup and Game State
- [ ] **Tests**: Castle deck construction (K bottom, Q middle, J top, each rank shuffled)
- [ ] **Tests**: Tavern deck construction (2-10 + Aces + Jesters by player count)
- [ ] **Tests**: Initial deal by player count
- [ ] **Tests**: GameState serialization round-trip (to_json/from_json)
- [ ] **Implement**: `GameState`, setup logic, serialization

### 1.5 Suit Powers
- [ ] **Tests**: Hearts - heal N cards from discard to tavern bottom
- [ ] **Tests**: Diamonds - draw N cards distributed across players
- [ ] **Tests**: Clubs - double damage calculation
- [ ] **Tests**: Spades - shield accumulation, attack reduction
- [ ] **Tests**: Immunity - enemy blocks own suit power
- [ ] **Tests**: Resolution order (Hearts before Diamonds)
- [ ] **Implement**: Suit power handlers

### 1.6 Card Play Validation
- [ ] **Tests**: Single card play
- [ ] **Tests**: Combos (2-4 same rank, total <=10)
- [ ] **Tests**: Animal Companion pairing (with one card, same suit = single power)
- [ ] **Tests**: Face card + Animal Companion pairing
- [ ] **Tests**: Invalid plays rejected
- [ ] **Implement**: Play validation logic

### 1.7 Turn Structure
- [ ] **Tests**: Step 1 - play card or yield
- [ ] **Tests**: Step 2 - suit power activation
- [ ] **Tests**: Step 3 - damage dealt, defeat check, exactsies
- [ ] **Tests**: Step 4 - suffer damage, discard requirement
- [ ] **Tests**: Turn advancement, player rotation
- [ ] **Implement**: Turn state machine

### 1.8 Yielding
- [ ] **Tests**: Solo - cannot yield
- [ ] **Tests**: 2+ players - yield restriction (cannot if all others yielded)
- [ ] **Tests**: Yield skips Steps 2-3, goes to Step 4
- [ ] **Implement**: Yield action

### 1.9 Win/Lose Conditions
- [ ] **Tests**: Win - all 12 enemies defeated
- [ ] **Tests**: Lose - cannot satisfy damage
- [ ] **Tests**: Lose - cannot play or yield
- [ ] **Implement**: Game end detection

### 1.10 Jester (if including multiplayer prep)
- [ ] **Tests**: Jester negates immunity
- [ ] **Tests**: Jester skip Steps 3-4, choose next player
- [ ] **Tests**: Spades retroactive, Clubs not retroactive
- [ ] **Implement**: Jester logic

**Deliverable**: `regicide/engine/` package with tests written before each implementation

### File Organization

```
regicide/
├── engine/
│   ├── __init__.py
│   ├── card.py              # Card class only
│   ├── deck.py              # Deck class only
│   ├── hand.py              # Hand class only
│   ├── player.py            # Player class only
│   ├── enemy.py             # Enemy class only
│   ├── game_state.py        # GameState class, serialization
│   ├── setup.py             # create_castle_deck(), create_tavern_deck(), deal_hands()
│   ├── powers.py            # apply_hearts(), apply_diamonds(), apply_clubs(), apply_spades()
│   ├── validation.py        # validate_play(), validate_combo(), validate_yield()
│   ├── combat.py            # deal_damage(), check_defeat(), apply_shield()
│   ├── turn.py              # execute_turn(), advance_player()
│   └── game.py              # Game class (orchestrates everything)
│
├── tests/
│   ├── __init__.py
│   ├── test_card.py
│   ├── test_deck.py
│   ├── test_hand.py
│   ├── test_player.py
│   ├── test_enemy.py
│   ├── test_game_state.py
│   ├── test_setup.py
│   ├── test_powers.py
│   ├── test_validation.py
│   ├── test_combat.py
│   ├── test_turn.py
│   └── test_game.py
```

### Code Style

**One component, one file:**
- Each class gets its own module
- Related pure functions grouped by domain (powers, validation, combat)

**One task, one function:**
- Functions do one thing and are named for that thing
- No multi-purpose functions with mode flags

**Human-readable test names:**
```python
# test_card.py
def test_ace_has_attack_value_of_one():
def test_number_cards_have_attack_value_equal_to_rank():
def test_jack_has_attack_value_of_ten():
def test_queen_has_attack_value_of_fifteen():
def test_king_has_attack_value_of_twenty():

# test_combo.py
def test_pair_of_fives_is_valid_combo():
def test_triple_threes_is_valid_combo():
def test_quad_twos_is_valid_combo():
def test_pair_of_sixes_rejected_because_total_exceeds_ten():
def test_face_cards_cannot_be_used_in_combos():

# test_powers.py
def test_hearts_moves_cards_from_discard_to_tavern_bottom():
def test_diamonds_distributes_draws_across_players_in_order():
def test_clubs_doubles_damage_dealt():
def test_spades_shield_accumulates_across_multiple_plays():
def test_enemy_is_immune_to_own_suit_power():
```

---

## Phase 2: Local Solo Game

**Goal**: Playable single-player game in terminal

### 2.1 Game Interface
- [ ] Abstract `GameInterface` class
- [ ] `LocalGameAdapter` - direct engine calls

### 2.2 Textual UI Components
- [ ] `CardWidget` - single card display
- [ ] `HandWidget` - player's hand with selection
- [ ] `EnemyWidget` - current enemy with health bar
- [ ] `GameStateWidget` - tavern/castle/discard counts
- [ ] `ActionBar` - available actions
- [ ] `GameLog` - recent events

### 2.3 Game Screen
- [ ] Main game layout
- [ ] Card selection flow
- [ ] Action confirmation
- [ ] Turn feedback (damage dealt, powers activated)
- [ ] Win/lose screens

### 2.4 Polish
- [ ] Keyboard navigation
- [ ] Help overlay (rules reference)
- [ ] Game restart

**Deliverable**: `python -m regicide` launches playable solo game

---

## Phase 3: Two-Player LAN (Browser)

**Goal**: Two players on same network via browser

### 3.1 Network Protocol
- [ ] Message types (JSON schema)
  - `JOIN` - player joins game
  - `STATE` - full game state update
  - `ACTION` - player action
  - `ERROR` - invalid action feedback
  - `CHAT` - optional player chat
- [ ] WebSocket connection handling

### 3.2 Server Adapter
- [ ] `LANServerAdapter` - hosts game, validates actions
- [ ] Player session management
- [ ] Turn enforcement
- [ ] Reconnection handling

### 3.3 Client Adapter  
- [ ] `NetworkClientAdapter` - connects to server
- [ ] State synchronization
- [ ] Action dispatch
- [ ] Connection status UI

### 3.4 Lobby System
- [ ] Host game screen
- [ ] Join game screen (enter IP/code)
- [ ] Player ready status
- [ ] Game start coordination

### 3.5 Browser Deployment
- [ ] `textual serve` configuration
- [ ] LAN discovery (optional: mDNS/Bonjour)
- [ ] Connection instructions for players

**Deliverable**: `python -m regicide --host` and `python -m regicide --join <ip>`

---

## Phase 4: Remote Multiplayer (Self-Hosted)

**Goal**: Play over internet with self-hosted server

### 4.1 Deployment Package
- [ ] Docker container for server
- [ ] Environment configuration
- [ ] HTTPS/WSS support (Let's Encrypt)
- [ ] Reverse proxy guide (nginx/caddy)

### 4.2 Connection Management
- [ ] Game codes (short joinable IDs)
- [ ] NAT traversal documentation
- [ ] Latency handling
- [ ] Disconnect/reconnect robustness

### 4.3 Security
- [ ] Rate limiting
- [ ] Input validation hardening
- [ ] No sensitive data exposure

### 4.4 Documentation
- [ ] Self-hosting guide
- [ ] Cloud deployment options (fly.io, Railway, VPS)
- [ ] Troubleshooting guide

**Deliverable**: Docker image + deployment docs

---

## Phase 5: Future Enhancements (Optional)

### 5.1 Additional Features
- [ ] 3-4 player support
- [ ] Jester variant
- [ ] Game statistics/history
- [ ] Spectator mode

### 5.2 Alternative Clients
- [ ] Web-only client (no Python required for players)
- [ ] Mobile-optimized layout
- [ ] Desktop executable (PyInstaller)

### 5.3 AI Opponent
- [ ] Solo mode with AI partner
- [ ] Difficulty levels

---

## File Structure (Planned)

```
regicide/
├── engine/                 # Phase 1: Core game logic
│   ├── __init__.py
│   ├── models.py          # Card, Deck, Hand, Enemy, GameState
│   ├── rules.py           # Game rules and validation
│   ├── actions.py         # Action definitions
│   └── serialization.py   # JSON encode/decode
│
├── interface/             # Phase 2+: Adapters
│   ├── __init__.py
│   ├── base.py            # Abstract GameInterface
│   ├── local.py           # LocalGameAdapter
│   └── network.py         # NetworkClientAdapter, LANServerAdapter
│
├── ui/                    # Phase 2+: Textual components
│   ├── __init__.py
│   ├── widgets/
│   │   ├── card.py
│   │   ├── hand.py
│   │   ├── enemy.py
│   │   └── game_state.py
│   ├── screens/
│   │   ├── game.py
│   │   ├── lobby.py
│   │   └── menu.py
│   └── app.py             # Main Textual App
│
├── server/                # Phase 3+: Network server
│   ├── __init__.py
│   ├── websocket.py
│   ├── protocol.py
│   └── session.py
│
├── tests/                 # All phases
│   ├── test_engine/
│   ├── test_interface/
│   └── test_server/
│
├── __main__.py            # Entry point
├── requirements.txt
└── Dockerfile             # Phase 4
```

---

## Technology Stack (Confirmed)

| Component | Technology |
|-----------|------------|
| Language | Python 3.11+ |
| Game Engine | Pure Python (no dependencies) |
| Text UI | Textual |
| Networking | asyncio + websockets |
| Serialization | JSON (stdlib) |
| Testing | pytest |
| Browser Serving | textual serve |
| Containerization | Docker |

---

## Next Steps

**Immediate (Phase 1.1)**:
1. Create `regicide/engine/` package structure
2. Implement `Card` and `Deck` models with tests
3. Implement `GameState` with serialization

Ready to begin?
