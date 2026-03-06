import os
import json

from scripts.file_utils import save_json, load_json, read_file
from scripts.extract_onboarding_updates import extract_onboarding_updates
from scripts.patch_engine import apply_patch
from scripts.agent_generator import generate_agent_spec
from scripts.diff_generator import generate_diff
from scripts.conflict_detector import detect_conflicts

DATASET = "dataset/onboarding_calls"


def run_onboarding():

    # Iterate through onboarding transcripts
    for file in os.listdir(DATASET):

        if not file.endswith(".txt"):
            continue

        transcript_path = f"{DATASET}/{file}"

        transcript = read_file(transcript_path)

        # Extract account id
        account_id = file.replace(".txt", "")

        print(f"Processing onboarding update for {account_id}")

        # -----------------------------
        # Extract updates from transcript
        # -----------------------------

        updates = extract_onboarding_updates(transcript)

        # -----------------------------
        # Load previous configuration
        # -----------------------------

        old_memo_path = f"outputs/accounts/{account_id}/v1/memo.json"

        old_memo = load_json(old_memo_path)

        # -----------------------------
        # Detect conflicts
        # -----------------------------

        conflicts = detect_conflicts(old_memo, updates)

        # -----------------------------
        # Apply updates
        # -----------------------------

        new_memo = apply_patch(old_memo, updates)

        # -----------------------------
        # Generate new agent configuration
        # -----------------------------

        agent = generate_agent_spec(new_memo, "v2")

        # -----------------------------
        # Generate diff (v1 → v2)
        # -----------------------------

        diff = generate_diff(old_memo, new_memo)

        # Convert DeepDiff object to JSON-safe dictionary
        diff_clean = json.loads(diff.to_json())

        # Attach conflict report
        diff_clean["conflicts"] = conflicts

        # -----------------------------
        # Save outputs
        # -----------------------------

        base = f"outputs/accounts/{account_id}/v2"

        os.makedirs(base, exist_ok=True)

        save_json(f"{base}/memo.json", new_memo)

        save_json(f"{base}/agent_spec.json", agent)

        save_json(
            f"outputs/accounts/{account_id}/changelog.json",
            diff_clean
        )

        print(f"Updated v2 for {account_id}")


if __name__ == "__main__":
    run_onboarding()