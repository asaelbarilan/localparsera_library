# File: examples/scrape_beachcam_langchain.py

from localparsera import LocalParsera

def main():
    url = "https://www.livebeaches.com/webcams/east-hampton-beach-cam/"

    elements = {
        "Title": "Webcam title",
        "Video": "Video source",
        "Description": "Webcam description"
    }

    scraper = LocalParsera()
    result = scraper.scrape(url, elements)

    print("Scraped Data:")
    print(result)

if __name__ == "__main__":
    main()
