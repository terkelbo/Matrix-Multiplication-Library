void
matmult_knm(int m, int n, int k, double **restrict A, double **restrict B, double **restrict C) {

    int i, j, l,x;
    
    for(i=0;i<m;i++){
    	for(j=0;j<n;j++){
    		C[i][j]=0;
    	}
	}
	for(l=0;l < k; l++){
		for(j=0;j < n;j++){
			x = B[l][j];
			for(i=0;i<m;i++){
				C[i][j] += A[i][l] * x;
			}
		}
	}
}
