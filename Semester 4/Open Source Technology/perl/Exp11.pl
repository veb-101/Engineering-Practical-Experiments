#Experiment No.: 11
#Roll No.: 77

#Arithmetic.pm
package Arithmetic; 
sub new
{ 
my $class=shift;
my $self={}; 
bless $self, $class; 
return $self; 
} 
sub add 
{ 
my $self= shift; 
my $a=$_[0]; 
my $b=$_[1]; 
return ($a+$b); 
} 
sub subtract 
{ 
my $self= shift; 
my $a=$_[0]; 
my $b=$_[1]; 
return ($a-$b); 
} 
1;

#Exp11.pl
use Arithmetic;
my $obj= Arithmetic->new();
my $result= $obj->add(5,6);
print "Addition of 5 and 6 is $result.";
$result = $obj->subtract(6,5);
print "\nSubtraction of 5 from 6 is $result.";

=for comment
Addition of 5 and 6 is 11.
Subtraction of 5 from 6 is 1.
=cut