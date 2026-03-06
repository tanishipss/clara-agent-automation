import streamlit as st
import os
import json

BASE_PATH = "outputs/accounts"

st.title("Clara Automation Pipeline Dashboard")

# Ensure outputs folder exists
if not os.path.exists(BASE_PATH):
    st.error("Outputs folder not found. Run the pipeline first.")
    st.stop()

accounts = sorted(os.listdir(BASE_PATH))

processed_accounts = len(accounts)
missing_data = 0
configured_accounts = 0

# -----------------------------
# CALCULATE METRICS
# -----------------------------

for acc in accounts:

    memo_path = f"{BASE_PATH}/{acc}/v1/memo.json"

    if os.path.exists(memo_path):

        with open(memo_path) as f:
            memo = json.load(f)

        missing = memo.get("questions_or_unknowns", [])

        if missing:
            missing_data += 1
        else:
            configured_accounts += 1


# -----------------------------
# PIPELINE METRICS
# -----------------------------

st.header("Pipeline Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Accounts Processed", processed_accounts)
col2.metric("Configured Accounts", configured_accounts)
col3.metric("Accounts Missing Info", missing_data)

if missing_data > 0:
    st.warning("Some accounts still have missing configuration fields.")
else:
    st.success("All accounts fully configured.")


# -----------------------------
# MISSING DATA ALERTS
# -----------------------------

st.header("Missing Data Alerts")

for acc in accounts:

    memo_path = f"{BASE_PATH}/{acc}/v1/memo.json"

    if os.path.exists(memo_path):

        with open(memo_path) as f:
            memo = json.load(f)

        missing = memo.get("questions_or_unknowns", [])

        if missing:
            st.warning(f"{acc} missing: {', '.join(missing)}")


# -----------------------------
# ACCOUNT EXPLORER
# -----------------------------

st.header("Account Explorer")

selected = st.selectbox("Select Account", accounts)
version = st.selectbox("Version", ["v1", "v2"])

memo_path = f"{BASE_PATH}/{selected}/{version}/memo.json"
agent_path = f"{BASE_PATH}/{selected}/{version}/agent_spec.json"


# -----------------------------
# ACCOUNT MEMO
# -----------------------------

st.subheader("Account Memo")

if os.path.exists(memo_path):

    with open(memo_path) as f:
        memo = json.load(f)

    st.json(memo)

else:
    st.error("Memo file not found.")


# -----------------------------
# AGENT SPEC
# -----------------------------

st.subheader("Agent Spec")

if os.path.exists(agent_path):

    with open(agent_path) as f:
        agent = json.load(f)

    st.json(agent)

else:
    st.error("Agent spec file not found.")


# -----------------------------
# CHANGELOG
# -----------------------------

changelog_path = f"{BASE_PATH}/{selected}/changelog.json"

if os.path.exists(changelog_path):

    st.subheader("Changes (v1 → v2)")

    with open(changelog_path) as f:
        diff = json.load(f)

    st.json(diff)