// C++ code
//
void setup()
{
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);
  
}

void loop()
{
  
  /*for(int i = 0; i < 2; i++)
  {
    digitalWrite(7, HIGH);
    digitalWrite(6, HIGH);
    delay(1000);
    digitalWrite(7, LOW);
    digitalWrite(6, LOW);
    delay(1000);
  }*/
    
  for(int i = 0; i < 2; i++)
  {
    digitalWrite(6, LOW);
  	digitalWrite(7, HIGH);
  	delay(1000);
  
  	digitalWrite(7, LOW);
    digitalWrite(6, HIGH);
  	delay(1000);
  }
  
  /*digitalWrite(6, LOW);
  
  for(int i = 0; i < 4; i++)
  {
  	digitalWrite(7, HIGH);
    delay(250);
    digitalWrite(6, HIGH);
    delay(250);
    
    
	digitalWrite(7, LOW);
    delay(250);
    digitalWrite(6, LOW);
    delay(250);
    
    
  }  
  */
  
}