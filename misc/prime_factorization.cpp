#include <iostream>
#include <vector>
using namespace std;
int main(){
	// prime numbers up to but not including n
	int n;
	cin >> n;
	int pi = 0;
	int primes[n];
	int crossed[n+1];
	for(int i = 2; i <= n; i++) crossed[i] = false;
	for(int i = 2; i <= n; i++){
		if(!crossed[i]){
			primes[pi] = i;
			pi++;
			for(int j = i; j <= n; j += i) crossed[j] = true;
		}
	}
	
	for(int i = pi-1; i >= 0; i--){
		if(n % primes[i] == 0){
			cout << primes[i] << endl;
			break;
		}
	}
}
