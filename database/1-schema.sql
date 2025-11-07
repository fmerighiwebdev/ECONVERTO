CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    office_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    team_id INTEGER REFERENCES teams(id) ON DELETE SET NULL,
    streak_days INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE action_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50),  -- es: 'individual', 'team'
    unit VARCHAR(20),      -- es: 'km', 'minutes', 'count'
    scoring_rule VARCHAR(20), -- 'less_is_better' o 'more_is_better'
    base_points INTEGER DEFAULT 10
);

CREATE TABLE user_actions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    action_type_id INTEGER REFERENCES action_types(id),
    value NUMERIC(10,2) NOT NULL,    -- es. km percorsi, numero stampe, ecc.
    points_awarded INTEGER DEFAULT 0,
    date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE team_scores (
    id SERIAL PRIMARY KEY,
    team_id INTEGER REFERENCES teams(id) ON DELETE CASCADE,
    date DATE DEFAULT CURRENT_DATE,
    total_points INTEGER DEFAULT 0
);

CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    date DATE,
    team_id INTEGER REFERENCES teams(id),
    participants_count INTEGER DEFAULT 0,
    points_awarded INTEGER DEFAULT 0
);