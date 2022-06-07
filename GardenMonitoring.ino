#include <LiquidCrystal.h>
#include <DHT.h>  
#define DHT_SENSOR_TYPE DHT_TYPE_11

int sensor_pin = A0;
int output_value ;
int LED = 8;

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);



static const int DHT_PIN = 8;
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  lcd.begin(16, 2);
  Serial.begin(9600);
  dht.begin();
  delay(2000);
  
}




void loop() {
  lcd.setCursor(0, 1);
  
output_value= analogRead(sensor_pin);
Serial.println(output_value);
lcd.clear();
lcd.print("Moisture ");

if(output_value < 300){
  digitalWrite(LED, HIGH);
  lcd.print("Low");
}else{
  digitalWrite(LED, LOW);
  lcd.print("Good");
}
  delay(2000);
float hum = dht.readHumidity();
  float temp = dht.readTemperature();
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Hum: ");
    lcd.print(hum);
    lcd.print(" %");
    lcd.setCursor(0, 1);
    lcd.print("Temp: ");
    lcd.print(temp);
    lcd.print(" *C");

  delay(2000);
  
}
