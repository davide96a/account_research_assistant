# Account Research Assistant

A command-line tool that takes a company name and produces a structured
research brief, built for enterprise sales reps who need to prepare an
account quickly. It calls an LLM and returns the brief as structured data,
so the output can be read by a person today and consumed by an automated
agent later.

> **Status:** 🚧 In progress. Core is working end-to-end — give it a company
> name and it returns a structured brief, with error handling for network and
> malformed-response failures. Currently expanding toward graceful handling of
> missing fields, multi-company batching, file output, and an eventual agentic
> workflow. Project A of a six-month AI Engineering portfolio.

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

# Run
python main.py
```

The tool will ask which company to research, then print a structured brief.

## Roadmap

- [x] Define the output contract (sector, sub-sector, employees, revenue)
- [x] First LLM call returning structured data
- [x] Parse the response into a Python dictionary
- [x] Format it into a human-readable sales brief
- [x] Error handling (network failure + malformed response)
- [x] Interactive company input at runtime
- [ ] Graceful handling of None / missing fields
- [ ] Loop for researching multiple companies
- [ ] Export briefs to file
- [ ] Evolve toward an agentic workflow
- [ ] Tests

---

Part of a part-time AI Engineering bootcamp (The Bridge × UAM), 2026.