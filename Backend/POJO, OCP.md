# POJO
Plain Old Java Object의 약자로, 특정 자바 프레임워크나 기술에 종속되지 않고 객체 지향 원칙에 충실하게 만든 <mark>순수한 자바 객체</mark>를 의미한다.

즉, IoC/DI(의존성 주입과 객체 관리), AOP(공통기능 분리), PSA(기술 추상화) 를 지키는 개발 방식이라고도 설명할 수 있다.

<br>
<br>

<big>특징  :</big>
**비종속성** <br>
대표적인 구성으로는 데이터를 저장하는 필드와 값을 읽고 쓰는 <mark>Getter/Setter</mark>등으로 이루어져있다.

<br>
<br>

### POJO가 왜 필요할까?
POJO를 지키지 않고 개발한다면 특정 프레임워크나 기술에 의존하게 되어 코드가 복잡해지고 **재사용과 테스트가 어려워**질 것이다.

그러니 특정 기술에 종속되지 않은 순수한 자바 객체인 POJO 프로그래밍을 사용해야한다!

<br>
<br>

### POJO의 규칙
<big>Java나 Java의 스펙에 정의된 것 이외에는 다른 기술이나 규약에 얽매이지 않아야 한다. </big>

예를 들어 아래와 같은 코드가 있다고 하자.
```java
public class User extends HttpServlet {
    
    private String name;

    public void doGet(HttpServletRequest request,
                      HttpServletResponse response) {
    }
}
```

`public class User extends HttpServlet`에서 알 수 있듯이, 이 코드는 현재 특정 기술에 의존하고 있다.

이런 경우는 후에 기술을 바꾸면 덩달아 코드까지 수정해야하는 불상사가 생겨버리고 말 것이다.

또한 JAVA는 다중 상속을 지원하지 않아 이미 extends를 통해 상속을 받아왔기에 객체지향적인 설계를 사용하기 힘들어진다.

<br>
<br>

그렇다면 이 코드를 POJO 형식으로 작성해보자.
```java
public class User {

    private String name;

    public User(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}
```
그저 일반적인 순수한 자바 클래스로 작성되었기에, 훨씬 쉽게 수정 및 유지보수가 가능할 것이다.

<br>
<br>

### 요약정리
POJO를 사용하면 특정 기술에 종속되지 않아 재사용성과 확장성을 향살할 수 있고, 테스트에 용이하며 객체지향적 설계가 가능하다!

<br>
<br>
<br>
<br>

# OCP
Open-Closed Principle(개방-폐쇄 원칙)의 약자로, <mark>확장에는 열려 있고 변경에는 닫혀 있어야 한다</mark>는 객체지향적 설계 원칙이다.

즉, 기존 코드를 수정하지 않고 새로운 기능을 추가할 수 있도록 하는 것이다.

<br>
<br>

### OCP가 왜 필요할까?
OCP를 지키지 않고 개발한다면 위에서 설명한 것처럼 새로운 기능을 추가할 때마다 기존 코드를 직접 수정해야 하기 때문에, 기존 기능에 오류가 발생하거나 코드가 복잡해지기 쉽상이다.

그러니 OCP 개발 원칙을 지키며 개발하는 것을 목표로 두어야 할 것이다!

<br>
<br>

이해를 위해 우선 예시 코드를 확인해보자.
```java
public class PaymentService {

    public void pay(String type) {

        if (type.equals("kakao")) {
            // 카카오페이 결제
        }

    }
}
```

처음 코드를 짤 때는 카카오페이 결제 방식만을 사용하니 이런 식으로 코드를 짰다.

그런데 네이버페이를 사용하도록 수정 요청이 들어온 것이다!

<br>

그렇다면 네이버 페이를 수정하기 위해 기존 코드를 

```java
if (type.equals("kakao")) {
    // 카카오페이
} else if (type.equals("naver")) {
    // 네이버페이
}
```
이런식으로 수정해야 한다...

<br>

그렇다면 기능이 추가될 때마다 PaymentService를 계속 수정해야 하므로 OCP를 지키지 않은 구조라고 볼 수 있겠다.

<br>
<br>

그렇다면 OCP를 지킨 구조는 무엇일까?

우선 인터페이스를 사용해 각 정보들이 무엇을 할 지 묶어주고,
```java
public interface Payment {
    void pay();
}
```
```java
public class NaverPay implements Payment {

    public void pay() {
        // 네이버페이 결제
    }
}
```
새 기능이 생길 때마다 이런식으로 새로운 클래스를 추가해 나가면 될 것이다.

<br>
<br>

### 요약정리

OCP를 사용하면 기존 코드를 수정하지 않고 새로운 기능을 추가할 수 있어 코드의 변경에 유연하고 유지보수가 쉬워지니 유의하며 코드를 작성해보자.