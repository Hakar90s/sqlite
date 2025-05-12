import os
import base64
import requests
import streamlit as st

# Load secrets
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
GITHUB_REPO = st.secrets["GITHUB_REPO"]
FILE_PATH = "mydatabase.db"
BRANCH = "main"

def push_database():
    try:
        # Read and encode the database
        with open(FILE_PATH, "rb") as f:
            content = f.read()
        b64_content = base64.b64encode(content).decode("utf-8")

        # Get file SHA (required for updates)
        url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{FILE_PATH}"
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }

        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            sha = res.json()["sha"]
        else:
            sha = None  # File does not exist yet

        payload = {
            "message": "Update mydatabase.db via Streamlit",
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
        st.error(f"Exception during push: {e}")

def pull_database():
    try:
        # Download the latest version from GitHub
        url = f"https://raw.githubusercontent.com/{GITHUB_REPO}/{BRANCH}/{FILE_PATH}"
        res = requests.get(url)

        if res.status_code == 200:
            with open(FILE_PATH, "wb") as f:
                f.write(res.content)
            st.success("✅ Pulled latest database from GitHub.")
        else:
            st.warning("⚠️ Could not pull database from GitHub.")

    except Exception as e:
        st.error(f"Exception during pull: {e}")
