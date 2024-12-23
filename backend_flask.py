from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Struktur data untuk menyimpan suhu dan timestamp
temperature_data = {
    'value': None,
    'timestamp': None
}


@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    global temperature_data

    if request.method == 'POST':
        try:
            temp = request.args.get('temperature')
            if temp is None:
                return jsonify({"error": "Parameter temperature tidak ditemukan"}), 400

            # Konversi ke float dan validasi
            temp_float = float(temp)
            if temp_float < -273.15:  # Validasi suhu tidak di bawah nol mutlak
                return jsonify({"error": "Nilai suhu tidak valid"}), 400

            temperature_data['value'] = temp_float
            temperature_data['timestamp'] = datetime.now().isoformat()

            return jsonify({"message": "Suhu berhasil disimpan", "data": temperature_data}), 200

        except ValueError:
            return jsonify({"error": "Nilai suhu harus berupa angka"}), 400

    elif request.method == 'GET':
        if temperature_data['value'] is None:
            return jsonify({"error": "Belum ada data suhu"}), 404

        return jsonify({
            "temperature": temperature_data['value'],
            "timestamp": temperature_data['timestamp']
        }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Struktur data untuk menyimpan suhu dan timestamp
temperature_data = {
    'value': None,
    'timestamp': None
}

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    global temperature_data

    if request.method == 'POST':
        try:
            temp = request.args.get('temperature')
            if temp is None:
                return jsonify({"error": "Parameter temperature tidak ditemukan"}), 400

            # Konversi ke float dan validasi
            temp_float = float(temp)
            if temp_float < -273.15:  # Validasi suhu tidak di bawah nol mutlak
                return jsonify({"error": "Nilai suhu tidak valid"}), 400

            temperature_data['value'] = temp_float
            temperature_data['timestamp'] = datetime.now().isoformat()

            return jsonify({"message": "Suhu berhasil disimpan", "data": temperature_data}), 200

        except ValueError:
            return jsonify({"error": "Nilai suhu harus berupa angka"}), 400

    elif request.method == 'GET':
        if temperature_data['value'] is None:
            return jsonify({"error": "Belum ada data suhu"}), 404

        return jsonify({
            "temperature": temperature_data['value'],
            "timestamp": temperature_data['timestamp']
        }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)