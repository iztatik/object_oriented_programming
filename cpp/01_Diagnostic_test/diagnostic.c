#include <stdio.h>
#define start 5
#define end 555

int i;
int res = 0;
float res2;

int main()
{
    for(i=start; i<=end; i++) {
        res = res + i; 
    }
    printf("Iterative result = %d \n", res);

    res2 = (start + end)*(end-start+1)/2;
    printf("Direct result = %f \n", res2); 
    return 0;
}
