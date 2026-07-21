# UberEats Restaurant Scraper

## Overview

UberEats Restaurant Scraper is a Flask-based web application that automates the extraction of restaurant information and menu data from UberEats using SeleniumBase. The application extracts structured restaurant details, menu items, and JSON data efficiently.

## Features

- Extract UberEats restaurant details
- Scrape menu items
- Extract structured JSON data
- Scrape DoorDash restaurant data
- Export scraped data into JSON format
- Flask-based API interface
- Organized and reusable scraper modules

## Technologies Used

- Python
- Flask
- SeleniumBase
- Selenium
- JSON
- HTML
- CSS

## Project Structure

```text
UberEats-Restaurant-Scraper/
│
├── ubereats.py
├── extract_json.py
├── doordash.py
├── doordash_roma.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── restaurant_detail.json
├── ubereats_menu_18344.json
└── ubereats_menu_18345.json
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Damalaamulya/UberEats-Restaurant-Scraper.git
```

### 2. Navigate to the project directory

```bash
cd UberEats-Restaurant-Scraper
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python ubereats.py
```

The Flask application will start at:

```text
http://127.0.0.1:5000
```

## Output Files

The scraper generates structured JSON files containing extracted data:

- `restaurant_detail.json`
- `ubereats_menu_18344.json`
- `ubereats_menu_18345.json`

## Future Improvements

- Export data to Excel and CSV
- Improve scraping performance
- Add advanced filtering options
- Enhance API functionality
- Improve error handling and logging
- Support additional food delivery platforms

## License

This project is intended for educational and portfolio purposes only.

## Author

Damala Amulya
GitHub: https://github.com/Damalaamulya
