#include <LiquidCrystal_I2C.h>
#include <dht11.h>
#define DHT11PIN 7

dht11 DHT11;
LiquidCrystal_I2C lcd(0x27,16,2);  // set the LCD address to 0x3F for a 16 chars and 2 line display

void setup() {
  lcd.init();
  lcd.clear();         
  lcd.backlight();   
  Serial.begin(9600);   // Make sure backlight is on
}

void loop() {
  int L=analogRead(A0);
  int C = analogRead(A1);
   int chk = DHT11.read(DHT11PIN);
    lcd.setCursor(10,0);   //Set cursor to character 2 on line 0
  lcd.print("H:");
  lcd.setCursor(12,0);   
  lcd.print((float)DHT11.humidity);  
lcd.setCursor(10,1);   
  lcd.print("T:");  
  lcd.setCursor(12,1);   
  lcd.print((float)DHT11.temperature);
  lcd.setCursor(0,1);   
  lcd.print("M:");  
  lcd.setCursor(2,1);   
  lcd.print(digitalRead(8));  
  lcd.setCursor(4,1);   
  lcd.print("C:");
if(C>99){
  lcd.setCursor(6,1);   
  lcd.print(C);
}
else{
  lcd.setCursor(6,1);   
  lcd.print(" ");
  lcd.setCursor(7,1);   
  lcd.print(C);
}
  lcd.setCursor(0,0);   
  lcd.print("L:");  
  Serial.println(C);
  if(L>9){
  if (L>99){
    if(L>999){
      lcd.setCursor(2,0);   
      lcd.print(L);  
    }
    else{
      lcd.setCursor(2,0);   
      lcd.print(" "); 
      lcd.setCursor(3,0);   
      lcd.print(L);
    }
  }
  else{
    lcd.setCursor(2,0);   
      lcd.print("  "); 
    lcd.setCursor(4,0);   
      lcd.print(L);
  }  
  }
  else{
    lcd.setCursor(2,0);   
      lcd.print("   "); 
    lcd.setCursor(5,0);   
      lcd.print(L);
  }
  
}
