#include <SoftwareSerial.h>

#define smoke_sensor_pin 5
boolean smoke_flag = 0;

#define buzzer_pin 4

void setup()
{
  Serial.begin(9600);

  pinMode(smoke_sensor_pin, INPUT);
  
  pinMode(buzzer_pin, OUTPUT);

  digitalWrite(buzzer_pin,LOW);
}

void loop()
{
  int smoke_value = digitalRead(smoke_sensor_pin);
  Serial.println(smoke_value);

  if(smoke_value == LOW)
  {
    digitalWrite(buzzer_pin,HIGH);
    if(smoke_flag == 0)
    {
      smoke_flag == 1;
      delay(10000);
    }
  }

  else
  {
    digitalWrite(buzzer_pin,LOW);
    smoke_flag = 0;
  }
  delay(1000);
}
