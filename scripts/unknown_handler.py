def register_unknown(memo, message):

    if "questions_or_unknowns" not in memo:
        memo["questions_or_unknowns"] = []

    memo["questions_or_unknowns"].append(message)