# Crypto Price Watch

A simple python app to watch the price of cryptocurrencies based on [CoinGecko API](https://www.coingecko.com/en/api#explore-api).

## Installation

Run a virtual env and install the packages.

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Watch List

Add your desired cryptocurrencies to `watch_list.txt` file. The default is:

```
bitcoin
ethereum
litecoin
dogecoin
```

### Run the app

Run the application with [watch linux command](https://www.geeksforgeeks.org/watch-command-in-linux-with-examples/) to update the prices.

```bash
watch -n 1 python app.py
```

**Note**: Here the time interval of updating is 1 second.

## Output

```bash
+----------+----------+
| Crypto   | Price    |
+----------+----------+
| litecoin | 140.4    |
| bitcoin  | 34810    |
| ethereum | 2230.27  |
| dogecoin | 0.249163 |
+----------+----------+
```

## Issues

In case of any issues, [Create an issue](https://github.com/daniyalmarofi/utattendance/issues/new/choose).

## About

Code by [Daniyal Marofi](https://github.com/daniyalmarofi).
