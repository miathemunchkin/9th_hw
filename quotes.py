import json

def process_quotes(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    quotes = []
    for item in data:
        if 'text' in item:
            quotes.append(item)

    with open(output_file, 'w') as f:
        json.dump(quotes, f, ensure_ascii=False, indent=4)

process_quotes('quotes.json', 'quotes_processed.json')
