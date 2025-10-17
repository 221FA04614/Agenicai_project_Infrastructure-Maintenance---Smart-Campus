from pathlib import Path

import pandas as pd

from data.generate_fake_iot import generate_time_series
from ml.train_predictive_model import train_model


def test_train_and_predict_tmp(tmp_path: Path):
	df = generate_time_series(num_assets=5, hours=4, frequency_minutes=30, seed=123)
	model = train_model(df)
	features = ["temperature_c", "humidity_pct", "vibration_g", "power_kw", "usage_hours", "age_years"]
	latest_idx = df.groupby("asset_id")["timestamp"].idxmax()
	latest = df.loc[latest_idx]
	proba = model.predict_proba(latest[features].values)[:, 1]
	assert len(proba) == latest.shape[0]

