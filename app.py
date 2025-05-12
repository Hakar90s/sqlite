import os
import base64
import requests
import streamlit as st

# Get secrets and remove quotes if they exist
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"].strip('"')
GITHUB_REPO = st.secrets["GITHUB_REPO"].strip('"')
FILE_PATH = "mydatabase.db"
BRANCH = "main"

def push_database():
    try:
        # Read and encode the file
        with open(FILE_PATH, "rb") as f:
            content = f.read()
        b64_content = base64.b64encode(content).decode("utf-8")

        url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{FILE_PATH}"
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }

        # Get SHA (required if file already exists)
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            sha = res.json()["sha"]
        else:
            sha = None

        payload = {
            "message": "Auto update mydatabase.db via Streamlit",
            "content": b64_content,
            "branch": BRANCH
        }
        if sha:
            payload["sha"] = sha

        res = requests.put(url, headers=headers, json=payload)

        if res.status_code in [200, 201]:
            st.success("✅ Database pushed successfully to GitHub!")
        else:
            st.error(f"❌ Push failed: {res.status_code}\n{res.json()}")

    except Exception as e:
        st.error(f"❌ Push error: {e}")
