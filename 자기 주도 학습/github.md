# Git Flow

### Git Flow는 협업 시 코드 충돌을 줄이고 안정적인 개발 및 배포를 하기 위해 사용하는 브랜치 관리 전략이다.

​

**main** : 배포하는 용도로 쓰는 최종 브랜치

**develop** : 개발용 브랜치로, 이 브랜치를 기준으로 feature 브랜치를 따고, 각 feature를 합치는 브랜치

**feature**: 단위 기능 개발용 브랜치

**release**: 다음배포를 위해 기능에 문제가 없는지 체크 용도의 브랜치

**hotfix**: 배포가 되고 나서 버그 발생 시 긴급 수정하는 브랜치

**support**: 버전 호환성을 위한 브랜치

<br>
<br>
<br>



## Git Flow 진행 과정

### 1. develop

```
git checkout develop
git pull
```

- 최신 코드 가져오기

### 2. 기능 브랜치 생성

```
git checkout -b feature/login
```

- 기능 개발 시작

### 3. 기능 개발 및 저장

```
git add .
git commit -m "feat: login"
```

- 기능 구현 후 커밋

### 4. GitHub 업로드

```
git push -u origin feature/login
```

- 브랜치 업로드

### 5. Pull Request(PR)

```
feature/login
↓
develop
```

- 코드 리뷰 요청

### 6. Merge

```text
feature/login
↓
develop
```

- 기능 반영

### 7. 배포

```text
develop
↓
main
```

- 테스트 완료 후 배포
