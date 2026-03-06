from scripts.logger import setup_logger
import run_demo_pipeline
import run_onboarding_pipeline


logger = setup_logger()

print("Starting Clara Automation Pipeline")

logger.info("Pipeline started")


# Step 1
print("Step 1: Generating v1 agents from demo calls")
logger.info("Running demo pipeline")

run_demo_pipeline.run_demo()


# Step 2
print("Step 2: Applying onboarding updates")
logger.info("Running onboarding pipeline")

run_onboarding_pipeline.run_onboarding()


print("Pipeline completed successfully")

logger.info("Pipeline finished successfully")