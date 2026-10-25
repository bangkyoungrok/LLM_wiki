# domains

업무 도메인 묶음 (P7). 도메인 → 핵심 테이블·조회 기준·프로세스. 테이블 문서의 `domain:` 태그와 1:1 (config `tags.domain_map`).

## 도메인 목록

- [BQMS 입찰/견적](/domains/bid-qt.md) — BQMS 입찰/견적. PR>입찰/견적>선정>발주(PO)>계약(CTR)>입고(GR)>정산(IV) 프로세스. 결합테이블 TI_BQMS810/820/830/840 중심.
- [BQMS MRO](/domains/mro.md) — BQMS MRO. MRO몰, MRO카테고리, MRO 미연계(공급사) 데이터.
- [BQMS 업체정보](/domains/vendor.md) — BQMS 업체정보. BQMS 벤더마스터+구매 벤더마스터 결합 마스터(TI_BQMS800) 중심.
- [BQMS 기준정보](/domains/master-bqms.md) — BQMS 기준정보. IP, 사용자, 사이트, 카테고리, 공통코드 마스터.
- [영업마케팅 마케팅비](/domains/mkt-exp.md) — 영업마케팅 마케팅비. 계획>캠페인>PP>EO>PR>충당>정산. 핵심 TI_GRPF_EO_REPORT, 조회 기준 PRCRDT·EO/PR상태·MBO.
- [영업마케팅 매출](/domains/sales.md) — 영업마케팅 매출. SO>DO>GI>빌링/Invoice>수금. 핵심 TI_GRPB004B(빌링), 판가 TI_GRPB_PRICE_CONDITION.
- [영업마케팅 업체정보](/domains/om-vendor.md) — 영업마케팅 업체정보. 업체(Vendor)마스터 TN_AD_VENDOR.
- [인사 임직원/부서정보](/domains/hr.md) — 인사 임직원/부서정보. GHR+KNOX(LDAP) 기준, TI_GRPF801/802/806/806H.
- [재무 기준정보(조직)](/domains/fin-org.md) — 재무 기준정보(조직). ERP 회사코드(TI_GRPF900)를 축으로 BA/코스트센터/Plant/MBO/영업·구매조직.
- [재무 기준정보(마스터)](/domains/fin-master.md) — 재무 기준정보(마스터). 코드마스터(TI_GRPF910), 총계정원장(TI_GRPF902), 환율(TI_MT_EXCHRATE), 공통코드(TC_CF_COMM_CODE).
- [영업마케팅 기준정보(마스터)](/domains/om-master.md) — 영업마케팅 기준정보(마스터). TimeZone, FTZ, 관리주재원(CFO) 등 부가 마스터.

> 출처: /references/domain-sources.md. `TI_BQMS001_URV_FULL`(스냅샷 밖), `TI_GRPB012`(AIAGT 접근 범위 밖)는 링크하지 않는다.
