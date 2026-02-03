cimport cython
import numpy as np
cimport numpy as np

ctypedef np.float32_t DTYPE_t


@cython.boundscheck(False)
@cython.wraparound(False)
cpdef np.ndarray[DTYPE_t, ndim=2] cy_extract_compressed(
    list data, int rows, int cols, int thresh, float MIN
):
    """
    Decode compressed spectrum blocks into a 2D NumPy array.

    Defensive decoding strategy:
    - The declared number of columns (cols / ndata) is authoritative.
    - Compressed streams may describe more samples than cols.
    - Any excess data is silently truncated to avoid buffer overflows.
    - This guarantees heap safety and stable execution, even with
      malformed or legacy CRFS BIN files.

    This function prioritizes metadata availability and process stability
    over full spectral reconstruction fidelity.
    """

    # Allocate output matrix filled with default (threshold - 1)
    cdef np.ndarray[DTYPE_t, ndim=2] decoded = np.full(
        (rows, cols), thresh - 1, np.float32
    )

    cdef const unsigned char[:] src
    cdef int RUN = 255
    cdef int ESC = 254
    cdef int nsrc
    cdef int i
    cdef int j
    cdef int ib
    cdef int nrun
    cdef Py_ssize_t row

    # Structural sanity check: number of rows must match input blocks
    if rows != len(data):
        raise ValueError("rows != len(data)")

    for row in range(rows):
        src = data[row]
        nsrc = len(src)
        i = 0   # index in compressed stream
        j = 0   # index in decoded spectrum (columns)

        # ------------------------------------------------------------------
        # MAIN DECODE LOOP
        #
        # CHANGE #1:
        #   Loop is explicitly bounded by BOTH:
        #     - i < nsrc  (compressed stream length)
        #     - j < cols  (physical spectrum size)
        #
        # This prevents any write beyond decoded[row, cols-1].
        # ------------------------------------------------------------------
        while i < nsrc and j < cols:
            ib = src[i]
            i += 1

            if ib == RUN:
                # RUN-length encoding: skip nrun bins
                if i >= nsrc:
                    break  # malformed stream → stop decoding this row

                nrun = src[i]
                i += 1

                # ----------------------------------------------------------
                # CHANGE #2:
                #   RUN truncation:
                #   If RUN would exceed cols, truncate to remaining space.
                # ----------------------------------------------------------
                if j + nrun > cols:
                    nrun = cols - j

                j += nrun

            elif ib == ESC:
                # ESC: next byte is a literal value
                if i >= nsrc:
                    break  # malformed stream

                decoded[row, j] = (src[i] / 2.0) + MIN
                i += 1
                j += 1

            else:
                # Literal value
                decoded[row, j] = (ib / 2.0) + MIN
                j += 1

        # ------------------------------------------------------------------
        # CHANGE #3:
        #   No post-condition error if j != cols.
        #
        # Rationale:
        #   - j < cols → remaining bins stay at default value (thresh - 1)
        #   - j > cols is impossible due to loop guards
        # ------------------------------------------------------------------

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
    

