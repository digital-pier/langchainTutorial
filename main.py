from config import validate_config, ANTHROPIC_MODEL
from agents.agent import run_agent
from rich.console import Console

console = Console()

def main():
    validate_config()
    console.print(f"[bold green]AI Agent starting...[/bold green] (model: {ANTHROPIC_MODEL})")

    # Example: single prompt run
    user_input = input("You: ")
    response = run_agent(user_input)
    console.print(f"\n[bold cyan]Agent:[/bold cyan] {response}")

if __name__ == "__main__":
    main()
