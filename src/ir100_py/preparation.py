from pathlib import Path

import polars as pl


def load_data(path: Path) -> pl.DataFrame:
    return pl.read_parquet(path)


def print_sample(df: pl.DataFrame) -> None:
    for _ in range(3):
        print(df.sample())


def make_en_data() -> tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame]:
    item_path = Path(
        "/Users/tsuchiya/workspace/esci-data/shopping_queries_dataset/shopping_queries_dataset_products.parquet"
    )
    query_path = Path(
        "/Users/tsuchiya/workspace/esci-data/shopping_queries_dataset/shopping_queries_dataset_examples.parquet"
    )

    en_item = load_data(item_path).filter(pl.col("product_locale") == "us")
    en_query = load_data(query_path).filter(pl.col("product_locale") == "us")
    en_joined = en_query.join(en_item, on="product_id")

    return en_item, en_query, en_joined
