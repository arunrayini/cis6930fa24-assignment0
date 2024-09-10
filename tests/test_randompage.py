import pytest
from main import retrieve_data, format_data

def test_random_page_retrieval():
    """Ensure data can be retrieved from a random page of the FBI API."""
    result = retrieve_data(4)
    assert 'items' in result, "'items' not found in API response."
    assert len(result['items']) > 0, "No data found in the 'items' list for page 4."

def test_thorn_formatted_output():
    """Test that formatted output is correctly thorn-separated (þ) for all fields."""
    test_data = {
        "items": [
            {
                "title": "Organized Crime Investigation",
                "subjects": ["Gang Leader", "Drug Trafficking"],
                "field_offices": ["Houston", "Phoenix"]
            }
        ]
    }
    thorn_output = format_data(test_data)
    expected_output = "Organized Crime InvestigationþGang Leader,Drug TraffickingþHouston,Phoenix"
    assert thorn_output == expected_output, f"Unexpected formatted output: {thorn_output}"
