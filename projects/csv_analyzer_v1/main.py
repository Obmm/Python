import pandas as pd

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.csv"


def load_data(file_path):
    return pd.read_csv(file_path)


def analyze_data(df):
    report = {}
    report["Average Salary"] = df["salary"].mean()
    report["Max Salary"] = df["salary"].max()
    report["Count by City"] = df["city"].value_counts().to_dict()
    return report


def save_report(report, file_path):
    # Transformar dicionário em DataFrame para salvar como CSV
    df_report = pd.DataFrame([
        {"Metric": k, "Value": v} for k, v in report.items()
    ])
    df_report.to_csv(file_path, index=False)


def main():
    df = load_data(INPUT_FILE)
    report = analyze_data(df)
    save_report(report, OUTPUT_FILE)
    print("Análise concluída!")


if __name__ == "__main__":
    main()