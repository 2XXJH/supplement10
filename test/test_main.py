import pytest
import sys
import os
from pymongo import MongoClient
from src.my_module import create_random_document
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from src.my_module import (
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

def test_create_random_document():
    document = create_random_document()
    assert "UUID" in document
    assert isinstance(document["UUID"], str)
    assert len(document["UUID"]) > 0

def test_save_document():
    document = create_random_document()
    inserted_id = save_document(document)
    assert inserted_id is not None
    saved_doc = collection.find_one({"_id": inserted_id})
    assert saved_doc["UUID"] == document["UUID"]

def test_find_document_by_uuid():
    document = create_random_document()
    save_document(document)
    found_doc = find_document_by_uuid(document["UUID"])
    assert found_doc is not None
    assert found_doc["UUID"] == document["UUID"]

def test_update_document_field():
    document = create_random_document()
    save_document(document)
    update_document_field(document["UUID"], "name", "Updated Name")
    updated_doc = find_document_by_uuid(document["UUID"])
    assert updated_doc["name"] == "Updated Name"

def test_delete_document_by_uuid():
    document = create_random_document()
    save_document(document)
    delete_document_by_uuid(document["UUID"])
    deleted_doc = find_document_by_uuid(document["UUID"])
    assert deleted_doc is None
