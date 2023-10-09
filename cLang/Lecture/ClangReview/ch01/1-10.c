#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

struct Time {
  long long us;
  long long ms;
};

int main() {
  struct Time *start = NULL;
  struct Time *end = NULL;

  start = (struct Time *)malloc(sizeof(struct Time));
  end = (struct Time *)malloc(sizeof(struct Time));

  struct timeval tv;
  gettimeofday(&tv, NULL);
  start -> us = tv.tv_usec;
  start -> ms = (start -> us) / 1000;

  long long cnt = 0;
  while (cnt < 1000000) {
    cnt++;
  }
  
  gettimeofday(&tv, NULL);
  end -> us = tv.tv_usec;
  end -> ms = (end -> us) / 1000;

  long long diff_us = (end->us) - (start->us);
  long long diff_ms = (end->ms) - (start->ms);

  printf("시작 시간 (us, ms) : %lld, %lld\n", start->us, start->ms);
  printf("종료 시간 (us, ms) : %lld, %lld\n", end->us, end->ms);
  printf("시간 차이 (us, ms) : %lld, %lld\n", diff_us, diff_ms);

  free(start);
  free(end);
}