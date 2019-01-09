void
matmult_kmn(int m, int n, int k, double **A, double **B, double **C) {

    int i, j, l, x;
    
    for(i=0;i<m;i++){
    	for(j=0;j<n;j++){
    		C[i][j]=0;
    	}
    }
	for(l=0;l < k; l++){
		for(i=0;i < m;i++){
			x = A[i][l];
			for(j=0;j < n; j++){
				C[i][j] += x * B[l][j];
			}
		}
	}
}
