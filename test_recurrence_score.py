import unittest

from recurrence_score import score_rows


class ScoreRowsTests(unittest.TestCase):
    def test_distinct_months_and_strong_bonus(self):
        rows = [
            {"video_id": "a", "month": "2026-08", "recommendation": "positive"},
            {"video_id": "a", "month": "2026-08", "recommendation": "positive"},
            {"video_id": "a", "month": "2026-09", "recommendation": "strong"},
        ]
        self.assertEqual(score_rows(rows)["a"], {"positive_months": 2, "strong_months": 1, "score": 2.5})

    def test_invalid_month_rejected(self):
        with self.assertRaises(ValueError):
            score_rows([{"video_id": "a", "month": "2026-13", "recommendation": "positive"}])


if __name__ == "__main__":
    unittest.main()
