from pyspark.sql import SparkSession, DataFrame

def product_category_pairs(products: DataFrame, categories: DataFrame, product_categories: DataFrame) -> DataFrame:
    """
    Возвращает пары (product_name, category_name) для всех продуктов.
    Если у продукта нет категорий, то category_name будет None.
    """
    prod_with_links = products.join(
        product_categories,
        on="product_id",
        how="left"
    )

    result = prod_with_links.join(
        categories,
        on="category_id",
        how="left"
    ).select(
        "product_name",
        "category_name"
    )

    return result


def test_product_category_pairs():
    spark = SparkSession.builder \
        .master("local[1]") \
        .appName("test") \
        .getOrCreate()

    products = spark.createDataFrame([
        (1, "Apple"),
        (2, "Banana"),
        (3, "Carrot"),
        (4, "Doughnut"),
    ], ["product_id", "product_name"])

    categories = spark.createDataFrame([
        (10, "Fruits"),
        (20, "Vegetables"),
    ], ["category_id", "category_name"])

    product_categories = spark.createDataFrame([
        (1, 10),
        (2, 10),
        (3, 20),
    ], ["product_id", "category_id"])

    result = product_category_pairs(products, categories, product_categories)

    expected = {
        ("Apple", "Fruits"),
        ("Banana", "Fruits"),
        ("Carrot", "Vegetables"),
        ("Doughnut", None),
    }

    actual = set([tuple(row) for row in result.collect()])

    assert actual == expected


if __name__ == "__main__":
    test_product_category_pairs()
    print("Тест прошёл успешно.")
