#include <stdio.h>
#include <string>

using namespace std;

char shift(char c, int n);

int main(){
    int n;
    scanf("%d\n", &n);
    char *arr;
    int index = 0;
    while(true){
        char c;
        scanf("%c", &c);
        if(c == '\n') break;
        *(arr+index) = c;
        index++;
    }
    for(int i = index -1; i >= 0; i--){
        printf("%c\n", shift(*(arr+i), n));
    }
}
char shift(char c, int n){
    char alphabet_lower[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    char alphabet_upper[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    bool uppercase = false;
    int index = 0;
    for(int i = 0; i < 26; i++){
        if(c == alphabet_lower[i]){
            index = i;
            break;
        }
    }
    if (index == 0 && c != 'a'){
        uppercase = true;
        for(int i = 0; i < 26; i++){
            if(c == alphabet_upper[i]){
                index = i;
                break;
            }
        }
    }
    
    if(uppercase){
        if(index-n < 0){
            index = 26-(n-index);
        }else{
            index = index - n;
        }
        return alphabet_upper[index];
    }else{
        if(index-n < 0){
            index = 26-(n-index);
        }else{
            index = index - n;
        }
        return alphabet_lower[index];
    }
}
