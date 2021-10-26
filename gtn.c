#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int rndRange(int min, int max) {
	return (rand() % (max - min + 1)) + 1;
}

int main() {
	srand(time(0));
	int x = rndRange(1, 20);
	int y;
	int win = 0;
	printf("Guess the number betweens 1 and 20\n");
	while (win == 0) {
		printf("=] ");
		scanf("%d", &y);
		if (y < x) {
			printf("Too small\n");
		} else if (y > x) {
			printf("Too big\n");
		} else if (y == x) {
			printf("You win! :D\n");
			win = 1;
		}
	}

	return 0;
}
