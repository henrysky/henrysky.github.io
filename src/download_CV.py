import os
import json
import argparse
import subprocess


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download the latest artifacts from GitHub Actions")
    parser.add_argument("--token", type=str, help="Github Token", required=True)
    args = parser.parse_args()

    workflow_result = subprocess.run(
        [f"curl -L -H 'Accept: application/vnd.github+json' -H 'Authorization: Bearer {args.token}' -H 'X-GitHub-Api-Version: 2022-11-28' https://api.github.com/repos/henrysky/CV/actions/workflows/99959437/runs"],
        stdout=subprocess.PIPE,
        shell=True
    )
    artifacts_url = json.loads(workflow_result.stdout.decode("utf-8"))["workflow_runs"][0]["artifacts_url"]
    artifacts_result = subprocess.run(
        [f"curl -L -H 'Accept: application/vnd.github+json' -H 'Authorization: Bearer {args.token}' -H 'X-GitHub-Api-Version: 2022-11-28' {artifacts_url}"],
        stdout=subprocess.PIPE,
        shell=True
    )
    artifacts_id = json.loads(artifacts_result.stdout.decode("utf-8"))["artifacts"][0]["id"]
    artifacts_download = subprocess.run(
        [f"curl -L -H 'Accept: application/vnd.github+json' -H 'Authorization: Bearer {args.token}' -H 'X-GitHub-Api-Version: 2022-11-28' https://api.github.com/repos/henrysky/CV/actions/artifacts/{artifacts_id}/zip -O"],
        stdout=subprocess.PIPE,
        shell=True
    )
    os.rename("zip", "CV_PDFs.zip")
