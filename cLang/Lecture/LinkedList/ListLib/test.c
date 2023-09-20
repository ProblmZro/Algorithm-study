#include <stdio.h>
#include "list.h"

struct student_t
{
    int age;
    char name[20];
    struct LIST_HEAD_T list;
};

int main() {

    LIST_HEAD(student_list);
    struct student_t p1 = { 21, "hyun", };
    struct student_t p2 = { 22, "cs", };
    struct LIST_HEAD_T* temp;
    struct student_t* p;

    list_add(&p1.list, &student_list);
    list_add(&p2.list, &student_list);


    //for( temp = head.prev; temp != &head; temp = temp->prev ) 
    list_for_each(temp, &student_list)
    {
        p = list_entry(temp, struct student_t, list);
        printf("name:%s, age:%d\n", p->name, p->age);
    }

	return 0;
}

/** 문제 1
위의 예제 프로그램을 아래와 같은 조건을 만족하도록 수정하세요.
1. 10명의 학생 정보를 동적 메모리 할당을 이용하여 리스트에 추가하세요.
2. list_add() 함수를 이용하여 student_list에 추가
3. list_for_each() 메크로를 이용하여 리스트에 존재하는 모든 학생 정보를 출력하고 list_for_each{} 내에서 할당된 메모리를 해제하세요.
4. 메모리가 잘 반납되는지 확인하고, 제대로 반납이 되지 않았다면 이를 해결하세요.
*/

/** 문제 2
1. 10명의 학생정보를 전역 변수 배열로 선언하세요.
2. 전역 변수로 선언 배열에서 빈 배열 요소를 할당하는 함수를 작성하세요.
3. 2에서 구현된 함수를 이용하여 문제 1의 동적 메모리 할당 부분을 대체하세요.
*/
