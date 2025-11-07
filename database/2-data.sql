\COPY teams FROM '/data/teams.csv' WITH (FORMAT csv, HEADER true);
\COPY users FROM '/data/users.csv' WITH (FORMAT csv, HEADER true);
\COPY action_types FROM '/data/action_types.csv' WITH (FORMAT csv, HEADER true);
\COPY user_actions FROM '/data/user_actions.csv' WITH (FORMAT csv, HEADER true);
\COPY team_scores FROM '/data/team_scores.csv' WITH (FORMAT csv, HEADER true);
\COPY events FROM '/data/events.csv' WITH (FORMAT csv, HEADER true);
