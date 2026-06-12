import time
from playwright.sync_api import sync_playwright
import os

def run_benchmark():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        path = os.path.abspath("index.html")
        page = browser.new_page()
        page.goto(f"file://{path}")

        # Number of iterations
        iterations = 100
        languages = ['en', 'ru', 'kz', 'jp', 'ch']

        # Warm up
        page.evaluate("window.setLang('en')")

        script = """
        () => {
            const start = performance.now();
            const languages = ['en', 'ru', 'kz', 'jp', 'ch'];
            for (let i = 0; i < 100; i++) {
                languages.forEach(lang => window.setLang(lang));
            }
            return performance.now() - start;
        }
        """
        result_ms = page.evaluate(script)

        print(f"BENCHMARK_RESULT: {result_ms / (iterations * len(languages))} ms per switch")
        browser.close()

if __name__ == "__main__":
    run_benchmark()
