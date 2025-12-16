#!/usr/bin/env python3
print("=== START ===")

try:
    import json
    from datetime import datetime
    print("✅ ライブラリOK")
except:
    print("❌ ライブラリエラー")
    exit(1)

campaigns = [
    {
        "title": "コカ・コーラ 年末キャンペーン",
        "products": ["コカ・コーラ", "コーラ", "コカコーラ"],
        "stores": ["全国スーパー", "コンビニ"],
        "period": "2025-12-01〜2025-12-31",
        "url": "https://www.coca-cola.co.jp/campaign",
        "scraped_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        "title": "ポテトチップス お正月キャンペーン",
        "products": ["ポテチ", "ポテトチップス", "カラムーチョ"],
        "stores": ["スーパー", "コンビニ"],
        "period": "2025-12-15〜2026-01-15",
        "url": "https://www.calbee.co.jp/campaign",
        "scraped_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
]

print(f"📊 生成データ数: {len(campaigns)}")

try:
    with open('campaigns.json', 'w', encoding='utf-8') as f:
        json.dump(campaigns, f, ensure_ascii=False, indent=2)
    
    with open('campaigns.json', 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"✅ ファイル生成成功！サイズ: {len(content)}文字")
        print(f"最初の行: {content[:100]}...")
        
except Exception as e:
    print(f"❌ 書き込みエラー: {e}")
    exit(1)

print("🎉 完了！")

