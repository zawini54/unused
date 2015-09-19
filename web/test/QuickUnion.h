//
//  QuickUnion.h
//  test
//
//  Created by Schwinn Saeree on 6/24/2558 BE.
//  Copyright (c) 2558 Schwinn Saeree. All rights reserved.
//

#ifndef test_QuickUnion_h
#define test_QuickUnion_h

int root(int * a, int i){
    while(a[i] != i){
        i = a[i];
    }
    return i;
}

void connectto(int * a, int i, int j){
    int rootv = root(a, j);
    a[i] = rootv;
}

int connected(int * a, int i, int j){
    return (a[i] == a[j]);
}


#endif
