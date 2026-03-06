import streamlit as st
import json
import os

BASE_PATH = "outputs/accounts"

st.title("Clara Agent Configuration Viewer")

accounts = os.listdir(BASE_PATH)

selected_account = st.selectbox("Select Account", accounts)

version = st.selectbox("Version", ["v1", "v2"])

memo_path = f"{BASE_PATH}/{selected_account}/{version}/memo.json"
agent_path = f"{BASE_PATH}/{selected_account}/{version}/agent_spec.json"

st.header("Account Memo")

with open(memo_path) as f:
    memo = json.load(f)

st.json(memo)

st.header("Agent Configuration")

with open(agent_path) as f:
    agent = json.load(f)

st.json(agent)

changelog_path = f"{BASE_PATH}/{selected_account}/changelog.json"

if os.path.exists(changelog_path):

    st.header("Changelog (v1 → v2)")

    with open(changelog_path) as f:
        diff = json.load(f)

    st.json(diff)