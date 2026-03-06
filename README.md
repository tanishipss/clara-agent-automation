# Clara AI Agent Automation Pipeline

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-red)
![Automation](https://img.shields.io/badge/Project-AI%20Automation-orange)
![License](https://img.shields.io/badge/License-MIT-green)

Automation pipeline that converts **client call transcripts into deployable AI voice agent configurations**.

---

# Overview

This project implements an **automation pipeline that processes service company call transcripts and generates structured AI agent configurations.**

The system processes two types of calls:

* **Demo Calls** → initial configuration extraction
* **Onboarding Calls** → updates existing configurations

The pipeline automatically:

* extracts structured configuration data
* generates AI agent specifications
* tracks configuration changes
* visualizes results through a dashboard

---

# Quick Demo

Run the full automation pipeline:

```
python run_all.py
```

Launch the dashboard:

```
streamlit run dashboard/pipeline_dashboard.py
```

Open the dashboard in your browser:

```
http://localhost:8501
```

The pipeline will process demo and onboarding transcripts and generate AI agent configurations automatically.

---

# Architecture

```
Demo Call Transcript
        ↓
Transcript Parser
        ↓
Structured Memo (Account Configuration)
        ↓
Agent Spec Generator
        ↓
Agent Configuration v1

------------------------------------------------

Onboarding Call Transcript
        ↓
Update Extraction Engine
        ↓
Patch Engine
        ↓
Agent Configuration v2

------------------------------------------------

Diff Generator
        ↓
Changelog + Conflict Detection
        ↓
Streamlit Dashboard
```

---

# Features

## Automated Transcript Processing

Extracts structured configuration data from conversation transcripts.

Example extracted fields:

```
services_supported:
- sprinkler service
- fire alarm inspection

business_hours:
  value: "8-6"
```

---

## Explicit Unknown Handling

The system avoids hallucination and explicitly surfaces missing information.

Example:

```
questions_or_unknowns:
- business hours not specified
- emergency definition unclear
```

---

## Configuration Versioning

Demo calls generate **v1 configurations**.
Onboarding calls generate **v2 updates**.

Example output structure:

```
outputs/accounts/account_01/

   v1/
      memo.json
      agent_spec.json

   v2/
      memo.json
      agent_spec.json

   changelog.json
```

---

## Conflict Detection

When onboarding updates contradict demo configurations the system logs the conflict.

Example:

```
conflicts:
 field: business_hours
 demo_value: 9-5
 onboarding_value: 8-4
 resolution: onboarding overrides
```

---

## Interactive Dashboard

A **Streamlit dashboard** provides visibility into pipeline results.

The dashboard displays:

* accounts processed
* missing configuration fields
* generated agent specifications
* version differences
* change logs

---

# Project Structure

```
clara-agent-automation
│
├── dataset
│   ├── demo_calls
│   └── onboarding_calls
│
├── scripts
│   ├── transcript_parser.py
│   ├── extract_demo_data.py
│   ├── extract_onboarding_updates.py
│   ├── agent_generator.py
│   ├── patch_engine.py
│   ├── diff_generator.py
│   └── conflict_detector.py
│
├── dashboard
│   └── pipeline_dashboard.py
│
├── config
│
├── run_demo_pipeline.py
├── run_onboarding_pipeline.py
├── run_all.py
│
├── requirements.txt
└── README.md
```

---

# Requirements

* Python 3.9+
* pip

---

# Installation

Clone the repository:

```
git clone https://github.com/tanishipss/clara-agent-automation.git
cd clara-agent-automation
```

Create virtual environment:

```
python -m venv venv
```

Activate environment (Windows):

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Run the Automation Pipeline

Run the pipeline:

```
python run_all.py
```

This will:

1. Generate **v1 agent configurations from demo calls**
2. Apply **onboarding updates**
3. Generate **change logs and configuration differences**

---

# Launch Dashboard

Start the dashboard:

```
streamlit run dashboard/pipeline_dashboard.py
```

Open:

```
http://localhost:8501
```

---

# Example Outputs

Example memo:

```
services_supported:
- sprinkler service
- fire alarm service
- inspection service
```

Example change log:

```
type_changes:
 business_hours:
  old_type: NoneType
  new_type: dict
```

---

# Technologies Used

* Python
* Streamlit
* DeepDiff
* Rule-based text extraction

---

# Design Principles

The pipeline is designed using the following principles:

* deterministic parsing where possible
* explicit handling of missing data
* versioned configuration updates
* transparent change tracking
* idempotent pipeline execution

---

# Author

**Tanisha Yadav**

B.Tech Final Year
Machine Learning / Software Engineering
