# Design Guidelines

This document outlines the core principles for designing mechanics, writing rules, and balancing for this game.

## Core Pillars
1. **Zone-Based Location & Miniature Agnostic:** Players can use any miniature. Therefore, the game handles model location by zones rather than traditional free-form movement. Zones pre-define movement costs, cover, and line of sight (LoS) to other zones. This simplifies movement, speeds up LoS checks, and completely removes the need for miniature bounding rules while preserving tactical depth.
2. **Small-Scale Skirmish:** Army sizes can be highly asymmetric (e.g., 1 giant vs. 20 minions). Point values must scale exponentially or non-linearly to account for action economy advantages.
3. **Streamlined Speed:** The game should play fast. 
   - No opposed rolls (e.g., Attacker rolls to hit, and that's it, or Attacker rolls to hit and Defender rolls armor saves, but keep it one-sided where possible).
   - Minimal math (avoid +1s and -1s stacking infinitely; prefer rerolls, advantage/disadvantage, or modifying the target number).
4. **D6 Pools & D6 Trackers:** Use D6s for everything. Large dice pools for attacks. Place D6s next to models to track Wounds, Action Points, or status effects, completely eliminating the need for custom tokens or cards.

## Rules Drafting Best Practices
- **Active Voice:** Write rules in the active voice. ("The Attacker rolls 3D6" instead of "3D6 are rolled by the Attacker".)
- **Keyword System:** Use bolded keywords for universal rules (e.g., **Flying**, **Blast**, **Lethal**). This keeps unit profiles clean.
- **Examples:** Always provide a clear, italicized example for complex interactions.

## Modularity ("Hooks")
Design the core rules to be a robust foundation. 
- Example: Ground movement is the core. The hook for other movement types is simply a keyword system in the Movement section (e.g., "A model with the **Fly** keyword ignores vertical distance when moving").
