#include "custom-library/HX711.h"

// HX711 circuit wiring
const int LOADCELL_DOUT_PIN = 5;  // 디지털핀 5번
const int LOADCELL_SCK_PIN = 4;   // 디지털핀 4번
const int Green = 12;
const int Red = 11;

HX711 scale;
float calibration_factor = -50;
float Weight;
float zero = 0;

void setup() {
  Serial.begin(115200);
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
}

void loop() {
  scale.set_scale(calibration_factor);    
  Weight=scale.get_units()-zero;
  Serial.println(Weight);
  delay(10); //10ms 0.01초에 한번씩 측정.
}
