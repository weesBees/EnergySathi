/*
  ACS712 DC Current Demonstration
  acs712-dc-demo.ino
  Read current using ACS712 Hall Effect sensor
  
  DroneBot Workshop 2021
  https://dronebotworkshop.com
*/

// Variables for Measured Voltage and Calculated Current
double Vout = 0;
double Current = 0;

// Constants for Scale Factor
// Use one that matches your version of ACS712

//const double scale_factor = 0.185; // 5A
const double scale_factor = 0.1; // 20A
//const double scale_factor = 0.066; // 30A

// Constants for A/D converter resolution
// Arduino has 10-bit ADC, so 1024 possible values
// Reference voltage is 5V if not using AREF external reference
// Zero point is half of Reference Voltage

const double vRef = 5.00;
const double resConvert = 1024;
double resADC = vRef/resConvert;
double zeroPoint = vRef/2;


void setup(){ 
  Serial.begin(9600);
}

void loop(){
  
  // Vout is read 1000 Times for precision
  for(int i = 0; i < 1000; i++) {
    Vout = (Vout + (resADC * analogRead(A0)));   
    delay(1);
  }
  
  // Get Vout in mv
  Vout = Vout /1000;
  
  // Convert Vout into Current using Scale Factor
  Current = (Vout - zeroPoint)/ scale_factor;                   

  // Print Vout and Current to two Current = ");                  
  int x=Current*1000;
  if (x<9){
    x=0;
  }
  float a=map(analogRead(A1),0.00,710.00,0.00,12.20);
float b=map(analogRead(A1),194.00,567.00,3.34,9.77);
float c=map(analogRead(A1),0.00,294.00,0.00,5.03);
float avg=(a+b+c)/3;
Serial.print("Voltage:  ");
Serial.print(avg);
Serial.print(" V");
  Serial.print("    Current:  ");                  
  Serial.print(x);
  Serial.print(" mA");                             
 Serial.print("    Power:  ");
 Serial.print((avg*x)/1000);
 Serial.println(" W");
}
