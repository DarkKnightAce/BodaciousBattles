# Bodacious Battles — Agent Guide

## Project overview
Markdown + Python tabletop game design. No build, test, or CI pipeline.

## Key documents
- `PLAN.md` — master checklist; update when completing tasks
- `docs/rules/` — numbered rulebook (`00_` through `07_`)
- `docs/design/DESIGN_GUIDELINES.md` — core design pillars
- `docs/design/RESEARCH_AND_DECISIONS.md` — log all design decisions here
- `docs/design/01_SAMPLE_UNITS.md` — worked examples of unit builds
- `docs/design/simulate_combat.py` — combat simulator

## Runnable commands
- `python3 docs/design/simulate_combat.py` — runs 1000-iteration matchups

## Formatting conventions
- GFM: blockquotes (`>`) for designer notes/examples; bold for keywords
- Every rule doc starts with `*Draft - Subject to change.*`
- Consistent terms: **Wounds** (not HP), **CMB** (not skill), **AP** (not movement), **Dodge/Parry/Armor** as Defense Triad

## Design constraints
- Miniature-agnostic; D6s as universal trackers (no custom tokens)
- Streamlined speed: no opposed rolls, minimal +1/-1 stacking
- Modular: core rules stay lean; Flying/Magic/Teleport are perk keywords
