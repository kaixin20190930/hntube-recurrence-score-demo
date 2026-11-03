"""Illustrative recurring-recommendation score for user-supplied CSV data."""

import csv
import re
import sys
from collections import defaultdict
from pathlib import Path


def score_rows(rows):
    months = defaultdict(lambda: {"positive": set(), "strong": set()})
    for row in rows:
        video_id = row["video_id"].strip()
        month = row["month"].strip()
        recommendation = row["recommendation"].strip().lower()
        if not video_id or not re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])", month):
            raise ValueError(f"Invalid video_id or month: {row!r}")
        if recommendation not in {"positive", "strong"}:
            raise ValueError(f"Invalid recommendation: {recommendation!r}")
        months[video_id]["positive"].add(month)
        if recommendation == "strong":
            months[video_id]["strong"].add(month)
    return {
        video_id: {
            "positive_months": len(values["positive"]),
            "strong_months": len(values["strong"]),
            "score": len(values["positive"]) + 0.5 * len(values["strong"]),
        }
        for video_id, values in months.items()
    }


def main(path):
    with Path(path).open(newline="", encoding="utf-8") as handle:
        rows = csv.DictReader(handle)
        if rows.fieldnames != ["video_id", "month", "recommendation"]:
            raise ValueError("Expected CSV columns: video_id,month,recommendation")
        results = score_rows(rows)
    print("video_id,positive_months,strong_months,score")
    for video_id, values in sorted(results.items(), key=lambda item: (-item[1]["score"], item[0])):
        print(f"{video_id},{values['positive_months']},{values['strong_months']},{values['score']:.1f}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 recurrence_score.py <recommendations.csv>")
    main(sys.argv[1])
