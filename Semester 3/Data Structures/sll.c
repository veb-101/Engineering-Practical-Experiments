#include <stdio.h>
#include<malloc.h>
#include<stdlib.h>

void insert_at_beg(int);
void insert_at_end(int);
void insert_at_pos(int);
void delete_at_beg(void);
void delete_at_end(void);
void delete_at_pos(void);
void display();

struct node{
  int data;
  struct node *next;
} *start;

int main(void) {
	int value, choice;
	do{
    	printf("\n1.Insert at beginning. \n2.Insert at end. \n3.Insert at position. \n4.Delete from beginning. \n5.Delete from end. \n6.Delete at position. \n7.Display. \n8.Exit.\nEnter Choice:");
    	scanf("%d", &choice);
    	printf("\n");

    	switch(choice){
    		case 1:
    			printf("\nEnter data: ");
    			scanf("%d",&value);
    			insert_at_beg(value);
    			break;
    		case 2:
    			printf("\nEnter data: ");
    			scanf("%d",&value);
    			insert_at_end(value);
    			break;
    		case 3:
    			printf("\nEnter data: ");
    			scanf("%d",&value);
    			insert_at_pos(value);
    			break;
    		case 4:
    			delete_at_beg();
    			break;
    		case 5:
    			delete_at_end();
    			break;
    		case 6:
    			delete_at_pos();
    			break;
    		case 7:
    			display();
    			break;
    		case 8:
    			exit(0);
    		default:
    			printf("\nEnter the correct choice:\n");
    	}
	}while(choice !=8);
	return 0;
}

// Insert
void insert_at_beg(int val){
	struct node *newnode;
	newnode = (struct node*)malloc(sizeof(struct node));
	newnode->data = val;
	if (start==NULL){
    	newnode->next = NULL;
    	start = newnode;
	}
    else{
    	newnode->next = start;
    	start = newnode;
	}
}

void insert_at_end(int val){
	struct node *newnode, *temp;
	newnode = (struct node*)malloc(sizeof(struct node));
	newnode->data = val;
	newnode->next =NULL;
	if(start == NULL)
		start = newnode;
  	else{
    	temp = start;
    	while(temp->next !=NULL)
    	temp=temp->next;
		temp->next = newnode;
  	}
}

void insert_at_pos(int val){
	struct node *temp,*newnode;
	int i, pos;
	newnode = (struct node *)malloc(sizeof(struct node));
	display();
	printf("\n");
	printf("\nEnter the position for the new node to be inserted:");
	scanf("%d",&pos);
	pos--;
	newnode->data = val;
	newnode->next=NULL;
	if(pos==0){
    	insert_at_beg(val);
    	return;
  	}
	else{
		for(i=0,temp=start;i<pos-1;i++){
        	temp=temp->next;
        	if(temp==NULL){
            	printf("\nPosition not found:\n");
            	return;
            }
        }
    	newnode->next =temp->next ;
    	temp->next=newnode;
    }
}

// Delete
void delete_at_beg(){
	struct node *temp;
	if(start == NULL){
		printf("\nLinked list doesn't exist");
		return;
 	}
	else{
    	temp = start;
    	start = start->next;
    	free(temp);
    	return;
  	}
}

void delete_at_end(){
	struct node *temp = start;
	if(start == NULL){
		printf("\nLinked list doesn't exist");
    	return;
  	}
	while(temp->next->next != NULL){
    temp = temp->next;
  	}
	free(temp->next->next);
	temp->next = NULL;
}



void delete_at_pos(){
	int i, pos;
	struct node *temp,*ptr;
	temp = start;
  	if(start==NULL){
    	printf("\nThe List is Empty:\n");
    	exit(0);
	}
    else{
    	printf("\nEnter the position of the node to be deleted:");
    	scanf("%d",&pos);
        if(pos==0){
            delete_at_beg();
            return;}
        else if(temp->next==NULL) {
				delete_at_end();
                return;
    	}
		for(int i=2; i<pos; i++) {
    		if(temp->next!=NULL)
				temp = temp->next;
		}
		ptr = temp->next;
		temp->next = temp->next->next;
		free(ptr);
    }
}



void display(){
	struct node *temp;
	if(start == NULL)
		printf("\n list is empty");
	else{
		temp = start;
    	printf("\nLinked List elements are:\n");
    	while(temp!=NULL){
    		printf("%d -->",temp->data);
    		temp = temp->next;
    	}
     	printf("NULL\n");
	}
}
