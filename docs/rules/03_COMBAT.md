# Combat Resolution

Combat in Bodacious Battles is designed to be fast and lethal, relying entirely on the active player rolling dice against the defender's static stats. There are no opposed rolls.

## Making an Attack
During a unit's activation, it can spend Action Points (AP) to make attacks against enemy units.
- A **Ranged Attack** costs **2 AP** (and requires the **Ranged** keyword).
- A **Melee Attack** costs **2 AP** (available to all models).

## Ranged Combat
If a model is equipped with ranged weaponry (possesses the **Ranged** keyword) and is not **Engaged** (occupying the same Zone as an enemy), it can make Ranged attacks.
To make a Ranged Attack, the attacker must have Line of Sight to the target. Line of Sight is determined by drawing a conceptual line between the attacker's Zone and the target's Zone. 
- If this line crosses an **Obscuring** Cover Zone, the attack cannot be made.
- If the target is standing in a **Light Cover** or **Heavy Cover** Zone, they gain the respective defensive bonuses.

### Resolving a Ranged Attack
1. **Spend AP:** The attacker spends 2 AP.
2. **Roll Dice:** The attacker rolls a number of D6s equal to their **Combat (CMB)** stat (minimum 3, per the Rule of 3).
3. **Calculate Hits:** By default, every die that rolls a **4, 5, or 6** is a Success (a Hit). However, check the target's **Dodge** stat, plus any bonus from Cover.
   - **The Rule of 6 (Maximum Target Value):** The target success number can never be modified to be higher than **6+**. A natural roll of a **6** is always a success, regardless of how much Dodge or Cover the target has. No model can ever be mathematically immune to being hit.
   - *Example:* The target has Dodge 2 and is in Heavy Cover (+1 Dodge). This would normally require a success roll of 7+ to hit. Because of the Rule of 6, the target number is capped, and the attacker still scores hits on rolls of 6.
4. **Count Critical Points:** Each natural 6 that is a successful hit generates 1 **Critical Point (CP)**. Models with the **Lethal Strike** keyword also generate 1 CP from successful hits that roll a natural 5.
5. **Apply Armor:** Take the total number of successful Hits and divide it by the target's **Armor** stat (rounding down). 
6. **Deal Wounds:** Apply the damage. If this number is 0 and the attack generated 2 or more Critical Points, raise it to 1. Tick down their Wound tracking die.

## Melee Combat
If a model is **Engaged** (occupying the same Zone as an enemy), it cannot make Ranged attacks. It can only make Melee attacks. 

### Resolving a Melee Attack
1. **Spend AP:** The attacker spends 2 AP.
2. **Roll Dice:** The attacker rolls D6s equal to their **Combat (CMB)** stat (minimum 3, per the Rule of 3).
3. **Calculate Hits:** Compare the dice to the target's **Dodge** stat (base 4+ success). Count the successful Hits.
4. **Count Critical Points:** Each natural 6 that is a successful hit generates 1 **Critical Point (CP)**. Models with the **Lethal Strike** keyword also generate 1 CP from successful hits that roll a natural 5.
5. **Apply Parry:** Subtract the target's **Parry** stat from the total number of successful Hits. (e.g., if you rolled 4 Hits, and the target has Parry 1, you now have 3 Hits).
6. **Apply Armor:** Divide the remaining Hits by the target's **Armor** stat (rounding down).
7. **Deal Wounds:** Apply the final damage. If this number is 0 and the attack generated 2 or more Critical Points, raise it to 1.

## Attrition & Degrading Combat Power
Models with the **Attrition** keyword become less effective as they take damage. When resolving an attack for an Attrition model, look up its current CMB based on its remaining Wounds rather than using its peak profile value. See the **Attrition** keyword entry for the exact threshold calculation.

## Critical Points & Minimum Damage
Every successful hit that rolls a natural 6 generates 1 **Critical Point (CP)**. Accumulating 2 or more CP during a single attack ensures the attack deals at least 1 Wound, even if heavy Armor or Parry would otherwise absorb all damage. This gives any unit, regardless of its stats, a fighting chance against heavily armored targets.

**Lethal Strike** expands CP generation to natural 5s as well as 6s, making it easier to reach the 2 CP threshold.

> [!NOTE]
> **Example — Minimum Damage in Action:** A Vanguard Commando (CMB: 3) fires at a Juggernaut (Dodge: 0, Armor: 3, Wounds: 6).
> 
> **The Action:** The Commando spends 2 AP to make a Ranged Attack.
> - **The Roll:** The Commando rolls 3 dice: 3, 4, 6.
> - **The Hits:** 2 successful hits (4, 6).
> - **Critical Points:** One natural 6 → 1 CP. The attack needs 2 CP to trigger the minimum.
> - **Armor:** The Juggernaut has Armor 3. We divide the 2 Hits by 3, which equals 0.66. We round down to 0.
> - **Minimum Check:** The attack dealt 0 Wounds, but only generated 1 CP (needs 2). No minimum applies.
> - **Result:** The bullet pings harmlessly off the Juggernaut's armor.

> [!NOTE]
> **Example — Critical Points Reaching Threshold:** A Grunt Swarm model (CMB reduced to 1 by Attrition, raised back to 3 by the Rule of 3) attacks a Heavy Vehicle (Armor: 4).
> 
> **The Action:** The Grunt rolls 3 dice: 6, 6, 3.
> - **The Hits:** 2 successful hits (both 6s).
> - **Critical Points:** Two natural 6s → 2 CP.
> - **Armor:** 2 Hits ÷ Armor 4 = 0 Wounds.
> - **Minimum Check:** 0 Wounds, but 2 CP. The attack deals a minimum of **1 Wound** anyway.
> - **Result:** The grunts land a lucky shot that rattles the vehicle.
