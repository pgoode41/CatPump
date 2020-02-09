#include "HX711.h"

// HX711 circuit wiring
const int LOADCELL_DOUT_PIN = 12;
const int LOADCELL_SCK_PIN = 13;

HX711 scale;

void setup() {
  Serial.begin(9600);
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
}

void loop() {

  if (scale.is_ready()) {
    double reading = scale.read();
    double kg_1 = 381783.96556755184;

    double weight_in_kilos = reading / kg_1;
    ///Serial.print("HX711 reading: ");
    //Serial.println(reading);
    Serial.println(weight_in_kilos);


  delay(1000);
}
  
}