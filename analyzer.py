import pandas as pd
import numpy as np

def risk_analysis(df):
    try:
        conditions = [
            (df["BP"] > 140) | (df["Sugar"] > 200),
            (df["BP"] > 120) | (df["Sugar"] > 140)
        ]

        choices = ["High Risk", "Medium Risk"]

        df["Risk"] = np.select(conditions, choices, default="Low Risk")

        print("\n📊 Risk Analysis:")
        print(df[["Name", "Village", "Risk"]])

    except Exception as e:
        print("❌ Error in risk analysis:", e)


def disease_analysis(df):
    try:
        print("\n🏥 Most Common Symptoms by Village:")
        result = df.groupby("Village")["Symptoms"].agg(lambda x: x.mode()[0])
        print(result)

    except Exception as e:
        print("❌ Error in disease analysis:", e)


def age_group_analysis(df):
    try:
        bins = [0, 20, 40, 60, 100]
        labels = ["0-20", "21-40", "41-60", "60+"]

        df["Age Group"] = pd.cut(df["Age"], bins=bins, labels=labels)

        print("\n👥 Age Group Most at Risk:")
        print(df.groupby("Age Group")["Risk"].value_counts())

    except Exception as e:
        print("❌ Error in age analysis:", e)


def compare_camps(df1, df2):
    try:
        avg_bp1 = df1["BP"].mean()
        avg_bp2 = df2["BP"].mean()

        print("\n📈 Camp Comparison:")
        print(f"Previous Avg BP: {avg_bp1}")
        print(f"Current Avg BP: {avg_bp2}")

        if avg_bp2 < avg_bp1:
            print("✅ Village health improving")
        else:
            print("⚠️ Health condition worsening")

    except Exception as e:
        print("❌ Error comparing camps:", e)