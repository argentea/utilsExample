#include <iostream>
#include "cAdd.h"

int main() {
	std::cout << "this is cppmain\n";

	Cadd a(10, 20);
	std::cout << a.add() << std::endl;
	
	return 0;
}
