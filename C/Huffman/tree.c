# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include "Compress.h"

# define LETTER 	0
# define NUMBER		1
# define ILLEGAL	2

extern info characters[];
char* buffer	= NULL;
unsigned long currsize	= BUFSIZ;

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
	
	if ( node -> data.datatype.type == LETTER ) nodeVal = characters[ node -> data.dataletter.letter].count;
	else nodeVal	= node -> data.datanum.num;


	for ( ; curr ; curr = curr -> right ) {
		if ( curr -> data.datatype.type	== LETTER ) currVal = characters[ curr -> data.dataletter.letter].count ;
		else currVal	= curr -> data.datanum.num;
		
		if ( nodeVal <= currVal ) break; // we may use < . it just gives small effect.
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
	for ( Node* temp = head; temp; temp= temp -> right ) printf("%lu\n",characters[ temp->data.dataletter.letter].count );
	}

Node* buildQueue(void){
	
	int index	= 0;

	for (; 	index 	< 128 && !characters[index].count ; ++index );
	if  ( 	index	< 128 ) { 
		head 	= createNode();
		head -> data.datatype.type	= LETTER;
		head -> data.dataletter.letter	= index;
		Node* temp	= NULL;
		for (index++;	index	< 128; ++index)
			if ( characters[index].count ){
				temp=createNode();
				temp -> data.datatype.type 	= LETTER;
				temp -> data.dataletter.letter	= index;
				addToQueue(temp);
				}
		}
	}

void traverseTree( Node* node ,long index) {
	if ( !node ) return;
	if ( !node -> bottomleft && !node -> bottomright ) {
		buffer[index]	= '\0';
		printf ("'%c'",node->data.dataletter.letter);
		characters[node	-> data.dataletter.letter].bitstring	 = (unsigned char*)malloc( strlen(buffer)+1 );
		strcpy(	characters[node	-> data.dataletter.letter].bitstring , buffer );
		return;
		}
	
	if ( index == currsize-1 ) buffer=realloc(buffer,currsize+BUFSIZ);
	buffer[index]	= '0';
	traverseTree( node -> bottomleft ,index+1);
	buffer[index]	= '1';
	traverseTree( node -> bottomright, index+1);
	if ( node -> data.datatype.type	== LETTER ) printf("'%c'", node -> data.dataletter.letter);
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
			lvalue	= characters[ temp -> bottomleft -> data.dataletter.letter ].count;
		else 	lvalue	= temp -> bottomleft -> data.datanum.num;

		if ( temp -> bottomright -> data.datatype.type == LETTER ) 
			rvalue = characters[ temp -> bottomright -> data.dataletter.letter ].count;
		else rvalue	= temp -> bottomright -> data.datanum.num;

		temp -> data.datatype.type = NUMBER;
		temp -> data.datanum.num= lvalue + rvalue;

		if ( !head ) head	= temp;
		else addToQueue( temp );
		}
	buffer	= (unsigned char*)malloc	( currsize );
	traverseTree(head,0UL);
	
	// tester
	for ( int var = 0; var <128 ;++ var ) {
		if ( characters[var].count ){
			printf("%c\t%s\n",var,characters[var].bitstring);
		//	writeBits( characters[var].bitstring );	
			}
		}
	writeBits( "011111111001" );
	writeBufferedString( NULL,1,0 );//start
	printf("OK\n");
	/*for ( int var = 0; var <128 ;++ var ) {
		if ( characters[var].count ){
		//	printf("%c\t%s\n",var,characters[var].bitstring);
		//	writeBits( characters[var].bitstring );	
			writeBufferedString(characters[var].bitstring,0,0);
			}
		}*/
	writeBufferedString("hello",0,0);
	writeBufferedString("hello",0,0);
writeBufferedString("hello",0,0);writeBufferedString("hello",0,0);writeBufferedString("hello",0,0);writeBufferedString("hellosaikirankasdlkjasdf",0,0);
	writeBufferedString(NULL,0,1);//stop
	}

