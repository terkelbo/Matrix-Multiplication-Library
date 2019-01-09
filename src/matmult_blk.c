#include <sys/param.h>

void
matmult_blk(int m, int n, int k, double **A, double **B, double **C, int bs) {
    
    int i, j, l;
	int blk_i, blk_j, blk_l;
	
	for(i = 0; i < m; i++){
		for(j = 0; j < n; j++){
			C[i][j] = 0;
		}
	}
	
	//for(blk_i = 0; blk_i < m; blk_i += bs){ 
	//	// start blk_i
	//	for(i=blk_i;i < MIN(blk_i + bs, m); i++){ 
	//		//start loop in blk_i
	//		//for(blk_j = 0; blk_j < n; blk_j +=bs){
	//		//	for(j=blk_j;j < MIN(blk_j+bs,n); j++){ //START TO FILL THE BLOCK WITH ZEROS
	//		//		C[i][j] = 0;
	//		//	}
	//		//}
	//		for(blk_l = 0; blk_l < k; blk_l += bs){
	//			//start blk_l
	//			for(l=blk_l;l < MIN(blk_l + bs, k);l++){
	//				//start loop in blk_l
	//				for(blk_j = 0; blk_j < n; blk_j +=bs){
	//					//start blk_j
	//					for(j=blk_j;j < MIN(blk_j + bs, n); j++){
	//						//start loop in blk_j
	//						C[i][j] += A[i][l] * B[l][j];
	//					}
	//				}
	//			}
	//		}
	//	}
	//}
	
	for(blk_j = 0; blk_j < n; blk_j += bs){
		for(blk_l = 0; blk_l < k; blk_l += bs){
			for(blk_i = 0; blk_i < m; blk_i += bs){
				for(i = blk_i;i < MIN(blk_i + bs, m); i++){
					for(l = blk_l;l < MIN(blk_l + bs, k); l++){
						for(j = blk_j; j < MIN(blk_j + bs, n); j++){
							C[i][j] += A[i][l] * B[l][j];
						}
					}
				}
			}
		}
	}	
	
	
}
