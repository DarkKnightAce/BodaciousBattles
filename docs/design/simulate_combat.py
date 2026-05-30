import random
import math

class Unit:
    def __init__(self, name, cmb, w, dodge, parry, armor, frail=False, activations=1, count=1,
                 lethal_strike=False, blast=False, combustible=False):
        self.name = name
        self.cmb = cmb
        self.w = w
        self.max_w = w
        self.dodge = dodge
        self.parry = parry
        self.armor = armor
        self.frail = frail
        self.activations = activations
        self.count = count # Number of identical models in this unit
        self.current_wounds = [w] * count
        
        # New modular abilities
        self.lethal_strike = lethal_strike
        self.blast = blast
        self.combustible = combustible

    def is_alive(self):
        return sum(self.current_wounds) > 0
    
    def active_models(self):
        return sum(1 for w in self.current_wounds if w > 0)

    def reset(self):
        self.current_wounds = [self.max_w] * self.count

    def attack(self, target, use_swarm=False):
        total_damage_dealt = 0
        for _ in range(self.activations):
            active_models = self.active_models()
            if active_models <= 0:
                continue
                
            if use_swarm:
                # Swarm Attack: Pool all CMB together into one massive attack
                regular_hits = 0
                lethal_hits = 0
                target_number = min(6, 4 + target.dodge)
                total_cmb = self.cmb * active_models
                for _ in range(total_cmb):
                    roll = random.randint(1, 6)
                    if roll == 6 and self.lethal_strike:
                        lethal_hits += 1
                    elif roll >= target_number:
                        regular_hits += 1
                
                # Resolve regular hits
                wounds_regular = 0
                if regular_hits > 0:
                    regular_hits = max(0, regular_hits - target.parry)
                    if regular_hits > 0 and target.frail:
                        regular_hits += 1
                    wounds_regular = math.floor(regular_hits / target.armor)
                
                # Resolve lethal hits (ignore Parry and Armor)
                wounds_lethal = lethal_hits
                
                total_wounds = wounds_regular + wounds_lethal
                
                if total_wounds > 0:
                    target.take_damage(total_wounds)
                    total_damage_dealt += total_wounds
                    
                    # Apply Blast splash damage
                    if self.blast:
                        self.resolve_blast_splash(target, total_wounds)
            else:
                # Individual Attacks
                for i in range(self.count):
                    if self.current_wounds[i] <= 0:
                        continue
                    regular_hits = 0
                    lethal_hits = 0
                    target_number = min(6, 4 + target.dodge)
                    for _ in range(self.cmb):
                        roll = random.randint(1, 6)
                        if roll == 6 and self.lethal_strike:
                            lethal_hits += 1
                        elif roll >= target_number:
                            regular_hits += 1
                    
                    # Resolve regular hits
                    wounds_regular = 0
                    if regular_hits > 0:
                        regular_hits = max(0, regular_hits - target.parry)
                        if regular_hits > 0 and target.frail:
                            regular_hits += 1
                        wounds_regular = math.floor(regular_hits / target.armor)
                    
                    # Resolve lethal hits (ignore Parry and Armor)
                    wounds_lethal = lethal_hits
                    
                    total_wounds = wounds_regular + wounds_lethal
                    if total_wounds > 0:
                        target.take_damage(total_wounds)
                        total_damage_dealt += total_wounds
                        
                        # Apply Blast splash damage
                        if self.blast:
                            self.resolve_blast_splash(target, total_wounds)
                            
            if not target.is_alive():
                return total_damage_dealt

        return total_damage_dealt

    def resolve_blast_splash(self, target, primary_wounds):
        # Target takes 1 additional wound if Combustible and damaged
        if target.combustible and primary_wounds > 0:
            target.take_damage(1)
            
        # Blast splash automatically hits all OTHER active models in the zone
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


def simulate_matchup(unit1_template, unit2_template, iterations=1000, u1_swarm=False, u2_swarm=False):
    u1_wins = 0
    u2_wins = 0
    draws = 0

    for _ in range(iterations):
        u1 = Unit(**unit1_template)
        u2 = Unit(**unit2_template)
        
        rounds = 0
        while u1.is_alive() and u2.is_alive() and rounds < 20:
            # Simultaneous combat for simplicity in evaluating raw stat efficiency
            u1_clone = Unit(**unit1_template)
            u1_clone.current_wounds = list(u1.current_wounds)
            
            u2_clone = Unit(**unit2_template)
            u2_clone.current_wounds = list(u2.current_wounds)
            
            u1_clone.attack(u2, use_swarm=u1_swarm)
            u2_clone.attack(u1, use_swarm=u2_swarm)
            
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
        "name": "Sniper Team (2)", "cmb": 4, "w": 2, "dodge": 2, "parry": 0, "armor": 1, 
        "frail": True, "blast": True, "count": 2
    }
    grunt_swarm_100 = {
        "name": "Grunt Swarm (20)", "cmb": 1, "w": 1, "dodge": 0, "parry": 0, "armor": 1, 
        "lethal_strike": True, "count": 20
    }
    
    # New Medium-Sized Units (3-7 models)
    vanguard_commando = {
        "name": "Vanguard Commando (5)", "cmb": 2, "w": 1, "dodge": 0, "parry": 0, "armor": 1, 
        "combustible": True, "count": 5
    }
    cyborg_striker = {
        "name": "Cyborg Striker (4)", "cmb": 3, "w": 1, "dodge": 1, "parry": 0, "armor": 1, 
        "lethal_strike": True, "combustible": True, "count": 4
    }
    heavy_specialist = {
        "name": "Heavy Specialist (5)", "cmb": 2, "w": 2, "dodge": 0, "parry": 0, "armor": 1, 
        "blast": True, "count": 5
    }
    
    print("--- 100 Pt Matchups (1000 iterations) ---")
    w1, w2, d = simulate_matchup(juggernaut, sniper_team)
    print(f"Juggernaut vs Sniper Team (2): Jugg={w1}, Snipers={w2}, Draws={d}")
    
    w1, w2, d = simulate_matchup(juggernaut, grunt_swarm_100) # Grunts have Solitary, no swarm attack
    print(f"Juggernaut vs Grunt Swarm (20): Jugg={w1}, Swarm={w2}, Draws={d}")

    w1, w2, d = simulate_matchup(sniper_team, grunt_swarm_100)
    print(f"Sniper Team (2) vs Grunt Swarm (20): Snipers={w1}, Swarm={w2}, Draws={d}")
    
    print("\n--- Medium Force Size (3-7 Models) Matchups ---")
    w1, w2, d = simulate_matchup(vanguard_commando, juggernaut)
    print(f"Vanguard Commando (5) vs Juggernaut: Commandos={w1}, Jugg={w2}, Draws={d}")
    
    w1, w2, d = simulate_matchup(vanguard_commando, grunt_swarm_100)
    print(f"Vanguard Commando (5) vs Grunt Swarm (20): Commandos={w1}, Swarm={w2}, Draws={d}")

    w1, w2, d = simulate_matchup(cyborg_striker, juggernaut)
    print(f"Cyborg Striker (4) vs Juggernaut: Strikers={w1}, Jugg={w2}, Draws={d}")
    
    w1, w2, d = simulate_matchup(cyborg_striker, grunt_swarm_100)
    print(f"Cyborg Striker (4) vs Grunt Swarm (20): Strikers={w1}, Swarm={w2}, Draws={d}")
    
    w1, w2, d = simulate_matchup(heavy_specialist, juggernaut)
    print(f"Heavy Specialist (5) vs Juggernaut: Specialists={w1}, Jugg={w2}, Draws={d}")
    
    w1, w2, d = simulate_matchup(heavy_specialist, grunt_swarm_100)
    print(f"Heavy Specialist (5) vs Grunt Swarm (20): Specialists={w1}, Swarm={w2}, Draws={d}")

    print("\n--- Point Efficiency Verification ---")
    baseline_20 = {"name": "Baseline (20 models, 100pts)", "cmb": 1, "w": 1, "dodge": 0, "parry": 0, "armor": 1, "count": 20}
    max_damage_boss = {"name": "Max Dmg Boss (~100pts)", "cmb": 10, "w": 10, "dodge": 0, "parry": 0, "armor": 1, "activations": 2, "count": 1}
    max_tank_boss = {"name": "Max Tank Boss (~100pts)", "cmb": 1, "w": 4, "dodge": 0, "parry": 0, "armor": 4, "activations": 2, "count": 1}
    
    w1, w2, d = simulate_matchup(baseline_20, max_damage_boss)
    print(f"Baseline (20) vs Max Dmg Boss: Base={w1}, Boss={w2}, Draws={d}")

    w1, w2, d = simulate_matchup(baseline_20, max_tank_boss)
    print(f"Baseline (20) vs Max Tank Boss: Base={w1}, Boss={w2}, Draws={d}")
