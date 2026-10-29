import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
bank_df = pd.read_csv("bank.csv", sep=";")

# Suggested Visualization 1:
# Subscription percentage by job category

# Suggested Visualization 2:
# Subscription percentage by marital status

# Implement Visualization 1

# Calculate subscription rate by job
job_subscription = (
    bank_df.groupby("job")["y"]
    .apply(lambda x: (x == "yes").mean() * 100)
    .reset_index(name="subscription_rate")
)

# Create barplot
sns.barplot(
    data=job_subscription,
    x="job",
    y="subscription_rate",
    color="skyblue"
)

plt.title("Subscription Rate by Job")
plt.xlabel("Job Category")
plt.ylabel("Subscription Rate (%)")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()