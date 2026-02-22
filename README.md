# AI Agent Template

Python AI agent template using LangChain + Anthropic (Claude).

## Setup

```bash
# 1. Clone/copy this template
# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
copy .env.example .env       # Windows
cp .env.example .env         # Mac/Linux
# Then edit .env and add your ANTHROPIC_API_KEY

# 5. Run
python main.py
```

## Project Structure

```
├── .env                 # Your secrets (never commit this)
├── .env.example         # Template for env vars
├── .gitignore
├── requirements.txt
├── config.py            # Centralized config & validation
├── main.py              # Entry point
└── agents/
    ├── __init__.py
    └── agent.py         # Core agent logic
```

## Extending

- Add tools to the agent in `agents/agent.py`
- Add new agents as separate files under `agents/`
- Add new API keys to `.env.example` and `config.py`
