
# Stock Price Alert with News and SMS Notifications

This project monitors stock prices using the **Alpha Vantage API**.
If the daily price change exceeds a set threshold (default: **5%**), it automatically fetches the latest news about the company from the **NewsAPI** and sends formatted alerts via **Twilio SMS**.

## Features

* Fetches **daily stock data** from Alpha Vantage.
* Calculates the **percentage change** between yesterday’s and the previous day’s closing prices.
* If change > 5% (configurable), fetches the **top 3 latest news articles**.
* Sends alerts as **SMS messages** with stock info + headlines.
* Supports **YAML configuration** for safer key management.

---

## Tech Stack

* **Python 3**
* [Alpha Vantage API](https://www.alphavantage.co/) (stock data)
* [NewsAPI](https://newsapi.org/) (company news)
* [Twilio API](https://www.twilio.com/) (SMS notifications)
* **requests** (HTTP requests)
* **twilio** (Python SDK for Twilio)
* **PyYAML** (load YAML config)

---

## Setup & Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/VasilisKokotakis/stock-alert-sms.git
   cd Stock-Price-Alert-with-News-and-SMS-Notifications-Alpha-Vantage-NewsAPI-Twilio-
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # on macOS/Linux
   venv\Scripts\activate     # on Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a configuration file** (`config.yaml`) in the root folder:

```yaml
STOCK_API_KEY: "your_alphavantage_api_key"
NEWS_API_KEY: "your_newsapi_key"
TWILIO_SID: "your_twilio_sid"
TWILIO_AUTH_TOKEN: "your_twilio_auth_token"
TWILIO_PHONE: "your Twilio number"
MY_PHONE: "your verified number"
```

---

## Usage

Run the script:

```bash
python main.py
```

If the stock moves more than **5%**, you’ll receive an SMS like:

```
TSLA: 🔺6%
Headline: Tesla announces new model.
Brief: The new release is expected to boost sales significantly.
```

---

## Notes

* Default threshold is **5%**, but you can change it in the script.
* Make sure your Twilio number is verified if you’re on a trial account.
* Alpha Vantage free tier has request limits (5 per minute / 500 per day).
* Use **YAML config** to avoid hardcoding sensitive credentials.

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.


