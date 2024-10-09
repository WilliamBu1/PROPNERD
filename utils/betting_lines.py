import requests

# Replace this with your actual API key for The Odds API
API_KEY = 'your_odds_api_key'


def get_player_prop_line(player_name):
    """
    Fetch prop lines for the given player from The Odds API.
    - player_name: Full name of the player (e.g., "LeBron James").

    Returns a dictionary with the player's prop lines (e.g., points, assists, rebounds).
    """
    url = f"https://api.the-odds-api.com/v4/sports/basketball_nba/odds/?regions=us&markets=player_points&apiKey={API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        return "Error fetching prop lines."

    odds_data = response.json()

    # Filter for the player's prop lines
    player_props = {}
    for game in odds_data:
        for bet in game['bookmakers'][0]['markets'][0]['outcomes']:
            if player_name in bet['name']:
                player_props[bet['name']] = bet['price']

    return player_props if player_props else f"No prop lines found for {player_name}."


def get_game_point_spread(team_name):
    """
    Fetch the point spread for the given team from The Odds API.
    - team_name: Full name of the team (e.g., "Los Angeles Lakers").

    Returns the point spread for the team's next game.
    """
    url = f"https://api.the-odds-api.com/v4/sports/basketball_nba/odds/?regions=us&markets=spreads&apiKey={API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        return "Error fetching point spread."

    odds_data = response.json()

    # Filter for the point spread for the team
    for game in odds_data:
        if team_name in game['teams']:
            point_spread = game['bookmakers'][0]['markets'][0]['outcomes']
            return {outcome['name']: outcome['point'] for outcome in point_spread}

    return f"No point spread found for {team_name}."
