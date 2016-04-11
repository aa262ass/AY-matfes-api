#include <boost/python.hpp>

std::string hello(std::string name)
{
	return "Hello, " + name + "!";
}

BOOST_PYTHON_MODULE(test)
{
	using namespace boost::python;
	def("hello", &hello);
}
