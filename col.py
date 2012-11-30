#!/usr/bin/env python3
import sys
from zlib import adler32

def ismatch(data,i):
    return i == adler32(data)

def matches():
    global block
    prefix = "the checksum of this string is "
    r1, r2 = int((2**32)*(block/4)), int((2**32)*((block+1)/4))
    print("range", r1, r2)
    for i in range(r1,r2):
            if i % pow(2,22) == 0: print("progress", i/r2*100)
            if ismatch((prefix + hex(i)[2:].zfill(8)).encode(),i):
                    yield i

if __name__ == "__main__":
  global block
  block = int(sys.argv[1]) # 0-3

  print("block", block)
  res = []

  for i in matches():
    print(i)
    res.append(i)

  print(res)
