open(FH,"<file.txt"); 
while(<FH>)
{ print "$_ "; } 
close FH;