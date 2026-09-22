# 스프링의 핵심 모듈
<br>

### Spring Core
- IoC(관점 지향)와 AOP(트랜잭션)를 통합하는 것을 지원해줌.

### Spring Context 
- 스프링 애플리케이션의 빈을 생성하고 관리하는 IoC 핵심 컨테이너

### Spring Web
- 웹 통합 기능 지원

<br>
<br>
<br>
<br>

# 의존성 종류
의존성이란 IoC에 기반에 대신하여 관리해줄 DI를 주입하는 것으로 대표적인 주입 방법은
- 생성자 주입
- 세터, 게터(LOMBOK, 메서드로 제공)
- 어노테이션

등이 있음

<br>
<br>
<br>
<br>

# 빈의 생명주기
1. 객체 만듦
2. 의존성 주입
3. 사용함
4. 프로그램에서 사용된 후 소멸
(필요 없는 사용된 자원일시 소멸. 재시작시 재생성됨)

<br>
<br>
<br>
<br>

# 스프링부트
스프링은 혼자쓰면 너무 불편하고 자동화 테스트도 불가능했음
그래서 POJO를 사용해 복잡성을 줄이고 개발 단순화가 가능하도록 프레임워크를 구축한 것이 스프링부트임.

(포조란 오래된 자바 객체라는 뜻으로, 특정 프레임워크나 기술에 종속되지 않고 일반적인 자바 객체로 작성된 객체임)

> 장점
> - 테스트 쉬움 라이브러리 관리 자동화됨
> - 초기 설정이 복잡하고 버전 관리 해줘야함

<br>
<br>
<br>
<br>

# Repository
JPA 일종임. DB랑 상호작용할때 CRUD 작업 쿼리(DB 명령어)랑 메서드를 제공해줘 지들이 관리를 싹 해줌

> **JPA란**    
> 스프링을 더 쉽게 사용할 수 있도록 일부 반복 코드 줄이고 작업 단순화 도움.   
> 영속성 컨텍스트(객체 관리 저장), JPQL언어 (객체지향쿼리언어) 지원

<br>
<br>
<br>
<br>

# DispatchServlet
SpringMVC에서 요청을 디스패치하고 처리한 후 응답을 생성해줌

즉, 사용자가 요청을 보내면 DispatcherServlet이 받고 어디서 처리할지 확인 후에 보냄. 그리고 작업이 끝나면 DispatcherServlet이 다시 받아서 응답 생성해 사용자에게 보내줌
  
<br>
<br>
<br>
<br>

# Spring AOP에서 Advice
부가기능 코드를 뜻함. 예를 들어 @after, @around, @before 같은 거

<br>
<br>
<br>
<br>

# Spring Profiles
 스프링 프레임워크에서 실행 환경에 따라 서로 다른 설정 파일이나 빈을 선택하여 적용할 수 있도록 지원하는 환경 분리 기능임

 <br>
 <br>
 <br>
 <br>

# 보안 구현
스프링에서 보안을 구현할 때는 스프링 시큐리티(접근제어 프레임워크)를 사용함.

> 구성요소
> - 인증 (너 권한 있음?)
> - 권한 부여 (권한 드림)
> - 서브릿필터 (인증을 확인하는 필터 제공)
> - 보안 컨텍스트 (인증 확인했다는 정보를 제공)

> 어떻게 사용?    
> 시큐리티 의존성 추가하고 Config 파일 구성 (접근 권한 같은 보안 설정하는 클래스)

<br>
<br>
<br>
<br>

# @RequestMapping, @GetMapping
말 그대로임

@RequestMapping은 method 속성 지정하여 GET, POST 등등... 다 처리가능
`@RequestMapping(value = "/users", method = RequestMethod.GET)`

 @GetMapping은 GET만 사용 가능

 <br>
 <br>
 <br>
 <br>

# Spring Bean Scope
Spring 컨텍스트 내에서 빈 생명주기랑 가시성(다른 코드 접근 범위)를 정의함

 우리가 평소에 쓰는 방식은 보통 singleton (이건 아무것도 지정 안하면 걍 하나 만들어서 계속 재사용하는 거)

 > 범위 어케 지정?   
 > @Scope("prototype")

 <br>
 <br>
 <br>
 <br>

 #  Spring Actuator

서비스에 문제가 없는지 모니터링하고 지표를 심어 감시할 수 있게 해주는 스프링부트 프레임워크임.

이런 기능들을 프로덕션 준비라고 하며, 문제가 생기기 전에 미리 대응할 수 있게 해주는 것.

> 어케 적용?   
> 의존성 추가

<br>
<br>
<br>
<br>

# Spring Cloud
MSA에서 시스템 구축을 도와주는 오픈소스 프레임워크   
(MSA란, 각 기능들마다 각각 나눠서 개발 후 연결해서 완성하는 것)

<br>
<br>
<br>
<br>

# Spring Cloud Config
MSA에서 애플리케이션에 대한 외부 속성을 중앙 서버에서 관리할 수 있도록 도와주는 시스템임

<br>
<br>
<br>
<br>

# Springboot Starter
종속성 추가 과정을 간소화해주는 의존성임   
(implementation 'org.springframework.boot:spring-boot-starter-web' 이런식으로 한줄만 써도 관련 기능들이 딸려오도록 도와줌)








