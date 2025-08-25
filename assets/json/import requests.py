import requests
import json
from datetime import datetime, timedelta

# Strava API credentials
ACCESS_TOKEN = <<access token here>>
ATHLETE_ID = <<id here>>

# Fetch the latest activities
def get_activities():
    url = "https://www.strava.com/api/v3/athlete/activities"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    params = {"per_page": 50}  # Fetch latest 50 activities
    
    response = requests.get(url, headers=headers, params=params)
    activities = response.json()
    
    print(activities)
    # Filter only running activities
    runs = [act for act in activities if act["type"] == "Run"]
    
    if not runs:
        return None

    latest_run = runs[0]
    latest_activity = {
        "date": latest_run["start_date_local"].split("T")[0],
        "distance": f"{latest_run['distance'] / 1000:.1f} km",
        "time": f"{int(latest_run['moving_time'] // 60)}:{int(latest_run['moving_time'] % 60):02d}",
        "pace": f"{(latest_run['moving_time'] / (latest_run['distance'] / 1000)):.2f} min/km"
    }
    
    return latest_activity, runs

# Aggregate data for weekly & monthly statistics
def get_stats(runs):
    monthly_stats = {}
    weekly_stats = {}

    for run in runs:
        date = datetime.strptime(run["start_date_local"], "%Y-%m-%dT%H:%M:%SZ")
        month = date.strftime("%b")
        week = f"Week {date.isocalendar()[1]}"

        # Monthly aggregation
        monthly_stats[month] = monthly_stats.get(month, 0) + run["distance"] / 1000

        # Weekly aggregation
        weekly_stats[week] = weekly_stats.get(week, 0) + run["distance"] / 1000

    # Convert to list format
    monthly_data = [{"month": k, "distance": v} for k, v in monthly_stats.items()]
    weekly_data = [{"week": k, "distance": v} for k, v in weekly_stats.items()]

    return monthly_data, weekly_data

def save_data():
    latest_activity, runs = get_activities()
    if not latest_activity:
        print("No running activities found.")
        return

    monthly_stats, weekly_stats = get_stats(runs)

    data = {
        "latest_activity": latest_activity,
        "monthly_stats": monthly_stats,
        "weekly_stats": weekly_stats
    }

    with open("assets/json/running_stats.json", "w") as f:
        json.dump(data, f, indent=4)

    
    print("Updated running_stats.json successfully.")

# Run the script
save_data()
