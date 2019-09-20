#include<stdio.h>
#include<stdlib.h>
#define SIZE 5

void enQueue(int);
void deQueue();
void display();
int items[SIZE], front = -1, rear = -1, i;
int main() {
	int choice, num;
	printf("\nImplrmentation of Queue Data Structureok using Stack...");
	do{
        printf("\n1.Insert.\n2.Delete\n3.Display Queue\n4.Exit\nChoice:");
		scanf("%d", &choice);
		switch(choice){
			case 1:
				printf("\nEnter element to add in queue:");
				scanf("%d",&num);
				enQueue(num);
				break;
			case 2:
				printf("\nPopping the the oldest element in queue...");
				deQueue();
				break;
			case 3:
				display();
				break;
			case 4:
				exit(0);
			default: printf("\nSelect the proper choice...");
		}
	}while(choice != 4);
    return 0;
}

void enQueue(int value) {
    if(rear == SIZE - 1)
        printf("\nQueue is Full!!\n");
    else{
        if(front == -1)
            front = 0;
        rear++;
        items[rear] = value;
        printf("\nInserted -> %d\n", value);
    }
}

void deQueue() {
    if(front == -1){
        printf("\nQueue is empty");
		printf("\n");
	}
    else{
        printf("\nDeleted -> %d\n", items[front]);
		front++;
        if(front > rear)
            front = rear = -1;
    }
}

void display(){
	if(rear == -1)
        printf("\nQueue is empty");
    else{
        printf("\nElements are: \n");
        for (i=front; i<=rear; i++)
            printf("%d\t", items[i]);
		printf("\n");
	}
}
