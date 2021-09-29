#include <iostream>
#include <vector>

class Cadd {
private:
    int a;
    int b;
    std::vector<int> data;
public:
    Cadd(int a, int b): a(a), b(b) {
        data.push_back(a);
        data.push_back(b);
    }
    int add();
	const std::vector<int>& raw_data();
};
