# Agent Guidelines (AGENTS.md)

This document provides rules and constraints for AI agents (and human contributors) interacting with this repository.

## 1. Project Management
- **Follow the PLAN.md:** Always check the top-level `PLAN.md` file to see current progress, next steps, and priorities.
- **Update the PLAN.md:** When completing a task, ensure the checkbox in `PLAN.md` is ticked `[x]`. Do not skip phases unless instructed by the user.

## 2. Design Process
- **Record Decisions:** Any significant design choice, mechanical change, or mathematical probability calculation must be documented in `docs/design/RESEARCH_AND_DECISIONS.md`.
- **Modularity:** Ensure the base system remains streamlined. Any complex rule (like Flying, Magic, Teleportation) should be built as a modular add-on rather than baked into the core engine.

## 3. Markdown Formatting
- Use standard GitHub Flavored Markdown (GFM).
- Use clear headers (`#`, `##`, `###`) to structure rules text logically.
- Use blockquotes (`>`) to denote designer notes or examples within rules documents.
- Maintain consistent terminology (e.g., if a unit has "Wounds", always capitalize it as "Wounds", not "HP" or "health").

## 4. Agnosticism
- Remember that the game is miniature-agnostic. Do not write rules that require a specific physical miniature or proprietary component (like a specific faction's tokens).
- Use D6s as the universal tracker for game states where possible.
