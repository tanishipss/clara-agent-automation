import os
import json

from scripts.file_utils import save_json, load_json, read_file
from scripts.extract_onboarding_updates import extract_onboarding_updates
from scripts.patch_engine import apply_patch
from scripts.agent_generator import generate_agent_spec
from scripts.diff_generator import generate_diff
from scripts.conflict_detector import detect_conflicts


DATASET = "dataset/onboarding_calls"
OUTPUT_BASE = "outputs/accounts"


def run_onboarding():

    print("Step 2: Applying onboarding updates")

    for file in os.listdir(DATASET):

        if not file.endswith(".txt"):
            continue

        account_id = file.replace(".txt", "")

        transcript = read_file(f"{DATASET}/{file}")

        # --------------------------------------
        # Extract updates from onboarding call
        # --------------------------------------
        updates = extract_onboarding_updates(transcript)

        # --------------------------------------
        # Load previous configuration (v1)
        # --------------------------------------
        old_memo_path = f"{OUTPUT_BASE}/{account_id}/v1/memo.json"

        if not os.path.exists(old_memo_path):
            print(f"Skipping {account_id}: v1 memo not found")
            continue

        old_memo = load_json(old_memo_path)

        # --------------------------------------
        # Apply updates to create v2 memo
        # --------------------------------------
        new_memo = apply_patch(old_memo, updates)

        # --------------------------------------
        # Detect conflicts between demo and onboarding
        # --------------------------------------
        conflicts = detect_conflicts(old_memo, updates)

        # --------------------------------------
        # Generate new agent specification
        # --------------------------------------
        agent = generate_agent_spec(new_memo, "v2")

        # --------------------------------------
        # Generate configuration diff
        # --------------------------------------
        diff = generate_diff(old_memo, new_memo)

        diff_clean = json.loads(diff.to_json())

        # attach conflict information
        diff_clean["conflicts"] = conflicts

        # --------------------------------------
        # Output paths
        # --------------------------------------
        base = f"{OUTPUT_BASE}/{account_id}/v2"

        os.makedirs(base, exist_ok=True)

        # --------------------------------------
        # Save outputs
        # --------------------------------------
        save_json(f"{base}/memo.json", new_memo)

        save_json(f"{base}/agent_spec.json", agent)

        save_json(
            f"{OUTPUT_BASE}/{account_id}/changelog.json",
            diff_clean
        )

        print(f"Updated v2 for {account_id}")


if __name__ == "__main__":
    run_onboarding()