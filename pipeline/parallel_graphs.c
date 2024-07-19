#include <stdio.h>
#include <stdlib.h>



int main(int argc, char *argv[])
{
	system("python model_pipelined.py | python model_pipelined2.py");

	return 0;
}