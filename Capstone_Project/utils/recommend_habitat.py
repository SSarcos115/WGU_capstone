def recommend_habitat(selected_fish, species_df):
    selected = species_df[species_df["Species"].isin(selected_fish)]

    if selected.empty:
        return "No matching fish found."

    water_types = selected["Water Type"].unique()

    if len(water_types) > 1:
        return {
            "Status": "Invalid community",
            "Reason": "Freshwater and saltwater species cannot share the same tank."
        }

    shared_temp_min = selected["Temp Min F"].max()
    shared_temp_max = selected["Temp Max F"].min()

    shared_ph_min = selected["pH Min"].max()
    shared_ph_max = selected["pH Max"].min()

    min_tank_size = selected["Min Tank Gallons"].max()

    if shared_temp_min > shared_temp_max:
        temp_status = "No shared temperature range"
    else:
        temp_status = f"{shared_temp_min}–{shared_temp_max}°F"

    if shared_ph_min > shared_ph_max:
        ph_status = "No shared pH range"
    else:
        ph_status = f"{shared_ph_min}–{shared_ph_max}"

    return {
        "Water Type": water_types[0],
        "Recommended Temperature Range": temp_status,
        "Recommended pH Range": ph_status,
        "Minimum Tank Size": f"{min_tank_size} gallons",
        "Fish Count Evaluated": len(selected)
    }