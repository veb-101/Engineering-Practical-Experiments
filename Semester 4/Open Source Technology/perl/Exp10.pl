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
{
    print "Executed If block -- The value is $a\n";
}
elsif($a==5)
{
    print "Executed elsif block --The value is $a\n";
}
else
{
    print "Executed else block � The value is $a\n";
}

unless($a==5)
{
    print "Inside the unless block --- The value is $a\n";
}
else
{
    print "Inside else block--- The value is $a\n";
}

my @narray=(1..10);
for(my $count=0;$count<10;$count++)
{
    print "The array index $count value is $narray[$count]";
    print "\n";
}
for(1..10)
{
    print "$_ n";
    print "\n";
}
foreach my $value (@narray)
{
    print " The value is $value\n";
}

$guess = 0;
$luckynum = 7;
print "Guess a Number Between 1 and 10\n"; $guess = <STDIN>;
print "You guessed the number $guess";
while ($guess != $luckynum)
{
    print "Guess a Number Between 1 and 10\n "; $guess = <STDIN>;
    print "You guessed the number $guess";
}
print "You guessed the lucky number 7\n";

$gues = 10;
do {
    print "$gues \n";
    $gues--;
}while ($gues >= 1);

print "Now value is less than 1";

print "\nEnter any name \n";
my $name=<STDIN>;
chomp($name);
until($name ne 'raj')
{
    print "Enter any name \n";
    $name=<STDIN>;
    chomp($name);
}

print "\nEnter any name \n";
my $name=<STDIN>;
chomp($name);
do {
    print "Enter any name \n"; $name=<STDIN>;
    chomp($name);
}until($name ne 'raj');

sub display
{
    my $var=@_;
    print "\nSubroutine\n$var is the value passed";
}
display(2,3,4);
