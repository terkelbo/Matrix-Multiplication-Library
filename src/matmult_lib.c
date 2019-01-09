#include <cblas.h>

void
matmult_lib(int m, int n, int k, double **A, double **B, double **C){
	double *a = A[0];
	double *b = B[0];
	double *c = C[0];

	int alpha = 1, beta = 0;
	cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans, 
    			m, n, k, alpha, a, k, b, n, beta, c, n);
}
