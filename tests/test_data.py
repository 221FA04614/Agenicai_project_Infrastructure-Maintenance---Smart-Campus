import pandas as pd

from data.generate_fake_iot import generate_time_series


def test_generate_time_series_basic():
	df = generate_time_series(num_assets=5, hours=4, frequency_minutes=30, seed=123)
	# Expect at least one row per time step per asset
	assert not df.empty
	assert {"temperature_c", "vibration_g", "power_kw", "humidity_pct", "usage_hours", "age_years"} <= set(df.columns)
	# Failure label exists
	assert "failure_within_30d" in df.columns

