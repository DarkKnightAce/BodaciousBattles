import random
import math

class Unit:
    def __init__(self, name, cmb, w, dodge, parry, armor, frail=False, activations=1, count=1):
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
                hits = 0
                target_number = min(6, 4 + target.dodge)
                total_cmb = self.cmb * active_models
                for _ in range(total_cmb):
                    roll = random.randint(1, 6)
                    if roll >= target_number:
                        hits += 1
                
                if hits > 0:
                    hits = max(0, hits - target.parry)
                    if hits > 0 and target.frail:
                        hits += 1
                    wounds_dealt = math.floor(hits / target.armor)
                    if wounds_dealt > 0:
                        target.take_damage(wounds_dealt)
                        total_damage_dealt += wounds_dealt
            else:
                # Individual Attacks
                for i in range(self.count):
                    if self.current_wounds[i] <= 0:
                        continue
                    hits = 0
                    target_number = min(6, 4 + target.dodge)
                    for _ in range(self.cmb):
                        roll = random.randint(1, 6)
                        if roll >= target_number:
                            hits += 1
                    
                    if hits > 0:
                        hits = max(0, hits - target.parry)
                        if hits > 0 and target.frail:
                            hits += 1
                        wounds_dealt = math.floor(hits / target.armor)
                        if wounds_dealt > 0:
                            target.take_damage(wounds_dealt)
                            total_damage_dealt += wounds_dealt
                            
            if not target.is_alive():
                return total_damage_dealt

        return total_damage_dealt

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
    juggernaut = {"name": "Juggernaut", "cmb": 6, "w": 6, "dodge": 0, "parry": 0, "armor": 3, "activations": 2, "count": 1}
    sniper_team = {"name": "Sniper Team", "cmb": 4, "w": 2, "dodge": 2, "parry": 0, "armor": 1, "frail": True, "count": 3}
    grunt_swarm = {"name": "Grunt Swarm", "cmb": 1, "w": 1, "dodge": 0, "parry": 0, "armor": 1, "count": 10} # 10 grunts is 50 pts, let's use 20 for 100pts
    grunt_swarm_100 = {"name": "Grunt Swarm (20)", "cmb": 1, "w": 1, "dodge": 0, "parry": 0, "armor": 1, "count": 20}
    
    print("--- 100 Pt Matchups (1000 iterations) ---")
    w1, w2, d = simulate_matchup(juggernaut, sniper_team)
    print(f"Juggernaut vs Sniper Team: Jugg={w1}, Snipers={w2}, Draws={d}")
    
    w1, w2, d = simulate_matchup(juggernaut, grunt_swarm_100, u2_swarm=True)
    print(f"Juggernaut vs Grunt Swarm (20) [SWARM ATTACK]: Jugg={w1}, Swarm={w2}, Draws={d}")

    w1, w2, d = simulate_matchup(sniper_team, grunt_swarm_100)
    print(f"Sniper Team vs Grunt Swarm (20): Snipers={w1}, Swarm={w2}, Draws={d}")
    
    print("\n--- Point Efficiency Verification ---")
    # Base baseline unit (5 pts) vs Max Stat unit
    # Base: AP 4, CMB 1, W 1, Dodge 0, Parry 0, Armor 1
    # Max: CMB 10 (+45pts), W 10 (+45pts) = 95 pts total (approx 100 pts)
    baseline_20 = {"name": "Baseline (20 models, 100pts)", "cmb": 1, "w": 1, "dodge": 0, "parry": 0, "armor": 1, "count": 20}
    max_damage_boss = {"name": "Max Dmg Boss (~100pts)", "cmb": 10, "w": 10, "dodge": 0, "parry": 0, "armor": 1, "activations": 2, "count": 1}
    max_tank_boss = {"name": "Max Tank Boss (~100pts)", "cmb": 1, "w": 4, "dodge": 0, "parry": 0, "armor": 4, "activations": 2, "count": 1}
    
    w1, w2, d = simulate_matchup(baseline_20, max_damage_boss)
    print(f"Baseline (20) vs Max Dmg Boss: Base={w1}, Boss={w2}, Draws={d}")

    w1, w2, d = simulate_matchup(baseline_20, max_tank_boss)
    print(f"Baseline (20) vs Max Tank Boss: Base={w1}, Boss={w2}, Draws={d}")
