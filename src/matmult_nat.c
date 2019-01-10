void
matmult_nat(int m, int n, int k, double **restrict A, double **restrict B, double **restrict C) {

    int i, j, l;

	for(i=0;i < m; i++){
		for(j=0;j < n;j++){
			C[i][j] = 0;
			for(l=0;l < k; l++){
				C[i][j] += A[i][l] * B[l][j];
			}
		}
	}
}
