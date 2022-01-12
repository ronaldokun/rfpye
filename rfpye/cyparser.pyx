cimport cython
import numpy as np
cimport numpy as np

ctypedef np.float32_t DTYPE_t


@cython.boundscheck(False)
@cython.wraparound(False)
cpdef np.ndarray[DTYPE_t, ndim=2] cy_extract_compressed(list data, int rows, int cols, int thresh, float MIN):
    cdef np.ndarray[DTYPE_t, ndim=2] decoded = np.full((rows, cols), thresh - 1, np.float32)
    cdef const unsigned char[:] src
    cdef int RUN = 255
    cdef int ESC = 254
    cdef int NRSC
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

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef np.ndarray[DTYPE_t, ndim=2] cy_extract_uncompressed(list blocks, int rows, int cols, float MIN):
    cdef np.ndarray[DTYPE_t, ndim=2] levels = np.full((rows, cols), MIN, dtype=np.float32)
    #cdef const unsigned char[:] src
    cdef Py_ssize_t row   
    cdef int b = 0
    for row in range(rows):
        #src = blocks[row]
        levels[b] = blocks[row]
        b+=1
    return levels
    

