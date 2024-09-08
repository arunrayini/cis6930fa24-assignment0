import pytest
from main import retrieve_data

def test_fetch_data_random_page():
    """Verify data retrieval from an arbitrary page of the FBI API."""
    # Retrieve data for page 3, as an example
    response_data = retrieve_data(3)
    
    # Ensure the response contains the 'items' key
    assert 'items' in response_data
    
    # Validate that 'items' is not an empty list
    assert len(response_data['items']) > 0
