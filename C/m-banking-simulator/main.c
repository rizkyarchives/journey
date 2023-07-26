#include "atm.h"
#include "atm.c"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

int main(void)
{
    int indicator = 0, totalRegist = 0, inactive = 0, loginInfo, Index, i;
    int * inactivePtr = &inactive;
    account * accounts = (account*)malloc(sizeof(account));
    char temp[50];
    do{
		//main menu
		printf("========================================================\n");
		printf("	    Mendiri Automatic Teller Machine		\n");
		printf("========================================================\n");
		printf("(1) Register to Mendiri (Total Registered Account(s): %d)\n", totalRegist);
		printf("(2) Login\n");
		printf("(3) Show All Mendiri's Customers\n");
		printf("(4) Show Deactivated/Blocked Accounts (Current: %d)\n", inactive);
		printf("(5) Clear Screen\n");
		printf("(99) Quit\n");
		printf("> ");
		scanf("%d", &indicator);
		getchar();
		if(indicator == 1) 
		{
			clrscr();
			printf("====Register to Mendiri====\n");
			totalRegist++;
			printf("\n");
			accounts = addAccount(accounts);
			menuTransition();
		}
		else if(indicator == 2) 
		{
			clrscr();
			printf("====Login====\n");
      		for(i = 2 ; i > -1 ; i--)
      		{
	  			printf("\nUser ID: ");
				scanf("%s", temp);
        		Index = findAccount(accounts, temp, totalRegist);
        		if(Index > -1)
          			break;
        		if(i != 0)
          			printf("<<User ID Not Found, Try Again! (%d attempt left)>>\n", i);
      		}
      		if(Index == -1)
        		printf("<<Log in Failed!>>");
     		 else
      		{
				Index = login(accounts, Index, totalRegist);
        		if(Index != -1)
        		{
          			printf("\n\n");
          			clrscr();
          			printf("<<Login Successful>>\n\n");
          			accountMenu(accounts, Index, totalRegist, inactivePtr);
        		}
        		else
        		{
          			inactive++;
          			printf("<<Account will be temporarily blocked!>>");
        		}
      		}
     		menuTransition();
		}
		else if(indicator == 3)
		{
			clrscr();
			printf("========================================================\n");
			printf("	          Mendiri Customer's		\n");
			printf("========================================================\n");
			printf("\n");
			printCustomer(accounts, totalRegist);
			menuTransition();
		}
		else if(indicator == 4)
		{
			clrscr();
			printf("========================================================\n");
			printf("	    Deactivated/Blocked Account(s)		\n");
			printf("========================================================\n");
			printf("\n");
			printDelCustomer(accounts, totalRegist);
			menuTransition();
		}
		else if(indicator == 5)
		{
			clrscr();	
		}
		else if(indicator == 99)//quit the program
			break;
	}while(indicator != 99);
	printf("Program End...");
	return 0;
}