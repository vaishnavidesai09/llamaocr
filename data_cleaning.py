import pandas as pd
import re

# Load the Markdown content
with open('REVISE_DFS.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Helper function to extract markdown tables
def extract_tables(text):
    tables = re.findall(r'\|.*?\|\n(?:\|[-| ]+\|\n)?(?:\|.*?\|\n)+', text)
    return tables

# Convert each table to DataFrame and save to CSV
tables = extract_tables(text)

for i, table in enumerate(tables, start=1):
    lines = table.strip().split('\n')
    header = lines[0].strip('|').split('|')
    data = [line.strip('|').split('|') for line in lines[2:] if '---' not in line]

    # Clean whitespace
    header = [h.strip() for h in header]
    data = [[cell.strip() for cell in row] for row in data]

    # Save to CSV with pipe delimiter
    df = pd.DataFrame(data, columns=header)
    df.to_csv(f'table_{i}.csv', sep='|', index=False)

    print(f"Saved table_{i}.csv with shape {df.shape}")
