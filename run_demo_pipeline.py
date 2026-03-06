import os

from scripts.file_utils import save_json, read_file
from scripts.extract_demo_data import extract_demo_data
from scripts.agent_generator import generate_agent_spec

DATASET = "dataset/demo_calls"


def run_demo():

    for file in os.listdir(DATASET):

        if not file.endswith(".txt"):
            continue

        transcript = read_file(f"{DATASET}/{file}")

        account_id = file.replace(".txt", "")

        print(f"Processing {account_id}")

        extracted = extract_demo_data(transcript, account_id)

        agent = generate_agent_spec(extracted, "v1")

        base = f"outputs/accounts/{account_id}/v1"

        os.makedirs(base, exist_ok=True)

        save_json(f"{base}/memo.json", extracted)

        save_json(f"{base}/agent_spec.json", agent)

        print(f"Created v1 for {account_id}")


if __name__ == "__main__":
    run_demo()