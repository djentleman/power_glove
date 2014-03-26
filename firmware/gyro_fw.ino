#include "Wire.h"
#include "I2Cdev.h"
#include "MPU6050.h"


MPU6050 accelgyro;
int16_t ax, ay, az;
int16_t gx, gy, gz;

void dump(){
  Serial.print(gx); 
  Serial.print("\t\t");
  Serial.print(gy); 
  Serial.print("\t\t");
  Serial.print(gz); 
  Serial.print("\t\t\t");
  Serial.print(ax);                                                                        
  Serial.print("\t\t");
  Serial.print(ay); 
  Serial.print("\t\t");
  Serial.print(az); 
  Serial.print("\t\t");
  Serial.println("");
}

int unsigned5bit(int in){
  if (in < 0){
    return 32 + in;
  }
  return in;
}

char getPacket(int id, int sensorVal){
  // returns one byte
  int dataPacket = map(sensorVal, -17000, 17000, -16, 16);
  dataPacket = unsigned5bit(dataPacket);
  int idPacket = id * pow(2, 5);
  return (char)(dataPacket + idPacket);
}

void writeToSerial(int debug){
  // we only care about gx and gy
  char x = getPacket(0, gx);
  char y = getPacket(1, gy);
  if (debug){
    Serial.print(x, BIN);
    Serial.print("\t\t");
    Serial.println(y, BIN);
  }
  Serial.write(x);
  Serial.write(y);
}


void setup(){
  Serial.begin(9800);
  accelgyro.initialize();
  
}

void loop(){
  accelgyro.getAcceleration(&gx, &gy, &gz);
  accelgyro.getRotation(&ax, &ay, &az);
  writeToSerial(0);
  //dump();

}


