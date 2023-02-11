#!/bin/bash

rn="$1"

score=0
bonus=0

echo "Evaluating for $rn"
mkdir temp 2> /dev/null
r=$(tar -xf "$rn"_outlab6.tar.gz -C temp || echo "X")
if [[ $r == "X" ]]; then
    echo "No submission/Wrong archive format"
    echo "Score: $score"
    exit
else
    tar -xf "$rn"_outlab6.tar.gz -C temp
fi
r=$(cd temp/"$rn"_outlab6 || echo "X")
if [[ $r == "X" ]]; then
    echo "Wrong folder name"
    echo "Score: $score"
    exit
else
    cd temp/"$rn"_outlab6
fi
r=$(cd q2 || echo "X")
if [[ $r == "X" ]]; then
    echo "Wrong directory structure/q2 not submitted"
    echo "Score $score"
    exit
else
    cd q2
fi

timeout 5s python3 -m doctest -v DSA.py > out.txt
ret="$?"
if [[ ! $ret -eq 0 ]]; then
    echo "Code timed out/Doctest did not run correctly"
    echo "Score: $score"
    cd ../../..
    rm -rf temp
    exit
fi
c=$(grep Test out.txt)
if [[ $c == "Test passed." ]]; then
    echo "All doctests passed, checking split"
    score=$(($score + 5))
else
    echo "Some tests failed, check out.txt"
fi

grep 'DSA.' out.txt > out1.txt
grep 'tests in' out1.txt > done.txt

c=$(grep 'SinglyLinkedList' done.txt | wc -l)
echo "SinglyLinkedList: $c"
score=$(($score + $((c > 4 ? 4 : c))))
bonus=$(($bonus + $((c > 4 ? 1 : 0))))

c=$(grep 'DoublyLinkedList' done.txt | wc -l)
echo "DoublyLinkedList: $c"
score=$(($score + $((c > 4 ? 4 : c))))
bonus=$(($bonus + $((c > 4 ? 1 : 0))))

c=$(grep 'BST\|BinarySearchTree' done.txt | wc -l)
echo "BST/BinarySearchTree: $c"
score=$(($score + $((c > 4 ? 4 : c))))
bonus=$(($bonus + $((c > 4 ? 1 : 0))))

c=$(grep 'Trie' done.txt | wc -l)
echo "Trie: $c"
score=$(($score + $((c > 4 ? 4 : c))))
bonus=$(($bonus + $((c > 4 ? 1 : 0))))

c=$(grep 'Heap' done.txt | wc -l)
echo "Heap: $c"
score=$(($score + $((c > 4 ? 4 : c))))
bonus=$(($bonus + $((c > 4 ? 1 : 0))))

echo "Score: $score"
echo "Bonus: $bonus"

cd ../../..
rm -rf temp