#include <iostream>

bool function ( void ){

	bool val = true;
	val = 1;
	// We use scope reoslution operator. Because we haven't specified that we are using std namespace.
	std::cin >> val;
	return 8;
	}

int main(void){
	std::cout << function () << std::endl;
	return false;
	}
