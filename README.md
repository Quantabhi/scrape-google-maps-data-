# Automated Location Search on Google Maps using Playwright

This Python script uses Playwright to automate browser actions and perform a location search on Google Maps. It navigates to Google Maps, searches for a specified location, scrolls down the page, and prints information about the found elements.

## Requirements
pip install playwright rich

## How It Works

The script performs the following steps:

- Uses Playwright to automate Chromium browser actions.
- Launches a Chromium browser instance with the option to show the browser window (headless=False).
- Navigates to Google Maps and searches for a specified location.
- Scrolls down the page using simulated mouse wheel actions.
- Hovers over an element with a specific class.
- Finds elements with a specific class after scrolling.
- Prints the total length and text content of the found elements.

## Disclaimer
This script is intended for educational purposes only. Use responsibly and ensure compliance with the terms of service of the websites you are scraping.
