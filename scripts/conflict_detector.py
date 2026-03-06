# scripts/conflict_detector.py

def detect_conflicts(old_memo, updates):

    conflicts = []

    for key, value in updates.items():

        if key in old_memo and old_memo[key] != value:

            conflicts.append({
                "field": key,
                "demo_value": old_memo[key],
                "onboarding_value": value,
                "resolution": "onboarding overrides"
            })

    return conflicts