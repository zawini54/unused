int main(){
    int n = 7, b = 2;
    int ret = 1, run = b;
    for(int i = 0; (1<<i)<=n; i++){
        if((n&(1<<i)) >= 0)
            ret *= run;
        run *= run;
    }
    printf("%d", ret);
}
