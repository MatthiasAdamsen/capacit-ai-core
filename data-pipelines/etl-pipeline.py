import pandas as pd

def run_etl_pipeline(source_path: str, target_path: str):
    print(f"Starting ETL pipeline for Capacit AI Core...")
    # Load data
    # df = pd.read_csv(source_path)
    # Transform
    # df_clean = df.dropna()
    # Save
    print(f"Data transformed and saved to {target_path}")

if __name__ == "__main__":
    run_etl_pipeline("raw_data.csv", "processed_data.csv")