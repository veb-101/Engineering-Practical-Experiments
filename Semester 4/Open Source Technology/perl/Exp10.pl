#Experiment No.: 10
#Roll No.: 77

#Arithmetic.pm
package Arithmetic;
sub add
{ my $a=$_[0];
my $b=$_[1];
return ($a+$b);
}
sub subtract {
my $a=$_[0];
my $b=$_[1];
return ($a-$b); }
1;

#scalar.pl
$x=15; 
$y = -7.78;
$z = 6 + 5;
print "$x \n";
print "$y \n";
print "$z \n";

$num = 7;
$txt1 = 'it is $num';
$txt2 = "it is $num";
print $txt1."\n";
print $txt2."\n";

my @array=(a,b,c,d);
print @array;
@numbers= (1..10);
print "\n";
print @numbers;
print "\n";
my $string="This is a kind of dynamic array";
my @array;
@array=split('a',$string);
foreach(@array) {
print "$_ \n";
}

print %hash=( 'Raj' => 23, 'Ravi' => 24, 'Shruthi' => 25);
print "\n";
print %hash=('Raj',23,'Ravi',24,'Shruthi',25);
print "\n";
print $hash{'Raj'};
print "\n";

my $a=5;
if($a==6)
{ print "Executed If block -- The value is $a\n"; }
elsif($a==5)
{ print "Executed elsif block --The value is $a\n"; }
else
{ print "Executed else block � The value is $a\n"; }

unless($a==5)
{ print "Inside the unless block --- The value is $a\n"; }
else
{ print "Inside else block--- The value is $a\n"; }

my @narray=(1..10);
for(my $count=0;$count<10;$count++)
{ print "The array index $count value is $narray[$count]";
print "\n"; }
for(1..10)
{ print "$_ n";
print "\n"; }
foreach my $value (@narray)
{ print " The value is $value\n"; }

$guess = 0;
$luckynum = 7;
print "Guess a Number Between 1 and 10\n"; $guess = <STDIN>;
print "You guessed the number $guess";
while ($guess != $luckynum)
{ print "Guess a Number Between 1 and 10\n "; $guess = <STDIN>;
  print "You guessed the number $guess"; }
print "You guessed the lucky number 7\n";

$gues = 10;
do { print "$gues \n";
$gues--; }
while ($gues >= 1);
print "Now value is less than 1";

print "\nEnter any name \n";
my $name=<STDIN>;
chomp($name);
until($name ne 'raj')
{ print "Enter any name \n";
$name=<STDIN>;
chomp($name); }

print "\nEnter any name \n";
my $name=<STDIN>;
chomp($name);
do { print "Enter any name \n"; $name=<STDIN>;
chomp($name); }
until($name ne 'raj');

sub display
{
my $var=@_;
print "\nSubroutine\n$var is the value passed";
}
display(2,3,4);

require Arithmetic;
print "\nAddition of 5 and 6: ".Arithmetic::add(5,6)."\n";
print "Subtraction of 5 from 6: ".Arithmetic::subtract(5,6);

=for comment
OUTPUT:
15
-7.78
11
it is $num
it is 7
abcd
12345678910
This is
 kind of dyn
mic
rr
y
Raj23Ravi24Shruthi25
Raj23Ravi24Shruthi25
23
Executed elsif block --The value is 5
Inside else block--- The value is 5
The array index 0 value is 1
The array index 1 value is 2
The array index 2 value is 3
The array index 3 value is 4
The array index 4 value is 5
The array index 5 value is 6
The array index 6 value is 7
The array index 7 value is 8
The array index 8 value is 9
The array index 9 value is 10
1 n
2 n
3 n
4 n
5 n
6 n
7 n
8 n
9 n
10 n
 The value is 1
 The value is 2
 The value is 3
 The value is 4
 The value is 5
 The value is 6
 The value is 7
 The value is 8
 The value is 9
 The value is 10
Guess a Number Between 1 and 10
9
You guessed the number 9
Guess a Number Between 1 and 10
7
You guessed the number 7
You guessed the lucky number 7
10
9
8
7
6
5
4
3
2
1
Now value is less than 1
Enter any name
Virag

Enter any name
Raj
Enter any name
raj
Enter any name
raj
Enter any name
raj
Enter any name
virag
Subroutine
3 is the value passed
Addition of 5 and 6: 11
Subtraction of 5 from 6: -1
=cut
