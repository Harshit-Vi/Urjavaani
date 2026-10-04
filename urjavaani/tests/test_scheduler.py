from urjavaani.scheduler.planner import Job, plan


def test_scheduler_picks_cheap_window() -> None:
    rates = {hour: 9.0 for hour in range(24)}
    for hour in range(2, 6):
        rates[hour] = 5.0

    job = Job("furnace", 100, 2, 0, 24)
    result = plan([job], rates)

    start_hour, _ = result["furnace"]
    assert 2 <= start_hour <= 4
