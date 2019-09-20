#include <stdio.h>
#include<stdlib.h>
#define SIZE 5

int items[SIZE];
int front = -1, rear =-1;
int isFull()
{
    if( (front == rear + 1) || (front == 0 && rear == SIZE-1))
    	return 1;
    return 0;
}

int isEmpty(){
 	if(front == -1)
	   return 1;
    return 0;
}

void enQueue(int element){
    if(isFull())
	   printf("\n Queue is full!! \n");
    else {
        if(front == -1)
		      front = 0;
        rear = (rear + 1) % SIZE;
        items[rear] = element;
        printf("\n Inserted -> %d\n", element);
    }}

int deQueue(){
    int element;
    if(isEmpty()){
        printf("\n Queue is empty !! \n");
        return(-1);
    }
	else{
        element = items[front];
        if (front == rear){
            front = -1;
            rear = -1;
        }
        else {
            front = (front + 1) % SIZE;
            }
        printf("\n Deleted element -> %d \n", element);
        return(element);
    }}

void display(){
    int i;
    if(isEmpty()) printf(" \n Empty Queue\n");
    else{
        printf("\n Front -> %d ",front);
        printf("\n Items -> ");
        for( i = front; i!=rear; i=(i+1)%SIZE) {
            printf("%d ",items[i]);
        }
        printf("%d ",items[i]);
        printf("\n Rear -> %d \n",rear);
    }
}

int main(){
    int ele, choice;
    printf("\n\tCircular Queue\n\t--------------\n");
    do{
	printf("\n1.Insert element.\n2.Delete element.\n3.Diplay queue\n4.Exit.\nChoice:");
	scanf("%d", &choice);
	switch(choice){
		case 1:
			printf("\nEnter element:");
			scanf("%d", &ele);
			enQueue(ele);
			break;
		case 2:
			deQueue();
			break;
		case 3:
			display();
			break;
		case 4:
			exit(0);
			default:
			printf("Enter valid choice(1/2/3/4)"); }
	}while(choice!=4);
    return 0;
}
