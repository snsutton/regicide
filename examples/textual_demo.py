#!/usr/bin/env python3
"""
Textual Demo - Regicide UI Concepts

Run with: python examples/textual_demo.py
Or serve as web: textual serve examples/textual_demo.py

Requires: pip install textual
"""

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Button, Footer, Header, Static, Label
from textual.reactive import reactive


# Card display using Unicode box drawing
CARD_TEMPLATE = """\
┌─────────┐
│ {rank:<2}      │
│ {suit}       │
│         │
│       {suit} │
│      {rank:>2} │
└─────────┘"""

SUIT_SYMBOLS = {
    "Hearts": "♥",
    "Diamonds": "♦", 
    "Clubs": "♣",
    "Spades": "♠"
}

SUIT_COLORS = {
    "Hearts": "red",
    "Diamonds": "red",
    "Clubs": "white",
    "Spades": "white"
}


class Card(Static):
    """A playing card widget."""
    
    def __init__(self, rank: str, suit: str, **kwargs):
        super().__init__(**kwargs)
        self.rank = rank
        self.suit = suit
        self.symbol = SUIT_SYMBOLS[suit]
        self.selected = False
    
    def compose(self) -> ComposeResult:
        card_text = CARD_TEMPLATE.format(rank=self.rank, suit=self.symbol)
        yield Static(card_text, classes="card-face")
    
    def on_click(self) -> None:
        self.selected = not self.selected
        self.toggle_class("selected")
        self.app.query_one("#status").update(
            f"{'Selected' if self.selected else 'Deselected'}: {self.rank} of {self.suit}"
        )


class EnemyDisplay(Static):
    """Display for the current enemy."""
    
    health = reactive(20)
    
    def __init__(self, rank: str, suit: str, max_health: int, **kwargs):
        super().__init__(**kwargs)
        self.rank = rank
        self.suit = suit
        self.max_health = max_health
        self.health = max_health
    
    def compose(self) -> ComposeResult:
        yield Static(f"⚔️  ENEMY: {self.rank} of {self.suit}", classes="enemy-title")
        yield Static(f"Health: {self.health}/{self.max_health}", id="enemy-health")
        yield Static(f"Attack: 10 | Immune to {SUIT_SYMBOLS[self.suit]}", classes="enemy-stats")
    
    def watch_health(self, health: int) -> None:
        """React to health changes."""
        try:
            health_widget = self.query_one("#enemy-health", Static)
            bar_width = 20
            filled = int((health / self.max_health) * bar_width)
            bar = "█" * filled + "░" * (bar_width - filled)
            health_widget.update(f"Health: [{bar}] {health}/{self.max_health}")
        except Exception:
            pass  # Widget not yet mounted


class GameInfo(Static):
    """Game state information panel."""
    
    def compose(self) -> ComposeResult:
        yield Static("📚 Tavern: 32 cards", classes="info-line")
        yield Static("🏰 Castle: 11 enemies", classes="info-line")
        yield Static("🗑️  Discard: 0 cards", classes="info-line")
        yield Static("🛡️  Shield: 0", classes="info-line")


class RegicideDemo(App):
    """Demonstration of Textual UI for Regicide."""
    
    CSS = """
    Screen {
        background: #1a1a2e;
    }
    
    Header {
        background: #16213e;
    }
    
    #main-container {
        layout: grid;
        grid-size: 3 3;
        grid-columns: 1fr 2fr 1fr;
        grid-rows: auto 1fr auto;
        height: 100%;
    }
    
    #game-info {
        column-span: 1;
        row-span: 1;
        border: solid #4a4a6a;
        padding: 1;
        margin: 1;
    }
    
    #enemy-area {
        column-span: 1;
        row-span: 1;
        border: solid #e94560;
        padding: 1;
        margin: 1;
        content-align: center middle;
    }
    
    .enemy-title {
        text-style: bold;
        color: #e94560;
    }
    
    .enemy-stats {
        color: #888;
    }
    
    #actions {
        column-span: 1;
        row-span: 1;
        border: solid #4a4a6a;
        padding: 1;
        margin: 1;
    }
    
    #hand-area {
        column-span: 3;
        row-span: 1;
        border: solid #0f3460;
        padding: 1;
        margin: 1;
    }
    
    #hand-container {
        layout: horizontal;
        height: auto;
    }
    
    Card {
        width: 13;
        height: 9;
        margin: 0 1;
    }
    
    .card-face {
        color: white;
        background: #2a2a4a;
    }
    
    Card.selected .card-face {
        background: #0f3460;
        border: solid #00d9ff;
    }
    
    Card:hover .card-face {
        background: #3a3a5a;
    }
    
    #status-bar {
        column-span: 3;
        row-span: 1;
        height: 3;
        border: solid #4a4a6a;
        padding: 1;
        margin: 1;
    }
    
    #status {
        color: #00d9ff;
    }
    
    Button {
        width: 100%;
        margin: 1 0;
    }
    
    Button.attack {
        background: #e94560;
    }
    
    Button.yield-btn {
        background: #4a4a6a;
    }
    """
    
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("a", "attack", "Attack"),
        ("y", "yield_turn", "Yield"),
    ]
    
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        
        with Container(id="main-container"):
            # Left column - game info
            with Vertical(id="game-info"):
                yield Static("📊 Game State", classes="section-title")
                yield GameInfo()
            
            # Center - enemy
            with Vertical(id="enemy-area"):
                yield EnemyDisplay("Jack", "Spades", max_health=20, id="enemy")
            
            # Right column - actions
            with Vertical(id="actions"):
                yield Static("⚡ Actions", classes="section-title")
                yield Button("Attack", id="attack-btn", classes="attack", variant="error")
                yield Button("Yield", id="yield-btn", classes="yield-btn", variant="default")
            
            # Bottom - player hand
            with Vertical(id="hand-area"):
                yield Static("🃏 Your Hand (click to select)", classes="section-title")
                with Horizontal(id="hand-container"):
                    yield Card("7", "Hearts")
                    yield Card("4", "Clubs")
                    yield Card("9", "Diamonds")
                    yield Card("2", "Spades")
                    yield Card("A", "Hearts")
                    yield Card("6", "Clubs")
                    yield Card("10", "Diamonds")
            
            # Status bar
            with Horizontal(id="status-bar"):
                yield Static("Ready - Select cards and attack!", id="status")
        
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "attack-btn":
            self.action_attack()
        elif event.button.id == "yield-btn":
            self.action_yield_turn()
    
    def action_attack(self) -> None:
        """Perform attack action."""
        enemy = self.query_one("#enemy", EnemyDisplay)
        selected_cards = [c for c in self.query(Card) if c.selected]
        
        if not selected_cards:
            self.query_one("#status").update("⚠️  Select cards to attack!")
            return
        
        # Calculate damage (simplified)
        damage = sum(int(c.rank) if c.rank.isdigit() else 1 for c in selected_cards)
        enemy.health = max(0, enemy.health - damage)
        
        card_names = ", ".join(f"{c.rank}{SUIT_SYMBOLS[c.suit]}" for c in selected_cards)
        self.query_one("#status").update(f"⚔️  Attacked with {card_names} for {damage} damage!")
        
        # Deselect cards
        for card in selected_cards:
            card.selected = False
            card.remove_class("selected")
        
        if enemy.health <= 0:
            self.query_one("#status").update("🎉 Enemy defeated!")
    
    def action_yield_turn(self) -> None:
        """Yield turn."""
        self.query_one("#status").update("🏳️  You yielded your turn")
    


if __name__ == "__main__":
    app = RegicideDemo()
    app.run()
