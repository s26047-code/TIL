# Java API란?
프로그램 개발에 사용할 수 있게 자바에서 제공하는 클래스&인터페이스의 모음. JDK 설치 압축 파일에 포함되어 있어 불러오거나 바로 사용할 수 있다.


<br>
<br>

### String
문자열을 다루는 클래스
- length() -> 길이 `"hello".length() → 5`
- equals() -> 같은 지 비교 `"a".equals("a") → true`
- toUpperCase() -> 대문자로 `"abc".toUpperCase() → ABC`
- toLowerCase() -> 소문자로 `"ABC".toLowerCase() → abc`
- substring() -> 문자열 자르기 `"hello".substring(1, 3) → "el"`
- contains() -> 포함되어 있는지 `"hello".contains("ell") → true`
- startsWith() -> ~로 시작하는지 `"hello".startsWith("he") → true`
- endsWith() -> ~로 끝나는지 `"hello".endsWith("lo") → true`
- trim() -> 앞 뒤 공백 제거 `" hi ".trim()`
- replace() -> 문자열 교체  `"hello".replace("h", "H") → Hello`

<br>
<br>

### ✓ Object
모든 Java 클래스의 가장 기본적인 부모 클래스 <br>
  <mark>Object에 있는 메서드는 거의 모든 객체에서 사용 가능</mark>

  - toString() -> 객체를 문자열로 표현<br>
  `System.out.println(객체.toString());`
  - equals() -> 두 객체가 같은 지 비교 <br>
  `객체1.equals(객체2);`

<br>
<br>

### Wrapper
자료형 객체 클래스
- Integer -> int
- Long -> long
- Double -> double
- Boolean -> boolean

예를 들어 `private Integer viewCount;` 라는 코드가 있다면, viewCount라는 변수가 아닌 객체가 생성되는 것

<br>
<br>

### Math
수학 관련 기능을 지원하는 클래스
- max -> 최대 `Math.max(10, 20); -> 20`
- min -> 최소 `Math.min(10, 20); -> 10`
- abs -> 절댓값 `Math.abs(-10); -> 10`
- round -> 반올림 `Math.round(3.6); -> 4`
- random -> 랜덤 `Math.random(); -> 랜덤값`

<br>
<br>

#### **아래부터는 Scanner처럼 import가 필요함.**

<br>
<br>

### Set/HashSet
중복을 허용하지 않는 자료 구조
```java
Set<String> names = new HashSet<>();

names.add("철수");
names.add("철수");
names.add("영희");
```
결과값 = 철수 영희

메서드(add, size..)는 List와 거의 유사함.

<br>
<br>

### Map/HashMap
key-value값으로 저장
```java
Map<String, Integer> scores = new HashMap<>();

scores.put("철수", 90);
scores.put("영희", 80);

scores.get("철수");
```
결과값 = 90

> - put -> 넣기 `scores.put("다원", 100);`
> - get -> 가져오기 `scores.get("철수");`
> - remove -> 삭제 `scores.remove("철수");`
> - containsKey -> 키가 있는지 `scores.containsKey("철수");`

<br>
<br>

### ✓ Objects 
`java.util.Objects`에 포함된 유틸리티 클래스. <mark>객체 관련</mark> 편의 기능을 함
- equals() -> 객체 비교 `Objects.equals(객체1, 객체2);`
- isNull() -> null인가? `Objects.isNull(객체);`
- nonNull() -> null이 아닌가? `Objects.nonNull(객체);`
 
 <br>
 <br>

### Optinal
값이 있을 수도 있고 없을 수도 있음(Null 오류 방지)

- isPresent() -> 값이 있는지 `user.isPresent();`
- isEmptu() -> 값이 없는지 `user.isEmpty();`
- get() -> 저장된 값 가져오기 `user.get();`
- orElse(null) -> null이라면 다른 값 사용 `user.orElse(null);`
- orElseThrow() -> null이라면 예외 발생 `user.orElseThrow();`

<br>
<br>

### Random

랜덤한 값을 만들어주는 클래스

```java
Random random = new Random();
```

- nextInt() -> 랜덤한 정수 `random.nextInt();`
- nextInt(10) -> 0~9 중 랜덤한 정수 `random.nextInt(10);`
- nextDouble() -> 0.0 이상 1.0 미만의 랜덤한 실수 `random.nextDouble();`
- nextBoolean() -> 랜덤한 true/false `random.nextBoolean();`

<br>
<br>

### LocalDate
날짜를 다루는 클래스 <br>
`LocalDate date = LocalDate.now();`

- now() -> 현재 날짜 `LocalDate.now();`
- of() -> 원하는 날짜 생성 `LocalDate.of(2026, 9, 29);`
- plusDays() -> 날짜에 일수 더하기 `date.plusDays(1);`
- minusDays() -> 날짜에서 일수 빼기 `date.minusDays(1);`

<br>
<br>

### LocalDateTime
날짜와 시간을 함께 다루는 클래스<br>
`LocalDateTime now = LocalDateTime.now();`

메서드는 위와 동일함.

<br>
<br>
<br>
<br>


## import 정리
### java.lang (자동 import)
- String
- Object
- Math
- System

### jaba.util (import 필요)
- Scanner
- List
- ArrayList
- Set/HashSet
- Map/HashMap
- Arrays
- Objects
- Optional
- Random

### java.time (import 필요)
- LocalDate
- LocalDateTime