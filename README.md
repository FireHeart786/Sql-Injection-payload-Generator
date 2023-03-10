# Sql-Injection-payload-Generator
WARNING!!
This code is just for the Educational Purpose Only.
The owner of the repo or code is not Responsible for any of its misuse.
# Important Notice
Note that using this code on a website without prior authorization from the website owner or legal authority is illegal and unethical. It's important to only use such tools for legitimate purposes and with proper authorization.


# Usage
python generate_payloads.py http://example.com --headers "User-Agent: Mozilla/5.0" --params "id:1;type:product"

This will generate payloads for http://example.com with a custom User-Agent header and query parameters id=1 and type=product. The payloads and their results will be saved to the payloads.txt file. The --headers and --params arguments are optional, and if not provided, no custom headers or parameters will be included in the requests. The --output argument specifies the file to save the generated payloads to, and defaults to payloads.txt if not provided.
