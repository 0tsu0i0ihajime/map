import os
from PIL import Image
import csv

folder_path = ''#ここにフォルダーパス

csv_header = ['ファイル名', '緯度', '経度', '撮影日時']

with open('./image_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(csv_header)
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                file_path = os.path.join(root, file_name)
                try:
                    with Image.open(file_path) as img:
                        exif_data = img._getexif()
                        # 緯度と経度を取得
                        lat, lon = exif_data.get(0x8825, [None, None])
                        # 撮影日時を取得
                        datetime_original = exif_data.get(0x9003, 'N/A')
                    csv_writer.writerow([file_name, lat, lon, datetime_original])
                except Exception as e:
                    print(f"エラー: {file_name} - {e}")
print("CSVファイルにデータを書き込みました。")