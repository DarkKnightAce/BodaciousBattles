import random
import math

class Unit:
    def __init__(self, name, cmb, w, dodge, parry, armor, frail=False, activations=1, count=1,
                 lethal_strike=False, blast=False, combustible=False,
                 attrition_tiers=None, group=False):
        self.name = name
        self.base_cmb = cmb
        self.w = w
        self.max_w = w
        self.dodge = dodge
        self.parry = parry
        self.armor = armor
        self.frail = frail
        self.activations = activations
        self.count = count
        self.current_wounds = [w] * count
        self.lethal_strike = lethal_strike
        self.blast = blast
        self.combustible = combustible
        self.attrition_tiers = attrition_tiers
        self.group = group

    def is_alive(self):
        return sum(self.current_wounds) > 0

    def active_models(self):
        return sum(1 for w in self.current_wounds if w > 0)

    def reset(self):
        self.current_wounds = [self.max_w] * self.count

    def _get_cmb(self, current_w):
        if self.attrition_tiers is None:
            return self.base_cmb
        if current_w > self.max_w * 2 / 3:
            return self.attrition_tiers[0]
        elif current_w > self.max_w * 1 / 3:
            return self.attrition_tiers[1]
        else:
            return self.attrition_tiers[2]

    def attack(self, target):
        total_damage_dealt = 0
        for _ in range(self.activations):
            active_models = self.active_models()
            if active_models <= 0:
                continue

            for i in range(self.count):
                if self.current_wounds[i] <= 0:
                    continue
                regular_hits = 0
                crit_points = 0
                target_number = min(6, 4 + target.dodge)
                effective_cmb = self._get_cmb(self.current_wounds[i])
                effective_cmb = max(3, effective_cmb)
                for _ in range(effective_cmb):
                    roll = random.randint(1, 6)
                    if roll >= target_number:
                        regular_hits += 1
                        if roll == 6 or (self.lethal_strike and roll >= 5):
                            crit_points += 1

                wounds_regular = 0
                if regular_hits > 0:
                    regular_hits = max(0, regular_hits - target.parry)
                    if regular_hits > 0 and target.frail:
                        regular_hits += 1
                    wounds_regular = math.floor(regular_hits / target.armor)

                total_wounds = wounds_regular
                if total_wounds == 0 and crit_points >= 2:
                    total_wounds = 1

                if total_wounds > 0:
                    target.take_damage(total_wounds)
                    total_damage_dealt += total_wounds

                    if self.blast:
                        self.resolve_blast_splash(target, total_wounds)

            if not target.is_alive():
                return total_damage_dealt

        return total_damage_dealt

    def resolve_blast_splash(self, target, primary_wounds):
        if target.combustible and primary_wounds > 0:
            target.take_damage(1)

        other_active_models = target.active_models()
        if other_active_models > 0:
            splash_targets_count = max(0, other_active_models - 1)
            for _ in range(splash_targets_count):
                hits = 1
                if target.frail:
                    hits += 1
                wounds = math.floor(hits / target.armor)
                if target.combustible and wounds > 0:
                    wounds += 1
                if wounds > 0:
                    target.take_damage(wounds)

    def take_damage(self, amount):
        for i in range(self.count):
            if self.current_wounds[i] > 0:
                if self.current_wounds[i] >= amount:
                    self.current_wounds[i] -= amount
                    amount = 0
                else:
                    amount -= self.current_wounds[i]
                    self.current_wounds[i] = 0
            if amount <= 0:
                break


def simulate_matchup(unit1_template, unit2_template, iterations=1000):
    u1_wins = 0
    u2_wins = 0
    draws = 0

    for _ in range(iterations):
        u1 = Unit(**unit1_template)
        u2 = Unit(**unit2_template)

        rounds = 0
        while u1.is_alive() and u2.is_alive() and rounds < 20:
            u1_clone = Unit(**unit1_template)
            u1_clone.current_wounds = list(u1.current_wounds)

            u2_clone = Unit(**unit2_template)
            u2_clone.current_wounds = list(u2.current_wounds)

            u1_clone.attack(u2)
            u2_clone.attack(u1)

            rounds += 1

        if u1.is_alive() and not u2.is_alive():
            u1_wins += 1
        elif u2.is_alive() and not u1.is_alive():
            u2_wins += 1
        else:
            draws += 1

    return u1_wins, u2_wins, draws


if __name__ == "__main__":
    juggernaut = {
        "name": "Juggernaut", "cmb": 8, "w": 6, "dodge": 0, "parry": 0, "armor": 3,
        "lethal_strike": True, "activations": 2, "count": 1
    }
    sniper_team = {
        "name": "Sniper Team (2)", "cmb": 4, "w": 3, "dodge": 2, "parry": 0, "armor": 1,
        "frail": True, "blast": True, "count": 2
    }
    grunt_v1 = {
        "name": "Grunt V1 (3, Attrition/Group)", "cmb": 5, "w": 5, "dodge": 0, "parry": 0,
        "armor": 1, "lethal_strike": True, "attrition_tiers": [5, 3, 1], "count": 3
    }
    grunt_v2 = {
        "name": "Grunt V2 (6, Baseline+Lethal)", "cmb": 3, "w": 3, "dodge": 0, "parry": 0,
        "armor": 1, "lethal_strike": True, "count": 6
    }
    vanguard_commando = {
        "name": "Vanguard Commando (4)", "cmb": 3, "w": 3, "dodge": 0, "parry": 0, "armor": 1,
        "combustible": True, "count": 4
    }
    cyborg_striker = {
        "name": "Cyborg Striker (4)", "cmb": 3, "w": 3, "dodge": 1, "parry": 0, "armor": 1,
        "lethal_strike": True, "combustible": True, "count": 4
    }
    heavy_specialist = {
        "name": "Heavy Specialist (5)", "cmb": 3, "w": 3, "dodge": 0, "parry": 0, "armor": 1,
        "blast": True, "count": 5
    }

    print("--- 100 Pt Matchups (1000 iterations) ---")
    w1, w2, d = simulate_matchup(juggernaut, sniper_team)
    print(f"Juggernaut vs Sniper Team (2): Jugg={w1}, Snipers={w2}, Draws={d}")

    w1, w2, d = simulate_matchup(juggernaut, grunt_v1)
    print(f"Juggernaut vs Grunt V1 (3): Jugg={w1}, V1={w2}, Draws={d}")

    w1, w2, d = simulate_matchup(juggernaut, grunt_v2)
    print(f"Juggernaut vs Grunt V2 (6): Jugg={w1}, V2={w2}, Draws={d}")

    w1, w2, d = simulate_matchup(sniper_team, grunt_v1)
    print(f"Sniper Team (2) vs Grunt V1 (3): Snipers={w1}, V1={w2}, Draws={d}")

    w1, w2, d = simulate_matchup(sniper_team, grunt_v2)
    print(f"Sniper Team (2) vs Grunt V2 (6): Snipers={w1}, V2={w2}, Draws={d}")

    print("\n--- Medium Force Size (3-7 Models) Matchups ---")
    w1, w2, d = simulate_matchup(vanguard_commando, juggernaut)
    print(f"Vanguard Commando (4) vs Juggernaut: Commandos={w1}, Jugg={w2}, Draws={d}")

    w1, w2, d = simulate_matchup(vanguard_commando, grunt_v1)
    print(f"Vanguard Commando (4) vs Grunt V1 (3): Commandos={w1}, V1={w2}, Draws={d}")

    w1, w2, d = simulate_matchup(cyborg_striker, juggernaut)
    print(f"Cyborg Striker (4) vs Juggernaut: Strikers={w1}, Jugg={w2}, Draws={d}")

    w1, w2, d = simulate_matchup(cyborg_striker, grunt_v1)
    print(f"Cyborg Striker (4) vs Grunt V1 (3): Strikers={w1}, V1={w2}, Draws={d}")

    w1, w2, d = simulate_matchup(heavy_specialist, juggernaut)
    print(f"Heavy Specialist (5) vs Juggernaut: Specialists={w1}, Jugg={w2}, Draws={d}")

    w1, w2, d = simulate_matchup(heavy_specialist, grunt_v1)
    print(f"Heavy Specialist (5) vs Grunt V1 (3): Specialists={w1}, V1={w2}, Draws={d}")

    print("\n--- Swarm Cross-Comparison ---")
    w1, w2, d = simulate_matchup(grunt_v1, grunt_v2)
    print(f"Grunt V1 (3) vs Grunt V2 (6): V1={w1}, V2={w2}, Draws={d}")

    w1, w2, d = simulate_matchup(sniper_team, vanguard_commando)
    print(f"Sniper Team (2) vs Vanguard Commando (4): Snipers={w1}, Commandos={w2}, Draws={d}")

    w1, w2, d = simulate_matchup(cyborg_striker, heavy_specialist)
    print(f"Cyborg Striker (4) vs Heavy Specialist (5): Strikers={w1}, Specialists={w2}, Draws={d}")

    print("\n--- Point Efficiency Verification ---")
    max_damage_boss = {"name": "Max Dmg Boss (~100pts)", "cmb": 10, "w": 10, "dodge": 0, "parry": 0, "armor": 1, "activations": 2, "count": 1}
    max_tank_boss = {"name": "Max Tank Boss (~100pts)", "cmb": 1, "w": 4, "dodge": 0, "parry": 0, "armor": 4, "activations": 2, "count": 1}

    w1, w2, d = simulate_matchup(max_damage_boss, max_tank_boss)
    print(f"Max Dmg Boss vs Max Tank Boss: Dmg={w1}, Tank={w2}, Draws={d}")

    w1, w2, d = simulate_matchup(grunt_v2, max_damage_boss)
    print(f"Grunt V2 (6) vs Max Dmg Boss: V2={w1}, Boss={w2}, Draws={d}")

    w1, w2, d = simulate_matchup(grunt_v2, max_tank_boss)
    print(f"Grunt V2 (6) vs Max Tank Boss: V2={w1}, Boss={w2}, Draws={d}")
