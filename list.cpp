#include <bits/stdc++.h>
using namespace std;

struct node{
	int data;
	struct node* next;
};

struct node *head = (node*) malloc(sizeof(node));

int main(){
	node *temp;
	temp = (struct node*) malloc(sizeof(struct node));
	int k = 45;
	temp -> data = k;
	temp -> next = head;
	cout << "Data is: " << temp->data << endl;
	cout << "Data address: " << temp->next << endl;
}
