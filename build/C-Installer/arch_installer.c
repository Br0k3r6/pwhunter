#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>

int execute_system_command(char* command) {
	system(command);
	return 0;
}

int main(void) {
	execute_system_command("pacman -Syu");
	execute_system_command("pacman -Syyuu");
	execute_system_command("pacman -S python3");
	execute_system_command("python3 -m pip install -r requirements.txt");
	printf("\n[*] Installation completed!\n");
	return 0;
}
