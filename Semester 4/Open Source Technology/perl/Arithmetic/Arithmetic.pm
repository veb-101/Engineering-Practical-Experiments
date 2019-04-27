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
