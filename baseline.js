const { chromium } = require('playwright');
const path = require('path');

(async () => {
  let browser;
  try {
    browser = await chromium.launch({ headless: true });
    const page = await browser.newPage();
    const filePath = 'file://' + path.resolve('index.html');
    await page.goto(filePath);

    const result = await page.evaluate(() => {
      const iterations = 100;
      const start = performance.now();
      for (let i = 0; i < iterations; i++) {
        window.setLang('en');
        window.setLang('ru');
        window.setLang('kz');
        window.setLang('jp');
        window.setLang('ch');
      }
      const end = performance.now();
      return (end - start) / (iterations * 5);
    });

    console.log('RESULT:' + result);
  } catch (err) {
    console.error(err);
  } finally {
    if (browser) await browser.close();
  }
})();
