#include<stdio.h>
#include<stdlib.h>

void dfs(int s,int n);
void push(int item);
int pop();

int top=-1, a[20][20], vis[20], stack[20];

int main() {
	int n,i,s,j;
	printf("Enter number of vertices:");
	scanf("%d",&n);
	for(i=1;i<=n;i++) {
		for(j=1;j<=n;j++) {
			printf("Enter 1 if %d has a node with %d else 0 ",i,j);
			scanf("%d",&a[i][j]);
		}
	}
	printf("Adjacency matrix\n");
	for(i=1;i<=n;i++){
		for(j=1;j<=n;j++){
			printf(" %d",a[i][j]);
		}
	printf("\n");
	}

	for(i=1;i<=n;i++)
		vis[i]=0;
	printf("Enter source vertex:");
	scanf("%d",&s);
    dfs(s,n);
}

void dfs(int s,int n) {
	int i,k;
	push(s);
	vis[s]=1;
	k=pop();
	if(k!=0)
		printf(" %d ",k);
	while(k!=0){
		for(i=1;i<=n;i++)
			if((a[k][i]!=0)&&(vis[i]==0)){
				push(i);
				vis[i]=1;
			}
		k=pop();
		if(k!=0)
			printf(" %d ",k);
	}
	for(i=1;i<=n;i++)
		if(vis[i]==0)
			dfs(i,n);
	}

void push(int item) {
	if(top==19)
		printf("Stack overflow ");
	else
		stack[++top]=item;
	}

int pop() {
	int k;
	if(top==-1)
		return(0);
	else {
		k=stack[top--];
		return(k);
	}
}
