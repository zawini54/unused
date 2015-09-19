#include <stdio.h>
#include <math.h>
using namespace std;

int a[22][22] = {};
int b[22][22] = {};

int main(){
    int n;
    int sc = 0;
    scanf("%d", &n);
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            char c;
            scanf(" %c", &c);
            if(c == '#')
                sc += 1, a[i][j] = 1;
            else
                a[i][j] = 0;

            // if(i-1 >=  0 && j-1 >= 0){
            b[i][j] = b[i-1][j] + b[i][j-1] + a[i][j] - b[i-1][j-1];
                // printf("%d\n", b[i][j]);
            // }else if(i-1 <= 0 && j-1 >= 0){
            //     b[i][j] = b[i][j-1] + a[i][j];
            // }else if(i-1 >= 0 && j-1 <= 0){
            //     b[i][j] = b[i-1][j] + a[i][j];
            // }else{
            //     b[i][j] = a[i][j];
                // printf("%d, %d i-1: %d j-1 %d \n", i, j, i-1, j-1);
            // }

        }
    }

    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            printf("%d ", b[i][j]);
        }
        printf("\n");
    }



    int sss = sqrt(sc);
    bool square = true;
    if(sss*sss == sc){
        for(int i = 1; i <= n; i++){ // ver
            for(int j = 1; j <= n; j++){ // hor
                if (a[i][j] == 1){
                    int sum = b[i+sss-1][j+sss-1] - b[i+sss-1][j-1] - b[i-1][j+sss-1] + b[i-1][j-1];
                    printf("%d\n", sum);
                    if(sum != sc) square = false;
                    goto abcd;
                }
            }
        }
    }else{
        square = false;
    }
    abcd:;
    if(square){
        printf("PEACEFUL\n");
    }else{
        printf("NON-PEACEFUL\n");
    }
}
