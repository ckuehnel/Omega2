// MicroView as SerialDisplay
// Displays temperature and humidity data serial received in format "D t.t h"
// t.t means temperature as floating point number
// h means humidity as interger number
// Configuration of serial interface is 9600 baud, 8n1, no handshake
// 2014-11-03/Claus Kühnel (info[at]ckuehnel.ch)

#include <MicroView.h>

int hum;
float temp;

void readData()
{
	if(Serial.available())
	{
		if(Serial.find("D"))
		{
			temp = Serial.parseFloat();
			hum  = Serial.parseInt();
		}
	}
}

void displayData()
{
	uView.clear(PAGE);
	uView.setCursor(0,0);
    uView.print("Temperatur");
    uView.setCursor(10,12);
    uView.print(temp, 1);
    uView.print(" *C");
    uView.setCursor(0,24);
    uView.print("Feuchte");
    uView.setCursor(16,36);
    uView.print(hum);
    uView.print("  %");
    uView.display();        	
}

void setup() 
{
    Serial.begin(9600);
    uView.begin();
}

void loop() 
{
	readData();    // Query data
	displayData(); // Refresh display
    delay(200);
}
