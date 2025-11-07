import random
from faker import Faker
import pandas as pd
from datetime import datetime, timedelta

fake = Faker('it_IT')
Faker.seed(42)
random.seed(42)

# ===========================
# CONFIG
# ===========================
NUM_TEAMS = 10
USERS_PER_TEAM = 10
NUM_USERS = NUM_TEAMS * USERS_PER_TEAM
DAYS_HISTORY = 30  # giorni di attività simulata

# ===========================
# 1️⃣ TEAMS
# ===========================
teams = []
for i in range(NUM_TEAMS):
    teams.append({
        "id": i + 1,
        "name": f"Team {fake.color_name()}",
        "office_name": f"Ufficio {fake.city()}",
        "created_at": fake.date_time_this_year()
    })
teams_df = pd.DataFrame(teams)

# ===========================
# 2️⃣ USERS
# ===========================
users = []
for i in range(NUM_USERS):
    team_id = (i // USERS_PER_TEAM) + 1
    users.append({
        "id": i + 1,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.unique.email(),
        "password_hash": fake.sha256(raw_output=False),
        "phone": fake.phone_number(),
        "team_id": team_id,
        "streak_days": random.randint(0, 15),
        "created_at": fake.date_time_this_year(),
        "updated_at": datetime.now()
    })
users_df = pd.DataFrame(users)

# ===========================
# 3️⃣ ACTION TYPES
# ===========================
action_types_data = [
    # Individual actions
    ("sustainable_commute", "Chilometraggio con mezzi sostenibili", "individual", "km", "more_is_better", 2),
    ("idle_minutes", "Minuti di inattività computer", "individual", "minutes", "less_is_better", 1),
    ("daily_prints", "Numero stampe giornaliere", "individual", "count", "less_is_better", 2),
    ("meal_co2", "CO2 del menu scelto", "individual", "kg_co2", "less_is_better", 3),
    ("vending_products", "Prodotti comprati alle macchinette", "individual", "count", "less_is_better", 2),
    ("plants_added", "Piante portate in ufficio", "individual", "count", "more_is_better", 10),
    ("eco_tip_shared", "Eco-tip pubblicati", "individual", "count", "more_is_better", 15),
    # Team actions
    ("office_energy", "Consumo elettrico team", "team", "kwh", "less_is_better", 3),
    ("team_prints", "Numero stampe team", "team", "count", "less_is_better", 2),
    ("sustainability_event", "Partecipazione eventi green", "team", "count", "more_is_better", 10)
]
action_types = [
    {
        "id": i + 1,
        "name": n,
        "description": d,
        "category": c,
        "unit": u,
        "scoring_rule": r,
        "base_points": p
    }
    for i, (n, d, c, u, r, p) in enumerate(action_types_data)
]
action_types_df = pd.DataFrame(action_types)

# ===========================
# 4️⃣ USER ACTIONS
# ===========================
user_actions = []
action_type_map = {a["name"]: a for a in action_types}

def calc_points(action_name, value):
    """Calcola punti in base al tipo di azione e al valore"""
    a = action_type_map[action_name]
    base = a["base_points"]
    rule = a["scoring_rule"]
    if rule == "more_is_better":
        return round(value * base / 10)
    else:
        # meno è meglio: punteggio inverso (normalizzato)
        return max(0, round((10 / (value + 1)) * base))

start_date = datetime.now() - timedelta(days=DAYS_HISTORY)

for u in users:
    for day in range(DAYS_HISTORY):
        date = start_date + timedelta(days=day)

        # Azioni quotidiane individuali
        commute_km = random.uniform(0, 20)
        idle_min = random.uniform(10, 180)
        prints = random.randint(0, 10)
        co2_meal = random.uniform(0.3, 2.0)
        vending = random.randint(0, 5)

        plants = 1 if random.random() < 0.02 else 0
        eco_tip = 1 if random.random() < 0.03 else 0

        actions_today = {
            "sustainable_commute": commute_km,
            "idle_minutes": idle_min,
            "daily_prints": prints,
            "meal_co2": co2_meal,
            "vending_products": vending,
            "plants_added": plants,
            "eco_tip_shared": eco_tip
        }

        for a_name, value in actions_today.items():
            if value > 0:
                points = calc_points(a_name, value)
                user_actions.append({
                    "user_id": u["id"],
                    "action_type_id": action_type_map[a_name]["id"],
                    "value": round(value, 2),
                    "points_awarded": points,
                    "date": date.date()
                })

user_actions_df = pd.DataFrame(user_actions)

# ===========================
# 5️⃣ TEAM SCORES
# ===========================
team_scores = []
for t in teams:
    for day in range(DAYS_HISTORY):
        date = start_date + timedelta(days=day)
        energy = random.uniform(50, 200)   # kWh consumati
        prints = random.randint(20, 100)
        events = random.randint(0, 2)

        team_points = (
            calc_points("office_energy", energy)
            + calc_points("team_prints", prints)
            + calc_points("sustainability_event", events)
        )

        team_scores.append({
            "team_id": t["id"],
            "date": date.date(),
            "total_points": team_points
        })
team_scores_df = pd.DataFrame(team_scores)

# ===========================
# 6️⃣ EVENTS
# ===========================
events = []
for i in range(random.randint(5, 15)):
    team = random.choice(teams)
    participants = random.randint(5, 20)
    date = start_date + timedelta(days=random.randint(0, DAYS_HISTORY - 1))
    events.append({
        "id": i + 1,
        "name": f"Evento Sostenibilità {fake.word()}",
        "description": fake.sentence(),
        "date": date.date(),
        "team_id": team["id"],
        "participants_count": participants,
        "points_awarded": participants * 10
    })
events_df = pd.DataFrame(events)

# ===========================
# 7️⃣ EXPORT CSV
# ===========================
output_dir = "fake_data/"
import os
os.makedirs(output_dir, exist_ok=True)

teams_df.to_csv(output_dir + "teams.csv", index=False)
users_df.to_csv(output_dir + "users.csv", index=False)
action_types_df.to_csv(output_dir + "action_types.csv", index=False)
user_actions_df.to_csv(output_dir + "user_actions.csv", index=False)
team_scores_df.to_csv(output_dir + "team_scores.csv", index=False)
events_df.to_csv(output_dir + "events.csv", index=False)

print("✅ Dati fake generati in:", output_dir)
print(f"- {len(users_df)} users")
print(f"- {len(user_actions_df)} user actions")
print(f"- {len(team_scores_df)} team scores")
