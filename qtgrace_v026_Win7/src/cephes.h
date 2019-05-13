/*
 * Prototypes of Cephes functions
 */

/* Variable for error reporting.  See mtherr.c.  */
#ifdef __cplusplus
extern "C" {
#endif
extern  int merror;

/*#if defined(_MSC_VER) && _MSC_VER>=1800
#else
// These functions should not be declared  in VS2013. They are in math.h already.
extern  double expm1 ( double x );
extern  double frexp ( double x, int *pw2 );
extern  double ldexp ( double x, int pw2 );
extern  double log1p ( double x );
#endif*/

extern  int airy ( double x, double *ai, double *aip, double *bi, double *bip );
extern  double beta ( double a, double b );
extern  double lbeta ( double a, double b );
extern  double chdtrc ( double df, double x );
extern  double chdtr ( double df, double x );
extern  double chdtri ( double df, double y );
extern  double dawsn ( double xx );
extern  double ellie ( double phi, double m );
extern  double ellik ( double phi, double m );
extern  double ellpe ( double x );
extern  double ellpk ( double x );
extern  double expn ( int n, double x );
extern  double fac ( int i );
extern  double fdtrc ( int ia, int ib, double x );
extern  double fdtr ( int ia, int ib, double x );
extern  double fdtri ( int ia, int ib, double y );
extern  int fresnl ( double xxa, double *ssa, double *cca );
extern  double gdtr ( double a, double b, double x );
extern  double gdtrc ( double a, double b, double x );
extern  double hyp2f0 ( double a, double b, double x, int type, double *err );
extern  double hyp2f1 ( double a, double b, double c, double x );
extern  double hyperg ( double a, double b, double x );
extern  double i0 ( double x );
extern  double i0e ( double x );
extern  double i1 ( double x );
extern  double i1e ( double x );
extern  double iv ( double v, double x );
extern  double igamc ( double a, double x );
extern  double igam ( double a, double x );
extern  double igami ( double a, double y0 );
extern  double incbet ( double aa, double bb, double xx );
extern  double incbi ( double aa, double bb, double yy0 );
extern  double jv ( double n, double x );
extern  double k0 ( double x );
extern  double k0e ( double x );
extern  double k1 ( double x );
extern  double k1e ( double x );
extern  double kn ( int nn, double x );
extern  int mtherr ( char *name, int code );
extern  double ndtr ( double a );
extern  double ndtri ( double y0 );
extern  double pdtrc ( int k, double m );
extern  double pdtr ( int k, double m );
extern  double pdtri ( int k, double y );
extern  double psi ( double x );
extern  void revers ( double y[], double x[], int n );
extern  double true_gamma ( double x );
extern  double rgamma ( double x );
extern  int shichi ( double x, double *si, double *ci );
extern  int sici ( double x, double *si, double *ci );
extern  double spence ( double x );
extern  double stdtr ( int k, double t );
extern  double stdtri ( int k, double p );
extern  double onef2 ( double a, double b, double c, double x, double *err );
extern  double threef0 ( double a, double b, double c, double x, double *err );
extern  double struve ( double v, double x );
extern  double cosm1 ( double x );
extern  double yv ( double v, double x );
extern  double zeta ( double x, double q );
extern  double zetac ( double x );

extern  double chbevl ( double x, void *P, int n );
extern  double polevl ( double x, void *P, int n );
extern  double p1evl ( double x, void *P, int n );

/* polyn.c */
extern  void polini ( int maxdeg );
extern  void polprt ( double a[], int na, int d );
extern  void polclr ( double *a, int n );
extern  void polmov ( double *a, int na, double *b );
extern  void polmul ( double a[], int na, double b[], int nb, double c[] );
extern  void poladd ( double a[], int na, double b[], int nb, double c[] );
extern  void polsub ( double a[], int na, double b[], int nb, double c[] );
extern  int poldiv ( double a[], int na, double b[], int nb, double c[] );
extern  void polsbt ( double a[], int na, double b[], int nb, double c[] );
extern  double poleva ( double a[], int na, double x );

union us2d_t {
   unsigned short   us[4];
   double      d;
};

#ifdef __cplusplus
}
#endif