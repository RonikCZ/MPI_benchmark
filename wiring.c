#include <wiringPi.h>

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main() {
  if (wiringPiSetup () == -1)
    exit (1) ;

  pinMode(23, OUTPUT);

  while(1) {
    digitalWrite(23, 0);
    delay(500);
    digitalWrite(23, 1);
    delay(500);
  }

  return 0 ;
}
