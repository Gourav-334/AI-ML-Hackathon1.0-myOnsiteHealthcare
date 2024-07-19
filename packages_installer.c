#include <stdio.h>
#include <stdlib.h>



int main(int argc, char *argv[])
{
	// Changing colour schema
	printf("COLOUR CHANGED TO GREEN (0A):\n");
	system("color 0a");

	//pip issues
	system("pip --version\n");
	system("python.exe -m pip install --upgrade pip");

	// Team insignia
	printf("TEAM NAME:\n");
	system("echo \"Pattern Hunters\"\n");

	// All non-standard library installation
	printf("INSTALLING NUMPY:\n");
	system("pip install numpy");

	printf("INSTALLING PANDAS:\n");
	system("pip install pandas");

	printf("INSTALLING MATPLOTLIB:\n");
	system("pip install matplotlib");

	printf("INSTALLING SCIKIT-LEARN:\n");
	system("pip install scikit-learn");

	printf("INSTALLING OPENXL:\n");
	system("pip install openpyxl");

	printf("INSTALLING STATSMODEL:\n");
	system("pip install statsmodels");

	printf("INSTALLING JOBLIB:\n");
	system("pip install joblib");

	return 0;
}