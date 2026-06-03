# Account Research Assistant

A command-line tool that takes a company name and produces a structured
research brief, built for enterprise sales reps who need to prepare an
account quickly. It calls an LLM and returns the brief as structured data,
so the output can be read by a person today and consumed by an automated
agent later.

> **Status:** 🚧 In progress. This is Project A of a six-month AI Engineering
> portfolio — the foundation that later grows into a RAG system and an
> autonomous sales agent. Core functionality is still being built.

## How it works

The tool keeps a clear line between two parts:

- A **non-deterministic core** — the LLM call, which returns the company
  data as structured output.
- A **deterministic shell** around it — preparing the input, parsing and
  validating the response, formatting it into a readable brief, and handling
  errors.

This separation is deliberate: the structured data is what an automated
agent will use downstream, while the formatted prose is what a human reads.

## Requirements

- Python 3.9+
- An OpenAI API key

## Installation & usage

> ⚠️ Work in progress — these steps will be finalized as the tool is built.

```bash
# Clone the repository
git clone https://github.com/davide96a/account_research_assistant.git
cd account_research_assistant

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI API key to a .env file
# OPENAI_API_KEY=your_key_here

# Run (command to be added)
```

## Roadmap

- [ ] Define the output contract (fields the brief must contain)
- [ ] First LLM call returning structured data
- [ ] Parsing and validation of the response
- [ ] Formatting into a human-readable brief
- [ ] Error handling
- [ ] Tests

---

Part of a part-time AI Engineering bootcamp (The Bridge × UAM), 2026.