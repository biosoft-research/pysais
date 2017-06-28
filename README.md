# PySAIS #

PySAIS is a wrapper to [Yuta Mori's](https://sites.google.com/site/yuta256/sais) implementation of the induced sorting algorithm to create suffix arrays. Both 32 bit and 64 bit indices are supported and automatically recognised.

## License ##
MIT - same as the original implementation, as this is just a wrapper.


## Requirements ##
Cython and numpy. 


## Useful features ##
This wrapper will automatically reduce the size of the computed array to uint16 or uint32 if possible. This is necessary as the algorithm makes use of the sign bit. If required, this can be disabled with the flag to the main function, which may be required on low-memory systems.

Both numpy byte-arrays as well as native byte and string types can be sent to the SAIS module.


(Further documentation to be added soon.)

## Example ##

```
#!python

In [1]: from PySAIS import sais

In [2]: s = 'test1 test2'

In [3]: sa = sais(s)

In [4]: sa
Out[4]: array([ 5,  4, 10,  1,  7,  2,  8,  3,  9,  0,  6], dtype=uint16)

In [5]: for i in range(len(sa)):
   ...:     print(s[sa[i]:])
 test2
1 test2
2
est1 test2
est2
st1 test2
st2
t1 test2
t2
test1 test2
test2

```