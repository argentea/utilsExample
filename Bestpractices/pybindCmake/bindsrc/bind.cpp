#include"cAdd.h"
#include"pybind11/pybind11.h"

namespace py = pybind11;

PYBIND11_MODULE(pybindCmake, m) {
	py::class_<Cadd>(m, "Cadd")
		.def(py::init<int, int>())
		.def("add", &Cadd::add);
}
