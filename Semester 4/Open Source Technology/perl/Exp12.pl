#Reading a file
open(FH,"<file.txt");
while(<FH>)
{
    print "$_";
}
close FH;

#Writing to a file
open(FH,">test.txt");
print "\nEnter Data to Write: ";
my $var=<>;
print FH $var;
print $var;
close FH;

#Appending to a file
open(FH,">>test.txt");
print "\nEnter Data to Append: ";
my $var=<>;
print FH $var;
close FH;

#Copying files
open(DATA1, "<file1.txt");
open(DATA2, ">file2.txt");
{
    print DATA2 $_;
}
print "Data from file1 to file2 copied Sucessfully.";
close( DATA1 );
close( DATA2 );

#Rename a file
rename("test1.txt", "test2.txt" );
print "\nFile test1 is renamed to test2";

#Delete an existing file
unlink ("test2.txt");
print "\nFile test2 is deleted";

#Count the number of lines, words and characters in a file
open FH, '+<','input.txt';
my ($lines, $words, $chars) = (0,0,0);
while (<FH>) {
    $lines++;
    $chars += length($_);
    $words += scalar(split(' ', $_));
}
print("lines=$lines words=$words chars=$chars\n");

print "\nRegular Experession";
my $userinput="Hello Everybody!";
if($userinput=~m/(Hello).*/)
{ print "\nFound Pattern"; }
else
{ print "\nUnable to find the pattern"; }

my $a="Hello how are you";
$a=~s/hello/cello/gi;
print "\n$a";

my $a="hello how are you";
$a=~tr/hello/cello/;
print "\n$a";
