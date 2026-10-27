import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

TARGET = "Churn"
NUMERIC_COLS = ["tenure", "MonthlyCharges", "TotalCharges"]
CATEGORICAL_COLS = ["gender", "Contract"]


def make_synthetic_data(n=2000, seed=42):
    rng = np.random.default_rng(seed)
    contract = rng.choice(["Month-to-month", "One year", "Two year"],
                          size=n, p=[0.55, 0.25, 0.20])
    tenure = rng.integers(0, 73, size=n)
    monthly = np.round(rng.normal(65, 25, size=n).clip(18, 120), 2)
    total = np.round(tenure * monthly, 2)

    p = (0.10
         + 0.25 * (contract == "Month-to-month")
         - 0.002 * tenure
         + 0.002 * (monthly - 65))
    churn = np.where(rng.random(n) < p.clip(0.02, 0.9), "Yes", "No")

    df = pd.DataFrame({
        "customerID": [f"C{i:05d}" for i in range(n)],
        "gender": rng.choice(["Male", "Female"], size=n),
        "SeniorCitizen": rng.choice([0, 1], size=n, p=[0.84, 0.16]),
        "tenure": tenure,
        "Contract": contract,
        "MonthlyCharges": monthly,
        "TotalCharges": total.astype(object),
        "Churn": churn,
    })

    df.loc[rng.choice(n, 15, replace=False), "TotalCharges"] = " "
    df.loc[rng.choice(n, 40, replace=False), "MonthlyCharges"] = np.nan
    df.loc[rng.choice(n, 25, replace=False), "gender"] = np.nan
    df = pd.concat([df, df.sample(10, random_state=1)], ignore_index=True)
    return df


def load_data():
    if len(sys.argv) > 1:
        print(f"Loading {sys.argv[1]} ...")
        return pd.read_csv(sys.argv[1])
    print("No CSV given - using synthetic data.")
    return make_synthetic_data()


def inspect(df):
    print("\n" + "=" * 60 + "\nBASIC INFO\n" + "=" * 60)
    print("Shape:", df.shape)
    print("\nData types:\n", df.dtypes)
    print("\nFirst 5 rows:\n", df.head())
    print("\nMissing values per column:\n", df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())


def clean(df):
    print("\n" + "=" * 60 + "\nCLEANING\n" + "=" * 60)
    df = df.copy()

    before = len(df)
    df = df.drop_duplicates()
    print(f"Removed {before - len(df)} duplicate rows")

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)
    df = df.replace("", np.nan)

    for col in NUMERIC_COLS:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    for col in NUMERIC_COLS:
        n_missing = df[col].isnull().sum()
        if n_missing:
            df[col] = df[col].fillna(df[col].median())
            print(f"Filled {n_missing} missing in '{col}' with median")

    for col in CATEGORICAL_COLS:
        n_missing = df[col].isnull().sum()
        if n_missing:
            df[col] = df[col].fillna(df[col].mode()[0])
            print(f"Filled {n_missing} missing in '{col}' with mode")

    for col in NUMERIC_COLS:
        q1, q3 = df[col].quantile([0.25, 0.75])
        iqr = q3 - q1
        low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        n_out = ((df[col] < low) | (df[col] > high)).sum()
        df[col] = df[col].clip(low, high)
        print(f"'{col}': capped {n_out} outliers to [{low:.1f}, {high:.1f}]")

    df["ChurnFlag"] = np.where(df[TARGET] == "Yes", 1, 0)
    print("\nMissing values after cleaning:", int(df.isnull().sum().sum()))
    return df


def summarize(df):
    print("\n" + "=" * 60 + "\nSUMMARY STATISTICS\n" + "=" * 60)
    print(df[NUMERIC_COLS].describe().round(2))

    churn_rate = df["ChurnFlag"].mean() * 100
    print(f"\nOverall churn rate: {churn_rate:.1f}%")

    print("\nMean of numeric features by churn status:")
    print(df.groupby(TARGET)[NUMERIC_COLS].mean().round(2))

    for col in CATEGORICAL_COLS:
        print(f"\nChurn rate (%) by {col}:")
        print((df.groupby(col)["ChurnFlag"].mean() * 100).round(1))

    print("\nCorrelation with churn:")
    corr = df[NUMERIC_COLS + ["SeniorCitizen", "ChurnFlag"]].corr()
    print(corr["ChurnFlag"].drop("ChurnFlag").round(3))
    return corr


def visualize(df, corr):
    print("\nSaving plots ...")
    fig, axes = plt.subplots(2, 3, figsize=(16, 9))
    fig.suptitle("Customer Churn - EDA", fontsize=16)

    counts = df[TARGET].value_counts()
    axes[0, 0].bar(counts.index, counts.values, color=["#4c72b0", "#dd8452"])
    axes[0, 0].set_title("Churn Distribution")
    axes[0, 0].set_ylabel("Customers")

    for label, color in [("No", "#4c72b0"), ("Yes", "#dd8452")]:
        axes[0, 1].hist(df.loc[df[TARGET] == label, "tenure"],
                        bins=20, alpha=0.6, label=label, color=color)
    axes[0, 1].set_title("Tenure by Churn")
    axes[0, 1].set_xlabel("Months")
    axes[0, 1].legend(title="Churn")

    data = [df.loc[df[TARGET] == k, "MonthlyCharges"] for k in ["No", "Yes"]]
    axes[0, 2].boxplot(data)
    axes[0, 2].set_xticks([1, 2], ["No", "Yes"])
    axes[0, 2].set_title("Monthly Charges by Churn")
    axes[0, 2].set_ylabel("$")

    rate = (df.groupby("Contract")["ChurnFlag"].mean() * 100).sort_values()
    axes[1, 0].barh(rate.index, rate.values, color="#c44e52")
    axes[1, 0].set_title("Churn Rate (%) by Contract")

    buckets = pd.cut(df["tenure"], bins=[-1, 12, 24, 48, 72],
                     labels=["0-12", "13-24", "25-48", "49-72"])
    rate_t = df.groupby(buckets, observed=True)["ChurnFlag"].mean() * 100
    axes[1, 1].plot(rate_t.index.astype(str), rate_t.values, marker="o")
    axes[1, 1].set_title("Churn Rate (%) by Tenure Bucket")
    axes[1, 1].set_xlabel("Months")

    im = axes[1, 2].imshow(corr.values, cmap="coolwarm", vmin=-1, vmax=1)
    axes[1, 2].set_xticks(range(len(corr)))
    axes[1, 2].set_yticks(range(len(corr)))
    axes[1, 2].set_xticklabels(corr.columns, rotation=45, ha="right")
    axes[1, 2].set_yticklabels(corr.columns)
    for i in range(len(corr)):
        for j in range(len(corr)):
            axes[1, 2].text(j, i, f"{corr.values[i, j]:.2f}",
                            ha="center", va="center", fontsize=8)
    axes[1, 2].set_title("Correlation Heatmap")
    fig.colorbar(im, ax=axes[1, 2], fraction=0.046)

    plt.tight_layout()
    plt.savefig("churn_eda.png", dpi=150)
    print("Saved: churn_eda.png")


def findings(df):
    print("\n" + "=" * 60 + "\nKEY FINDINGS\n" + "=" * 60)
    worst = (df.groupby("Contract")["ChurnFlag"].mean() * 100).idxmax()
    t_churn = df.loc[df["ChurnFlag"] == 1, "tenure"].mean()
    t_stay = df.loc[df["ChurnFlag"] == 0, "tenure"].mean()
    m_churn = df.loc[df["ChurnFlag"] == 1, "MonthlyCharges"].mean()
    m_stay = df.loc[df["ChurnFlag"] == 0, "MonthlyCharges"].mean()

    print(f"- Highest churn contract type : {worst}")
    print(f"- Avg tenure   churned vs stayed: {t_churn:.1f} vs {t_stay:.1f} months")
    print(f"- Avg monthly  churned vs stayed: {m_churn:.1f} vs {m_stay:.1f}")


if __name__ == "__main__":
    raw = load_data()
    inspect(raw)
    clean_df = clean(raw)
    corr_matrix = summarize(clean_df)
    visualize(clean_df, corr_matrix)
    findings(clean_df)
    clean_df.to_csv("churn_cleaned.csv", index=False)
    print("\nSaved: churn_cleaned.csv")
