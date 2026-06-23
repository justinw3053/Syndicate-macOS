# Textbook: POSTing JSON Payloads (KATA_NET_02)

## Theoretical Foundation
We send queries to LLMs or vector databases via HTTP POST. Unlike GET requests (where arguments are passed inside the URL string), POST requests transmit data payloads in the request body. We must explicitly declare the data format by passing the header `"Content-Type": "application/json"`.

---

## Step-by-Step Exercise Instructions
1. Serialize the dictionary payload to bytes using `json.dumps(payload).encode("utf-8")`.
2. Construct the request using `urllib.request.Request(url, data=bytes_data, headers={"Content-Type": "application/json"}, method="POST")`.
3. Query the server inside a `with urllib.request.urlopen(req) as resp:` block.
4. Read, decode, and return the response string.
