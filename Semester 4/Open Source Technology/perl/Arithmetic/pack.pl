use FindBin;                     # locate this script
use lib "$FindBin::RealBin/..";  # use the parent directory
require Arithmetic;
print "Addition of 5 and 6: ".Arithmetic::add(5,6)."\n";
print "Subtraction of 5 from 6: ".Arithmetic::subtract(5,6);
