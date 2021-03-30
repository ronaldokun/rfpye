cimport cython
import numpy as np
cimport numpy as np


@cython.boundscheck(False)
@cython.wraparound(False)
cpdef object cy_decode_blocks(list blocks):
    cdef float offset = blocks[0].offset
    cdef float MIN = offset - 127.5
    cdef int rows = len(blocks)
    cdef int columns = blocks[0].norig
    cdef np.ndarray decoded = np.full((rows, columns), MIN, dtype=np.float16)
    cdef list data = [b.data[b.start:b.stop] for b in blocks]
    cdef int RUN = 255
    cdef int ESC = 254
    cdef const unsigned char[:] src
    cdef int NRSC
    cdef float thresh = blocks[0].thresh
    cdef int i
    cdef int j
    cdef int ib
    cdef int nrun
    cdef Py_ssize_t row   
    for row in range(rows):
        src = data[row]
        nsrc = len(src)
        i = 0
        j = 0
        while i < nsrc:
            ib = src[i] 
            i+=1
            if ib == RUN:
                nrun = src[i] 
                i+=1
                decoded[row, j:j+nrun] = MIN + thresh/2.
                j+=nrun
            elif ib == ESC:
                # next value is literal
                decoded[row, j] = MIN + src[i]/2.
                i+=1 ; j+=1
            else:
                # value
                decoded[row, j] = MIN + ib/2.
                j+=1
    return decoded