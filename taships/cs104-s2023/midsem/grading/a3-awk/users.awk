BEGIN {
    FS=";"
}
{
    if($4 == "/bin/false") print $1
}
END {
}