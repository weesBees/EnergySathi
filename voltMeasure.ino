
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
float a=map(analogRead(A0),0.00,710.00,0.00,12.20);
float b=map(analogRead(A0),194.00,567.00,3.34,9.77);
float c=map(analogRead(A0),0.00,294.00,0.00,5.03);
float avg=(a+b+c)/3;
Serial.println(avg);
}
