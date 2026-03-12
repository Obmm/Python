import pandas as pd

INPUT_FILE = "input.csv"


def load_data():
    return pd.read_csv(INPUT_FILE)


def salary_by_city(df):
    return df.groupby("city")["salary"].mean()


def top_salaries(df):
    return df.sort_values(by="salary", ascending=False).head(3)


def save_reports(city_salary, top_salary):
    city_salary.to_csv("salary_by_city.csv")
    top_salary.to_csv("top_salaries.csv", index=False)


def main():
    df = load_data()

    city_salary = salary_by_city(df)
    top_salary = top_salaries(df)

    save_reports(city_salary, top_salary)

    print("Relatórios gerados!")


if __name__ == "__main__":
    main()