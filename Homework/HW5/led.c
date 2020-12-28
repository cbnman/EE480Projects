#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>

#define GPIO_NUMBER "17"
#define GPIO_PATH "/sys/class/gpio/gpio17/"
#define GPIO_SYSFS "/sys/class/gpio/"

void writeGPIO(char filename[], char value[]) {
	FILE* fp;
	fp = fopen(filename, "w+");
	fprintf(fp, "%s", value);
	fclose(fp);
}

int main(){
	/*Setting up the LED pin for use*/
	writeGPIO(GPIO_SYSFS "export", GPIO_NUMBER);
	sleep(1);
	writeGPIO(GPIO_PATH "direction", "out");
	/*Blinking the LED at 0.5s intervals*/
	for (int a = 0; a < 20; a = a +1){
		writeGPIO(GPIO_PATH "value", "1");
		sleep(.5);
		writeGPIO(GPIO_PATH "value", "0");	
		sleep(.5);
	}
	/*Shutting down the LED pin*/
	writeGPIO(GPIO_SYSFS "unexport", GPIO_NUMBER);
	return 0;
}
