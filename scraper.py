import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def scrape_campaigns():
    campaigns = []
    
    # 例：懸賞サイトをスクレイピング（実際のサイトに合わせて調整）
    try:
        url = "https://example.com/receipt-campaigns"  # 実際のURL
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # サイトの構造に合わせて調整
        for item in soup.select('.campaign-item'):  # クラス名は実際のHTMLに合わせる
            campaign = {
                'title': item.select_one('.title').text.strip(),
                'products': item.select_one('.products').text.strip(),
                'period': item.select_one('.period').text.strip(),
                'url': item.find('a')['href'],
                'scraped_at': datetime.now().strftime('%Y-%m-%d')
            }
            campaigns.append(campaign)
    except Exception as e:
        print(f"Error: {e}")
    
    # JSONファイルに保存
    with open('campaigns.json', 'w', encoding='utf-8') as f:
        json.dump(campaigns, f, ensure_ascii=False, indent=2)
    
    print(f"Scraped {len(campaigns)} campaigns")

if __name__ == "__main__":
    scrape_campaigns()
