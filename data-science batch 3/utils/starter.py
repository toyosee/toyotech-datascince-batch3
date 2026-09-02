import datetime as dt

current_date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

api_health = {
    "status": "Healthy",
    "date": current_date
}