/* Constants */
#define MA_1 3
#define MA_2 4
#define MA_EN 5

/* Functions */
void setDirection(bool);
void setSpeed(unsigned int);
void stop();

void setup()
{
  /* IO configuration */
  pinMode(MA_1, OUTPUT);
  pinMode(MA_2, OUTPUT);
  pinMode(MA_EN, OUTPUT);
  
  /* Initial pin states */
  digitalWrite(MA_1, LOW);
  digitalWrite(MA_2, LOW);
  digitalWrite(MA_EN, LOW);
}

void loop()
{
  setDirection(true);
  setSpeed(50);
  delay(4000);
  
  stop();
  delay(2000);
  
  setDirection(false);
  setSpeed(90);
  delay(4000);
  
  stop();
  delay(2000);
}

void setDirection(bool dir){
  if (dir){
   digitalWrite(MA_1, LOW);
   digitalWrite(MA_2, HIGH); 
  }
  else{
    digitalWrite(MA_1, HIGH);
    digitalWrite(MA_2, LOW);
  }
  return;
}

void setSpeed(unsigned int spd){
  spd = constrain(spd, 0, 100);
  spd = map(spd, 0, 100, 0, 255);
  analogWrite(MA_EN, spd);
  return;
}

void stop(void){
  digitalWrite(MA_EN, LOW);
  return;
}