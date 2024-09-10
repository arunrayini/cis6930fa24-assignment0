import pytest
from main import retrieve_data

def test_data_retrieval():
    """Ensure non-empty data is fetched from the FBI API for a specific page."""
    # Fetch the data for page 1
    result = retrieve_data(1)
    
    # Check if 'items' key exists
    assert 'items' in result, "Expected 'items' key in the API response."
    
    # Ensure 'items' contains data
    assert len(result['items']) > 0, "Expected non-empty 'items' in the API response."

def test_title_field_extraction():
    """Validate that the 'title' field is correctly extracted from API data."""
    # Fetch data and check the first entry's title
    data = retrieve_data(1)
    first_item = data['items'][0]
    assert first_item.get('title'), "Expected 'title' field to be present and non-empty."

def test_subjects_field_extraction():
    """Check if the 'subjects' field is extracted and formatted correctly."""
    data = retrieve_data(1)
    first_item = data['items'][0]
    subjects = first_item.get('subjects', [])
    assert len(subjects) > 0, "Expected 'subjects' field to have at least one entry."

def test_field_offices_extraction():
    """Ensure that the 'field_offices' field is extracted properly."""
    data = retrieve_data(1)
    first_item = data['items'][0]
    field_offices = first_item.get('field_offices', [])
    assert len(field_offices) > 0, "Expected 'field_offices' to contain at least one entry."

