# SECRET
secret이란 앱, 서버 등에서 사용자를 위해 인증서, 키, 비밀번호, 토큰을 포함한 **민감한 정보를 보호**하는 기능이다.

<br>

종류로는 
- API 키 (외부 서비스와 통신을 위한 인증 키)
- 비밀번호 (시스템 또는 애플리케이션 로그인 자격 증명)
- 인증서 (보안 통신을 위한 인증서)
- 암호화 키 (데이터 암호화 용도)
- 토큰 (OAuth와 같은 인증 시스템에서 사용되는 액세스 토큰)

등이 있다.

<br>
<br>

만약 협업 프로젝트를 할 때 깃허브를 사용하여, 그대로 코드를 게시하면 나의 서버 비밀번호 같은 **민감한 정보들이 유출**되어 버릴 수도 있다.

그것을 **방지하기 위해 secret 관리를 사용**해야 하며, 대표적으로는 **환경 변수와 .env 파일** 설정 등이 있다.

<br>
<br>
 
 ### 관리 방식
 #### 1. 인텔리제이 환경 변수에 저장
- modify option에서 관련 설정을 추가할 수 있으며, 가장 편리하게 적용 가능하다.

     {$DB_PASSWORD} 같은 식으로 표기 가능함

<br>

#### 2. .env파일 사용.
- env를 다운받은 후 추가하여 사용 가능하며, 환경별로 파일을 관리할 수 있다.

<br>

#### 3. Cloud Secret Manager
- 클라우드가 직접 Secret을 관리하며, AWS Secret Manager이 담당한다. <br> <br>
즉, 애플리케이션이 필요할 때 manager을 거쳐 권한을 확인하고 인증해 Secret을 받아오는 것이다.

<br>


#### 4. HashiCorp Vault
- secret을 중앙에서 관리하는 것이다.
<br> <br> DB 비밀번호, API 키 등을 Vault 서버에 저장하고 관리해두는 것이며, <br><br>
애플리케이션에서 이러한 Secret이 필요할 경우 Vault 서버에 요청하여 필요한 값을 가져올 수 있다.
<br><br>
이때 아무 애플리케이션이나 Secret을 가져갈 수 있는 것은 아니며, 먼저 Vault에서 정해진 인증 방식을 통해 권한을만 확인받아야 한다. <br><br> 만약 인증에 성공하면 `Vault`가 `Token`을 발급하고 해당 `Token`에 설정된 정책에 따라 접근할 수 있는 Secret의 범위가 결정된다.

#### 요약하자면, 
Vault에 인증 요청 → 인증 성공 → Token 발급 → 권한 확인 → 필요한 Secret 전달

이를 통해 민감한 정보를 코드나 GitHub에 저장하지 않음으로써, 정보를 안전하게 숨기고 별도의 Vault 서버에서 관리할 수 있다.

<br>


#### 5. Kubernetes Secret
- Kubernetes 환경에서 Secret 관리한다. Pod에서 Secret을 환경변수나 파일 형태로 전달받아 사용할 수 있지만, <mark>Base64</mark>로 표현되어도 자체가 암호화 된 것은 아니니 보안 설정을 함께 고려해야 한다.

> base64란, **문자나 데이터를 특정한 규칙에 따라 다른 문자 형태로 바꾸는 인코딩 방식**이다.
<br> <br>
하지만 누구나 원래의 값으로 되돌릴 수 있어 암호화의 용도에 적합하지 않다!

<br>
<br>
<br>
<br>

# MQ
mq란 Message Queue의 약자로, 메시지를 줄에 넣어두고, 다른 프로그램이 나중에 가져가 처리하도록 하는 방식이다.

<br>

예를 들어, 주문 서비스가 결제 서비스를 호출하기 위해서는 결제 서비스의 응답을 기다려야 한다.

그런데 이것은 서비스끼리 내내 기다려야함으로 너무 비효율적이다.

게다가 처리 속도가 달라 호환이 되지 않을 수도 있다.

<br>

하지만 MQ를 사용하면, 중간에 Message Queue가 들어와 "이거 해야 돼" 라는 메세지를 넣어놓는다. 그러면 나중에 메세지를 가져와서 처리하기에 서비스간 결합을 낮출 수 있다. 즉, **완충 역할**을 해줄 수 있는 것이다.

<br>
<br>

구조
```
                 Message
Producer ─────────────────→ Queue
                              │
                              │
                              ↓
                           Consumer
                           
```

<br>
<br>
<br>
<br>

# Messege Broker
방금 알아본 MQ와 같이, Producer와 Consumer 사이에서 메시지를 받아 저장하고, 적절한 Consumer에게 전달해주는 중간 시스템이다.

<br>

### 그렇다면 MQ랑은 무엇이 다를까?
MQ는 메세지를 전달하기 위한 **개념**이지만, Messege Broker은 실제로 메세지를 받아 관리하는 **시스템**이다.

대표적인 기술으로는 <mark>RabbitMQ, Kafka</mark> 등이 있다.

<br>
<br>

### kafka
Kafka란, 대용량의 메시지와 이벤트를 실시간으로 처리하고 전달하기 위한 분산 이벤트 스트리밍 플랫폼이다.

Producer가 메시지를 Kafka에 보내면 Kafka가 이를 <mark>Topic</mark>에 저장하고, Consumer가 <mark>Topic</mark>에서 메시지를 읽어 처리한다.

> ### <span style="color: gray;"> Topic
> kafka에서 메세지를 종류별로 구분하여 저장하는 공간이다.
>
> 구성 요소로는 
> 하나의 Topic을 여러 개로 나눈 저장 단위인 **partition** 과, Kafka의 메시지를 저장하고 전달하는 서버인 **Broker**, 여러 Consumer를 하나의 그룹으로 묶어 Topic의 Partition을 나누어 처리하는 **Consumer Group**이 있다.

<br>

이처럼 Kafka는 **여러 서버에 메시지를 분산해서 저장하고 처리**할 수 있기 때문에 대용량의 데이터를 빠르게 처리할 수 있다.

또한 메시지를 바로 삭제하지 않고 일정 기간 저장할 수 있어, Consumer가 메시지를 다시 읽는 것도 가능하다.

<br>
<br>

### RabbitMQ

RabbitMQ란, **메시지를 전달하고 관리하기 위한 오픈소스 메시지 브로커**이다.

Producer가 메시지를 RabbitMQ에 보내면 <mark>Exchange</mark>가 메시지를 적절한 Queue로 전달하고, Consumer가 Queue에서 메시지를 가져와 처리한다.

> ### <span style="color: gray;"> Exchange
> Producer에게 받은 메시지를 **Routing Key와 설정된 규칙에 따라 적절한 Queue로 전달하는 역할**을 한다.


<br>

이처럼 RabbitMQ는 여러 Queue와 Exchange를 이용해 메시지를 다양한 방식으로 전달할 수 있으며,

메시지 처리에 실패하거나 Consumer가 잠시 사용할 수 없는 경우에도 메시지를 다시 처리할 수 있도록 <mark>ACK, Retry</mark> 등의 기능을 사용할 수 있다!

> ### <span style="color: gray;"> ACK
> Acknowledgement의 약자로, Consumer가 메시지를 정상적으로 처리했다는 것을 Broker에게 알리는 응답이다.

> ### <span style="color: gray;"> Retry
> 이름 그대로 Consumer가 메시지 처리에 실패했을 경우 메시지를 다시 처리하도록 하는 것이다.
>
> 만약 일정 횟수 이상 계속 실패하면 <mark>DLQ</mark>​로 보내 별도로 관리하는 것이 가능하다.

> ### <span style="color: gray;"> DLQ
> Dead Letter Queue의 약자로 계속 실패하는 메세지가 정상 처리를 방해하지 않게끔 따로 보관해두는 Queue이다.

