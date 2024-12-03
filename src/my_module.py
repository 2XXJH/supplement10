import pymongo
import uuid

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["test_db"]
collection = db["test_collection"]

def create_random_document():
    """
    Creates a random MongoDB document with a unique UUID field.

    The generated document includes:
        - UUID: A string representation of a version 4 UUID.
        - name: A placeholder string "Random Name".
        - value: An integer, e.g., 42.
        - active: A boolean, set to True.

    Returns:
        dict: The generated document with all fields.
    """
    document = {
        "UUID": str(uuid.uuid4()),  # Generate a version 4 UUID
        "name": "Random Name",
        "value": 42,
        "active": True
    }
    return document

def save_document(document):
    """
    Saves a MongoDB document to the specified collection.

    Args:
        document (dict): The document to be inserted into the database.

    Returns:
        ObjectId: The unique ID of the inserted document.
    """
    return collection.insert_one(document).inserted_id

def find_document_by_uuid(uuid_str):
    """
    Retrieves a document from the MongoDB collection based on its UUID.

    Args:
        uuid_str (str): The UUID of the document to retrieve.

    Returns:
        dict or None: The document matching the UUID, or None if not found.
    """
    return collection.find_one({"UUID": uuid_str})

def update_document_field(uuid_str, field, value):
    """Updates a field in a MongoDB document by UUID."""
    return collection.update_one({"UUID": uuid_str}, {"$set": {field: value}})

def delete_document_by_uuid(uuid_str):
     """
    Deletes a document from the MongoDB collection based on its UUID.

    Args:
        uuid_str (str): The UUID of the document to delete.

    Returns:
        DeleteResult: The result of the delete operation.
    """
    return collection.delete_one({"UUID": uuid_str})
