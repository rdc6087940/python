#!/root/anaconda3/bin/python
import sys
last_key=None
running_total=0
for input_line in sys.stdin:
  input_line=input_line.strip()
  this_key,value=input_line.split("\t",1)
  value=int(value)
    #기존에 존재하는 단어이면 카운트 증가 처리
  if last_key == this_key:
    running_total += value
  else: #새로운 단어이면
    if last_key:
      print("{0}\t{1}".format(last_key,running_total))
    running_total=value
    last_key=this_key
if last_key==this_key:
  print("{0}\t{1}".format(last_key, running_total))