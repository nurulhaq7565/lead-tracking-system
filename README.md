# Lead Tracking & Analytics Backend System

A backend lead tracking system built using Flask and SQLite.

## Features

- Create leads
- Generate unique lead IDs
- Store lead data in database
- Track supplier clicks
- View all leads
- View click tracking data
- REST API architecture

## Tech Stack

- Python
- Flask
- SQLite
- SQLAlchemy

## API Routes

### Create Lead

POST /create-lead

### Get All Leads

GET /leads

### Track Click

POST /track-click

### Get Click Logs

GET /clicks

## Run Project

1. Activate virtual environment

```bash
.\venv\Scripts\activate
```

2. Run Flask server

```bash
python app.py
```

## Author

Nurul Haq