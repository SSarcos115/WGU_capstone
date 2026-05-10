import pandas as pd

from utils.evaluate_community_tank import evaluate_community_tank
from utils.explain_pair_result import explain_pair_result
from utils.recommend_habitat import recommend_habitat


def predict_aquarium_setup(selected_fish, species_df, pair_df):
    print("Selected Fish")
    print("-------------")
    for fish in selected_fish:
        print("-", fish)

    print("\nHabitat Recommendation")
    print("----------------------")

    habitat_result = recommend_habitat(selected_fish, species_df)

    if isinstance(habitat_result, dict):
        for key, value in habitat_result.items():
            print(f"{key}: {value}")
    else:
        print(habitat_result)

    print("\nCommunity Tank Evaluation")
    print("-------------------------")

    community_result = evaluate_community_tank(selected_fish, pair_df)

    if not isinstance(community_result, dict):
        print(community_result)
        return

    print("Community Rating:", community_result["Community Rating"])
    print("Average Compatibility Score:", community_result["Average Compatibility Score"])
    print("Lowest Pair Score:", community_result["Lowest Pair Score"])

    detailed_columns = [
        "Fish A",
        "Fish B",
        "Same Water Type",
        "Temperature Overlap Ratio",
        "pH Overlap Ratio",
        "Salinity Overlap Ratio",
        "Tank Requirement Similarity",
        "Adult Size Ratio",
        "Predation Size Risk",
        "Temperament Risk",
        "Diet/Predation Risk",
        "Water Level Compatibility",
        "Schooling Conflict",
        "Reef Safety Conflict",
        "Same Group Aggression Conflict",
        "Overall Compatibility Score 0-100",
        "Compatibility Label Code",
        "Compatibility Label"
    ]

    detailed_results = []

    for _, row in community_result["Pair Results"].iterrows():
        fish_a = row["Fish A"]
        fish_b = row["Fish B"]

        match = pair_df[
            ((pair_df["Fish A"] == fish_a) & (pair_df["Fish B"] == fish_b)) |
            ((pair_df["Fish A"] == fish_b) & (pair_df["Fish B"] == fish_a))
        ]

        if not match.empty:
            detailed_results.append(match[detailed_columns].iloc[0])

    detailed_results_df = pd.DataFrame(detailed_results)

    detailed_results_df["Reason"] = detailed_results_df.apply(
        explain_pair_result,
        axis=1
    )

    print("\nDetailed Pair Compatibility Results")
    print("-----------------------------------")

    return detailed_results_df