# AI-Assisted Development Workflow

This project uses a multi-model AI workflow for development.

## Model Assignments

| Model | Role | Responsibilities |
|-------|------|------------------|
| **Opus 4.5** | Design & Planning | Architecture decisions, system design, high-level planning |
| **Sonnet 4.5** | Prompt Engineering | Generating prompts for code generation, documentation |
| **GPT-5.1-Codex** | Code Generation | Implementation, writing code, tests |

## Workflow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Opus 4.5   │────▶│ Sonnet 4.5  │────▶│ GPT-5.1     │
│  (Design)   │     │  (Prompts)  │     │  (Code)     │
└─────────────┘     └─────────────┘     └─────────────┘
       │                                       │
       └───────────── Review ◀─────────────────┘
```

### Phase 1: Design (Opus 4.5)
- Analyze requirements
- Propose architecture options
- Make technology recommendations
- Define interfaces and contracts

### Phase 2: Prompt Generation (Sonnet 4.5)
- Convert designs into implementation prompts
- Break down tasks into codeable units
- Specify test requirements

### Phase 3: Implementation (GPT-5.1-Codex)
- Generate code from prompts
- Write unit tests
- Implement features

### Phase 4: Review
- Human review of generated code
- Opus 4.5 for architectural review if needed
- Iterate as necessary

## Guidelines

### For Design Prompts (to Opus 4.5)
- Provide context about project goals
- Ask for trade-off analysis
- Request evidence-based recommendations

### For Code Generation Prompts (to GPT-5.1-Codex)
- Include interface definitions
- Specify error handling requirements
- Reference existing code patterns
- Include test case requirements

### Critical Rules for All Models
- **Disclose limitations immediately** - If you cannot read a file format (e.g., PDF, images), say so upfront rather than generating content from general knowledge
- **Never present paraphrased or inferred content as transcription** - Be explicit about the source of information
- **No emojis** - Do not use emojis in code or documentation

## Current Phase

**Phase 1: Core Game Engine** (see [ROADMAP.md](ROADMAP.md))

Technology decisions complete:
- Text UI: Textual
- Networking: asyncio + websockets  
- Serialization: JSON
- Architecture: Client-server (authoritative)

Next steps:
1. Implement `Card` and `Deck` models
2. Implement `GameState` with serialization
3. Build rules engine with full test coverage
