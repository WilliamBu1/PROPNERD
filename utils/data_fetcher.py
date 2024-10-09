from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog


def get_player_id(player_name):
    """
    Returns the player's NBA ID using nba_api.
    """
    player = players.find_players_by_full_name(player_name)
    if len(player) == 0:
        return f"Player {player_name} not found."
    return player[0]['id']


def get_last_5_games(player_id):
    """
    Fetch the last 5 games played by the player, regardless of location.
    """
    game_log = playergamelog.PlayerGameLog(player_id=player_id, season='2023')
    games = game_log.get_data_frames()[0]  # Returns a DataFrame with the game logs
    return games.head(5)  # Return the last 5 games


def get_last_5_home_or_away_games(player_id, location):
    """
    Fetch the last 5 home or away games, based on location.
    - location: 'home' or 'away'
    """
    game_log = playergamelog.PlayerGameLog(player_id=player_id, season='2023')
    games = game_log.get_data_frames()[0]

    # Filter based on location
    if location == 'home':
        return games[games['MATCHUP'].str.contains('vs.')].head(5)
    elif location == 'away':
        return games[games['MATCHUP'].str.contains('@')].head(5)


def get_last_5_games_against_opponent(player_id, opponent_abbreviation):
    """
    Fetch the last 5 games played by the player against a specific opponent.
    - opponent_abbreviation: NBA team abbreviation (e.g., 'HOU' for Houston Rockets)
    """
    game_log = playergamelog.PlayerGameLog(player_id=player_id, season='2023')
    games = game_log.get_data_frames()[0]

    # Filter by the opponent team abbreviation
    return games[games['MATCHUP'].str.contains(opponent_abbreviation)].head(5)
