# Clara AI Agent Automation Pipeline

## Overview

This project builds an **automation pipeline that converts client call transcripts into deployable AI call-agent configurations**.

The system processes two types of calls:

* **Demo Calls** → initial configuration extraction
* **Onboarding Calls** → updates existing configurations

The pipeline automatically generates structured agent configurations, tracks changes between versions, and exposes results in an interactive dashboard.

---

## Architecture

```
Demo Transcript
      ↓
Transcript Parser
      ↓
Structured Memo
      ↓
Agent Spec Generator
      ↓
Agent Config v1
      ↓
Onboarding Transcript
      ↓
Update Extraction
      ↓
Patch Engine
      ↓
Agent Config v2
      ↓
Diff Generator
      ↓
Changelog + Dashboard
```

---

## Features

### Automated Transcript Processing

Extracts structured configuration data from call transcripts.

### Explicit Unknown Handling

The system avoids hallucination and explicitly reports missing information.

Example:

```
questions_or_unknowns:
- business hours not specified
- emergency definition unclear
```

### Configuration Versioning

Demo calls generate **v1 configurations**, onboarding updates create **v2**.

```
outputs/accounts/account_01/
  v1/
  v2/
  changelog.json
```

### Conflict Detection

When onboarding contradicts demo configuration the system records the change.

Example:

```
conflict:
 field: business_hours
 demo: 9-5
 onboarding: 8-4
 resolution: onboarding overrides
```

### Dashboard Monitoring

A Streamlit dashboard provides visibility into:

* Accounts processed
* Missing configuration data
* Generated agent configs
* Version differences

---

## Project Structure

```
clara-agent-automation
│
├── dataset
├── scripts
├── dashboard
├── config
│
├── run_all.py
├── run_demo_pipeline.py
├── run_onboarding_pipeline.py
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone repository:

```
git clone https://github.com/tanishipss/clara-agent-automation.git
cd clara-agent-automation
```

Create virtual environment:

```
python -m venv venv
```

Activate environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Run the Pipeline

```
python run_all.py
```

This will:

1. Generate v1 configurations from demo calls
2. Apply onboarding updates
3. Generate changelog files

---

## Launch Dashboard

```
streamlit run dashboard/pipeline_dashboard.py
```

Open browser:

```
http://localhost:8501
```

---

## Technologies Used

* Python
* Streamlit
* DeepDiff
* Rule-based text extraction

---

## Author

Tanisha Yadav
B.Tech Final Year
Machine Learning / Software Engineering
