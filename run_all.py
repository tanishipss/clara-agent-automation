import run_demo_pipeline
import run_onboarding_pipeline
import time

start = time.time()

print("Starting Clara Automation Pipeline")

print("Step 1: Generating v1 agents from demo calls")
run_demo_pipeline.run_demo()

print("Step 2: Applying onboarding updates")
run_onboarding_pipeline.run_onboarding()

print("Pipeline completed")

end = time.time()

print(f"Execution time: {round(end-start,2)} seconds")