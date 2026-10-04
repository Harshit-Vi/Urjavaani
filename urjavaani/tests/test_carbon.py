from urjavaani.carbon.engine import Batch, batch_footprint


def test_batch_footprint_example() -> None:
    ef = {hour: 0.5 for hour in range(24)}
    batch = Batch(
        batch_id="B1",
        product="casting",
        good_units=10,
        kwh_by_hour={9: 100, 10: 100},
        scope1_kg_co2e=20,
    )

    result = batch_footprint(batch, ef)

    assert result["scope2_kg"] == 100
    assert result["total_kg"] == 120
    assert result["kg_per_unit"] == 12
