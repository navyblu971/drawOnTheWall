#include <wiringPi.h>
int main (void)
{
  wiringPiSetup () ;
  pinMode (14, OUTPUT) ;
  for (;;)
  {
    digitalWrite (14, HIGH) ; delay (500) ;
    digitalWrite (14,  LOW) ; delay (500) ;
  }
  return 0 ;
}


