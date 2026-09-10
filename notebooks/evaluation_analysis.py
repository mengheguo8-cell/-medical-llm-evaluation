import pandas as pd
import matplotlib.pyplot as plt

# Load evaluation results
df = pd.read_csv("data/model_responses.csv")

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
# Visualize prompt strategy performance
plt.figure(figsize=(8, 5))

strategy_scores.plot(kind="bar")

plt.title("Medical LLM Prompt Strategy Performance")
plt.xlabel("Prompt Strategy")
plt.ylabel("Average Overall Score")
plt.ylim(0, 5.5)

plt.xticks(rotation=0)
plt.tight_layout()

# Save figure
plt.savefig("results/figures/prompt_strategy_comparison.png", dpi=300)

print("\nFigure saved as results/figures/prompt_strategy_comparison.png")