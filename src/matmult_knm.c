void
matmult_knm(int m, int n, int k, double **A, double **B, double **C) {
    
    int i, j, l;

	for(l=0;l < k; l++){
		for(j=0;j < n;j++){
			for(i=0;i < m; i++){
				if(l==0){ C[i][j]=0; }
				C[i][j] += A[i][l] * B[l][j];
			}
		}
	}
}
