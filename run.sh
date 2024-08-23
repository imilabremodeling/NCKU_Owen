#!/bin/bash
number_of_training=1
echo "正要開始第 $number_of_training 輪預測"
python3 predict.py
number_of_training=$((number_of_training+1))