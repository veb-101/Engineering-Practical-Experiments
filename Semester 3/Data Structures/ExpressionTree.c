#include <stdio.h>
#include <string.h>
#include <malloc.h>

struct node
{
  struct node *right, *left, *prev;
  char data;
} * cur, *par, *root = NULL;

void preorder(struct node *);
void inorder(struct node *);

int main()
{
  char a[100];
  int len, i;
  struct node *new_node;
  printf("Enter Postfix Expression\n");
  fgets(a, 100, stdin);
  len = strlen(a);
  for (i = len - 1; i >= 0; i--)
  {
    new_node = (struct node *)malloc(sizeof(struct node));
    new_node->data = a[i];
    new_node->left = new_node->right = new_node->prev = NULL;
    if (root == NULL)
    {
      root = new_node;
      cur = par = root;
    }
    else
    {
      if (a[i] == '+' || a[i] == '-' || a[i] == '*' || a[i] == '/')
      {
        if (par->right == NULL)
        {
          cur = new_node;
          par->right = cur;
          cur->prev = par;
          par = cur;
        }
        else if (par->left == NULL)
        {
          cur = new_node;
          par->left = cur;
          cur->prev = par;
          par = cur;
        }
        else
        {
          while (par->left != NULL)
          {
            par = par->prev;
          }
          cur = new_node;
          par->left = cur;
          cur->prev = par;
          par = cur;
        }
      }
      else
      {
        if (par->right == NULL)
        {
          cur = new_node;
          par->right = cur;
          cur->prev = par;
        }
        else if (par->left == NULL)
        {
          cur = new_node;
          par->left = cur;
          cur->prev = par;
        }
        else
        {
          while (par->left != NULL)
          {
            par = par->prev;
          }
          cur = new_node;
          par->left = cur;
          cur->prev = par;
        }
      }
    }
  }
  printf("\nInorder Traversal: \n");
  inorder(root);
  printf("\n\nPreorder Traversal: \n");
  preorder(root);
}

//-------INORDER-------
void inorder(struct node *root)
{
  if (root != NULL)
  {
    inorder(root->left);
    printf("%c\t", root->data);
    inorder(root->right);
  }
}

//-------PREORDER-------
void preorder(struct node *root)
{
  if (root != NULL)
  {
    printf("%c\t", root->data);
    preorder(root->left);
    preorder(root->right);
  }
}
