# Git Flow

### Git Flow는 협업 시 코드 충돌을 줄이고 안정적인 개발 및 배포를 하기 위해 사용하는 브랜치 관리 전략이다.

<br>

## 사용 목적

- 여러 개발자가 동시에 작업할 수 있도록 한다.
- 기능별로 개발 내용을 분리/교체 할 수 있다.
- 코드 리뷰를 통해 코드 품질 향상된다.
- 배포 중인 코드와 개발 중인 코드를 분리할 수 있다.
- 버그 수정 및 유지보수를 체계적으로 관리 가능하다.

<br>

## 브랜치 종류

**main** : 실제 배포되는 최종 브랜치

**develop** : 개발한 기능들을 모아두는 브랜치

**feature** : 기능 개발용 브랜치

**release** : 배포 전 테스트 및 검증용 브랜치

**hotfix** : 운영 중 긴급 버그 수정 브랜치

**support** : 버전 호환성 유지 브랜치

<br>

## 브랜치 구조

```
main
 └─ develop
      ├─ feature/login
      ├─ feature/signup
      └─ feature/board
```

<br>
<br>
<br>

## Git Flow 진행 과정

### 1. develop

```
git checkout develop
git pull
```

- 팀원이 수정한 최신 코드를 내 파일로 불러온다.

### 2. 기능 브랜치 생성

```bash
git checkout -b feature/---
```

- 어떠한 기능용 브랜치를 따로 생성해 개발한다.

### 3. 기능 개발 및 저장

```bash
git add .
git commit -m "feat: ---"
```

- 기능 구현 후 커밋

### 4. GitHub 업로드

```bash
git push -u origin feature/---
```

- 브랜치 업로드

### 5. Pull Request(PR)

```text
feature/---
↓
develop
```

- 코드 리뷰를 요청 후,

### 6. Merge

```text
feature/---
↓
develop
```

- 리뷰가 끝나면 머지로 최종 수정 완료한다.

### 7. 배포

```text
develop
↓
main
```

* 테스트 완료 후 배포.


