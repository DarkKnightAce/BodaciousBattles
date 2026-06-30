# Combat Resolution

*Draft - Subject to change.*

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
4. **Count Critical Points:** Each natural 6 that is a successful hit generates 1 **Critical Point (CP)**. Models with the **Lethal Strike** keyword also generate 1 CP from successful hits that roll a natural 5. (These are temporary CP spent during this attack resolution).
5. **Apply Armor:** Take the total number of successful Hits and divide it by the target's **Armor** stat (rounding down). *Note: The attacker can spend Critical Points here to reduce the defender's Armor (see Critical Point Options below).*
6. **Deal Wounds:** Apply the final damage to the target. Tick down their Wound tracking die. *Note: The attacker can spend Critical Points here to apply various combat buffs or ensure a minimum damage floor (see Critical Point Options below).*

## Melee Combat
If a model is **Engaged** (occupying the same Zone as an enemy), it cannot make Ranged attacks. It can only make Melee attacks. 

### Resolving a Melee Attack
1. **Spend AP:** The attacker spends 2 AP.
2. **Roll Dice:** The attacker rolls D6s equal to their **Combat (CMB)** stat (minimum 3, per the Rule of 3).
3. **Calculate Hits:** Compare the dice to the target's **Dodge** stat (base 4+ success). Count the successful Hits.
4. **Count Critical Points:** Each natural 6 that is a successful hit generates 1 **Critical Point (CP)**. Models with the **Lethal Strike** keyword also generate 1 CP from successful hits that roll a natural 5. (These are temporary CP spent during this attack resolution).
5. **Apply Parry:** Subtract the target's **Parry** stat from the total number of successful Hits. (e.g., if you rolled 4 Hits, and the target has Parry 1, you now have 3 Hits).
6. **Apply Armor:** Divide the remaining Hits by the target's **Armor** stat (rounding down). *Note: The attacker can spend Critical Points here to reduce the defender's Armor (see Critical Point Options below).*
7. **Deal Wounds:** Apply the final damage to the target. *Note: The attacker can spend Critical Points here to apply various combat buffs or ensure a minimum damage floor (see Critical Point Options below).*

## Attrition & Degrading Combat Power
Models with the **Attrition** keyword become less effective as they take damage. When resolving an attack for an Attrition model, look up its current CMB based on its remaining Wounds rather than using its peak profile value. See the **Attrition** keyword entry for the exact threshold calculation.

## Critical Points & Combat Options
Every successful hit that rolls a natural 6 generates 1 **Critical Point (CP)**. Models with the **Lethal Strike** keyword also generate 1 CP from successful hits that roll a natural 5. 

Unlike force-wide **Command Points (CP)**, Critical Points are temporary resources that must be spent immediately during the resolution of the attack in which they were generated. Unspent Critical Points are lost once the attack resolution finishes.

The active player can spend these Critical Points on the following combat options during attack resolution:

- **Ensured Wound [2 CP]:** If the final damage deals 0 Wounds after resolving Parry and Armor, raise the damage to 1 Wound. (This represents the minimum damage floor; attacks already dealing 1+ Wounds are unaffected).
- **Sunder Armor [1 CP]:** Reduce the target's **Armor** by 1 for this attack (to a minimum of 1). This must be spent before dividing hits in the Apply Armor step.
- **Critical Strike [3 CP]:** If the attack deals 1 or more Wounds, deal 1 additional Wound.
- **Shove [2 CP]:** Push the target model into an adjacent Zone of your choice. If you are Engaged with the target, you may immediately move into that Zone for 0 AP.
- **Concussive Blow [1 CP]:** The target unit has -1 AP on its next activation this round (to a minimum of 3).
- **Sweeping Attack [2 CP]:** Select a different enemy model in the target's Zone. That model suffers 1 Hit (which must be resolved using its own **Armor** stat; **Parry** does not apply).

> [!NOTE]
> **Example — Sunder Armor & Critical Strike:** A Heavy Support Specialist (CMB: 5) fires at a Heavy Tank (Armor: 3).
> - **The Roll:** The Specialist rolls 5 dice: 2, 4, 5, 6, 6.
> - **The Hits:** 4 hits (4, 5, 6, 6).
> - **Critical Points:** Two natural 6s generate 2 CP.
> - **Spending CP:** The attacker spends 1 CP on **Sunder Armor**, reducing the Tank's Armor to 2 for this attack. They have 1 CP remaining.
> - **Resolving Armor:** The 4 Hits are divided by the reduced Armor 2. `4 / 2 = 2 Wounds`.
> - **Result:** The Tank suffers 2 Wounds. (The remaining 1 CP cannot buy any other options and is lost).

> [!NOTE]
> **Example — Minimum Damage Floor (Ensured Wound):** A Grunt Swarm model (CMB: 3) attacks a Juggernaut (Armor: 3).
> - **The Roll:** The Grunt rolls 3 dice: 6, 6, 3.
> - **The Hits:** 2 hits (6, 6).
> - **Critical Points:** Two natural 6s generate 2 CP.
> - **Resolving Armor:** The 2 Hits are divided by Armor 3, rounding down to 0 Wounds.
> - **Spending CP:** The attacker spends 2 CP on **Ensured Wound** to raise the damage to 1 Wound.
> - **Result:** The Juggernaut suffers 1 Wound.

