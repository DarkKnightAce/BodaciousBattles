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

## Entry 5: Playtesting Prep & Perk Points Rework
*Date: 2026-05-30*

### Decision: The Perk Points System
- **Rationale:** Previously, custom abilities directly added or subtracted from the model's Army Points cost. This made point calculations confusing and created weird scaling, such as Sniper Team math errors. By decoupling stats (purchased with Army Points) from abilities (purchased with a secondary Perk Point currency), we create a highly clean and modular build system.
- **Mechanics:** Models earn Perk Points on a **1:1 ratio** with their total Stat Cost. This means larger, more expensive models naturally have a larger capacity to slot in thematic, complex keywords, making them feel like true heroic characters.
- **The Special Abilities (SPA) Stat:** We added a dedicated SPA stat (+5 Army Points per level). Each level grants +5 additional Perk Points (on top of the 5 points added to the Stat Cost, for +10 total Perk Points). This gives players a dedicated channel to buy lots of special abilities/keywords without inflating physical stats like Wounds or Armor.

### Decision: Ranged Weapon Acquisition (The Ranged Keyword)
- **Rationale:** In earlier drafts, CMB represented both melee and ranged attacks automatically. This meant a wild beast or a swordsman could shoot by default, which broke immersion and balance. Ranged combat is now an acquired ability costing **10 Perk Points**. Units must dedicate a portion of their perk pool to shoot, which clearly defines pure melee, pure ranged, and hybrid units.

### Decision: Boss Keyword as a Paid Perk
- **Rationale:** Under the original passive rules, any model costing over 33 points automatically became a "Boss" and activated twice per round. This restricted player agency and forced tanky but low-activation giants into the Boss role. Decoupling this allows players to choose: they can spend **30 Perk Points** to purchase the Boss keyword, or they can build a 50+ point "golem" that only activates once but has massive base stats.

### Decision: Introducing Medium-Sized Units (3-7 Models)
- **Rationale:** Simulation data showed that extremes (1 giant Boss or 20 cheap Grunts) dominated matchups, while middle-sized units were poorly represented or tested. We designed three new mid-size sample units (Vanguard Commandos, Cyborg Strikers, and Heavy Support Specialists) ranging from 16 to 25 points each. This creates a healthy testing spectrum (4-6 models per 100-point army) to evaluate tactical flexibility, movement capabilities (Flying, Teleporting), and area-denial (Blast mortars) against the extreme swarms and single boss titans.

---

## Entry 6: Base Cost Rework & Attrition/Group System
*Date: 2026-05-31*

### Decision: Base Cost and Profile Increase

**Problem:** Simulation data confirmed that swarms of ultra-cheap models (5 pts each, 20 per 100pt army) were too effective due to action economy advantage — more activation dice, more bodies on objectives, and high dice volume that overwhelmed Defense Triad math.

**Solution:** Raise the base cost from 5 to **15 points** and increase the base profile from CMB 1 / W 1 to **CMB 3 / W 3**. This achieves three goals:
1. **Hard cap on spam:** Max swarm size drops from 20 to 6 models per 100 pts.
2. **Every model is meaningful:** Base CMB 3 means even the cheapest model rolls 3 dice, making individual models feel impactful.
3. **Fewer activation dice:** Smaller armies mean the bag pull goes faster and single-model bosses have a fairer activation share.

**Math verification:** The 5 → 15 cost change combined with +2 free CMB and +2 free Wounds means most unit costs shifted slightly (Juggernaut 100 → 100 with AP 5 bump, Snipers 50 → 45, etc.). The key metric: 6 baseline models × 15 pts = 90 pts, leaving 10 for force upgrades, versus the old 20 models for 100 pts.

### Decision: Attrition Keyword (Negative, +15 PP)

**Rationale:** Previously, swarm units either fought at full strength until the last model died, or required tedious per-model tracking. Attrition provides a clean, single-die tracking mechanism where a model's combat output degrades as it takes damage. The 3-tier breakpoint system (top/middle/bottom thirds of max Wounds) gives a natural-feeling power curve.

**Mechanics:**
- Model defines 3 CMB values at thresholds: > 2/3 max, > 1/3 max, ≤ 1/3 max
- Player always uses the CMB matching current remaining Wounds
- +15 PP grant reflects the drawback of predictable degradation

### Decision: Group Keyword (Positive, 15 PP, requires Attrition)

**Rationale:** To give swarm players tactical flexibility despite having fewer individual models, Group allows splitting a high-Wound model during activation. The Attrition requirement ensures split pieces are appropriately weaker (each has fewer Wounds → lower CMB tier). This creates a genuine trade-off: more board presence vs. less killing power per piece.

**Mechanics:**
- Requires Attrition
- During activation, model splits into 2+ models, dividing current Wounds
- Each new model inherits Attrition and calculates CMB from its individual Wounds

### Decision: Swarm Attack Removed

**Rationale:** The Swarm Attack mechanic (pooling CMB of multiple models into one attack) existed to help weak units pierce high Armor. With Attrition models starting at higher peak CMB and naturally degrading, Swarm Attack is no longer needed. The new base CMB 3 ensures even cheap models can threaten armored targets without special pooling rules.

### Decision: Solitary Keyword Removed

**Rationale:** Solitary only existed to prevent units from using Swarm Attack. With Swarm Attack removed, Solitary has no mechanical function and is retired.

---

## Entry 7: Critical Point System & Rule of 3
*Date: 2026-05-31*

### Problem: Invincible Armor
Simulation data showed that units without Lethal Strike had 0% win probability against Armor 3+ targets (e.g., Vanguard Commandos vs Juggernaut). This created deterministic, uninteresting matchups where certain unit types were mathematically incapable of damaging others.

### Decision: Critical Points (CP) as a Minimum Damage Floor

**Mechanics:**
- Each natural 6 that is a successful hit generates 1 Critical Point (CP)
- If an attack deals 0 Wounds after regular damage resolution but generated 2+ CP, the damage is raised to 1
- This is a minimum floor, not bonus damage — attacks already dealing 1+ Wounds are unaffected

**Rationale:** Using CP as a floor rather than bonus damage specifically helps the units that need it most (low-CMB units facing high Armor) without inflating damage for units that are already effective. The 2 CP threshold means a baseline CMB 3 model has approximately 7.4% chance per attack to trigger the floor — enough to make matchups non-deterministic without trivializing Armor as a stat.

### Decision: Lethal Strike Rewritten to Enhance CP

**Old behavior:** 6s bypass Parry and Armor (melee only, 10 PP)
**New behavior:** 5s also generate CP (all attacks, 10 PP same cost)

This makes Lethal Strike a force multiplier for the CP system rather than the sole method of bypassing Armor. A model with LS generates CP from 5+ instead of 6-only, roughly doubling its CP output (33% per die vs 17% per die), making the 2 CP threshold reachable at lower CMB values.

### Decision: Rule of 3 (Minimum Pool)

A companion to the existing Rule of 4 and Rule of 6. Every attack pool has a minimum of 3 dice, preventing Attrition or negative keywords from reducing a model to irrelevance. This ensures the CP system has enough dice to work with even for degraded units.

---

## Entry 8: Thematic Command Abilities Expansion
*Date: 2026-06-22*

### Decision: Expand Command Abilities List (12 Options Across Genres)
- **Problem:** The original rules had only 3 basic examples of Thematic Abilities, offering little diversity for players to build their custom armies. Players building sci-fi, horror, or magical factions needed standard mechanical baselines to reference or adopt.
- **Solution:** Designed 12 diverse thematic abilities grouped across 6 genres (Sci-Fi, Fantasy, Weird War, Post-Apocalyptic, Gothic Horror, and Steampunk).
- **Core Design Alignment:**
  - **No Opposed Rolls:** None of the abilities require target reaction rolls. For example, **Rad-Burst** asks the victim to roll a simple D6 check directly, and **Grip of Terror** applies a flat AP penalty.
  - **Keyword Synergy:** Leveraging existing keywords like **Teleport** (for **Phase Shift**), **Armor** (for **Overcharge Weapons** and **Arcane Shield**), **Hazardous Zone** (for **Artillery Barrage**), and **Attrition** (for healing units).
  - **Resource Economy:** Costs are scaled between 1 CP and 5 CP. Higher-impact actions like summoning units or resurrecting dead ones require substantial pools (5 CP), while utility effects (like ignoring cover or gaining net CP) are cheap (1-2 CP) to keep decision-making dynamic.

---

## Entry 9: Critical Point Combat Options Design Rationale
*Date: 2026-06-22*

### Decision: Expand Critical Point (CP) Options with 6 New Abilities
- **Problem:** While the minimum damage floor (Ensured Wound) solved the problem of invincible high-Armor units, it offered only one binary use for Critical Points generated during attack rolls. Attacks that naturally dealt damage but rolled multiple 6s had no way to spend their CP, wasting critical successes.
- **Solution:** Added 6 new combat options for spending CP, offering a range of utility and tactical trade-offs:
  - **Damage & Armor Manipulation:** *Sunder Armor [1 CP]* offers a cost-effective way to crack medium armor when you have lots of normal hits, while *Critical Strike [3 CP]* rewards rolls that successfully pierce defense with raw extra damage.
  - **Crowd Control & Movement:** *Shove [2 CP]* utilizes the Zone system to reposition enemies or disengage for free. *Concussive Blow [1 CP]* disrupts the opponent's action economy by draining their AP for the round.
  - **Status & Area Damage:** *Bleeding Wound [2 CP]* introduces delayed damage tracked with a D6 on their card, and *Sweeping Attack [2 CP]* allows split hits to damage adjacent models without rolling separate attack sequences.
- **Key Design Principles Maintained:**
  - **Immediate Resource Use:** These Critical Points remain non-persistent, generating and expiring within a single attack resolution. This avoids the bookkeeping of carrying points across phases or turns.
  - **Opposed Roll Avoidance:** None of the new options require the defender to roll saves or resistance checks; the attacker spends their generated successes directly to apply the effects, maintaining rapid, one-sided combat resolution.

---

## Entry 10: Sample Army Command System Synergy
*Date: 2026-06-22*

### Decision: Assign Thematic Command Configurations to Sample Units
- **Problem:** The newly expanded Command System (specifically CP Generation Mechanics and Thematic Abilities) needed concrete examples of playstyle synergy integrated within the existing sample unit rosters.
- **Solution:** Assigned specific Command Generation Mechanics and two Thematic Abilities to each of the 7 sample unit/army profiles, creating functional and thematic builds:
  - **The Juggernaut (Solo Boss):** Assigned **Inspiring Leadership** (allowing the boss to act as its own CP engine) combined with *Steam Overdrive* (for out-of-turn burst melee attacks) and *Nanite Reconstruction* (for critical self-healing to maintain its 100-point presence).
  - **Sniper Team (Cover Marksmen):** Assigned **Strategic Control** (rewards covering key zones) with *Smoke Screen* (defensive obscurity) and *Overcharge Weapons* (armor piercing sniper fire).
  - **Grunt Swarms (Horde Swarms):** Assigned **Swarm Intelligence** (scales CP generation with model count, synergizing with *Group* splitting) with *Necrotic Resurrection* (to recycle casualty models) and *Alchemical Mutagen* (for sudden horde combat surges).
  - **Vanguard Commando (Fast Recon):** Assigned **Strategic Control** (capitalizes on quick Vanguard zone captures) with *Tactical Infiltration* (free repositioning without paying Fall Back costs) and *Smoke Screen* (advance cover).
  - **Cyborg Striker (Teleporting Assassins):** Assigned **Bloodlust** (rewards surgical kills) with *Phase Shift* (increased blink availability) and *Grip of Terror* (restricting target AP).
  - **Heavy Support Specialist (Stationary Defense):** Assigned **Strategic Control** (securing areas with mortar fire) with *Artillery Barrage* (creating Hazardous Zones) and *Nanite Reconstruction* (repairing stationary specialists).
- **Synergy Alignment:** These configurations demonstrate how players can choose mechanics and abilities that mathematically and thematic scale with their army sizes and archetypes (e.g. Swarm Intelligence for high model counts, Inspiring Leadership for single elite bosses).


