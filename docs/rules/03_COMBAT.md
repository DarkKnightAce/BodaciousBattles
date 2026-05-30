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
2. **Roll Dice:** The attacker rolls a number of D6s equal to their **Combat (CMB)** stat.
3. **Calculate Hits:** By default, every die that rolls a **4, 5, or 6** is a Success (a Hit). However, check the target's **Dodge** stat, plus any bonus from Cover.
   - **The Rule of 6 (Maximum Target Value):** The target success number can never be modified to be higher than **6+**. A natural roll of a **6** is always a success, regardless of how much Dodge or Cover the target has. No model can ever be mathematically immune to being hit.
   - *Example:* The target has Dodge 2 and is in Heavy Cover (+1 Dodge). This would normally require a success roll of 7+ to hit. Because of the Rule of 6, the target number is capped, and the attacker still scores hits on rolls of 6.
4. **Apply Armor:** Take the total number of successful Hits and divide it by the target's **Armor** stat (rounding down). 
5. **Deal Wounds:** The final number is the amount of Wounds the target takes. Tick down their Wound tracking die.

## Melee Combat
If a model is **Engaged** (occupying the same Zone as an enemy), it cannot make Ranged attacks. It can only make Melee attacks. 

### Resolving a Melee Attack
1. **Spend AP:** The attacker spends 2 AP.
2. **Roll Dice:** The attacker rolls D6s equal to their **Combat (CMB)** stat.
3. **Calculate Hits:** Compare the dice to the target's **Dodge** stat (base 4+ success). Count the successful Hits.
4. **Apply Parry:** Subtract the target's **Parry** stat from the total number of successful Hits. (e.g., if you rolled 4 Hits, and the target has Parry 1, you now have 3 Hits).
5. **Apply Armor:** Divide the remaining Hits by the target's **Armor** stat (rounding down).
6. **Deal Wounds:** Apply the final damage.

## The Swarm Attack Mechanic
Because Armor divides incoming hits on a per-attack basis, heavily armored targets are virtually immune to scattered, weak attacks. To overcome this, infantry must fight as a coordinated unit.

If multiple models from the same unit have Line of Sight to a target (for Ranged Attacks) or are Engaged with the target (for Melee Attacks), they may declare a **Swarm Attack**.

### Resolving a Swarm Attack
1. **Spend AP:** Each participating model must spend 2 AP simultaneously.
2. **Pool Dice:** Combine the **Combat (CMB)** stat of all participating models into one single, massive dice pool.
3. **Roll & Resolve:** Roll this massive pool as a single attack. Because it is resolved as one attack, the target's Parry and Armor are only applied *once* to the grand total of hits, allowing sheer volume to overwhelm thick armor plating.

## Step-by-Step Combat Example
> [!NOTE]
> **The Scenario:** A Cyborg Ninja (CMB: 8) charges into a Zone to engage a Heavy Mech (Dodge: 0, Parry: 0, Armor: 3, Wounds: 6).
> 
> **The Action:** The Ninja spends 2 AP to make a Melee Attack.
> - **The Roll:** The Ninja rolls 8 dice. Because the Mech has Dodge 0, the Ninja needs 4+ to hit. The dice land: 1, 2, 3, 4, 4, 5, 5, 6.
> - **The Hits:** That's 5 successful Hits.
> - **Parry:** The Mech has 0 Parry, so all 5 Hits go through.
> - **Armor:** The Mech has Armor 3. We divide the 5 Hits by 3, which equals 1.66. We round down to 1.
> - **Result:** The Heavy Mech's massive plating absorbs most of the flurry, and it takes 1 Wound. Its tracker is turned down to 5.
