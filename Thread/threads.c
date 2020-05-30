#include<stdio.h>
#include<pthread.h>
#include<unistd.h>
int s = 0;
int m = 0;
int h = 0;
int x = 1;

void *seconds(){
	while(x){
		sleep(1);
		s++;
		if(s == 60){
			m++;
			s = 0;
		}
	}
}

void *minutes(){
	while(x){
		if (m == 60){
			h++;
			m = 0;
		}
	}
}

void *hours(){
	while(x){
		if (h == 24){
			h = 0;
		}
	}
}
void *print_clock(){
	while(x){
		if(h<=9){
			printf("\r0%d:",h);
		}
		else{
			printf("\r%d:",h);
		}
		if(m<=9){
			printf("0%d:",m);
		}
		else{
			printf("%d:",m);
		}
		if(s<=9){
			printf("0%d",s);
		}
		else{
			printf("%d",s);
		}
	}
}


int main(){
	printf("Stopwatch:  \n");
	pthread_t sec,min,hr,print;
	pthread_create(&sec,NULL,seconds,NULL);
	pthread_create(&min,NULL,minutes,NULL);
	pthread_create(&hr,NULL,hours,NULL);
	pthread_create(&print,NULL,print_clock,NULL);
	pthread_join(sec,NULL);
	pthread_join(min,NULL);
	pthread_join(hr,NULL);
	pthread_join(print,NULL);
	return 0;
}