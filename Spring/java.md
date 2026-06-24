# 1. 자바

자바는 프로그램을 만들기 위해 사용하는 프로그래밍 언어로, 컴퓨터에게 명령을 내리는 코드를 작성할 때 사용된다. 
<br> <br> 
대표적인 특징으로는 **객체 지향 언어**이며, 운영체제에 **독립적**이라는 점이 있다.

<br>
<br>
<br>
<br>

# 2. 변수와 연산자

자바를 사용하기 위해 기본적으로 알아야 하는 개념이다.

###  변수
변수란 데이터를 저장하기 위한 공간이다.
<BR>
<br>
<br>

### 연산자

- 산술 연산자: `+`, `-`, `*`, `/`
- 증감 연산자: `++`, `--`
- 논리 연산자: `&&`, `||`, `!`
- 대입 연산자: `=`, `+=`, `-=`, `*=`, `/=`, `%=`
- 비교 연산자: `==`, `!=`, `>`, `<`, `>=`, `<=`
<br>
<br>
<br>
<br>



# 3. If문


조건을 판단하여 참일 때 코드를 실행하는 조건문이다.
<br>

##### 예시
```java
if (조건식) {
    실행할 코드
}
```
<br>
<br>
<br>

### else 와 else if

- else는 위 조건이 모두 거짓일 때 실행한다.
- else if는 여러 조건을 순서대로 조건 여러개를 나열할 수 있다.
<br>

##### 예시

```java
if (조건1) {
} else if (조건2) {
} else {
}
```
<br>
<br>
<br>
<br>

### switch
switch문은 조건 값에 따라 맞는 값을 실행하며, 반복문의 끝에 `break`를 사용해야 한다.
<br>
<br>
<br>
<br>

### 삼항 연산자
조건이 참이면 왼쪽, 거짓이면 오른쪽 값을 출력한다.
<br>
##### 예시
```java
int age = 15;
String status = (age >= 18) ? "성인" : "미성년자";
```

<br>
<br>
<br>
<br>


# 4. 반복문

반복되는 특정 조건이 만족되는 동안 코드를 반복 실행한다.
<br>
<br>
<br>
<br>

### while문

- 조건이 복잡할 때 사용  
- `while(true)`는 무한 반복  

##### 예시
```java
int count = 1;
while (count <= 10) {
    System.out.println(count);
    count++;
}
```
<br>
<br>
<br>
<br>

## for문

- 초기화, 체크, 반복 후 작업 등을 한번에 처리에 편리하다.
- 초기식, 조건식, 코드, 증감식 순으로 실행되며, 초기식은 한번만 실행한다.
- 실무에선 대부분 for문을 가장 많이 사용한다고 한다.
<br>
<br>
<br>

##### 예시

```java
for (int i = 1; i <= 10; i++) {
    System.out.println(i);
}
```

<br>
<br>
<br>
<br>
<br>

## 추가 개념

- 중첩 반복문은 반복문 안에 반복문을 만들 수 있다. 
- 이때, 내부와 외부의 곱이 수행된다.
- break로 while 반복문을 종료한다.
- continue는 다시 조건문의 처음으로 돌아간다. 

<br>
<br>
<br>
<br>


# 5. 스코프와 형변환

### 스코프
변수가 선언된 위치에 따라 사용 범위가 분류된다.

> 메모리 낭비를 막기 위해

<br>
<br>
<br>
<br>

### 형변환

데이터의 타입을 맞게 변환하는 것이다.
<br>
<br>

> 단, 타입에 의해 소수점등이 날아갈 수도 있다.

> 작은 타입 → 큰 타입: 자동 변환  
> 큰 타입 → 작은 타입: 강제 변환 필요  
<br>
<br>
<br>

##### 예시

```java
double doubleValue = 1.5;
int intValue;

intValue = (int) doubleValue; // 소수점 버려짐
```
<br>
<br>
<br>
<br>

 ### Scanner

 파이썬의 input과 같이, 입력받는 도구이다.

 ##### 예제로 익히는 편이 효율적.

 ```java
Scanner scanner = new Scanner(System.in);

System.out.print("문자열을 입력하세요");
String str = scanner.nextLine();
System.out.println("입력한 문자열: " + str);

System.out.print("정수를 입력하세요");
int intValue = scanner.nextInt();
System.out.println("입력한 정수: " + intValue);

System.out.print("실수를 입력하세요");
float aaa = scanner.nextFloat();
System.out.println("입력한 실수: " + aaa);
```
<br>
<br>
<br>

**알아두면 좋은 점**
> 실수형을 쓰려면 보통 double을 사용한다.

> println은 줄을 뛰지만, print는 뛰지 않는다.

>문자열로 비교구문을 사용하고 싶을땐 str(equals("--")) 형태로 써야한다.

<br>
<br>
<br>
<br>

 ### 배열
 같은 타입의 여러 값을 한 번에 저장하는 공간이다.
 >사용 예시 : int[] arr = new int[3];

<br>
<br>
<br>

 ### 향상된 for문
 이전에 정리했듯 for문은 반복적인 특징을 가진 코드를 반복 실행할 수 있다.
 이때, for문을 더 간결하고 편하게 쓸 수 있는 방법이다.


'''

    java
    int[] a = {1, 2, 3, 4, 5};
    for (int i = 0; i < a.length; i++) {

    //과

    for (int num : a) {
    }

     //은 같은 뜻이다.
'''
<br>
<br>
<br>
<br>

# 메서드
특정 기능을 수행하는 코드의 묶음으로, 필요할 때마다 호출하여 사용할 수 있다.
코드를 반복해서 작성하지 않아도 되어 효율적인 프로그램 작성이 가능하다.
<br>
<br>
<br>

#### 메서드의 기본 구조

'''반환타입 메서드이름(매개변수) {
    실행문;
    return 반환값;
}'''

> 반환타입: 메서드 실행 후 돌려주는 값의 자료형
<br>
> 메서드이름: 기능을 나타내는 이름
<br>
> 매개변수: 메서드에 전달되는 입력값
<br>
> return: 결과 값을 호출한 곳으로 반환

<br>
<br>
<br>
<br>

### 메서드 호출
```int result = add(3, 5);
System.out.println(result);
```

해당 기능이 실행되면 결과 값이 반환된다.

### 반환값이 없는 메서드
```void printHello() {
    System.out.println("Hello");
}
```

void는 반환값이 없음을 의미하고 이때는 기능만 수행한다.

### 매개변수가 없는 메서드
```void hello() {
    System.out.println("Hi");
}
```

입력 없이 실행되는 메서드다.
<br>
<br>
<br>
<br>
#### 주요 개념 정리

> 메서드는 코드를 기능별로 나누어 관리할 수 있게 해준다.
<br>
> 코드의 재사용성을 높여준다.
<br>
> 프로그램의 구조를 더 이해하기 쉽게 만들어준다.













<br>
<br>
<br>
<br>




# 클래스

자바에서의 메서드는 부모 메서드와 자식 메서드를 가진다. 자식 메서드는 부모 메서드를 사용할 수 있으며, <b>super</b>로 부모 메서드를 지정할 수 있다.

- 하지만 부모가 자식을 참조하려면 형변환을 거쳐야한다. 
 ##### ex)
 ``` public class BusExam{
        public static void main(String args[]){
            Car car = new Bus();
            car.run();
            //car.ppangppang(); // 컴파일 오류 발생

            Bus bus = (Bus)car;  //부모타입을 자식타입으로 형변환 
            bus.run();
            bus.ppangppang();
        }
    } 
```
<br>
<br>
<br>
<br>

## enum

자바에서 열거형을 사용할 때 작성한다.
#### ex
```
public class Main {
    enum Day { MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY }

    public static void main(String[] args) {
        Day today = Day.WEDNESDAY;

        if(today == Day.WEDNESDAY) {
            System.out.println("오늘은 수요일이야!");
        }
    }
}
```
<br>
<br>

### 추상 클래스

> 추상 클래스는 직접 객체를 만들 수 없고, 자식 클래스가 상속받도록 설계된 클래스

> 추상 메소드를 포함할 수 있고, 자식 클래스가 반드시 구현해야됨

>일반 메소드와 변수도 가질 수 있어서 공통 기능 재사용이 가능

<br>

### 익명 클래스와 내부 클래스


| 구분 | 정의 | 이름 | 재사용 | 외부 클래스 접근 | 코드 길이 | 사용 사례 |
|------|------|------|--------|----------------|-----------|-----------|
| **내부 클래스** | 클래스 안에 선언된 클래스 | 있음 | 가능 | 가능 | 중간 | 이벤트 처리, 외부 클래스 참조 필요, 재사용 가능 |
| **익명 클래스** | 이름 없이 바로 객체 생성 | 없음 | 불가 | 가능 | 길어질 수 있음 | 버튼 클릭, 스레드, 콜백, 일회용 객체 |

<br>

- 재사용 필요 → 내부 클래스
- 일회성, 외부 <b>this</b> 필요 → 익명 클래스

<br>
<br>
<br>
<br>

# 여러 자바 기능들

- ### exception
  - 예외 상황을 미리 예측하고 처리하는 문법 (예외 여부에 상관없이 실행된다. ex:10/0)

<br>

- ### throws
  - 예외가 발생했을때 예외를 호출한 쪽에서 처리하도록 던져준다.

<br>

> throw는 오류를 떠넘기는 throws와 함께 보통 사용된다. (exceptoin 발생)