# Research & Decisions Logbook

This document tracks the *why* behind our game design. It includes probability math (Mathhammer), rationale for specific mechanics, and playtest notes.

## Entry 1: Project Kickoff & Core Mechanic Rationale
*Date: 2026-05-09*

### Decision: D6 Pool System
We have opted for a D6 pool system. The goal is to roll lots of dice quickly without the slowdown of opposed rolls. 

**Initial Math Considerations for D6 Pools:**
- If a target number (Target Value or TV) is 4+, each die has a 50% chance of success.
- If a unit rolls 10 dice hitting on 4+, the average number of hits is 5.
- To avoid massive token clutter, we will use D6s as trackers. For instance, a model with 5 Wounds might start with a D6 showing a '5' placed next to it. As it takes damage, the die ticks down.

### Decision: Miniature Agnostic & Scale
To support "bring your own miniatures" (from 1 model to 24 models), we need a robust point-creation system. 
- **Action Economy:** A single powerful model will inherently be at a disadvantage against 24 weak models due to action economy (the weak models can activate more often, secure more objectives, and overwhelm with raw dice volume). We will likely need a system that gives the single model multiple activations or area-of-effect capabilities to compensate.

### Decision: Zone-Based Movement & Location
Rather than traditional free-form movement (measured in inches with a tape measure), the game will use a Zone-based system.
- **Rationale:** Since the game allows any miniatures, traditional true line-of-sight and base-size measurements would create huge balance disparities (a model with a larger base/taller sculpt is easier to hit). Zones abstract this away.
- **Mechanics:** The battlefield is divided into discrete areas (zones). Movement is defined by moving from one zone to an adjacent one. Cover and LoS are predefined by the relationships between these zones, which speeds up gameplay and eliminates arguments over measurements and model heights.

## Entry 2: The Defense Triad & Bag Pull Activation
*Date: 2026-05-09*

### Decision: The Defense Triad
To completely eliminate opposed rolls (which slow down gameplay), we are implementing a "Defense Triad" that modifies incoming attack pools at different mathematical stages:
- **Dodge (Probability Modifier):** Alters the target number. Base attacks hit on a 4+. A model with Dodge 1 forces the attacker to roll 5s. This is incredibly powerful against small dice pools (e.g., snipers) but less effective against swarms of dice.
- **Parry (Flat Reduction):** Subtracts a flat amount of successful hits from Melee attacks before Armor applies. Excellent against swarms of weak attacks that would otherwise force damage through via sheer volume.
- **Armor (Divider):** Divides the total successful hits. `Floor(Hits / Armor) = Wounds`. This ensures big, tough models don't get chipped away instantly by small arms fire unless the attacker concentrates massive fire.

### Decision: Randomized Bag Pull Activation
- **Rationale:** We opted for drawing colored D6s from a bag rather than strictly alternating (I go, you go). This creates tension and fog-of-war without needing complex command-and-control rules. Using D6s matches our core pillar of keeping component requirements minimal (no tokens or cards).

## Entry 3: AP Scaling and Zone Movement
*Date: 2026-05-12*

### Decision: Eliminating the "Speed" Stat via Scaled AP
- **Rationale:** To keep the unit profile clean, we eliminated a dedicated Movement/Speed stat. Instead, we scaled up the average Action Point (AP) pool from 2-3 to 4-6. This allows us to use AP as a highly granular currency for traversing the Zone map.
- **Mechanics:** Moving into an Open Zone costs 2 AP. Difficult Terrain costs 3 AP. This means a standard model with 4 AP can move two Open Zones, but only one Difficult Zone. This creates deep tactical movement choices without measuring tape or complex movement calculations.

### Decision: Scaled Melee and Fall Back Costs
- **Rationale:** Because AP pools are larger, making a Melee Attack costs 2 AP. More importantly, Falling Back (leaving an Engaged Zone) costs 4 AP. This effectively eats an entire turn for an average unit, accurately representing the danger of turning your back in close combat and punishing players who get caught out of position.

### Decision: Multiple Cover Types
- **Rationale:** The Zone system naturally supports Cover without needing to draw lines from bases. We split Cover into Light (+1 Dodge), Heavy (+1 Dodge, +1 Armor), and Obscuring (Blocks LoS) to interact directly with the Defense Triad.

## Entry 4: The Command System
*Date: 2026-05-12*

### Decision: Customized CP Generation
- **Rationale:** Rather than giving everyone the same random or flat CP generation, we moved CP generation into the customization ruleset. This allows players to deeply tie their force's theme into their resource mechanics (e.g., Bloodlust vs. Strategic Control). It forces armies to play to their thematic strengths to fuel their abilities.

### Decision: The Command Card
- **Rationale:** Continuing the "no custom tokens" design pillar, CP is tracked via D6s placed on a dedicated "Command Card." This consolidates all force-wide rules and resources into one clean, manageable spot off the table.
