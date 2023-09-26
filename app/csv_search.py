import csv
import sys

csv_file_path = 'image_data.csv'

min_latitude = sys.argv[1]#最小緯度
max_latitude = sys.argv[2]#最大緯度
min_longitude = sys.argv[3]#最小経度
max_longitude = sys.argv[4]#最大経度

matching_images = []

with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        latitude = float(row[1])
        longitude = float(row[2])
        if(
            min_latitude <= latitude <= max_latitude and
            min_longitude <= longitude <= max_longitude
        ):
            matching_images.append([row[0], row[1], row[2]])