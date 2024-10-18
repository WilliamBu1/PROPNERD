import streamlit as st


# Simulating the sample data for point spread
def get_sample_point_spread(team_name):
    """
    Simulate fetching point spread for the given team.
    """
    sample_point_spreads = {
        "Los Angeles Lakers": -12.5,  # Lakers are favored by 12.5 points
        "Houston Rockets": +12.5
    }
    return sample_point_spreads.get(team_name, None)


# Simulating the sample data for player prop lines
def get_sample_prop_line(player_name):
    """
    Simulate fetching player prop lines for points.
    """
    sample_prop_lines = {
        "LeBron James": 27.5  # LeBron's points prop line
    }
    return sample_prop_lines.get(player_name, None)


# Function to calculate blowout risk based on point spread
def calculate_blowout_risk(point_spread, threshold=10):
    """
    Calculate the blowout risk based on the point spread.
    - point_spread: The point spread for the game.
    - threshold: The spread at which a blowout risk becomes significant.

    Returns a string indicating low, medium, or high blowout risk.
    """
    if abs(point_spread) >= threshold:
        return "High"
    elif abs(point_spread) >= threshold / 2:
        return "Medium"
    else:
        return "Low"


# Simulate player stats and calculate analysis with blowout risk
def analyze_prop_bet_with_blowout(player_stats, prop_line, blowout_risk_score):
    """
    Analyze the player stats versus the prop line, factoring in the blowout risk.
    - player_stats: Simulated average player points.
    - prop_line: The prop line for the player's points.
    - blowout_risk_score: Blowout risk calculated based on point spread.

    Adjusts the recommendation based on blowout risk.
    """
    analysis_result = {}

    if blowout_risk_score == "High":
        # Reduce player stats by 20% in a blowout scenario
        adjusted_points = player_stats * 0.8
        if adjusted_points > prop_line:
            analysis_result["Points"] = "Bet Over (with blowout risk)"
        else:
            analysis_result["Points"] = "Bet Under"
    else:
        # Normal analysis if blowout risk is low or medium
        if player_stats > prop_line:
            analysis_result["Points"] = "Bet Over"
        else:
            analysis_result["Points"] = "Bet Under"

    return analysis_result


# Streamlit UI
st.title("PropNerd: NBA Player Blowout Risk Calculator")

# Input: NBA player name
player_name = st.text_input("Enter NBA player name (e.g., 'LeBron James'):", "LeBron James")

# Input: Team name for point spread
team_name = st.text_input("Enter the player's team name (e.g., 'Los Angeles Lakers'):", "Los Angeles Lakers")

# Simulate player average stats (points per game in the last 5 games)
player_avg_points = st.number_input("Enter player's average points over the last 5 games:", value=30.0)

# Analyze button
if st.button("Analyze"):
    if player_name and team_name:
        # Step 1: Fetch the point spread (using sample data)
        point_spread = get_sample_point_spread(team_name)
        if point_spread is None:
            st.write(f"No point spread data found for {team_name}")
        else:
            st.write(f"Point Spread: {team_name}: {point_spread}")

            # Step 2: Fetch the player's prop line (using sample data)
            prop_line = get_sample_prop_line(player_name)
            if prop_line is None:
                st.write(f"No prop line data found for {player_name}")
            else:
                st.write(f"{player_name} Points Prop Line: {prop_line}")

                # Step 3: Calculate blowout risk
                blowout_risk_score = calculate_blowout_risk(point_spread)
                st.write(f"Blowout Risk: **{blowout_risk_score}**")

                # Step 4: Analyze prop bet considering blowout risk
                analysis = analyze_prop_bet_with_blowout(player_avg_points, prop_line, blowout_risk_score)
                st.write(f"Analysis Result: {analysis['Points']}")
    else:
        st.write("Please enter both player and team names.")
