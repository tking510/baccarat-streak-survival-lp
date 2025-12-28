#!/usr/bin/env python3
"""
キャラクター画像の背景を除去するスクリプト
rembgを使用して背景のみを透過し、キャラクターの白い部分（目など）は保持
"""

from rembg import remove
from PIL import Image
import os

# 処理対象の画像ファイル
images_to_process = [
    'arquel-hero.png',
    'lucifire-hero.png',
    'rafiel-overview.png',
    'harpina-prizes.png',
    'lilicia-dream.png',
    'gaterian-rules.png',
    'celephim-cta.png',
    'lucifire-cta.png'
]

images_dir = '/home/ubuntu/baccarat-lp/images'

for img_name in images_to_process:
    input_path = os.path.join(images_dir, img_name)
    output_path = os.path.join(images_dir, img_name.replace('.png', '-nobg.png'))
    
    if os.path.exists(input_path):
        print(f"Processing: {img_name}")
        
        # 画像を読み込み
        with open(input_path, 'rb') as f:
            input_data = f.read()
        
        # 背景を除去
        output_data = remove(input_data)
        
        # 出力を保存
        with open(output_path, 'wb') as f:
            f.write(output_data)
        
        print(f"  Saved: {output_path}")
    else:
        print(f"  Not found: {input_path}")

print("\nBackground removal complete!")
