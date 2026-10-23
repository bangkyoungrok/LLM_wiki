---
type: Business Domain
title: 인사 임직원/부서정보
description: 인사 임직원/부서정보. GHR+KNOX(LDAP) 기준, TI_GRPF801/802/806/806H.
tags: ["domain:hr"]
system: 인사
domain_name: 임직원/부서정보
status: draft
sources:
- id: add-info
  resource: /references/domain-sources.md
  title: add_info/domain 이식
---

# 인사 / 임직원/부서정보

## 프로세스

(없음)

## 테이블과 조회 기준

임직원정보 : TI_GRPF801, TI_GRPF802
부서정보 : TI_GRPF806
# 데이터 소스 : 인사시스템(GHR), KNOX(포털)
     . 인사시스템 : 임직원 기본정보 + 부가정보, 퇴직자/현채인 포함, 비정규직 제외
     . KNOX(LDAP) : 임직원 기본정보 Only, 현재기준, 업무용/비정규/임시/파견직 포함
# 키값 : 회사코드(COCD) + Knox ID(SGID) / 사번(EMID) / EPID (관계사 전배시 동일정보 보유할 수 있음)
# 부서코드/명은 인사시스템 vs KNOX 차이가 있음(관리체계 다름)
# 부서코드는 내부부서코드(innr_dpcd)를 사용 (dpcd는 법인코드를 제외한 편집한 컬럼)
# 임직원 정보는 KNOX 부서기준을 기준으로 보여줌 (없으면 인사정보 사용)

* 임직원정보(GHR) : TI_GRPF801
* 임직원정보(KNOX) : TI_GRPF802
* 부서정보(GHR+KNOX) : TI_GRPF806
* 부서정보(GHR+KNOX) 월별 히스토리 : TI_GRPF806H

## 테이블 목록

| 테이블 | 유형 (table_type) | 설명 (table_rule) |
|---|---|---|
| [TI_GRPF801](/schemas/APPADAMSUSER/tables/TI_GRPF801.md) |  | 키값 : 회사코드(COCD) + EMID + EMID_YN='Y' 키값 : 회사코드(COCD) + SGID + SGID_YN='Y' 키값 : 회사코드(COCD) + EPID + EPID_YN='Y * DS/DX구분 컬럼: GB * IF구분 컬럼 : IF_GB * 부서코드/코드명 : INNR_DPCD, DEPT_NM (GHR기준) * 부서코드/코드명 : INNR_DPCD2, DEPT_NM2 (KNOX기준) |
| [TI_GRPF802](/schemas/APPADAMSUSER/tables/TI_GRPF802.md) |  | 키값 : 회사코드(COCD) + EMID + EMID_YN='Y' 키값 : 회사코드(COCD) + SGID + SGID_YN='Y' 키값 : 회사코드(COCD) + EPID + EPID_YN='Y |
| [TI_GRPF806](/schemas/APPADAMSUSER/tables/TI_GRPF806.md) |  | * IF구분 컬럼 : IF_GB (LDAP, GHRP) |
| [TI_GRPF806H](/schemas/APPADAMSUSER/tables/TI_GRPF806H.md) |  | 부서정보 월별 누적 내역 |
