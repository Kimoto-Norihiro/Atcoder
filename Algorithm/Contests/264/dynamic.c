#include <stdio.h>
#include <cstring>

#define N 10
#define M 10

int main() {
    int i,j;
    bool x[N+1][M+1]
    int S = 10;
    int a[] = {2,5,8,9};
    int n = sizeof a /sizeof a[0];

    memset(x,0,sizeof(x))
    x[0][0] = true;

    for(i=0;i<n;i++){
        for(j=0;j<=S;j++){
            if(j < a[i]) x[i+1][j]=x[i][j];
            else x[i+1][j]=x[i][j]+x[i][j-a[i]];
        }
    }

    for (i=0;i<n;i++){
        printf("%2d:",a[i]);
        for(j=0;j<=S;j++){
            printf("%2d",x[i][j]);
        }
        printf("¥n");
    }


}