#ifndef __MATMULT_BLK_H
#define __MATMULT_BLK_H

void matmult_blk(int m, int n, int k, double **restrict A, double **restrict B, double **restrict C, int bs);

#endif
