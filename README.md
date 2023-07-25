# Web Scraping Application using Scrapy

This is a web scraping application built in Python using the Scrapy framework. It allows you to scrape data from the website [https://quotes.toscrape.com/](https://quotes.toscrape.com/) and provides options to export the scraped data in JSON, CSV, or XML format. Additionally, you can choose to store the scraped data using SQLite3, allowing you to access and manipulate the data locally.

## Prerequisites

Before running this application, ensure that you have the following software installed on your system:

1. Python: Make sure you have Python 3.x installed. You can download it from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

## Installation

1. Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/mmt2597/python-scrapy
```

2. Change your current directory to the project folder:
```bash
cd your-repo
```

3. Install the required dependencies by running:
```bash
pip install scrapy
```

## Usage
To use the web scraping application, follow these steps:

1. Open the terminal (or command prompt) and navigate to the project folder.
2. Go to quotetutorial folder
```bash
cd quotetutorial
```
3. Run the following command to start the scraping process:
```bash
scrapy crawl quotes
```

