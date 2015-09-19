#include <stdio.h>

int u[3]; // holds value of either 0 or 1 at each index. Index represents value
int r = 3; // depth of array
int res[3];

void permute(int lvl){
	if(lvl > r){
		// print res
	}
	for(int i = 0; i < n; i++){
		if(u[i]) continue;
		u[i] = 1;
		res[lvl] = i;
		permute(lvl+1);
		u[i] = 0;
	}
}
