import requests

webhook_url = "https://urbeena.app.n8n.cloud/webhook-test/bf2f1d1e-a561-4d99-b64a-92b200e54815"
def post_to_n8n(payload: dict):
    try:
        response = requests.post(webhook_url, json=payload)
        return response
    except Exception as e:
        print(f"Error sending data to n8n: {e}")
