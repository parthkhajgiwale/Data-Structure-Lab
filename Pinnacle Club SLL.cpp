#include<iostream>
using namespace std;
class SLL{
struct node{
    int prn;
    string name;
    node* next;
}*start,*tail;
public:
SLL(){
    start=NULL;
}
void create();
void display();
void insertp();
void inserts();
void insertm();
void deletep();
void deletem();
void deletes();
void total();
};
void SLL::create(){
    node *temp, *current;
    char ans;
    do
    {
        temp=new node;
        temp->next=NULL;
        cout<<"\nEnter PRN: ";
        cin>>temp->prn;
        cout<<"\nEnter Name: ";
        cin>>temp->name;
        if(start==NULL){
            start=temp;
            current=temp;
        }
        else{
            current->next=temp;
            current=temp;
        }
        cout<<"\nAdd more y/n: ";
        cin>>ans;
    }while(ans=='y');
}
void SLL::insertp(){
    node *president=new node;
    cout<<"\nEnter PRN: ";
    cin>>president->prn;
    cout<<"\nEnter Name: ";
    cin>>president->name;
    president->next=start;
    start=president;
}
void SLL::inserts(){
    node *secretary=new node;
    if (start==NULL)
    {
        cout<<"\nList is Empty!!!";
    }
    else{
        cout<<"\nEnter PRN: ";
        cin>>secretary->prn;
        cout<<"\nEnter Name: ";
        cin>>secretary->name;
        secretary->next=NULL;
        node *temp = start;
        while(temp->next != NULL)
        {
            temp=temp->next;
        }
        temp->next=secretary;
    }  
    tail=secretary;
}
void SLL::insertm()
{
int prev_no;
    if (start==NULL)
    {
        cout<<"\nList is Empty!!!";
    }
    else{
             cout<<"\nEnter PRN No. after do you want insert:";
	cin>>prev_no;
	node *t;
	t=start;
	int flag=0;
	while(t!=NULL)
	{
		if(t->prn==prev_no)
		{
			flag=1;
            break;
		}
		t=t->next;
	}
	if(flag==1)
	{
		node *p=new node;
		cout<<"\nEnter PRN number: ";
	    cin>>p->prn;
	    cout<<"\nEnter name: ";
	    cin>>p->name;
	    p->next=t->next;
	    t->next=p;
	}
	else
	{
		cout<<"\n"<<prev_no<<" is not in list.";
	}
    }
}
void SLL::deletep()
{
	node *t;
	if(start==NULL)
		cout<<"\nList is Empty!!!";
	else
	{
	t=start;
	start=start->next;
	t->next=NULL;
	delete t;
	cout<<"\nPresident deleted..";
    }
}
void SLL::deletem()
{
	int no,flag=0;
	node *t,*prev;
	if(start==NULL)
		cout<<"\nList is Empty;";
	else
	{
		cout<<"\nEnter PRN no. of member to be deleted: ";
		cin>>no;
		t=start; 
		while(t->next!=NULL)
		{
			if(t->prn==no){
				flag=1;
				break;
			}
			prev=t;
			t=t->next;
		}
		if(flag==1)
		{
			prev->next=t->next;
			t->next=NULL;
			delete t;
			cout<<"\nMember with prn no: "<<no<<" is deleted.";
		}
		else
			cout<<"\nMember not found in List./president or secretary cannot be deleted.";
	}
}
void SLL::deletes()
{
	node *t,*prev;
	t=start;
		if(start==NULL)
		cout<<"\nClub is Empty..";
	else
	{
	while(t->next!=NULL)
	{
		prev=t;
		t=t->next;
	}
	prev->next=NULL;
	delete t;
	cout<<"\nSecretary Deleted.";
}
}
void SLL::total(){
	node *t; 
	int count=0;
    t=start;
	if(start==NULL){
		cout<<"List Is Empty";
	}
	else{
		while(t!=NULL){
			count++;
			t=t->next;
		}
	cout<<"\nTotal No. of Members are: "<<count;
	}
}
void SLL::display(){
    node *t;
    t=start;
    while (t != NULL) {
      cout<< t->prn <<" : "<<t->name<<" -> ";
      t = t->next;
   }
   cout<<"NULL";
}
int main(){
    SLL s;
    int choice;
   do
   {
    cout<<"\n1.Create\n2.Display\n3.Insert President\n4.Insert Secretary\n5.Insert Member\n6.Delete President\n7.Delete Member\n8.Delete Secretary\n9.Total No. of Members\nEnter Your Choice: ";
    cin>>choice;

    switch (choice)
    {
    case 1: s.create();
        break;
    case 2: s.display();
        break;
    case 3: s.insertp();
        break;
    case 4: s.inserts();
        break;
    case 5: s.insertm();
        break;
    case 6: s.deletep();
        break;
    case 7: s.deletem();
        break;
    case 8: s.deletes();
        break;
    case 9: s.total();
        break;
    default:
        break;
    }
   } while (choice<10);
    
return 0;
}
]
