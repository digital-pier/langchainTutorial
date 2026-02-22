from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage
from config import ANTHROPIC_API_KEY, ANTHROPIC_MODEL

# Initialize the model
llm = ChatAnthropic(
    model=ANTHROPIC_MODEL,
    api_key=ANTHROPIC_API_KEY,
    max_tokens=1024,
)

SYSTEM_PROMPT = """You are a helpful AI assistant. Be concise and clear in your responses."""

def run_agent(user_input: str) -> str:
    """Run a single-turn agent call. Extend this for multi-turn or tool use."""
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_input),
    ]
    response = llm.invoke(messages)
    return response.content
