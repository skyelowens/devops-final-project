import os
import sys
import requests

WEBEX_TOKEN = os.getenv("WEBEX_TOKEN")
WEBEX_ROOM_ID = os.getenv("WEBEX_ROOM_ID")

status = sys.argv[1] if len(sys.argv) > 1 else "unknown"
build_number = sys.argv[2] if len(sys.argv) > 2 else "N/A"

if status == "success":
    message = f"✅ Deployment successful! Build #{build_number} has been deployed."
elif status == "failure":
    message = f"❌ Deployment failed for Build #{build_number}. Check Jenkins logs."
else:
    message = f"ℹ️ Build #{build_number} finished with status: {status}."

url = "https://webexapis.com/v1/messages"
headers = {
    "Authorization": f"Bearer {WEBEX_TOKEN}",
    "Content-Type": "application/json"
}
data = {
    "roomId": WEBEX_ROOM_ID,
    "text": message
}

response = requests.post(url, json=data, headers=headers)
print(response.status_code, response.text)

