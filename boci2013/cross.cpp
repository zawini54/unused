#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n*3; j++){
            if(!(j < n || j >= 2*n)){
                printf("*");
            }else if(j != n*3-1){
                printf(" ");
            }else{
                printf("\n");
            }
        }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n*3; j++){
            if(j != n*3-1){
                printf("*");
            }else{
                printf("*\n");
            }
        }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n*3; j++){
            if(!(j < n || j >= 2*n)){
                printf("*");
            }else if(j != n*3-1){
                printf(" ");
            }else{
                printf("\n");
            }
        }
    }
}