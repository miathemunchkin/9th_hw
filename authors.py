import json

def process_authors(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    authors = []
    for item in data:
        if 'name' in item:
            authors.append(item)

    with open(output_file, 'w') as f:
        json.dump(authors, f, ensure_ascii=False, indent=4)

process_authors('quotes.json', 'authors.json')
