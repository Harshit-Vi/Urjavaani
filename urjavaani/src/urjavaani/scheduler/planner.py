"""Phase 3 greedy baseline planner; upgrade to OR-Tools CP-SAT in later phases."""

from dataclasses import dataclass


@dataclass
class Job:
    """Flexible load job."""

    name: str
    kw: float
    duration_h: int
    earliest: int
    latest_end: int


def hourly_cost(rate_by_hour: dict[int, float], start: int, job: Job) -> float:
    """Compute total cost for a job start hour."""
    return sum(rate_by_hour[(start + i) % 24] * job.kw for i in range(job.duration_h))


def plan(jobs: list[Job], rate_by_hour: dict[int, float]) -> dict[str, tuple[int, float]]:
    """Plan each job at cheapest feasible start hour."""
    result: dict[str, tuple[int, float]] = {}
    for job in jobs:
        feasible_starts = range(job.earliest, job.latest_end - job.duration_h + 1)
        best_start = None
        best_cost = None
        for start in feasible_starts:
            cost = hourly_cost(rate_by_hour, start, job)
            if best_cost is None or cost < best_cost:
                best_start = start
                best_cost = cost
        if best_start is None or best_cost is None:
            raise ValueError(f"No feasible window for job: {job.name}")
        result[job.name] = (best_start, best_cost)
    return result
