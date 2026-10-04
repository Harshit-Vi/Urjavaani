"""Generate synthetic data; always label outputs as synthetic."""

import random


def machine_week(base_kw: float, idle_waste_kw: float = 0.0, seed: int = 0) -> list[float]:
    """Generate 168 hourly synthetic kW values."""
    rng = random.Random(seed)
    sigma = 0.05 * base_kw
    values: list[float] = []
    for _ in range(168):
        kw = base_kw + idle_waste_kw + rng.gauss(0.0, sigma)
        values.append(max(0.0, kw))
    return values
