def explain_pair_result(row):
    fish_a = row["Fish A"]
    fish_b = row["Fish B"]
    label = row["Compatibility Label"]

    reasons = []

    if row["Same Water Type"] == 0:
        reasons.append(
            "Saltwater fish cannot be kept in the same tank as freshwater fish."
        )

    if row["Temperature Overlap Ratio"] < 0.5:
        reasons.append(
            "The temperature requirements for these fish do not overlap enough."
        )

    if row["pH Overlap Ratio"] < 0.5:
        reasons.append(
            "The pH requirements for these fish do not overlap enough."
        )

    if row["Predation Size Risk"] == 1:
        reasons.append(
            f"{fish_a} and {fish_b} have a size or predation risk, meaning one fish may harm or eat the other."
        )

    if row["Temperament Risk"] == 1:
        reasons.append(
            f"{fish_a} and {fish_b} may be too aggressive or territorial to safely share the same tank."
        )

    if row["Diet/Predation Risk"] == 1:
        reasons.append(
            "Their diet or feeding behavior may create a compatibility risk."
        )

    if row["Schooling Conflict"] == 1:
        reasons.append(
            "A schooling fish may become stressed if paired with a more aggressive tank mate."
        )

    if row["Reef Safety Conflict"] == 1:
        reasons.append(
            "This saltwater pairing may not be safe for a reef aquarium setup."
        )

    if row["Same Group Aggression Conflict"] == 1:
        reasons.append(
            "These fish are from similar groups and may become territorial toward each other."
        )

    if len(reasons) == 0:
        reasons.append(
            "These fish have compatible water parameters and no major aggression, size, or diet conflicts were detected."
        )

    return f"{label}: " + " ".join(reasons)