def apply_patch(old_memo, updates):

    new_memo = old_memo.copy()

    for key, value in updates.items():
        if value is not None:
            new_memo[key] = value

    return new_memo