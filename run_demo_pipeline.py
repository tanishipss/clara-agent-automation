import os

from scripts.file_utils import save_json, read_file
from scripts.extract_demo_data import extract_demo_data
from scripts.agent_generator import generate_agent_spec
from scripts.logger import setup_logger


DATASET = "dataset/demo_calls"

logger = setup_logger()


def run_demo():

    print("Step 1: Generating v1 agents from demo calls")
    logger.info("Starting demo pipeline")

    for file in os.listdir(DATASET):

        if not file.endswith(".txt"):
            continue

        account_id = file.replace(".txt", "")

        transcript_path = f"{DATASET}/{file}"

        logger.info(f"Processing demo transcript for {account_id}")

        transcript = read_file(transcript_path)

        extracted = extract_demo_data(transcript, account_id)

        agent = generate_agent_spec(extracted, "v1")

        base = f"outputs/accounts/{account_id}/v1"

        os.makedirs(base, exist_ok=True)

        save_json(f"{base}/memo.json", extracted)

        save_json(f"{base}/agent_spec.json", agent)

        print(f"Created v1 for {account_id}")

        logger.info(f"Created v1 agent configuration for {account_id}")

    logger.info("Demo pipeline completed")


if __name__ == "__main__":
    run_demo()