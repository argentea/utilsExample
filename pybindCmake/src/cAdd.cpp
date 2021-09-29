#include "cAdd.h"
#include <vector>

int Cadd::add() {
    return a + b;
}

const std::vector<int>& Cadd::raw_data() {
	return data;
}
