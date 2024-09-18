# WeatherBot

### Telegram: [click](https://t.me/handy_weather_bot)

**This bot was created using [Python](https://www.python.org/) and the [aiogram 3](https://aiogram.dev/) and [aoigram-dialog 2](https://github.com/Tishka17/aiogram_dialog) frameworks**

A handy bot for getting weather information.

Functions:
- View the current weather
- Forecast for several days
- Save your favourite places

Weather data API: [click](https://www.weatherapi.com/)


## How to start
1. Create a virtual environment.
```shell
python3 -m venv .venv
```

2. Activation of the of the virtual environment.
```shell
.venv/bin/activate
```

3. Install packages.
```shell
pip install -r requirements.txt
```

4. Run the program.
```shell
python3 run main.py
```

## Using Docker
1. Create image.
```shell
docker build -t weather-bot:latest .
```

2. Run Docker container.
```shell
docker run --name bot -d weather-bot:latest
```

3. View container logging.
```shell
docker container attach bot
```

4. Stop Docker container.
```shell
docker stop bot
```