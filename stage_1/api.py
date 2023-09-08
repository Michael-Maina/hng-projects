#!/usr/bin/python3
"""
Simple API module
"""
from datetime import datetime, timezone
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/api', strict_slashes=False)
def index():
    """
    Reads URL parameters and returns JSON content
    """
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]

    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    repo_url = 'https://github.com/Michael-Maina/hng-projects',
    file_url = 'https://github.com/Michael-Maina/hng-projects/blob/master/stage_1/api.py'

    utc_time = datetime.now(timezone.utc)
    today = days[utc_time.weekday()]
    formatted_time = utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    output = {
        'slack_name': slack_name,
        'current_day': today,
        'utc_time': formatted_time,
        'track': track,
        'github_file_url': file_url,
        'github_repo_url': repo_url,
        'status_code': 200
    }
    return jsonify(output), 200


if __name__ == "__main__":
    app.run(port=3000, host='0.0.0.0')
