# Importing necessary modules
from playwright.sync_api import sync_playwright
from rich import print
import time

# Define the main function
def main():
    # Using Playwright to automate browser actions
    with sync_playwright() as p:
        # Launch a Chromium browser instance with the option to show the browser window (headless=False)
        browser = p.chromium.launch(headless=False)
        # Create a new page in the browser
        page = browser.new_page()

        # Navigate to Google Maps
        page.goto("https://www.google.com/maps", timeout=60000)
        # Adding a wait time (5 seconds) during development for the page to load. Can be removed in production.
        page.wait_for_timeout(5000)

        # Fill in the search input box with the specified location
        page.locator('//input[@id="searchboxinput"]').fill('Reliance Market in Kolkata, West Bengal')
        # Adding a wait time (3 seconds) after filling the search box
        page.wait_for_timeout(3000)

        # Simulate pressing the "Enter" key
        page.keyboard.press("Enter")
        # Adding a wait time (5 seconds) to let the page load. Adjust as needed based on page load time.
        time.sleep(5)

        # Simulate hovering over an element with the specified class
        page.hover('//a[contains(@class, "hfpxzc")]')

        # Scroll down in a loop (twice in this case, adjust as needed)
        for _ in range(2):
            # Simulate scrolling the mouse wheel
            page.mouse.wheel(0, 10000)
            # Adding a wait time (3 seconds) after each scroll action
            page.wait_for_timeout(3000)

        # Find elements with a specific class after scrolling
        main_divs = page.locator("//div[contains(@class, 'Nv2PK tH5CWc THOPZb ')]").all_text_contents()
        # Print the total length and text content of the found elements
        print(f"Total length of main_divs: {len(main_divs)}")
        print(main_divs)

        # Close the browser
        browser.close()

# Entry point of the script
if __name__ == "__main__":
    main()
