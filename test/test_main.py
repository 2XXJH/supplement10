import pytest
import sys
import os
from pymongo import MongoClient
from my_module import (
    create_random_document,
    save_document,
    find_document_by_uuid,
    update_document_field,
    delete_document_by_uuid,
)

client = MongoClient("mongodb://localhost:27017/")
db = client["test_db"]
collection = db["test_collection"]

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    # Clear the collection before and after each test
    collection.delete_many({})
    yield
    collection.delete_many({})
