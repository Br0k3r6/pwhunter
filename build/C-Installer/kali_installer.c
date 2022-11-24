#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>

int execute_system_command(char* command) {
	system(command);
	return 0;
}

int main(void) {
	execute_system_command("apt update");
	execute_system_command("apt-get upgrade");
	execute_system_command("apt-get install python3");
	execute_system_command("python3 -m pip install -r requirements.txt");
	printf("\n[*] Installation completed!\n");
	return 0;
}
