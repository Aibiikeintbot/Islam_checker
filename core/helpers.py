def get_score_color(score: float) -> str:
    if score is None:
        return "gray"
    if score >= 80:
        return "green"
    elif score >= 60:
        return "orage"
    else:
        return "red"


















