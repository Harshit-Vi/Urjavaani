"""WhatsApp notification formatter and sender mock."""


def format_daily_plan(plan_result: dict[str, tuple[int, float]], saving_inr: float) -> str:
    """Format a daily schedule message."""
    lines = ["Today's plan:"]
    for name, (hour, _) in plan_result.items():
        lines.append(f"- {name}: start {hour:02d}:00")
    lines.append(f"Estimated saving: Rs {saving_inr:,.0f}")
    return "\n".join(lines)


def send(message: str) -> None:
    """Send message via console mock."""
    print(message)
