import pandas as pd
import matplotlib.pyplot as plt

# Load evaluation results
df = pd.read_csv("../data/model_responses.csv")

print("Medical LLM Evaluation Results")
print("=" * 40)

print("\nDataset size:")
print(df.shape)

print("\nPrompt strategies:")
print(df["prompt_strategy"].value_counts())

print("\nAverage overall score by prompt strategy:")
strategy_scores = (
    df.groupby("prompt_strategy")["overall_score"]
    .mean()
    .sort_values(ascending=False)
)

print(strategy_scores)
