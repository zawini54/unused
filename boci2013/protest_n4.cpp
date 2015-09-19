#include <stdio.h>
#include <math.h>

int main(){
    int n;
    int sc = 0;
    scanf("%d", &n);
    char arr[n][n];
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            scanf(" %c", &arr[i][j]);
            if(arr[i][j] == '#') sc += 1;
        }
    }

    int sss = sqrt(sc);
    bool square = true;
    if(sss*sss == sc){
        for(int a = 0; a < n; a++){ // ver
            for(int b = 0; b < n; b++){ // hor
                if (arr[a][b] == '#'){
                    for(int c = a; c < a+sss && c < n; c++){
                        for(int d = b; d < b+sss && d < n; d++){
                            if(arr[c][d] != '#'){
                                square = false;
                            }
                        }
                    }
                    goto abcd;
                }
            }
        }
    }else{
        square = false;
    }
    abcd:;
    if(square){
        printf("PEACEFUL");
    }else{
        printf("NON-PEACEFUL");
    }
}
