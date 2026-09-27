import os
import pytest

from pages.home_page import HomePage
from pages.products_page import ProductsPage
from utilities.csv_reader import CSVReader


data_file = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "test_data",
    "product_data.csv"
)


test_data = CSVReader.read_data(data_file)


@pytest.mark.parametrize("data", test_data)
def test_product_search(driver, data):

    home_page = HomePage(driver)

    products_page = ProductsPage(driver)

    home_page.click_products()

    products_page.search_product(
        data["product"]
    )

    result_title = products_page.get_search_results_title()

    assert "searched products" in result_title.lower()