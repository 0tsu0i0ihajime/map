// CSVファイルのパス
const csvFilePath = 'image_data.csv';

// 最小緯度、最大緯度、最小経度、最大経度を関数の引数として受け取る
function findMatchingImages(minLat, maxLat, minLon, maxLon) {
    const matchingImages = [];

    fetch(csvFilePath)
        .then(response => response.text())
        .then(data => {
            // CSVデータをパース
            const rows = data.split('\n');
            for (let i = 1; i < rows.length; i++) { // 最初の行はヘッダーなのでスキップ
                const row = rows[i].split(',');
                const latitude = parseFloat(row[1]);
                const longitude = parseFloat(row[2]);

                if (
                    minLat <= latitude && latitude <= maxLat &&
                    minLon <= longitude && longitude <= maxLon
                ) {
                    matchingImages.push([row[0], row[1], row[2]]);
                }
            }

            // 結果を表示
            console.log(matchingImages);
        })
        .catch(error => console.error('データの読み込みエラー:', error));
}

// 例: 最小緯度、最大緯度、最小経度、最大経度を指定して関数を呼び出す
findMatchingImages(35.0, 36.0, -140.0, -138.0);
