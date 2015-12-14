# include <stdio.h>
# include <stdlib.h>

# define LETTER 	0
# define NUMBER		1
# define ILLEGAL	2

extern unsigned long int frequencies[];

typedef struct block Node;

struct block {
	union {
		struct {
			unsigned char type; 
			} datatype;
		struct {
			unsigned char type;
			unsigned char letter;
			} dataletter;
		struct {
			unsigned char type;
			unsigned long num;
			} datanum;
		} data;
	Node* bottomleft;
	Node* bottomright;
	Node* right;
	} ;

static Node* head	= NULL;

Node* createNode(void){
	Node* temp 	= (Node*)malloc(sizeof(Node));
	temp -> bottomleft	= temp -> bottomright	= temp -> right	= NULL;
	temp -> data.datatype.type	= ILLEGAL;
	return temp;
	}

void addToQueue(Node* node) {
	
	Node* curr	= head;
	Node* prev	= NULL;
	unsigned long	nodeVal,currVal;
	
	if ( node -> data.datatype.type == LETTER ) nodeVal = frequencies[ node -> data.dataletter.letter];
	else nodeVal	= node -> data.datanum.num;


	for ( ; curr ; curr = curr -> right ) {
		if ( curr -> data.datatype.type	== LETTER ) currVal = frequencies[ curr -> data.dataletter.letter] ;
		else currVal	= curr -> data.datanum.num;
		
		if ( nodeVal < currVal ) break; // we may use <= . it just gives small effect.
		prev	= curr;
		}

	if ( prev == NULL ){
		node -> right	= head;
		head		= node;
		}
	else {
		node -> right	= prev -> right;
		prev -> right	= node;
		}
	}

void printQueue (void) {
	for ( Node* temp = head; temp; temp= temp -> right ) printf("%lu\n",frequencies[ temp->data.dataletter.letter] );
	}

Node* buildQueue(void){
	
	int index	= 0;

	for (; 	index 	< 128 && !frequencies[index] ; ++index );
	if  ( 	index	< 128 ) { 
		head 	= createNode();
		head -> data.datatype.type	= LETTER;
		head -> data.dataletter.letter	= index;
		Node* temp	= NULL;
		for (index++;	index	< 128; ++index)
			if ( frequencies[index] ){
				temp=createNode();
				temp -> data.datatype.type 	= LETTER;
				temp -> data.dataletter.letter	= index;
				addToQueue(temp);
				}
		}
	}

void traverseTree( Node* node ) {
	if ( !node ) return;
	traverseTree( node -> bottomleft );
	traverseTree( node -> bottomright);
	if ( node -> data.datatype.type	== LETTER ) printf("'%c'",node -> data.dataletter.letter);
	else printf("%lu",node -> data.datanum.num);
	}

void buildTree(void) {
	buildQueue();
	printQueue();

	int lvalue,rvalue;
	if ( !head ) exit(EXIT_FAILURE);
	while ( head -> right ) {
		Node* temp = createNode();
		temp 	-> bottomleft = head;
		temp	-> bottomright = head -> right;
		head 	=  head  -> right -> right;

		temp	-> bottomleft	-> right = NULL;
		temp	-> bottomright	-> right = NULL;
		
		if ( temp -> bottomleft -> data.datatype.type == LETTER ) 
			lvalue	= frequencies[ temp -> bottomleft -> data.dataletter.letter ];
		else 	lvalue	= temp -> bottomleft -> data.datanum.num;

		if ( temp -> bottomright -> data.datatype.type == LETTER ) 
			rvalue = frequencies[ temp -> bottomright -> data.dataletter.letter ];
		else rvalue	= temp -> bottomright -> data.datanum.num;

		temp -> data.datatype.type = NUMBER;
		temp -> data.datanum.num= lvalue + rvalue;

		if ( !head ) head	= temp;
		else addToQueue( temp );
		}
	traverseTree(head);
	}

