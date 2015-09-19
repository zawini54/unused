//
//  main.c
//  test
//
//  Created by Schwinn Saeree on 6/24/2558 BE.
//  Copyright (c) 2558 Schwinn Saeree. All rights reserved.
//

#include <stdio.h>
#include "QuickUnion.h"
void print(char* c){
    int i = 0;
    while(c[i] != '\0'){
        printf("%d\n",&c[i]);
        i++;
    }
}

int main(int argc, const char * argv[]) {
    
    int id[9] = {0, 1, 2, 3, 4, 5, 6, 7, 8};
    connectto(id, 0, 1); // function is actually receiving &id[0]
    connectto(id, 1, 2);
    connectto(id, 3, 0);
    int tf = connected(id, 7, 3);
    printf("%d\n", tf);
    
    for(int i = 0; i < 9; i++){
        printf("%d",id[i]);
    }
    /*int a[3] = {1,2,3};
    int *b = a;
    printf("%d", ++b[0]);
    
    char * gg = "ggwp";
    printf(++gg);
    
    char n[] = "hoihoi";
    print(n);
    
    char r[] = "ppooiiuu";
    char * k = r;
    printf("%d\n", &k); //memory address of pointer
    printf("%d\n", k); // pointer value
    printf("%d\n", &k[0]); // same value as above
    printf("%c", k[0]); // p*/
    
    return 0;
}