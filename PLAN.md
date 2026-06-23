# Bodacious Battles Development Plan

This document serves as the master checklist for developing the tabletop miniature game. 
It must be updated as tasks are started or completed.

## Phase 1: Project Initialization
- [x] Establish directory structure (`docs/rules`, `docs/design`, `docs/best_practices`).
- [x] Create `PLAN.md`.
- [x] Draft `AGENTS.md` and `DESIGN_GUIDELINES.md`.
- [x] Setup `RESEARCH_AND_DECISIONS.md`.
- [x] Create skeleton rules files (`00_CORE_CONCEPTS.md`, `01_TURN_STRUCTURE.md`).

## Phase 2: Core Mechanics Concepting
- [x] Define the D6 dice pool mechanic (success numbers, exploding dice, etc.).
- [x] Establish how models use D6s as trackers (e.g., for Wounds, Action Points).
- [x] Define the base unit profile/stats block.
- [x] Draft `00_CORE_CONCEPTS.md` and `01_TURN_STRUCTURE.md`.

## Phase 3: Action & Combat Resolution
- [x] Design Movement rules (base ground movement, measuring tools, terrain).
- [x] Design Shooting/Ranged Combat (line of sight, cover, hit/wound rolls).
- [x] Design Melee Combat (engaging, striking, breaking off).
- [x] Log math/probabilities in `RESEARCH_AND_DECISIONS.md`.

## Phase 4: The Command System
- [x] Design Command Point (CP) generation mechanics.
- [x] Define how CP is tracked (e.g., Command Card).
- [x] Draft example thematic force-wide abilities.
- [x] Draft `04_COMMAND_SYSTEM.md`.

## Phase 5: Factions, Units, & Customization Ruleset
- [x] Create Unit Creation / Point Cost framework.
- [x] Design hooks for modular complexity (e.g., Flying, Teleportation, Magic).
- [x] Draft 2-3 sample diverse units (e.g., 1 strong hero vs 10 weak grunts) for testing.
- [x] Draft 1-2 scenarios/missions.

## Phase 6: Playtesting Prep & Tweaks
- [x] Rework Unit Creation to use the new **Perk Point** system (points spent on stats, perks spent on abilities).
- [x] Clarify ranged attack acquisition (must purchase the **Ranged** keyword) and mechanics.
- [x] Correct point cost math in `01_SAMPLE_UNITS.md` (specifically the Sniper Team math error).
- [x] Create 3 new medium-sized sample units (3-7 models) to address extreme size bias in playtesting.
- [x] Log design decisions and math considerations in `RESEARCH_AND_DECISIONS.md`.

## Phase 7: Playtesting & Iteration
- [x] Run simulated combats with new medium units.
- [x] Balance unit costs and test mechanics.
- [x] Refine rules phrasing for clarity and edge-cases.

## Phase 8: Base Cost Rework & Attrition/Group System
- [x] Increase base cost to 15 pts and base profile to CMB 3 / W 3 in `05_UNIT_CREATION.md`.
- [x] Add **Attrition** (negative keyword) and **Group** (positive keyword) to `06_MODULAR_ABILITIES.md`.
- [x] Remove Swarm Attack mechanic from `03_COMBAT.md`; reference Attrition in combat resolution.
- [x] Log design rationale in `RESEARCH_AND_DECISIONS.md` (Entry 6).
- [x] Recalculate all sample units in `01_SAMPLE_UNITS.md` with new base cost/profile.
- [x] Add two Grunt Swarm variants (V1: Attrition+Group, V2: cheapest baseline) for testing.
- [x] Update `simulate_combat.py` with Attrition support; run matchups.
- [x] Retire **Solitary** keyword (no longer needed after Swarm Attack removal).

## Phase 9: Critical Point System & Rule of 3
- [x] Add **Rule of 3** (minimum pool of 3 dice) to `00_CORE_CONCEPTS.md`.
- [x] Add **Critical Point** generation and minimum damage floor to Ranged and Melee resolution in `03_COMBAT.md`.
- [x] Rewrite **Lethal Strike** to generate CP on 5+ instead of bypassing armor on 6s.
- [x] Log design rationale in `RESEARCH_AND_DECISIONS.md` (Entry 7).
- [x] Update `simulate_combat.py` with CP tracking, Rule of 3 enforcement, and new LS behavior; run matchups.

