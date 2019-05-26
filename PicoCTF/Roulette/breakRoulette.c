/*
 * Upon inputting the starting cash value your next four bets will be given
 */

#include <stdio.h>
#include <stdlib.h>

int main(){
        int cash;
        int temp;
        scanf("%i",&cash);
        srand(cash);
        for (int i = 0; i < 3; i++){
                printf("bet: %i\n",((rand()%36)+1));
                temp = rand();
        }
        printf("don't bet: %i\n",((rand()%36)+1));
}