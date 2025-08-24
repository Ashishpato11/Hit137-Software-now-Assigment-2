#!/usr/bin/env python3
"""
Question 2 – Temperature analysis for monthly station CSVs.
Looks for files named stations_group_YYYY.csv in ./temperatures.
Writes: average_temp.txt, largest_temp_range_station.txt, temperature_stability_stations.txt
Saves: tidy_temperatures.csv
"""
from pathlib import Path
import pandas as pd, re

BASE = Path(__file__).resolve().parent
TEMPS = BASE / "temperatures"
OUT_AVG = BASE / "average_temp.txt"
OUT_RANGE = BASE / "largest_temp_range_station.txt"
OUT_STAB = BASE / "temperature_stability_stations.txt"
TIDY = BASE / "tidy_temperatures.csv"

SEASONS = {"Summer": (12,1,2), "Autumn": (3,4,5), "Winter": (6,7,8), "Spring": (9,10,11)}
MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"]
M2N = {m:i+1 for i,m in enumerate(MONTHS)}

def load_tidy():
    frames = []
    for fp in sorted(TEMPS.glob("stations_group_*.csv")):
        m = re.search(r"(\d{4})", fp.name)
        year = int(m.group(1)) if m else None
        df = pd.read_csv(fp)
        name_col = next((c for c in df.columns if str(c).upper() in ("STATION_NAME","NAME","STATION")), None)
        id_col = next((c for c in df.columns if str(c).upper() in ("STN_ID","STATION_ID","ID")), None)
        month_cols = [c for c in df.columns if c in MONTHS]
        if not month_cols or name_col is None or id_col is None:
            continue
        tidy = df[[name_col, id_col] + month_cols].melt(
            id_vars=[name_col, id_col], var_name="month_name", value_name="temperature_c")
        tidy["year"] = year
        tidy["month"] = tidy["month_name"].map(M2N).astype("Int64")
        tidy["temperature_c"] = pd.to_numeric(tidy["temperature_c"], errors="coerce")
        tidy = tidy.dropna(subset=["temperature_c","month"]).rename(
            columns={name_col:"station_name", id_col:"station_id"})
        tidy = tidy[["station_id","station_name","year","month","temperature_c"]]
        frames.append(tidy)
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame(
        columns=["station_id","station_name","year","month","temperature_c"])

def seasonal_average(df):
    lines = []
    for s, months in SEASONS.items():
        vals = df[df["month"].isin(months)]["temperature_c"].dropna()
        lines.append(f"{s}: {vals.mean():.1f}°C" if not vals.empty else f"{s}: N/A")
    return "\n".join(lines)

def largest_range(df):
    if df.empty: return "No data."
    g = df.groupby(["station_id","station_name"])["temperature_c"]
    stats = g.agg(["min","max"]); stats["range"] = stats["max"] - stats["min"]
    idx = stats["range"].idxmax(); row = stats.loc[idx]
    return f"{idx[1]} (Station {idx[0]}): Range {row['range']:.1f}°C (Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)"

def stability(df):
    if df.empty: return "No data."
    g = df.groupby(["station_id","station_name"])["temperature_c"]
    stds = g.std(ddof=0); min_idx = stds.idxmin(); max_idx = stds.idxmax()
    return (f"Most Stable: {min_idx[1]} (Station {min_idx[0]}): StdDev {stds.loc[min_idx]:.1f}°C\n"
            f"Most Variable: {max_idx[1]} (Station {max_idx[0]}): StdDev {stds.loc[max_idx]:.1f}°C")

def main():
    df = load_tidy()
    df.to_csv(TIDY, index=False)
    OUT_AVG.write_text(seasonal_average(df), encoding="utf-8")
    OUT_RANGE.write_text(largest_range(df), encoding="utf-8")
    OUT_STAB.write_text(stability(df), encoding="utf-8")
    print("Wrote:", OUT_AVG.name, OUT_RANGE.name, OUT_STAB.name)

if __name__ == "__main__":
    main()
