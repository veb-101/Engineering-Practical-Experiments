#include <stdio.h>
#include<stdlib.h>
#include<malloc.h>

struct Node{
	int data;
	struct Node *next;
	struct Node *prev;
} *head=NULL, *tail=NULL, *newnode=NULL;

void insert_beg(int data);
void insert_end(int data);
void insert_middle(int data, int index);

void delete_beg();
void delete_end();
void delete_middle(int index);

void display();
void print_forward_order();
void print_reverse_order();
int getListLength();

struct Node *newNode(int data){
		newnode = (struct Node *)malloc(sizeof(struct Node));
		newnode->data = data;
		newnode->prev = NULL;
		newnode->next = NULL;
		return newnode;
}

int main(){
	int choice, data, index, i;
	printf("Circular doubly linked list.\n");
	do{
		printf("\n1.Insert at begining\n2.Insert at end\n3.Insert middle\n4.Delete at begining\n5.Delete at end\n6.Delete middle\n7.Display\n8.Exit\nEnter choice: ");
		scanf("%d", &choice);
		switch(choice){
			case 1:
				printf("Enter data to add to head:");
				scanf("%d", &data);
				insert_beg(data);
				printf("\n");
				break;

			case 2:
				printf("Enter data to add to end:");
				scanf("%d", &data);
				insert_end(data);
				printf("\n");
				break;

			case 3:
				display();
				printf("Enter data:");
				scanf("%d", &data);
				printf("\n");
				printf("Enter location to add data:");
				scanf("\%d", &index);
				insert_middle(data, index);
				printf("After addition of data...\n");
				display();
				printf("\n");
				break;

			case 4:
				delete_beg();
				display();
				printf("\n");
				break;

			case 5:
				delete_end();
				display();
				printf("\n");
				break;

			case 6:
				printf("\n");
				display();
				printf("Enter location of data:");
				scanf("%d", &index);
				delete_middle(index);
				printf("\nAfter Deletion...\n");
				display();
				printf("\n");
				break;

			case 7:
				display(head);
				break;

			case 8:
    			exit(0);

    		default:
    			printf("\nEnter the correct choice:\n");
		}
	}while(choice != 8);
	return 0;
}


void insert_beg(int data){
	newnode = newNode(data);
	if (head == NULL){
		head = tail= newnode;
		newnode->next = newnode;
		newnode->prev = newnode;
	}
	else{
		newnode->next = head;
		newnode->prev = tail;
		head->prev = newnode;
		tail->next = newnode;
		head = newnode;
	}
}

void insert_end(int data){
	newnode = newNode(data);
	if(head==NULL)
    {
        head = newnode;
        tail = newnode;
		newnode->next= newnode;
		newnode->prev = newnode;
    }
	else{
		tail->next = newnode;
		newnode->next=head;
		newnode->prev = tail;
		tail=newnode;
		head->prev= tail;
	}
}

void insert_middle(int data, int index){
	if (index == 0){
		insert_beg(data);
		return;
	}
	else if(index > 1 && head!=NULL){
		struct Node *current = head;
		struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
		int count = 0;
		do{
			count++;
			temp = current;
			current = current->next;
		}while(current->next!=head && count<index -1);

		if(count ==index -1){
			if(temp==tail)
				insert_end(data);
			else{
				newnode = newNode(data);
				newnode->next = current;
				temp->next= newnode;
				newnode->prev = temp;
				current->prev = newnode;
			}
		return;
		}
	}
	printf("Position Doesn't exist");
}

void delete_beg(){
	if(head==NULL) return;
	struct Node *temp = head;
	tail->next = head->next;
	head = head->next;
	head->prev = tail;
	free(temp);
}

void delete_end(){
	if(head==NULL) return;
	struct Node *temp = head;
	struct Node *current = head;
	while(current->next != head)
    {
        temp = current;
        current = current->next;
    }
	temp->next =head;
	tail = temp;
	head->prev = tail;
	free(current);
}

void delete_middle(int index){
	if(head==NULL)  return;

    if(index==1)
    {
        delete_beg();
        return;
    }
	struct Node *current = head;
	struct Node *temp;
	int count = 0;
	do
    {
        count++;
        temp = current;
        current = current->next;
    }   while(current->next != head && count<index-1);

	if(count==index-1)
    {
        if(current==tail)
        {
            delete_end();
            return;
        }

		temp->next = current->next;
		current->next->prev = temp;
		free(current);
		return;
	}
	printf("Postion not found....\n");
}
void display()
{	printf("\n");
    printf("FORWARD order print:\n");
    print_forward_order();

    printf("REVERSE order print:\n");
    print_reverse_order();
}

void print_forward_order()
{
    if(head==NULL)  return;

    struct Node *current = head;

    do
    {
        printf("%d--> ", current->data);
        current = current->next;
    }   while(current != head);

    printf("\nList Length: %d\n", getListLength());
}

void print_reverse_order()
{
    if(head==NULL)  return;

    struct Node *current = tail;

    do
    {
        printf("%d--> ", current->data);
        current = current->prev;
    }   while(current != tail);

    printf("\nList Length: %d\n", getListLength());
}

int getListLength()
{
    if(head==NULL) return 0;

    int count = 0;
    struct Node *current = head;

    do
    {
        count++;
        current = current->next;
    }   while(current != head);

    return count;
}
