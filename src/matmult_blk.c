#include <sys/param.h>

void
matmult_blk(int m, int n, int k, double **A, double **B, double **C, int bs) {
    
    int i, j, l;
	int blk_i, blk_j, blk_l;
	double x;
	
	for(i = 0; i < m; i++){
		for(j = 0; j < n; j++){
			C[i][j] = 0;
		}
	}
	
	for(blk_j = 0; blk_j < n; blk_j += bs){
		for(blk_l = 0; blk_l < k; blk_l += bs){
			for(blk_i = 0; blk_i < m; blk_i += bs){
				for(i = blk_i;i < MIN(blk_i + bs, m); i++){
					for(l = blk_l;l < MIN(blk_l + bs, k); l++){
						x = A[i][l];
						for(j = blk_j; j < MIN(blk_j + bs, n); j++){
							C[i][j] += x * B[l][j];
						}
					}
				}
			}
		}
	}	
	
	
}
