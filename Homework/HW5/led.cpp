#include<iostream>
#include<unistd.h>
#include<fstream>
#include<string>
using namespace std;

#define GPIO "/sys/class/gpio/"
#define Flash_Delay 500000

//This class is how all LED pins are constructed and dealt with
class LED { 
	private: 
		string gpioPath;
		int gpioNumber;
		void writeSysfs(string path, string filename, string value);
	public: 
		LED(int gpioNumber);
		virtual void turnOn();
		virtual void turnOff();
		virtual ~LED();
};

//This is how the GPIO pin is set up when an led object is created
LED::LED (int gpioNumber){
	this->gpioNumber = gpioNumber;
	gpioPath = string(GPIO "gpio") + to_string(gpioNumber) + string("/");
	writeSysfs(string(GPIO), "export", to_string(gpioNumber));
	usleep(100000);
	writeSysfs(gpioPath, "direction", "out");
}

//This defines the writing process to the GPIO
void LED::writeSysfs(string path, string filename, string value){
	ofstream fs;
	fs.open((path+filename).c_str());
	fs<<value;
	fs.close();
}

//Turns on the LED
void LED::turnOn(){
	writeSysfs(gpioPath, "value", "1");
}

//Turns off the LED
void LED::turnOff(){
	writeSysfs(gpioPath, "value", "0");
}

//The distructor is called automatically at the end of the program
LED::~LED(){
	writeSysfs(string(GPIO), "unexport", to_string(gpioNumber));
}

int main(){
	/*Setting up the LED pin for use*/
	LED led1(17);
	/*Blinking the LED at 0.5s intervals*/
	for (int a = 0; a < 20; a++){
		led1.turnOn();
		usleep(500000);
		led1.turnOff();	
		usleep(500000);
	}
	return 0;
}
