/* This program demonstrates how to use namespaces */

#include <iostream> // This will contain std namespace..

using namespace std;

// Defining namespace

namespace inputs { 
	int var;
	void print(void) {
		cout << var << endl;
		} 
	} 

int main(void) {
	inputs :: var = 638; 
	using namespace inputs;
	// At this moment we are using std and inputs namespaces , there should not be any common names in those two namespaces.
	cout << var << endl;
	print();
	return 0;
	}




