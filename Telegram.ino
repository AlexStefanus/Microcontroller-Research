#include <WiFi.h>
#include <HTTPClient.h>

// Konfigurasi WiFi
const char* ssid = "Samsung Galaxy S25 Ultra";  // Periksa nama WiFi
const char* password = "987654321";             // Periksa password
const char* serverURL = "http://192.168.0.101:5000/temperature";

void setup() {
  Serial.begin(115200);
  delay(1000);
  
  Serial.println("\nMemulai koneksi WiFi...");
  Serial.print("Menghubungkan ke: ");
  Serial.println(ssid);
  
  WiFi.mode(WIFI_STA);  // Set mode Station
  WiFi.begin(ssid, password);
  
  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 20) {  // Timeout setelah 20 detik
    delay(1000);
    Serial.print(".");
    attempts++;
  }
  
  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\nBerhasil terhubung ke WiFi!");
    Serial.print("IP Address: ");
    Serial.println(WiFi.localIP());
    Serial.print("Signal Strength (RSSI): ");
    Serial.println(WiFi.RSSI());
  } else {
    Serial.println("\nGagal terhubung ke WiFi!");
    Serial.println("Status WiFi: " + String(WiFi.status()));
    Serial.println("Coba periksa:");
    Serial.println("1. Nama WiFi dan password");
    Serial.println("2. Jarak ke WiFi router/hotspot");
    Serial.println("3. Apakah hotspot sudah aktif");
  }
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    // Kode pengiriman suhu di sini
  } else {
    Serial.println("Koneksi WiFi terputus...");
    delay(5000);
  }
}