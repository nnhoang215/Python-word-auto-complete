#!/bin/bash

python3 dictionary_test_script.py -v ./ linkedlist data500.txt test500.in
python3 dictionary_test_script.py -v ./ linkedlist data1k.txt test1k.in
python3 dictionary_test_script.py -v ./ linkedlist data5k.txt test5k.in
python3 dictionary_test_script.py -v ./ linkedlist data10k.txt test10k.in
python3 dictionary_test_script.py -v ./ linkedlist data50k.txt test50k.in
python3 dictionary_test_script.py -v ./ linkedlist data100k.txt test100k.in

python3 dictionary_test_script.py -v ./ trie data500.txt test500.in
python3 dictionary_test_script.py -v ./ trie data1k.txt test1k.in
python3 dictionary_test_script.py -v ./ trie data5k.txt test5k.in
python3 dictionary_test_script.py -v ./ trie data10k.txt test10k.in
python3 dictionary_test_script.py -v ./ trie data50k.txt test50k.in
python3 dictionary_test_script.py -v ./ trie data100k.txt test100k.in

python3 dictionary_test_script.py -v ./ array data500.txt test500.in
python3 dictionary_test_script.py -v ./ array data1k.txt test1k.in
python3 dictionary_test_script.py -v ./ array data5k.txt test5k.in
python3 dictionary_test_script.py -v ./ array data10k.txt test10k.in
python3 dictionary_test_script.py -v ./ array data50k.txt test50k.in
python3 dictionary_test_script.py -v ./ array data100k.txt test100k.in

# default tests
python3 dictionary_test_script.py -v ./ linkedlist sampleData.txt test1.in test2.in
python3 dictionary_test_script.py -v ./ linkedlist sampleDataToy.txt testToy.in

python3 dictionary_test_script.py -v ./ trie sampleData.txt test1.in test2.in
python3 dictionary_test_script.py -v ./ trie sampleDataToy.txt testToy.in

python3 dictionary_test_script.py -v ./ array sampleData.txt test1.in test2.in
python3 dictionary_test_script.py -v ./ array sampleDataToy.txt testToy.in