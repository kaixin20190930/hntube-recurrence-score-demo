# Recurring recommendations: a small reproducible example

HN Tube ranks technical videos partly by repeated positive recommendations across calendar months. Its [publication methodology](https://hntube.app/methodology/) describes the score as distinct positive months plus half the number of distinct strong-recommendation months. Multiple comments in the same month do not multiply the score.

This standalone Python example shows how to calculate that score from **your own CSV**. It is an educational illustration, not HN Tube's production code or a download of its dataset. It does not determine whether a video is eligible, accurately labelled, or good teaching material.

```sh
python3 recurrence_score.py examples/synthetic_recommendations.csv
python3 -m unittest discover -s tests
```

Input columns are `video_id`, `month` (`YYYY-MM`), and `recommendation` (`positive` or `strong`). A strong recommendation counts for both the positive-month and strong-month sets. In the synthetic example, video A has positive recommendations in two different months and a strong recommendation in one of them, so its score is `2.5`. Repeating a positive comment in the same month does not change it.

Use the score to examine *recurring attention*, not to infer accuracy or universal approval. Newer videos have had less time to accumulate distinct months. For the actual curated video index and its caveats, see [HN Tube](https://hntube.app/).
