import json

def remove_duplicates(data_list):
    seen = set()
    unique_data = []

    for item in data_list:
        item_frozen = frozenset(item.items())
        if item_frozen not in seen:
            seen.add(item_frozen)
            unique_data.append(item)

    return unique_data

def lambda_handler(event, context):
    try:
        # Decode stringified body from API Gateway
        if "body" in event:
            body = json.loads(event["body"])
        else:
            body = event  # fallback for local test

        # Safely get records
        records = body.get("records")
        if records is None:
            raise ValueError("Missing 'records' in request body")

        cleaned_data = remove_duplicates(records)

        return {
            "statusCode": 200,
            "body": json.dumps({"cleaned_records": cleaned_data})
        }

    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }
