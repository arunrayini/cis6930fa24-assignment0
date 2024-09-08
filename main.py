import argparse
import requests
import json

SEPARATOR = "þ"

def retrieve_data(page_num=1):
    """Retrieve data from the FBI API for a specified page."""
    api_url = f"https://api.fbi.gov/wanted/v1/list?page={page_num}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: HTTP Status {response.status_code}")

def format_data(fetched_data):
    """Format the retrieved data using thorn as a separator."""
    result = []
    
    for entry in fetched_data.get('items', []):
        case_title = entry.get('title', '')
        case_subjects = ','.join(entry.get('subjects', []))
        
        # Handle empty or missing field_offices
        fbi_offices = entry.get('field_offices', [])
        if not fbi_offices:
            fbi_offices = ''
        else:
            fbi_offices = ','.join(fbi_offices)
        
        result.append(f"{case_title}{SEPARATOR}{case_subjects}{SEPARATOR}{fbi_offices}")
    
    return "\n".join(result)

def execute(page_num=None, filepath=None):
    """Main function to handle data retrieval and formatting."""
    if page_num:
        data = retrieve_data(page_num)
    elif filepath:
        with open(filepath, 'r') as file:
            data = json.load(file)
    else:
        raise ValueError("You must provide either a page number or a file path")
    
    formatted_output = format_data(data)
    print(formatted_output)

if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser(description="Retrieve and format FBI Wanted data")
    argument_parser.add_argument("--page", type=int, help="Page number to retrieve data from the FBI API")
    argument_parser.add_argument("--file", type=str, help="Path to a local JSON file for testing")
    
    args = argument_parser.parse_args()
    execute(page_num=args.page, filepath=args.file)
