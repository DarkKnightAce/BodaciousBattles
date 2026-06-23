# Unit Creation & Point Costs

*Draft - Subject to change.*

Bodacious Battles is completely miniature-agnostic. To field an army, you will calculate the point cost of your models using a strict formulaic system. 

The standard game size is **100 Points**. 

## The Formulaic System

Every model in your army starts with a base cost and base profile. You then increase its stats by purchasing them for the listed point cost. Note that because some stats (like Armor or Dodge) drastically increase survivability, their cost scales exponentially. 

In this system, **Army Points** are spent strictly on base stats. Special abilities (Keywords) are purchased using a separate currency called **Perk Points**, which models earn based on their stats and choices.

### Base Cost
Every single model added to your army has a base cost of **15 Points**. This ensures each model is a meaningful portion of the army budget and prevents cheap spamming.

### Base Profile (0 Additional Points)
By paying the base 15 points, the model inherently possesses the following profile:
- **Action Points (AP):** 4
- **Combat (CMB):** 3 (Melee only; Ranged must be purchased as a perk)
- **Wounds (W):** 3
- **Dodge:** 0
- **Parry:** 0
- **Armor:** 1
- **Special Abilities (SPA):** 0

### Upgrading Stats

**Action Points (AP)**
- 5 AP: +10 pts
- 6 AP: +25 pts

**Combat (CMB)**
*Linear cost. Represents base combat capacity (Melee only by default).*
- Each +1 CMB (up to 10): +5 pts per point

**Wounds (W)**
*Linear cost.*
- Each +1 Wound: +5 pts per point

**Dodge**
*Exponential cost. Increases the target number to hit this model.*
- Dodge 1: +10 pts
- Dodge 2: +20 pts
- Dodge 3: +35 pts

**Parry**
*Exponential cost. Flat reduction in successful melee hits taken.*
- Parry 1: +5 pts
- Parry 2: +12 pts
- Parry 3: +25 pts

**Armor**
*Exponential cost. Divider for total incoming hits.*
- Armor 2: +15 pts
- Armor 3: +35 pts
- Armor 4: +60 pts

**Special Abilities (SPA)**
*Linear cost. Represents dedicated slots or capacity for special perks, magic, or advanced equipment.*
- Each +1 SPA (up to 5): +5 pts per point (grants +5 additional Perk Points)

---

## The Perk Point System

Special abilities, equipment, and modifiers are purchased using a pool of **Perk Points** calculated during unit creation. 

### Calculating Your Perk Point Pool
A model's total Perk Point pool is calculated using the following formula:
$$\text{Perk Points} = \text{Total Stat Cost} + (\text{SPA Level} \times 5) + \text{Negative Keyword Bonuses}$$

1. **Stat Cost (1:1 Ratio):** A model receives Perk Points equal to its total point cost spent on base stats (Base Cost + Stat Upgrades).
   * *Example:* A model with a Stat Cost of 33 points automatically earns 33 free Perk Points.
2. **SPA Stat Bonus:** Each level of the **Special Abilities (SPA)** stat costs +5 Army Points (adding +5 to the Stat Cost, which already gives +5 Perk Points) and grants **+5 additional Perk Points**. This yields **+10 total Perk Points** per level of SPA.
   * *Example:* If a model's 33 Stat Cost includes 5 points in SPA (1 level), it earns 33 Perk Points (from Stat Cost) + 5 additional Perk Points (from SPA) = 38 total Perk Points.
3. **Negative Keywords:** Taking a negative keyword (like **Slow** or **Clumsy / Frail**) adds bonus Perk Points directly to your pool to represent sacrifice for capability.

### Spending Perk Points
- Perk Points are spent to purchase positive keywords (Special Abilities) during unit creation.
- A model cannot spend more Perk Points than it has in its pool.
- Any unused Perk Points at the end of unit creation are lost; they cannot be converted back into Army Points.

---

## Boss Models
Balancing a single powerful hero against a swarm of weak enemies is notoriously difficult in alternate-activation games due to the action economy.

To mitigate this, models can purchase the **Boss** keyword upgrade for **30 Perk Points** (representing a massive portion of a model's perk pool). 

**Boss Models** contribute two activation dice to the draw bag instead of one, meaning they will get to activate twice per game round. This allows players to build either a highly active solo character or a high-stat single-activation titan.

