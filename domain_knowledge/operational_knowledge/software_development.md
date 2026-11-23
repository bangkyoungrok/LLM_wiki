---
topic: software_development
title: 소프트웨어 개발·유지보수
description: 시스템 개발, 사용자 권한 관리, API 연동 및 소프트웨어 유지보수 관련 실무 노하우와 사고 교훈
sources: [BQMS#AZfF7aw8M9UVtEET.pdf, drm.txt]
updated: 2026-11-18
---

# 소프트웨어 개발·유지보수

## 업무 노하우
- [software_development-001] UAS 사용자 등록 프로세스는 Registration Form 생성, 자동 사용자 생성 Job, 관리자 플래그 및 상태(pending/approved) DB 업데이트, Azure AD B2C 연동, SSO GUID 필드 추가, UI 승인/거절 버튼, User Details 페이지 생성의 8단계로 구성됨 (출처: p.2) (출처: BQMS#AZfF7aw8M9UVtEET.pdf p.2)
- [software_development-002] PDB 서비스 SSO 연동 시 SSO 토큰의 SSO GUID를 확인하여 UAS 사용자로 매핑한 후, 해당 사용자가 리소스에 대한 보기(view) 또는 편집(edit) 권한이 있는지 판별하는 로직을 구현해야 함 (출처: p.3) (출처: BQMS#AZfF7aw8M9UVtEET.pdf p.3)
- [software_development-003] 사용자 생성(User Creation) 로직은 HttpHelper로 문화 정보/헤더 가져오기, Email/UserRoleGuid/MarketGuid/BusinessUnits GUID 검증, Status를 Pending으로 설정, UserBusinessUnitModel 관계 삽입, 관리자 알림 호출, 예외 로깅 및 재투의 순서로 수행됨 (출처: p.8) (출처: BQMS#AZfF7aw8M9UVtEET.pdf p.8)
- [software_development-004] 등록 플로우(Registration Flow)는 Email check, Market selection, Business Unit selection, Role selection(Admin, Product Manager, Visitor, Super Admin), Post registration의 5단계로 구성됨 (출처: p.6-7) (출처: BQMS#AZfF7aw8M9UVtEET.pdf p.6-7)
- [software_development-005] User Page의 Functional Areas는 'PDS Service'와 'User Authorization Service' 그룹으로 나뉘며, 각 하위 항목에 대해 Read, Create, Update, Delete 권한 체크박스를 설정함 (출처: p.10) (출처: BQMS#AZfF7aw8M9UVtEET.pdf p.10)
- [software_development-010] 역할별 권한 제한 로직(예: 관리자 자신의 권한 재할당 방지)은 User Stories에 명시된 요구사항을 기반으로 구현해야 함 (출처: p.4) (출처: BQMS#AZfF7aw8M9UVtEET.pdf p.4)
- [software_development-011] UAS 권한이 PDB, CES, TTS의 다양한 리소스에 실제로 적용되는지 테스트해야 하며, 초기 테스트는 디버깅을 위해 개발자가 직접 수행해야 함 (출처: p.4) (출처: BQMS#AZfF7aw8M9UVtEET.pdf p.4)
- [software_development-012] 서버DRM 적용 시 업무시스템 서버는 NASCA CLIENT 설치 확인, 사용자 인증 요청, 문서 업로드/다운로드, 권한 관리 및 응답, 화면통제 정책 관리 및 응답 기능을 수행해야 하며, 인증 서버는 사용자 인증, 권한 중계, 정책 중계, 이력 전송을 담당함 (출처: p.4) (출처: drm.txt p.4)
- [software_development-013] 서버문서 DRM 개발 모듈은 1) 시스템 접속(Client 연계모듈 활용), 2) 문서 업로드(서버 API 활용), 3) 문서 다운로드(서버 API 활용), 4) ACL 응답 기능(Web Program 개발)의 4단계로 구성됨 (출처: p.7) (출처: drm.txt p.7)
- [software_development-014] 시스템 접속 시 NASCA CLIENT 설치 여부를 확인하고, 미설치 시 시스템 초기 진입 및 중간 진입(URL 복사/붙여넣기)을 허용하지 않아야 하며, 크롬 계열 브라우저 사용 시 크롬 확장 프로그램 설치 여부도 확인해야 함 (출처: p.15) (출처: drm.txt p.15)
- [software_development-015] 사용자 인증 연계 시 자체 인증(ID/PW)은 SetOnX 함수로 사용자 정보 및 인증 서버 정보를 전달하고, 마이싱글 SSO 인증은 SetSys 함수로 인증 서버 정보만 전달하며, 사용자 정보는 SSO 인증정보로 자동 판별됨 (출처: p.22) (출처: drm.txt p.22)
- [software_development-016] 서버DRM 문서 보관 기준에 따라 업로드/다운로드 시 패키징/언패키징 처리가 달라지며, 일반 문서 보관 시 업로드 시 언패키징(본 시스템 문서만) 또는 다운로드 시 패키징을 수행하고, 서버DRM 문서 보관 시 업로드 시 패키징을 수행함 (출처: p.52) (출처: drm.txt p.52)
- [software_development-017] ACL 응답 기능 Web Program은 문서 개봉 시 NASCA CLIENT의 권한 질의에 응답하며, 결과값은 개봉, 수정, 캡쳐, 인쇄, 복호화, 권한변경, 클립보드, WaterMark 인쇄, 암호화 저장 등 10자리 Y/N 문자열로 구성되어야 함 (출처: p.86) (출처: drm.txt p.86)
- [software_development-022] 서버DRM 인증 보안성 개선 버전 사용 시 NASCA Client Build Version 확인이 필요하며, http만 가능한 버전은 2019121610, http/https 모두 가능한 버전은 202006xxxx 이상임 (출처: p.28) (출처: drm.txt p.28)
- [software_development-023] 서버DRM 문서 기능제어(SetNE2)를 통해 읽기전용 경고메시지 표시 여부, 수정/클립보드 권한 없는 문서의 우클릭 및 시트 이동/복사 허용 여부를 시스템 코드별로 설정할 수 있음 (출처: p.48) (출처: drm.txt p.48)

## 사고 사례와 교훈

## 주의사항
- [software_development-006] UAS에서 구현된 권한이 PDB, CES, TTS의 다양한 리소스에 실제로 적용되는지 테스트해야 하며, 초기 테스트는 디버깅을 위해 개발자가 직접 수행해야 함 (출처: p.4) (출처: BQMS#AZfF7aw8M9UVtEET.pdf p.4)
- [software_development-007] 사용자 생성 시 Email, UserRoleGuid, MarketGuid, BusinessUnits의 GUID가 필수적으로 유효해야 하며, 검증 실패 시 예외 처리가 수행됨 (출처: p.8) (출처: BQMS#AZfF7aw8M9UVtEET.pdf p.8)
- [software_development-008] 입력/출력 데이터의 상세 로깅(Verbose)은 _settings.AllowLoggingInputs 및 _settings.AllowLoggingOutputs 플래그에 따라 활성화됨 (출처: p.8) (출처: BQMS#AZfF7aw8M9UVtEET.pdf p.8)
- [software_development-009] 역할별 시간 및 단가 기준(2024년 11-12월)에서 Senior Application Developer 및 Senior Development Backend는 83,00 €와 91,25 € 단가가 혼재되어 있어 실무 적용 시 단가 변동 사유 확인 필요 (출처: p.2) (출처: BQMS#AZfF7aw8M9UVtEET.pdf p.2)
- [software_development-018] 서버 API 설정 파일(NSDSCodeInfo.ini, NSDMasterInfo.ini, NSDConfig.ini)의 내용은 임의 변경이 절대 금지되며, 변경이 필요할 경우 Endpoint개발그룹에 문의해야 함 (출처: p.53) (출처: drm.txt p.53)
- [software_development-019] ACL 응답 Web Page는 'Y' 또는 'N'으로 구성된 10자리 문자열 이외의 값(공란, HTML 태그 등)이 포함되어 있으면 안 되며, 반드시 웹 브라우저의 '소스보기' 메뉴를 통해 확인해야 함 (출처: p.89) (출처: drm.txt p.89)
- [software_development-020] 서버DRM 사용자 인증이 해제된 이후라도, 한 번 인증된 오피스 프로세스가 종료되지 않은 상태라면 해당 프로세스를 통해 서버DRM 문서를 활용할 수 있으므로 로그아웃 후에도 문서 접근이 가능한 예외 상황이 존재함 (출처: p.95) (출처: drm.txt p.95)
- [software_development-021] Windows 서버 API 설치 시 NSD_HOME 환경변수 등록 후 iisreset 명령 실행이 필요하며, 이 명령 실행 시 IIS 재시작으로 WEB 서비스가 일시적으로 중지되므로 주의해야 함 (출처: p.58) (출처: drm.txt p.58)

## 확인 필요
- [software_development-009 충돌] 역할별 시간 및 단가 기준(2024년 11-12월)에서 Senior Application Developer는 83,00 €와 91,25 € 단가가 혼재되어 있으며, Senior Development Backend는 83,00 €와 91,25 € 단가가 혼재되어 있어 실무 적용 시 단가 변동 사유 확인 필요 (출처: p.2) (출처: BQMS#AZfF7aw8M9UVtEET.pdf p.2)