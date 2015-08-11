/* This program demonstrates nested namespaces in C++ .*/

#include <iostream>

using namespace std;

int var = 90;
namespace {
	/*
	We should not have any identifiers in unnamed namespace with same name as of externally defined varialbles.
	We can have nested unnamed namespaces but we can access members as we access outer namespace's members.
	Nested unnamed namespaces are same as 
	*/
	}
namespace outer { 

	int var;
	void print(void){

		cout << var << endl;
		int var = 638;
		cout << var << endl;
		}
	namespace inner {
		int var = 6380;
		void print(void) {
			cout << var << endl;
			int var = 2015;
			cout << var << endl;
			}
		}
	}

int main(void) {
	int var = 0;
	cout<<outer::inner::var;
	cout<<var;
	return 0;
	} // What is it
