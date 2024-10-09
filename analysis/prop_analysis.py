# utils/prop_analysis.py

def analyze_prop_bet(player_stats, prop_lines):
    """
    Analyze the player stats versus the prop lines to give a recommendation.
    """
    analysis_result = {}

    for stat, prop_line in prop_lines.items():
        actual_stat = player_stats.get(f"{stat}_per_game", None)
        if actual_stat is not None:
            if actual_stat > prop_line:
                analysis_result[stat] = "Bet Over"
            else:
                analysis_result[stat] = "Bet Under"
        else:
            analysis_result[stat] = "Data not available"

    return analysis_result
