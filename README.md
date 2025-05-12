### 📄 `README.md`

````markdown
# 🌦️ Celery Climate App

This is a simple asynchronous Python application that uses **Celery** and **Redis** to fetch real-time weather data (temperature and humidity) from the [Open-Meteo API](https://open-meteo.com/). It demonstrates parallel task execution and how to coordinate results using Celery workers.

---

## 🚀 Features

- Fetches **temperature** and **humidity** for a user-provided location.
- Runs both fetches as **Celery background tasks**.
- Supports calculation of:
  - Average
  - Median
  - Standard Deviation
- Prints the first completed result immediately and waits for the other.

---

## 🧱 Tech Stack

- **Python**
- **Celery** (for asynchronous task management)
- **Redis** (as message broker)
- **Open-Meteo API** (no API key needed)

---

## 📦 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/celery-climate-app.git
   cd celery-climate-app
````

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Start Redis** (if using Docker):

   ```bash
   docker run -d -p 6379:6379 redis
   ```

---

## 🧪 Running the App

### 1. Start the Celery workers (in separate terminals)

```bash
# Terminal 1
celery -A app worker -Q temperature --loglevel=info --pool=solo

# Terminal 2
celery -A app worker -Q humidity --loglevel=info --pool=solo
```

### 2. Run the orchestrator script

```bash
# From the project root
python -m app.main
```

You'll be prompted to enter a latitude and longitude, and select a statistical operation.

---

## 🗂️ Project Structure

```
celery_climate_app/
├── app/
│   ├── __init__.py
│   ├── main.py          # User orchestrator script
│   ├── tasks.py         # Celery tasks
│   └── climate_api.py   # Open-Meteo API fetch logic
├── celeryconfig.py      # Celery config
├── requirements.txt
└── README.md
```

---

## ✅ Example Output

```
Fetching weather data (async)...
Waiting for remaining result...

✅ Humidity result is ready: 88.50%
Waiting for remaining result...

✅ Temperature result is ready: 17.45°C
```

---

## 🧠 Tips

* Tasks are assigned to specific **queues** for true parallelism.
* You can experiment with `time.sleep()` in `climate_api.py` to simulate network delay.
* Try using different coordinates for different cities.

---

## 📃 License

MIT License – feel free to use, modify, and learn from it.
