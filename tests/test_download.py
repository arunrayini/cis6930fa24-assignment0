import pytest
from main import retrieve_data

def test_fetch_data_from_api():
    """Verify data is retrieved from the FBI API."""
    # Retrieve data for the first page
    response_data = retrieve_data(1)
    
    # Ensure 'items' key is present in the response
    assert 'items' in response_data
    
    # Validate that the 'items' list contains entries
    assert len(response_data['items']) > 0
