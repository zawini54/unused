#include <stdio.h>
using namespace std;

int res[3]; // holds resulting combination (size = r)
int r = 3; // depth of array
int n = 9; // range of values (not including n)
void combi(int lvl, int st){
	if(lvl == r+1){
		for(int i = 0; i < 3; i++){
			printf("%d", res[i]); // repeats same permutations while printing, idk why
		}
		printf("\n");
		return;
	}
	for(int i = st; i < n; i++){
		res[lvl] = i;
		combi(lvl+1, i+1);
	}
}
int main(){
	combi(0,0);
}
