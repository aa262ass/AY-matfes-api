#include <boost/python.hpp>

char const* hello(){
  return "Hello!";
}

BOOST_PYTHON_MODULE(test){
  boost::python::def("hello",hello);
}
