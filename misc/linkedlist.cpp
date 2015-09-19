#include <cstdio>
#include <cstdlib>
using namespace std;

struct student{
    int c;
    int s;
};

struct Node{
    student data;
    Node *next;
};

Node *head;
Node *prev;

void addNode(student s, bool first){
    Node *temp = new Node();
    temp->data = s;
    temp->next = NULL;
    if(first){
        head = temp;
        prev = temp;
    }else{
        prev->next = temp;
        prev = temp;
   }
}

int main(){
    // Node *temp = new Node();
    // temp->data = 2;
    // temp->next = NULL;
    // head = temp;
    // temp = new Node();
    // temp->data = 3;
    // temp->next = NULL;
    // head->next = temp;
    addNode(2, true);
    addNode(3, false);
    printf("%d %d", head->data, head->next->data);
}