import pandas as pd
from itertools import combinations

def evaluate_community_tank(selected_fish, pair_df):
    pair_results = []

    for fish_a, fish_b in combinations(selected_fish, 2):
        match = pair_df[
            ((pair_df["Fish A"] == fish_a) & (pair_df["Fish B"] == fish_b)) |
            ((pair_df["Fish A"] == fish_b) & (pair_df["Fish B"] == fish_a))
        ]

        if not match.empty:
            row = match.iloc[0]

            pair_results.append({
                "Fish A": fish_a,
                "Fish B": fish_b,
                "Compatibility Score": row["Overall Compatibility Score 0-100"],
                "Compatibility": row["Compatibility Label"]
            })

    results_df = pd.DataFrame(pair_results)

    if results_df.empty:
        return "No pair compatibility records found."

    average_score = results_df["Compatibility Score"].mean()
    lowest_score = results_df["Compatibility Score"].min()

    if lowest_score < 50:
        community_rating = "Not Recommended"
    elif average_score >= 75 and lowest_score >= 50:
        community_rating = "Good Community Tank"
    else:
        community_rating = "Use Caution"

    return {
        "Community Rating": community_rating,
        "Average Compatibility Score": round(average_score, 2),
        "Lowest Pair Score": lowest_score,
        "Pair Results": results_df
    }