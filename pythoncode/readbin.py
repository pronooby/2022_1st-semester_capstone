import numpy as np

with open('bin.png') as f:
    rectype = np.dtype(np.int32)
    bdata = np.fromfile(f, dtype=rectype)

print(bdata)
#fromfile로 포맷데이터 지정 후 바이너리 데이터읽기