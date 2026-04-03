from scraper import scrape_google_news, scrape_reddit
from fake_filter import filter_data
from analyzer import extract_trends
from database import save_trends


def run(query="AI careers"):
    data = []

    print("Đang lấy dữ liệu...")
    data += scrape_google_news(query)
    data += scrape_reddit(query)

    print(f"Lấy được {len(data)} dữ liệu")

    clean = filter_data(data)
    print(f"Sau lọc còn {len(clean)} dữ liệu")

    trends = extract_trends(clean)

    print("\n🔥 Top Trends:")
    for word, score in trends:
        print(f"{word}: {score}")

    save_trends(trends)


if __name__ == "__main__":
    run("AI jobs")
