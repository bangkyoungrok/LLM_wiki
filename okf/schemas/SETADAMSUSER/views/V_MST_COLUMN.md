---
type: Oracle View
title: 마스터 컬럼정보
description: '마스터 컬럼정보. 참조: TN_AD_MASTER_COLUMN.'
resource: oracle://PRD/SETADAMSUSER/V_MST_COLUMN
tags: ['kind:view', 'owner:setadamsuser', 'class:view', 'access:select-full']
owner: SETADAMSUSER
table_name: V_MST_COLUMN
query_name: SETADAMSUSER.V_MST_COLUMN
table_class: view
status: draft
stale_after: 2027-01-11T13:53:08+09:00
sources:
- id: dict
  resource: /references/dictionary-sources.md
  title: 딕셔너리 추출 스냅샷
generated:
  by: process:okf-dict-builder/0.1
  at: 2026-10-13T13:53:08+09:00
table_type: 기준정보
business_area: 시스템
business_detail: 시나리오
---

# 개요
(사람이 보완: 이 뷰가 무엇을 조인해서 보여 주는지)

# Schema
<!-- AUTO:BEGIN schema -->
| # | 컬럼 | 한글명 | 타입 | NULL | 키 | 코드/참조 | 비고 |
|---|---|---|---|---|---|---|---|
| 1 | MASTER_ID | 마스터ID | VARCHAR2(20) | Y |  |  |  |
| 2 | MASTER_VER | 마스터버전 | NUMBER(10,1) | Y |  |  |  |
| 3 | NO | 순번 | NUMBER | Y |  |  |  |
| 4 | GB | 컬럼속성구분 | VARCHAR2(16) | Y |  |  |  |
| 5 | COL01 | 컬럼1 | VARCHAR2(500) | Y |  |  |  |
| 6 | COL02 | 컬럼2 | VARCHAR2(500) | Y |  |  |  |
| 7 | COL03 | 컬럼3 | VARCHAR2(500) | Y |  |  |  |
| 8 | COL04 | 컬럼4 | VARCHAR2(500) | Y |  |  |  |
| 9 | COL05 | 컬럼5 | VARCHAR2(500) | Y |  |  |  |
| 10 | COL06 | 컬럼6 | VARCHAR2(500) | Y |  |  |  |
| 11 | COL07 | 컬럼7 | VARCHAR2(500) | Y |  |  |  |
| 12 | COL08 | 컬럼8 | VARCHAR2(500) | Y |  |  |  |
| 13 | COL09 | 컬럼9 | VARCHAR2(500) | Y |  |  |  |
| 14 | COL10 | 컬럼10 | VARCHAR2(500) | Y |  |  |  |
| 15 | COL11 | 컬럼11 | VARCHAR2(500) | Y |  |  |  |
| 16 | COL12 | 컬럼12 | VARCHAR2(500) | Y |  |  |  |
| 17 | COL13 | 컬럼13 | VARCHAR2(500) | Y |  |  |  |
| 18 | COL14 | 컬럼14 | VARCHAR2(500) | Y |  |  |  |
| 19 | COL15 | 컬럼15 | VARCHAR2(500) | Y |  |  |  |
| 20 | COL16 | 컬럼16 | VARCHAR2(500) | Y |  |  |  |
| 21 | COL17 | 컬럼17 | VARCHAR2(500) | Y |  |  |  |
| 22 | COL18 | 컬럼18 | VARCHAR2(500) | Y |  |  |  |
| 23 | COL19 | 컬럼19 | VARCHAR2(500) | Y |  |  |  |
| 24 | COL20 | 컬럼20 | VARCHAR2(500) | Y |  |  |  |
| 25 | COL21 | 컬럼21 | VARCHAR2(500) | Y |  |  |  |
| 26 | COL22 | 컬럼22 | VARCHAR2(500) | Y |  |  |  |
| 27 | COL23 | 컬럼23 | VARCHAR2(500) | Y |  |  |  |
| 28 | COL24 | 컬럼24 | VARCHAR2(500) | Y |  |  |  |
| 29 | COL25 | 컬럼25 | VARCHAR2(500) | Y |  |  |  |
| 30 | COL26 | 컬럼26 | VARCHAR2(500) | Y |  |  |  |
| 31 | COL27 | 컬럼27 | VARCHAR2(500) | Y |  |  |  |
| 32 | COL28 | 컬럼28 | VARCHAR2(500) | Y |  |  |  |
| 33 | COL29 | 컬럼29 | VARCHAR2(500) | Y |  |  |  |
| 34 | COL30 | 컬럼30 | VARCHAR2(500) | Y |  |  |  |
| 35 | COL31 | 컬럼31 | VARCHAR2(500) | Y |  |  |  |
| 36 | COL32 | 컬럼32 | VARCHAR2(500) | Y |  |  |  |
| 37 | COL33 | 컬럼33 | VARCHAR2(500) | Y |  |  |  |
| 38 | COL34 | 컬럼34 | VARCHAR2(500) | Y |  |  |  |
| 39 | COL35 | 컬럼35 | VARCHAR2(500) | Y |  |  |  |
| 40 | COL36 | 컬럼36 | VARCHAR2(500) | Y |  |  |  |
| 41 | COL37 | 컬럼37 | VARCHAR2(500) | Y |  |  |  |
| 42 | COL38 | 컬럼38 | VARCHAR2(500) | Y |  |  |  |
| 43 | COL39 | 컬럼39 | VARCHAR2(500) | Y |  |  |  |
| 44 | COL40 | 컬럼40 | VARCHAR2(500) | Y |  |  |  |
| 45 | COL41 | 컬럼41 | VARCHAR2(500) | Y |  |  |  |
| 46 | COL42 | 컬럼42 | VARCHAR2(500) | Y |  |  |  |
| 47 | COL43 | 컬럼43 | VARCHAR2(500) | Y |  |  |  |
| 48 | COL44 | 컬럼44 | VARCHAR2(500) | Y |  |  |  |
| 49 | COL45 | 컬럼45 | VARCHAR2(500) | Y |  |  |  |
| 50 | COL46 | 컬럼46 | VARCHAR2(500) | Y |  |  |  |
| 51 | COL47 | 컬럼47 | VARCHAR2(500) | Y |  |  |  |
| 52 | COL48 | 컬럼48 | VARCHAR2(500) | Y |  |  |  |
| 53 | COL49 | 컬럼49 | VARCHAR2(500) | Y |  |  |  |
| 54 | COL50 | 컬럼50 | VARCHAR2(500) | Y |  |  |  |
| 55 | COL51 | 컬럼51 | VARCHAR2(500) | Y |  |  |  |
| 56 | COL52 | 컬럼52 | VARCHAR2(500) | Y |  |  |  |
| 57 | COL53 | 컬럼53 | VARCHAR2(500) | Y |  |  |  |
| 58 | COL54 | 컬럼54 | VARCHAR2(500) | Y |  |  |  |
| 59 | COL55 | 컬럼55 | VARCHAR2(500) | Y |  |  |  |
| 60 | COL56 | 컬럼56 | VARCHAR2(500) | Y |  |  |  |
| 61 | COL57 | 컬럼57 | VARCHAR2(500) | Y |  |  |  |
| 62 | COL58 | 컬럼58 | VARCHAR2(500) | Y |  |  |  |
| 63 | COL59 | 컬럼59 | VARCHAR2(500) | Y |  |  |  |
| 64 | COL60 | 컬럼60 | VARCHAR2(500) | Y |  |  |  |
| 65 | COL61 | 컬럼61 | VARCHAR2(500) | Y |  |  |  |
| 66 | COL62 | 컬럼62 | VARCHAR2(500) | Y |  |  |  |
| 67 | COL63 | 컬럼63 | VARCHAR2(500) | Y |  |  |  |
| 68 | COL64 | 컬럼64 | VARCHAR2(500) | Y |  |  |  |
| 69 | COL65 | 컬럼65 | VARCHAR2(500) | Y |  |  |  |
| 70 | COL66 | 컬럼66 | VARCHAR2(500) | Y |  |  |  |
| 71 | COL67 | 컬럼67 | VARCHAR2(500) | Y |  |  |  |
| 72 | COL68 | 컬럼68 | VARCHAR2(500) | Y |  |  |  |
| 73 | COL69 | 컬럼69 | VARCHAR2(500) | Y |  |  |  |
| 74 | COL70 | 컬럼70 | VARCHAR2(500) | Y |  |  |  |
| 75 | COL71 | 컬럼71 | VARCHAR2(500) | Y |  |  |  |
| 76 | COL72 | 컬럼72 | VARCHAR2(500) | Y |  |  |  |
| 77 | COL73 | 컬럼73 | VARCHAR2(500) | Y |  |  |  |
| 78 | COL74 | 컬럼74 | VARCHAR2(500) | Y |  |  |  |
| 79 | COL75 | 컬럼75 | VARCHAR2(500) | Y |  |  |  |
| 80 | COL76 | 컬럼76 | VARCHAR2(500) | Y |  |  |  |
| 81 | COL77 | 컬럼77 | VARCHAR2(500) | Y |  |  |  |
| 82 | COL78 | 컬럼78 | VARCHAR2(500) | Y |  |  |  |
| 83 | COL79 | 컬럼79 | VARCHAR2(500) | Y |  |  |  |
| 84 | COL80 | 컬럼80 | VARCHAR2(500) | Y |  |  |  |
| 85 | COL81 | 컬럼81 | VARCHAR2(500) | Y |  |  |  |
| 86 | COL82 | 컬럼82 | VARCHAR2(500) | Y |  |  |  |
| 87 | COL83 | 컬럼83 | VARCHAR2(500) | Y |  |  |  |
| 88 | COL84 | 컬럼84 | VARCHAR2(500) | Y |  |  |  |
| 89 | COL85 | 컬럼85 | VARCHAR2(500) | Y |  |  |  |
| 90 | COL86 | 컬럼86 | VARCHAR2(500) | Y |  |  |  |
| 91 | COL87 | 컬럼87 | VARCHAR2(500) | Y |  |  |  |
| 92 | COL88 | 컬럼88 | VARCHAR2(500) | Y |  |  |  |
| 93 | COL89 | 컬럼89 | VARCHAR2(500) | Y |  |  |  |
| 94 | COL90 | 컬럼90 | VARCHAR2(500) | Y |  |  |  |
| 95 | COL91 | 컬럼91 | VARCHAR2(500) | Y |  |  |  |
| 96 | COL92 | 컬럼92 | VARCHAR2(500) | Y |  |  |  |
| 97 | COL93 | 컬럼93 | VARCHAR2(500) | Y |  |  |  |
| 98 | COL94 | 컬럼94 | VARCHAR2(500) | Y |  |  |  |
| 99 | COL95 | 컬럼95 | VARCHAR2(500) | Y |  |  |  |
| 100 | COL96 | 컬럼96 | VARCHAR2(500) | Y |  |  |  |
| 101 | COL97 | 컬럼97 | VARCHAR2(500) | Y |  |  |  |
| 102 | COL98 | 컬럼98 | VARCHAR2(500) | Y |  |  |  |
| 103 | COL99 | 컬럼99 | VARCHAR2(500) | Y |  |  |  |
| 104 | COL100 | 컬럼100 | VARCHAR2(500) | Y |  |  |  |
| 105 | COL101 | 컬럼101 | VARCHAR2(500) | Y |  |  |  |
| 106 | COL102 | 컬럼102 | VARCHAR2(500) | Y |  |  |  |
| 107 | COL103 | 컬럼103 | VARCHAR2(500) | Y |  |  |  |
| 108 | COL104 | 컬럼104 | VARCHAR2(500) | Y |  |  |  |
| 109 | COL105 | 컬럼105 | VARCHAR2(500) | Y |  |  |  |
| 110 | COL106 | 컬럼106 | VARCHAR2(500) | Y |  |  |  |
| 111 | COL107 | 컬럼107 | VARCHAR2(500) | Y |  |  |  |
| 112 | COL108 | 컬럼108 | VARCHAR2(500) | Y |  |  |  |
| 113 | COL109 | 컬럼109 | VARCHAR2(500) | Y |  |  |  |
| 114 | COL110 | 컬럼110 | VARCHAR2(500) | Y |  |  |  |
| 115 | COL111 | 컬럼111 | VARCHAR2(500) | Y |  |  |  |
| 116 | COL112 | 컬럼112 | VARCHAR2(500) | Y |  |  |  |
| 117 | COL113 | 컬럼113 | VARCHAR2(500) | Y |  |  |  |
| 118 | COL114 | 컬럼114 | VARCHAR2(500) | Y |  |  |  |
| 119 | COL115 | 컬럼115 | VARCHAR2(500) | Y |  |  |  |
| 120 | COL116 | 컬럼116 | VARCHAR2(500) | Y |  |  |  |
| 121 | COL117 | 컬럼117 | VARCHAR2(500) | Y |  |  |  |
| 122 | COL118 | 컬럼118 | VARCHAR2(500) | Y |  |  |  |
| 123 | COL119 | 컬럼119 | VARCHAR2(500) | Y |  |  |  |
| 124 | COL120 | 컬럼120 | VARCHAR2(500) | Y |  |  |  |
| 125 | COL121 | 컬럼121 | VARCHAR2(500) | Y |  |  |  |
| 126 | COL122 | 컬럼122 | VARCHAR2(500) | Y |  |  |  |
| 127 | COL123 | 컬럼123 | VARCHAR2(500) | Y |  |  |  |
| 128 | COL124 | 컬럼124 | VARCHAR2(500) | Y |  |  |  |
| 129 | COL125 | 컬럼125 | VARCHAR2(500) | Y |  |  |  |
| 130 | COL126 | 컬럼126 | VARCHAR2(500) | Y |  |  |  |
| 131 | COL127 | 컬럼127 | VARCHAR2(500) | Y |  |  |  |
| 132 | COL128 | 컬럼128 | VARCHAR2(500) | Y |  |  |  |
| 133 | COL129 | 컬럼129 | VARCHAR2(500) | Y |  |  |  |
| 134 | COL130 | 컬럼130 | VARCHAR2(500) | Y |  |  |  |
| 135 | COL131 | 컬럼131 | VARCHAR2(500) | Y |  |  |  |
| 136 | COL132 | 컬럼132 | VARCHAR2(500) | Y |  |  |  |
| 137 | COL133 | 컬럼133 | VARCHAR2(500) | Y |  |  |  |
| 138 | COL134 | 컬럼134 | VARCHAR2(500) | Y |  |  |  |
| 139 | COL135 | 컬럼135 | VARCHAR2(500) | Y |  |  |  |
| 140 | COL136 | 컬럼136 | VARCHAR2(500) | Y |  |  |  |
| 141 | COL137 | 컬럼137 | VARCHAR2(500) | Y |  |  |  |
| 142 | COL138 | 컬럼138 | VARCHAR2(500) | Y |  |  |  |
| 143 | COL139 | 컬럼139 | VARCHAR2(500) | Y |  |  |  |
| 144 | COL140 | 컬럼140 | VARCHAR2(500) | Y |  |  |  |
| 145 | COL141 | 컬럼141 | VARCHAR2(500) | Y |  |  |  |
| 146 | COL142 | 컬럼142 | VARCHAR2(500) | Y |  |  |  |
| 147 | COL143 | 컬럼143 | VARCHAR2(500) | Y |  |  |  |
| 148 | COL144 | 컬럼144 | VARCHAR2(500) | Y |  |  |  |
| 149 | COL145 | 컬럼145 | VARCHAR2(500) | Y |  |  |  |
| 150 | COL146 | 컬럼146 | VARCHAR2(500) | Y |  |  |  |
| 151 | COL147 | 컬럼147 | VARCHAR2(500) | Y |  |  |  |
| 152 | COL148 | 컬럼148 | VARCHAR2(500) | Y |  |  |  |
| 153 | COL149 | 컬럼149 | VARCHAR2(500) | Y |  |  |  |
| 154 | COL150 | 컬럼150 | VARCHAR2(500) | Y |  |  |  |
<!-- AUTO:END schema -->

# Definition
<!-- AUTO:BEGIN definition -->
```sql
select a.master_id, a.master_ver, 1 as no, 'COLUMN_SEQ' as gb
, max(a.no1_col) as col01, max(a.no2_col) as col02, max(a.no3_col) as col03, max(a.no4_col) as col04, max(a.no5_col) as col05, max(a.no6_col) as col06, max(a.no7_col) as col07, max(a.no8_col) as col08, max(a.no9_col) as col09, max(a.no10_col) as col10
, max(a.no11_col) as col11, max(a.no12_col) as col12, max(a.no13_col) as col13, max(a.no14_col) as col14, max(a.no15_col) as col15, max(a.no16_col) as col16, max(a.no17_col) as col17, max(a.no18_col) as col18, max(a.no19_col) as col19, max(a.no20_col) as col20
, max(a.no21_col) as col21, max(a.no22_col) as col22, max(a.no23_col) as col23, max(a.no24_col) as col24, max(a.no25_col) as col25, max(a.no26_col) as col26, max(a.no27_col) as col27, max(a.no28_col) as col28, max(a.no29_col) as col29, max(a.no30_col) as col30
, max(a.no31_col) as col31, max(a.no32_col) as col32, max(a.no33_col) as col33, max(a.no34_col) as col34, max(a.no35_col) as col35, max(a.no36_col) as col36, max(a.no37_col) as col37, max(a.no38_col) as col38, max(a.no39_col) as col39, max(a.no40_col) as col40
, max(a.no41_col) as col41, max(a.no42_col) as col42, max(a.no43_col) as col43, max(a.no44_col) as col44, max(a.no45_col) as col45, max(a.no46_col) as col46, max(a.no47_col) as col47, max(a.no48_col) as col48, max(a.no49_col) as col49, max(a.no50_col) as col50
, max(a.no51_col) as col51, max(a.no52_col) as col52, max(a.no53_col) as col53, max(a.no54_col) as col54, max(a.no55_col) as col55, max(a.no56_col) as col56, max(a.no57_col) as col57, max(a.no58_col) as col58, max(a.no59_col) as col59, max(a.no60_col) as col60
, max(a.no61_col) as col61, max(a.no62_col) as col62, max(a.no63_col) as col63, max(a.no64_col) as col64, max(a.no65_col) as col65, max(a.no66_col) as col66, max(a.no67_col) as col67, max(a.no68_col) as col68, max(a.no69_col) as col69, max(a.no70_col) as col70
, max(a.no71_col) as col71, max(a.no72_col) as col72, max(a.no73_col) as col73, max(a.no74_col) as col74, max(a.no75_col) as col75, max(a.no76_col) as col76, max(a.no77_col) as col77, max(a.no78_col) as col78, max(a.no79_col) as col79, max(a.no80_col) as col80
, max(a.no81_col) as col81, max(a.no82_col) as col82, max(a.no83_col) as col83, max(a.no84_col) as col84, max(a.no85_col) as col85, max(a.no86_col) as col86, max(a.no87_col) as col87, max(a.no88_col) as col88, max(a.no89_col) as col89, max(a.no90_col) as col90
, max(a.no91_col) as col91, max(a.no92_col) as col92, max(a.no93_col) as col93, max(a.no94_col) as col94, max(a.no95_col) as col95, max(a.no96_col) as col96, max(a.no97_col) as col97, max(a.no98_col) as col98, max(a.no99_col) as col99, max(a.no100_col) as col100
, max(a.no101_col) as col101, max(a.no102_col) as col102, max(a.no103_col) as col103, max(a.no104_col) as col104, max(a.no105_col) as col105, max(a.no106_col) as col106, max(a.no107_col) as col107, max(a.no108_col) as col108, max(a.no109_col) as col109, max(a.no110_col) as col110
, max(a.no111_col) as col111, max(a.no112_col) as col112, max(a.no113_col) as col113, max(a.no114_col) as col114, max(a.no115_col) as col115, max(a.no116_col) as col116, max(a.no117_col) as col117, max(a.no118_col) as col118, max(a.no119_col) as col119, max(a.no120_col) as col120
, max(a.no121_col) as col121, max(a.no122_col) as col122, max(a.no123_col) as col123, max(a.no124_col) as col124, max(a.no125_col) as col125, max(a.no126_col) as col126, max(a.no127_col) as col127, max(a.no128_col) as col128, max(a.no129_col) as col129, max(a.no130_col) as col130
, max(a.no131_col) as col131, max(a.no132_col) as col132, max(a.no133_col) as col133, max(a.no134_col) as col134, max(a.no135_col) as col135, max(a.no136_col) as col136, max(a.no137_col) as col137, max(a.no138_col) as col138, max(a.no139_col) as col139, max(a.no140_col) as col140
, max(a.no141_col) as col141, max(a.no142_col) as col142, max(a.no143_col) as col143, max(a.no144_col) as col144, max(a.no145_col) as col145, max(a.no146_col) as col146, max(a.no147_col) as col147, max(a.no148_col) as col148, max(a.no149_col) as col149, max(a.no150_col) as col150

from (
select *
from (
select a.master_id, a.master_ver, to_char(a.COLUMN_SEQ) as col
        , row_number() over (partition by a.master_id, a.master_ver order by column_seq) as no
from TN_AD_MASTER_COLUMN a
)
pivot (max(col) col for no
   in (1 as no1, 2 as no2, 3 as no3, 4 as no4, 5 as no5, 6 as no6, 7 as no7, 8 as no8, 9 as no9, 10 as no10
       ,11 as no11, 12 as no12, 13 as no13, 14 as no14, 15 as no15, 16 as no16, 17 as no17, 18 as no18, 19 as no19, 20 as no20
   ,21 as no21, 22 as no22, 23 as no23, 24 as no24, 25 as no25, 26 as no26, 27 as no27, 28 as no28, 29 as no29, 30 as no30
   ,31 as no31, 32 as no32, 33 as no33, 34 as no34, 35 as no35, 36 as no36, 37 as no37, 38 as no38, 39 as no39, 40 as no40
   ,41 as no41, 42 as no42, 43 as no43, 44 as no44, 45 as no45, 46 as no46, 47 as no47, 48 as no48, 49 as no49, 50 as no50
   ,51 as no51, 52 as no52, 53 as no53, 54 as no54, 55 as no55, 56 as no56, 57 as no57, 58 as no58, 59 as no59, 60 as no60
   ,61 as no61, 62 as no62, 63 as no63, 64 as no64, 65 as no65, 66 as no66, 67 as no67, 68 as no68, 69 as no69, 70 as no70
   ,71 as no71, 72 as no72, 73 as no73, 74 as no74, 75 as no75, 76 as no76, 77 as no77, 78 as no78, 79 as no79, 80 as no80
   ,81 as no81, 82 as no82, 83 as no83, 84 as no84, 85 as no85, 86 as no86, 87 as no87, 88 as no88, 89 as no89, 90 as no90
   ,91 as no91, 92 as no92, 93 as no93, 94 as no94, 95 as no95, 96 as no96, 97 as no97, 98 as no98, 99 as no99, 100 as no100
   ,101 as no101, 102 as no102, 103 as no103, 104 as no104, 105 as no105, 106 as no106, 107 as no107, 108 as no108, 109 as no109, 110 as no110
   ,111 as no111, 112 as no112, 113 as no113, 114 as no114, 115 as no115, 116 as no116, 117 as no117, 118 as no118, 119 as no119, 120 as no120
   ,121 as no121, 122 as no122, 123 as no123, 124 as no124, 125 as no125, 126 as no126, 127 as no127, 128 as no128, 129 as no129, 130 as no130
   ,131 as no131, 132 as no132, 133 as no133, 134 as no134, 135 as no135, 136 as no136, 137 as no137, 138 as no138, 139 as no139, 140 as no140
   ,141 as no141, 142 as no142, 143 as no143, 144 as no144, 145 as no145, 146 as no146, 147 as no147, 148 as no148, 149 as no149, 150 as no150
   )
)
) a
group by a.master_id, a.master_ver

union all
select a.master_id, a.master_ver, 2 as no,  'COLUMN_ID' as gb
, max(a.no1_col) as col01, max(a.no2_col) as col02, max(a.no3_col) as col03, max(a.no4_col) as col04, max(a.no5_col) as col05, max(a.no6_col) as col06, max(a.no7_col) as col07, max(a.no8_col) as col08, max(a.no9_col) as col09, max(a.no10_col) as col10
, max(a.no11_col) as col11, max(a.no12_col) as col12, max(a.no13_col) as col13, max(a.no14_col) as col14, max(a.no15_col) as col15, max(a.no16_col) as col16, max(a.no17_col) as col17, max(a.no18_col) as col18, max(a.no19_col) as col19, max(a.no20_col) as col20
, max(a.no21_col) as col21, max(a.no22_col) as col22, max(a.no23_col) as col23, max(a.no24_col) as col24, max(a.no25_col) as col25, max(a.no26_col) as col26, max(a.no27_col) as col27, max(a.no28_col) as col28, max(a.no29_col) as col29, max(a.no30_col) as col30
, max(a.no31_col) as col31, max(a.no32_col) as col32, max(a.no33_col) as col33, max(a.no34_col) as col34, max(a.no35_col) as col35, max(a.no36_col) as col36, max(a.no37_col) as col37, max(a.no38_col) as col38, max(a.no39_col) as col39, max(a.no40_col) as col40
, max(a.no41_col) as col41, max(a.no42_col) as col42, max(a.no43_col) as col43, max(a.no44_col) as col44, max(a.no45_col) as col45, max(a.no46_col) as col46, max(a.no47_col) as col47, max(a.no48_col) as col48, max(a.no49_col) as col49, max(a.no50_col) as col50
, max(a.no51_col) as col51, max(a.no52_col) as col52, max(a.no53_col) as col53, max(a.no54_col) as col54, max(a.no55_col) as col55, max(a.no56_col) as col56, max(a.no57_col) as col57, max(a.no58_col) as col58, max(a.no59_col) as col59, max(a.no60_col) as col60
, max(a.no61_col) as col61, max(a.no62_col) as col62, max(a.no63_col) as col63, max(a.no64_col) as col64, max(a.no65_col) as col65, max(a.no66_col) as col66, max(a.no67_col) as col67, max(a.no68_col) as col68, max(a.no69_col) as col69, max(a.no70_col) as col70
, max(a.no71_col) as col71, max(a.no72_col) as col72, max(a.no73_col) as col73, max(a.no74_col) as col74, max(a.no75_col) as col75, max(a.no76_col) as col76, max(a.no77_col) as col77, max(a.no78_col) as col78, max(a.no79_col) as col79, max(a.no80_col) as col80
, max(a.no81_col) as col81, max(a.no82_col) as col82, max(a.no83_col) as col83, max(a.no84_col) as col84, max(a.no85_col) as col85, max(a.no86_col) as col86, max(a.no87_col) as col87, max(a.no88_col) as col88, max(a.no89_col) as col89, max(a.no90_col) as col90
, max(a.no91_col) as col91, max(a.no92_col) as col92, max(a.no93_col) as col93, max(a.no94_col) as col94, max(a.no95_col) as col95, max(a.no96_col) as col96, max(a.no97_col) as col97, max(a.no98_col) as col98, max(a.no99_col) as col99, max(a.no100_col) as col100
, max(a.no101_col) as col101, max(a.no102_col) as col102, max(a.no103_col) as col103, max(a.no104_col) as col104, max(a.no105_col) as col105, max(a.no106_col) as col106, max(a.no107_col) as col107, max(a.no108_col) as col108, max(a.no109_col) as col109, max(a.no110_col) as col110
, max(a.no111_col) as col111, max(a.no112_col) as col112, max(a.no113_col) as col113, max(a.no114_col) as col114, max(a.no115_col) as col115, max(a.no116_col) as col116, max(a.no117_col) as col117, max(a.no118_col) as col118, max(a.no119_col) as col119, max(a.no120_col) as col120
, max(a.no121_col) as col121, max(a.no122_col) as col122, max(a.no123_col) as col123, max(a.no124_col) as col124, max(a.no125_col) as col125, max(a.no126_col) as col126, max(a.no127_col) as col127, max(a.no128_col) as col128, max(a.no129_col) as col129, max(a.no130_col) as col130
, max(a.no131_col) as col131, max(a.no132_col) as col132, max(a.no133_col) as col133, max(a.no134_col) as col134, max(a.no135_col) as col135, max(a.no136_col) as col136, max(a.no137_col) as col137, max(a.no138_col) as col138, max(a.no139_col) as col139, max(a.no140_col) as col140
, max(a.no141_col) as col141, max(a.no142_col) as col142, max(a.no143_col) as col143, max(a.no144_col) as col144, max(a.no145_col) as col145, max(a.no146_col) as col146, max(a.no147_col) as col147, max(a.no148_col) as col148, max(a.no149_col) as col149, max(a.no150_col) as col150

from (
select *
from (
select a.master_id, a.master_ver, a.COLUMN_ID as col
        , row_number() over (partition by a.master_id, a.master_ver order by column_seq) as no
from TN_AD_MASTER_COLUMN a
)
pivot (max(col) col for no
   in (1 as no1, 2 as no2, 3 as no3, 4 as no4, 5 as no5, 6 as no6, 7 as no7, 8 as no8, 9 as no9, 10 as no10
       ,11 as no11, 12 as no12, 13 as no13, 14 as no14, 15 as no15, 16 as no16, 17 as no17, 18 as no18, 19 as no19, 20 as no20
   ,21 as no21, 22 as no22, 23 as no23, 24 as no24, 25 as no25, 26 as no26, 27 as no27, 28 as no28, 29 as no29, 30 as no30
   ,31 as no31, 32 as no32, 33 as no33, 34 as no34, 35 as no35, 36 as no36, 37 as no37, 38 as no38, 39 as no39, 40 as no40
   ,41 as no41, 42 as no42, 43 as no43, 44 as no44, 45 as no45, 46 as no46, 47 as no47, 48 as no48, 49 as no49, 50 as no50
   ,51 as no51, 52 as no52, 53 as no53, 54 as no54, 55 as no55, 56 as no56, 57 as no57, 58 as no58, 59 as no59, 60 as no60
   ,61 as no61, 62 as no62, 63 as no63, 64 as no64, 65 as no65, 66 as no66, 67 as no67, 68 as no68, 69 as no69, 70 as no70
   ,71 as no71, 72 as no72, 73 as no73, 74 as no74, 75 as no75, 76 as no76, 77 as no77, 78 as no78, 79 as no79, 80 as no80
   ,81 as no81, 82 as no82, 83 as no83, 84 as no84, 85 as no85, 86 as no86, 87 as no87, 88 as no88, 89 as no89, 90 as no90
   ,91 as no91, 92 as no92, 93 as no93, 94 as no94, 95 as no95, 96 as no96, 97 as no97, 98 as no98, 99 as no99, 100 as no100
   ,101 as no101, 102 as no102, 103 as no103, 104 as no104, 105 as no105, 106 as no106, 107 as no107, 108 as no108, 109 as no109, 110 as no110
   ,111 as no111, 112 as no112, 113 as no113, 114 as no114, 115 as no115, 116 as no116, 117 as no117, 118 as no118, 119 as no119, 120 as no120
   ,121 as no121, 122 as no122, 123 as no123, 124 as no124, 125 as no125, 126 as no126, 127 as no127, 128 as no128, 129 as no129, 130 as no130
   ,131 as no131, 132 as no132, 133 as no133, 134 as no134, 135 as no135, 136 as no136, 137 as no137, 138 as no138, 139 as no139, 140 as no140
   ,141 as no141, 142 as no142, 143 as no143, 144 as no144, 145 as no145, 146 as no146, 147 as no147, 148 as no148, 149 as no149, 150 as no150
   )
)
) a
group by a.master_id, a.master_ver

union all

select a.master_id, a.master_ver, 3 as no,  'COLUMN_NAME' as gb
, max(a.no1_col) as col01, max(a.no2_col) as col02, max(a.no3_col) as col03, max(a.no4_col) as col04, max(a.no5_col) as col05, max(a.no6_col) as col06, max(a.no7_col) as col07, max(a.no8_col) as col08, max(a.no9_col) as col09, max(a.no10_col) as col10
, max(a.no11_col) as col11, max(a.no12_col) as col12, max(a.no13_col) as col13, max(a.no14_col) as col14, max(a.no15_col) as col15, max(a.no16_col) as col16, max(a.no17_col) as col17, max(a.no18_col) as col18, max(a.no19_col) as col19, max(a.no20_col) as col20
, max(a.no21_col) as col21, max(a.no22_col) as col22, max(a.no23_col) as col23, max(a.no24_col) as col24, max(a.no25_col) as col25, max(a.no26_col) as col26, max(a.no27_col) as col27, max(a.no28_col) as col28, max(a.no29_col) as col29, max(a.no30_col) as col30
, max(a.no31_col) as col31, max(a.no32_col) as col32, max(a.no33_col) as col33, max(a.no34_col) as col34, max(a.no35_col) as col35, max(a.no36_col) as col36, max(a.no37_col) as col37, max(a.no38_col) as col38, max(a.no39_col) as col39, max(a.no40_col) as col40
, max(a.no41_col) as col41, max(a.no42_col) as col42, max(a.no43_col) as col43, max(a.no44_col) as col44, max(a.no45_col) as col45, max(a.no46_col) as col46, max(a.no47_col) as col47, max(a.no48_col) as col48, max(a.no49_col) as col49, max(a.no50_col) as col50
, max(a.no51_col) as col51, max(a.no52_col) as col52, max(a.no53_col) as col53, max(a.no54_col) as col54, max(a.no55_col) as col55, max(a.no56_col) as col56, max(a.no57_col) as col57, max(a.no58_col) as col58, max(a.no59_col) as col59, max(a.no60_col) as col60
, max(a.no61_col) as col61, max(a.no62_col) as col62, max(a.no63_col) as col63, max(a.no64_col) as col64, max(a.no65_col) as col65, max(a.no66_col) as col66, max(a.no67_col) as col67, max(a.no68_col) as col68, max(a.no69_col) as col69, max(a.no70_col) as col70
, max(a.no71_col) as col71, max(a.no72_col) as col72, max(a.no73_col) as col73, max(a.no74_col) as col74, max(a.no75_col) as col75, max(a.no76_col) as col76, max(a.no77_col) as col77, max(a.no78_col) as col78, max(a.no79_col) as col79, max(a.no80_col) as col80
, max(a.no81_col) as col81, max(a.no82_col) as col82, max(a.no83_col) as col83, max(a.no84_col) as col84, max(a.no85_col) as col85, max(a.no86_col) as col86, max(a.no87_col) as col87, max(a.no88_col) as col88, max(a.no89_col) as col89, max(a.no90_col) as col90
, max(a.no91_col) as col91, max(a.no92_col) as col92, max(a.no93_col) as col93, max(a.no94_col) as col94, max(a.no95_col) as col95, max(a.no96_col) as col96, max(a.no97_col) as col97, max(a.no98_col) as col98, max(a.no99_col) as col99, max(a.no100_col) as col100
, max(a.no101_col) as col101, max(a.no102_col) as col102, max(a.no103_col) as col103, max(a.no104_col) as col104, max(a.no105_col) as col105, max(a.no106_col) as col106, max(a.no107_col) as col107, max(a.no108_col) as col108, max(a.no109_col) as col109, max(a.no110_col) as col110
, max(a.no111_col) as col111, max(a.no112_col) as col112, max(a.no113_col) as col113, max(a.no114_col) as col114, max(a.no115_col) as col115, max(a.no116_col) as col116, max(a.no117_col) as col117, max(a.no118_col) as col118, max(a.no119_col) as col119, max(a.no120_col) as col120
, max(a.no121_col) as col121, max(a.no122_col) as col122, max(a.no123_col) as col123, max(a.no124_col) as col124, max(a.no125_col) as col125, max(a.no126_col) as col126, max(a.no127_col) as col127, max(a.no128_col) as col128, max(a.no129_col) as col129, max(a.no130_col) as col130
, max(a.no131_col) as col131, max(a.no132_col) as col132, max(a.no133_col) as col133, max(a.no134_col) as col134, max(a.no135_col) as col135, max(a.no136_col) as col136, max(a.no137_col) as col137, max(a.no138_col) as col138, max(a.no139_col) as col139, max(a.no140_col) as col140
, max(a.no141_col) as col141, max(a.no142_col) as col142, max(a.no143_col) as col143, max(a.no144_col) as col144, max(a.no145_col) as col145, max(a.no146_col) as col146, max(a.no147_col) as col147, max(a.no148_col) as col148, max(a.no149_col) as col149, max(a.no150_col) as col150
from (
select *
from (
select a.master_id, a.master_ver, a.COLUMN_NAME as col
        , row_number() over (partition by a.master_id, a.master_ver order by column_seq) as no
from TN_AD_MASTER_COLUMN a
)
pivot (max(col) col for no
   in (1 as no1, 2 as no2, 3 as no3, 4 as no4, 5 as no5, 6 as no6, 7 as no7, 8 as no8, 9 as no9, 10 as no10
       ,11 as no11, 12 as no12, 13 as no13, 14 as no14, 15 as no15, 16 as no16, 17 as no17, 18 as no18, 19 as no19, 20 as no20
   ,21 as no21, 22 as no22, 23 as no23, 24 as no24, 25 as no25, 26 as no26, 27 as no27, 28 as no28, 29 as no29, 30 as no30
   ,31 as no31, 32 as no32, 33 as no33, 34 as no34, 35 as no35, 36 as no36, 37 as no37, 38 as no38, 39 as no39, 40 as no40
   ,41 as no41, 42 as no42, 43 as no43, 44 as no44, 45 as no45, 46 as no46, 47 as no47, 48 as no48, 49 as no49, 50 as no50
   ,51 as no51, 52 as no52, 53 as no53, 54 as no54, 55 as no55, 56 as no56, 57 as no57, 58 as no58, 59 as no59, 60 as no60
   ,61 as no61, 62 as no62, 63 as no63, 64 as no64, 65 as no65, 66 as no66, 67 as no67, 68 as no68, 69 as no69, 70 as no70
   ,71 as no71, 72 as no72, 73 as no73, 74 as no74, 75 as no75, 76 as no76, 77 as no77, 78 as no78, 79 as no79, 80 as no80
   ,81 as no81, 82 as no82, 83 as no83, 84 as no84, 85 as no85, 86 as no86, 87 as no87, 88 as no88, 89 as no89, 90 as no90
   ,91 as no91, 92 as no92, 93 as no93, 94 as no94, 95 as no95, 96 as no96, 97 as no97, 98 as no98, 99 as no99, 100 as no100
   ,101 as no101, 102 as no102, 103 as no103, 104 as no104, 105 as no105, 106 as no106, 107 as no107, 108 as no108, 109 as no109, 110 as no110
   ,111 as no111, 112 as no112, 113 as no113, 114 as no114, 115 as no115, 116 as no116, 117 as no117, 118 as no118, 119 as no119, 120 as no120
   ,121 as no121, 122 as no122, 123 as no123, 124 as no124, 125 as no125, 126 as no126, 127 as no127, 128 as no128, 129 as no129, 130 as no130
   ,131 as no131, 132 as no132, 133 as no133, 134 as no134, 135 as no135, 136 as no136, 137 as no137, 138 as no138, 139 as no139, 140 as no140
   ,141 as no141, 142 as no142, 143 as no143, 144 as no144, 145 as no145, 146 as no146, 147 as no147, 148 as no148, 149 as no149, 150 as no150
   )
)
) a
group by a.master_id, a.master_ver

union all

select a.master_id, a.master_ver, 4 as no,  'COLUMN_TYPE' as gb
, max(a.no1_col) as col01, max(a.no2_col) as col02, max(a.no3_col) as col03, max(a.no4_col) as col04, max(a.no5_col) as col05, max(a.no6_col) as col06, max(a.no7_col) as col07, max(a.no8_col) as col08, max(a.no9_col) as col09, max(a.no10_col) as col10
, max(a.no11_col) as col11, max(a.no12_col) as col12, max(a.no13_col) as col13, max(a.no14_col) as col14, max(a.no15_col) as col15, max(a.no16_col) as col16, max(a.no17_col) as col17, max(a.no18_col) as col18, max(a.no19_col) as col19, max(a.no20_col) as col20
, max(a.no21_col) as col21, max(a.no22_col) as col22, max(a.no23_col) as col23, max(a.no24_col) as col24, max(a.no25_col) as col25, max(a.no26_col) as col26, max(a.no27_col) as col27, max(a.no28_col) as col28, max(a.no29_col) as col29, max(a.no30_col) as col30
, max(a.no31_col) as col31, max(a.no32_col) as col32, max(a.no33_col) as col33, max(a.no34_col) as col34, max(a.no35_col) as col35, max(a.no36_col) as col36, max(a.no37_col) as col37, max(a.no38_col) as col38, max(a.no39_col) as col39, max(a.no40_col) as col40
, max(a.no41_col) as col41, max(a.no42_col) as col42, max(a.no43_col) as col43, max(a.no44_col) as col44, max(a.no45_col) as col45, max(a.no46_col) as col46, max(a.no47_col) as col47, max(a.no48_col) as col48, max(a.no49_col) as col49, max(a.no50_col) as col50
, max(a.no51_col) as col51, max(a.no52_col) as col52, max(a.no53_col) as col53, max(a.no54_col) as col54, max(a.no55_col) as col55, max(a.no56_col) as col56, max(a.no57_col) as col57, max(a.no58_col) as col58, max(a.no59_col) as col59, max(a.no60_col) as col60
, max(a.no61_col) as col61, max(a.no62_col) as col62, max(a.no63_col) as col63, max(a.no64_col) as col64, max(a.no65_col) as col65, max(a.no66_col) as col66, max(a.no67_col) as col67, max(a.no68_col) as col68, max(a.no69_col) as col69, max(a.no70_col) as col70
, max(a.no71_col) as col71, max(a.no72_col) as col72, max(a.no73_col) as col73, max(a.no74_col) as col74, max(a.no75_col) as col75, max(a.no76_col) as col76, max(a.no77_col) as col77, max(a.no78_col) as col78, max(a.no79_col) as col79, max(a.no80_col) as col80
, max(a.no81_col) as col81, max(a.no82_col) as col82, max(a.no83_col) as col83, max(a.no84_col) as col84, max(a.no85_col) as col85, max(a.no86_col) as col86, max(a.no87_col) as col87, max(a.no88_col) as col88, max(a.no89_col) as col89, max(a.no90_col) as col90
, max(a.no91_col) as col91, max(a.no92_col) as col92, max(a.no93_col) as col93, max(a.no94_col) as col94, max(a.no95_col) as col95, max(a.no96_col) as col96, max(a.no97_col) as col97, max(a.no98_col) as col98, max(a.no99_col) as col99, max(a.no100_col) as col100
, max(a.no101_col) as col101, max(a.no102_col) as col102, max(a.no103_col) as col103, max(a.no104_col) as col104, max(a.no105_col) as col105, max(a.no106_col) as col106, max(a.no107_col) as col107, max(a.no108_col) as col108, max(a.no109_col) as col109, max(a.no110_col) as col110
, max(a.no111_col) as col111, max(a.no112_col) as col112, max(a.no113_col) as col113, max(a.no114_col) as col114, max(a.no115_col) as col115, max(a.no116_col) as col116, max(a.no117_col) as col117, max(a.no118_col) as col118, max(a.no119_col) as col119, max(a.no120_col) as col120
, max(a.no121_col) as col121, max(a.no122_col) as col122, max(a.no123_col) as col123, max(a.no124_col) as col124, max(a.no125_col) as col125, max(a.no126_col) as col126, max(a.no127_col) as col127, max(a.no128_col) as col128, max(a.no129_col) as col129, max(a.no130_col) as col130
, max(a.no131_col) as col131, max(a.no132_col) as col132, max(a.no133_col) as col133, max(a.no134_col) as col134, max(a.no135_col) as col135, max(a.no136_col) as col136, max(a.no137_col) as col137, max(a.no138_col) as col138, max(a.no139_col) as col139, max(a.no140_col) as col140
, max(a.no141_col) as col141, max(a.no142_col) as col142, max(a.no143_col) as col143, max(a.no144_col) as col144, max(a.no145_col) as col145, max(a.no146_col) as col146, max(a.no147_col) as col147, max(a.no148_col) as col148, max(a.no149_col) as col149, max(a.no150_col) as col150

from (
select *
from (
select a.master_id, a.master_ver, a.COLUMN_TYPE as col
        , row_number() over (partition by a.master_id, a.master_ver order by column_seq) as no
from TN_AD_MASTER_COLUMN a
)
pivot (max(col) col for no
   in (1 as no1, 2 as no2, 3 as no3, 4 as no4, 5 as no5, 6 as no6, 7 as no7, 8 as no8, 9 as no9, 10 as no10
       ,11 as no11, 12 as no12, 13 as no13, 14 as no14, 15 as no15, 16 as no16, 17 as no17, 18 as no18, 19 as no19, 20 as no20
   ,21 as no21, 22 as no22, 23 as no23, 24 as no24, 25 as no25, 26 as no26, 27 as no27, 28 as no28, 29 as no29, 30 as no30
   ,31 as no31, 32 as no32, 33 as no33, 34 as no34, 35 as no35, 36 as no36, 37 as no37, 38 as no38, 39 as no39, 40 as no40
   ,41 as no41, 42 as no42, 43 as no43, 44 as no44, 45 as no45, 46 as no46, 47 as no47, 48 as no48, 49 as no49, 50 as no50
   ,51 as no51, 52 as no52, 53 as no53, 54 as no54, 55 as no55, 56 as no56, 57 as no57, 58 as no58, 59 as no59, 60 as no60
   ,61 as no61, 62 as no62, 63 as no63, 64 as no64, 65 as no65, 66 as no66, 67 as no67, 68 as no68, 69 as no69, 70 as no70
   ,71 as no71, 72 as no72, 73 as no73, 74 as no74, 75 as no75, 76 as no76, 77 as no77, 78 as no78, 79 as no79, 80 as no80
   ,81 as no81, 82 as no82, 83 as no83, 84 as no84, 85 as no85, 86 as no86, 87 as no87, 88 as no88, 89 as no89, 90 as no90
   ,91 as no91, 92 as no92, 93 as no93, 94 as no94, 95 as no95, 96 as no96, 97 as no97, 98 as no98, 99 as no99, 100 as no100
   ,101 as no101, 102 as no102, 103 as no103, 104 as no104, 105 as no105, 106 as no106, 107 as no107, 108 as no108, 109 as no109, 110 as no110
   ,111 as no111, 112 as no112, 113 as no113, 114 as no114, 115 as no115, 116 as no116, 117 as no117, 118 as no118, 119 as no119, 120 as no120
   ,121 as no121, 122 as no122, 123 as no123, 124 as no124, 125 as no125, 126 as no126, 127 as no127, 128 as no128, 129 as no129, 130 as no130
   ,131 as no131, 132 as no132, 133 as no133, 134 as no134, 135 as no135, 136 as no136, 137 as no137, 138 as no138, 139 as no139, 140 as no140
   ,141 as no141, 142 as no142, 143 as no143, 144 as no144, 145 as no145, 146 as no146, 147 as no147, 148 as no148, 149 as no149, 150 as no150
   )
)
) a
group by a.master_id, a.master_ver

union all

select a.master_id, a.master_ver, 5 as no,  'COLUMN_SIZE' as gb
, max(a.no1_col) as col01, max(a.no2_col) as col02, max(a.no3_col) as col03, max(a.no4_col) as col04, max(a.no5_col) as col05, max(a.no6_col) as col06, max(a.no7_col) as col07, max(a.no8_col) as col08, max(a.no9_col) as col09, max(a.no10_col) as col10
, max(a.no11_col) as col11, max(a.no12_col) as col12, max(a.no13_col) as col13, max(a.no14_col) as col14, max(a.no15_col) as col15, max(a.no16_col) as col16, max(a.no17_col) as col17, max(a.no18_col) as col18, max(a.no19_col) as col19, max(a.no20_col) as col20
, max(a.no21_col) as col21, max(a.no22_col) as col22, max(a.no23_col) as col23, max(a.no24_col) as col24, max(a.no25_col) as col25, max(a.no26_col) as col26, max(a.no27_col) as col27, max(a.no28_col) as col28, max(a.no29_col) as col29, max(a.no30_col) as col30
, max(a.no31_col) as col31, max(a.no32_col) as col32, max(a.no33_col) as col33, max(a.no34_col) as col34, max(a.no35_col) as col35, max(a.no36_col) as col36, max(a.no37_col) as col37, max(a.no38_col) as col38, max(a.no39_col) as col39, max(a.no40_col) as col40
, max(a.no41_col) as col41, max(a.no42_col) as col42, max(a.no43_col) as col43, max(a.no44_col) as col44, max(a.no45_col) as col45, max(a.no46_col) as col46, max(a.no47_col) as col47, max(a.no48_col) as col48, max(a.no49_col) as col49, max(a.no50_col) as col50
, max(a.no51_col) as col51, max(a.no52_col) as col52, max(a.no53_col) as col53, max(a.no54_col) as col54, max(a.no55_col) as col55, max(a.no56_col) as col56, max(a.no57_col) as col57, max(a.no58_col) as col58, max(a.no59_col) as col59, max(a.no60_col) as col60
, max(a.no61_col) as col61, max(a.no62_col) as col62, max(a.no63_col) as col63, max(a.no64_col) as col64, max(a.no65_col) as col65, max(a.no66_col) as col66, max(a.no67_col) as col67, max(a.no68_col) as col68, max(a.no69_col) as col69, max(a.no70_col) as col70
, max(a.no71_col) as col71, max(a.no72_col) as col72, max(a.no73_col) as col73, max(a.no74_col) as col74, max(a.no75_col) as col75, max(a.no76_col) as col76, max(a.no77_col) as col77, max(a.no78_col) as col78, max(a.no79_col) as col79, max(a.no80_col) as col80
, max(a.no81_col) as col81, max(a.no82_col) as col82, max(a.no83_col) as col83, max(a.no84_col) as col84, max(a.no85_col) as col85, max(a.no86_col) as col86, max(a.no87_col) as col87, max(a.no88_col) as col88, max(a.no89_col) as col89, max(a.no90_col) as col90
, max(a.no91_col) as col91, max(a.no92_col) as col92, max(a.no93_col) as col93, max(a.no94_col) as col94, max(a.no95_col) as col95, max(a.no96_col) as col96, max(a.no97_col) as col97, max(a.no98_col) as col98, max(a.no99_col) as col99, max(a.no100_col) as col100
, max(a.no101_col) as col101, max(a.no102_col) as col102, max(a.no103_col) as col103, max(a.no104_col) as col104, max(a.no105_col) as col105, max(a.no106_col) as col106, max(a.no107_col) as col107, max(a.no108_col) as col108, max(a.no109_col) as col109, max(a.no110_col) as col110
, max(a.no111_col) as col111, max(a.no112_col) as col112, max(a.no113_col) as col113, max(a.no114_col) as col114, max(a.no115_col) as col115, max(a.no116_col) as col116, max(a.no117_col) as col117, max(a.no118_col) as col118, max(a.no119_col) as col119, max(a.no120_col) as col120
, max(a.no121_col) as col121, max(a.no122_col) as col122, max(a.no123_col) as col123, max(a.no124_col) as col124, max(a.no125_col) as col125, max(a.no126_col) as col126, max(a.no127_col) as col127, max(a.no128_col) as col128, max(a.no129_col) as col129, max(a.no130_col) as col130
, max(a.no131_col) as col131, max(a.no132_col) as col132, max(a.no133_col) as col133, max(a.no134_col) as col134, max(a.no135_col) as col135, max(a.no136_col) as col136, max(a.no137_col) as col137, max(a.no138_col) as col138, max(a.no139_col) as col139, max(a.no140_col) as col140
, max(a.no141_col) as col141, max(a.no142_col) as col142, max(a.no143_col) as col143, max(a.no144_col) as col144, max(a.no145_col) as col145, max(a.no146_col) as col146, max(a.no147_col) as col147, max(a.no148_col) as col148, max(a.no149_col) as col149, max(a.no150_col) as col150

from (
select *
from (
select a.master_id, a.master_ver, to_char(a.COLUMN_SIZE) as col
        , row_number() over (partition by a.master_id, a.master_ver order by column_seq) as no
from TN_AD_MASTER_COLUMN a
)
pivot (max(col) col for no
   in (1 as no1, 2 as no2, 3 as no3, 4 as no4, 5 as no5, 6 as no6, 7 as no7, 8 as no8, 9 as no9, 10 as no10
       ,11 as no11, 12 as no12, 13 as no13, 14 as no14, 15 as no15, 16 as no16, 17 as no17, 18 as no18, 19 as no19, 20 as no20
   ,21 as no21, 22 as no22, 23 as no23, 24 as no24, 25 as no25, 26 as no26, 27 as no27, 28 as no28, 29 as no29, 30 as no30
   ,31 as no31, 32 as no32, 33 as no33, 34 as no34, 35 as no35, 36 as no36, 37 as no37, 38 as no38, 39 as no39, 40 as no40
   ,41 as no41, 42 as no42, 43 as no43, 44 as no44, 45 as no45, 46 as no46, 47 as no47, 48 as no48, 49 as no49, 50 as no50
   ,51 as no51, 52 as no52, 53 as no53, 54 as no54, 55 as no55, 56 as no56, 57 as no57, 58 as no58, 59 as no59, 60 as no60
   ,61 as no61, 62 as no62, 63 as no63, 64 as no64, 65 as no65, 66 as no66, 67 as no67, 68 as no68, 69 as no69, 70 as no70
   ,71 as no71, 72 as no72, 73 as no73, 74 as no74, 75 as no75, 76 as no76, 77 as no77, 78 as no78, 79 as no79, 80 as no80
   ,81 as no81, 82 as no82, 83 as no83, 84 as no84, 85 as no85, 86 as no86, 87 as no87, 88 as no88, 89 as no89, 90 as no90
   ,91 as no91, 92 as no92, 93 as no93, 94 as no94, 95 as no95, 96 as no96, 97 as no97, 98 as no98, 99 as no99, 100 as no100
   ,101 as no101, 102 as no102, 103 as no103, 104 as no104, 105 as no105, 106 as no106, 107 as no107, 108 as no108, 109 as no109, 110 as no110
   ,111 as no111, 112 as no112, 113 as no113, 114 as no114, 115 as no115, 116 as no116, 117 as no117, 118 as no118, 119 as no119, 120 as no120
   ,121 as no121, 122 as no122, 123 as no123, 124 as no124, 125 as no125, 126 as no126, 127 as no127, 128 as no128, 129 as no129, 130 as no130
   ,131 as no131, 132 as no132, 133 as no133, 134 as no134, 135 as no135, 136 as no136, 137 as no137, 138 as no138, 139 as no139, 140 as no140
   ,141 as no141, 142 as no142, 143 as no143, 144 as no144, 145 as no145, 146 as no146, 147 as no147, 148 as no148, 149 as no149, 150 as no150
   )
)
) a
group by a.master_id, a.master_ver

union all

select a.master_id, a.master_ver, 6 as no,  'COLUMN_SIZE2' as gb
, max(a.no1_col) as col01, max(a.no2_col) as col02, max(a.no3_col) as col03, max(a.no4_col) as col04, max(a.no5_col) as col05, max(a.no6_col) as col06, max(a.no7_col) as col07, max(a.no8_col) as col08, max(a.no9_col) as col09, max(a.no10_col) as col10
, max(a.no11_col) as col11, max(a.no12_col) as col12, max(a.no13_col) as col13, max(a.no14_col) as col14, max(a.no15_col) as col15, max(a.no16_col) as col16, max(a.no17_col) as col17, max(a.no18_col) as col18, max(a.no19_col) as col19, max(a.no20_col) as col20
, max(a.no21_col) as col21, max(a.no22_col) as col22, max(a.no23_col) as col23, max(a.no24_col) as col24, max(a.no25_col) as col25, max(a.no26_col) as col26, max(a.no27_col) as col27, max(a.no28_col) as col28, max(a.no29_col) as col29, max(a.no30_col) as col30
, max(a.no31_col) as col31, max(a.no32_col) as col32, max(a.no33_col) as col33, max(a.no34_col) as col34, max(a.no35_col) as col35, max(a.no36_col) as col36, max(a.no37_col) as col37, max(a.no38_col) as col38, max(a.no39_col) as col39, max(a.no40_col) as col40
, max(a.no41_col) as col41, max(a.no42_col) as col42, max(a.no43_col) as col43, max(a.no44_col) as col44, max(a.no45_col) as col45, max(a.no46_col) as col46, max(a.no47_col) as col47, max(a.no48_col) as col48, max(a.no49_col) as col49, max(a.no50_col) as col50
, max(a.no51_col) as col51, max(a.no52_col) as col52, max(a.no53_col) as col53, max(a.no54_col) as col54, max(a.no55_col) as col55, max(a.no56_col) as col56, max(a.no57_col) as col57, max(a.no58_col) as col58, max(a.no59_col) as col59, max(a.no60_col) as col60
, max(a.no61_col) as col61, max(a.no62_col) as col62, max(a.no63_col) as col63, max(a.no64_col) as col64, max(a.no65_col) as col65, max(a.no66_col) as col66, max(a.no67_col) as col67, max(a.no68_col) as col68, max(a.no69_col) as col69, max(a.no70_col) as col70
, max(a.no71_col) as col71, max(a.no72_col) as col72, max(a.no73_col) as col73, max(a.no74_col) as col74, max(a.no75_col) as col75, max(a.no76_col) as col76, max(a.no77_col) as col77, max(a.no78_col) as col78, max(a.no79_col) as col79, max(a.no80_col) as col80
, max(a.no81_col) as col81, max(a.no82_col) as col82, max(a.no83_col) as col83, max(a.no84_col) as col84, max(a.no85_col) as col85, max(a.no86_col) as col86, max(a.no87_col) as col87, max(a.no88_col) as col88, max(a.no89_col) as col89, max(a.no90_col) as col90
, max(a.no91_col) as col91, max(a.no92_col) as col92, max(a.no93_col) as col93, max(a.no94_col) as col94, max(a.no95_col) as col95, max(a.no96_col) as col96, max(a.no97_col) as col97, max(a.no98_col) as col98, max(a.no99_col) as col99, max(a.no100_col) as col100
, max(a.no101_col) as col101, max(a.no102_col) as col102, max(a.no103_col) as col103, max(a.no104_col) as col104, max(a.no105_col) as col105, max(a.no106_col) as col106, max(a.no107_col) as col107, max(a.no108_col) as col108, max(a.no109_col) as col109, max(a.no110_col) as col110
, max(a.no111_col) as col111, max(a.no112_col) as col112, max(a.no113_col) as col113, max(a.no114_col) as col114, max(a.no115_col) as col115, max(a.no116_col) as col116, max(a.no117_col) as col117, max(a.no118_col) as col118, max(a.no119_col) as col119, max(a.no120_col) as col120
, max(a.no121_col) as col121, max(a.no122_col) as col122, max(a.no123_col) as col123, max(a.no124_col) as col124, max(a.no125_col) as col125, max(a.no126_col) as col126, max(a.no127_col) as col127, max(a.no128_col) as col128, max(a.no129_col) as col129, max(a.no130_col) as col130
, max(a.no131_col) as col131, max(a.no132_col) as col132, max(a.no133_col) as col133, max(a.no134_col) as col134, max(a.no135_col) as col135, max(a.no136_col) as col136, max(a.no137_col) as col137, max(a.no138_col) as col138, max(a.no139_col) as col139, max(a.no140_col) as col140
, max(a.no141_col) as col141, max(a.no142_col) as col142, max(a.no143_col) as col143, max(a.no144_col) as col144, max(a.no145_col) as col145, max(a.no146_col) as col146, max(a.no147_col) as col147, max(a.no148_col) as col148, max(a.no149_col) as col149, max(a.no150_col) as col150

from (
select *
from (
select a.master_id, a.master_ver, to_char(a.COLUMN_SIZE2) as col
        , row_number() over (partition by a.master_id, a.master_ver order by column_seq) as no
from TN_AD_MASTER_COLUMN a
)
pivot (max(col) col for no
   in (1 as no1, 2 as no2, 3 as no3, 4 as no4, 5 as no5, 6 as no6, 7 as no7, 8 as no8, 9 as no9, 10 as no10
       ,11 as no11, 12 as no12, 13 as no13, 14 as no14, 15 as no15, 16 as no16, 17 as no17, 18 as no18, 19 as no19, 20 as no20
   ,21 as no21, 22 as no22, 23 as no23, 24 as no24, 25 as no25, 26 as no26, 27 as no27, 28 as no28, 29 as no29, 30 as no30
   ,31 as no31, 32 as no32, 33 as no33, 34 as no34, 35 as no35, 36 as no36, 37 as no37, 38 as no38, 39 as no39, 40 as no40
   ,41 as no41, 42 as no42, 43 as no43, 44 as no44, 45 as no45, 46 as no46, 47 as no47, 48 as no48, 49 as no49, 50 as no50
   ,51 as no51, 52 as no52, 53 as no53, 54 as no54, 55 as no55, 56 as no56, 57 as no57, 58 as no58, 59 as no59, 60 as no60
   ,61 as no61, 62 as no62, 63 as no63, 64 as no64, 65 as no65, 66 as no66, 67 as no67, 68 as no68, 69 as no69, 70 as no70
   ,71 as no71, 72 as no72, 73 as no73, 74 as no74, 75 as no75, 76 as no76, 77 as no77, 78 as no78, 79 as no79, 80 as no80
   ,81 as no81, 82 as no82, 83 as no83, 84 as no84, 85 as no85, 86 as no86, 87 as no87, 88 as no88, 89 as no89, 90 as no90
   ,91 as no91, 92 as no92, 93 as no93, 94 as no94, 95 as no95, 96 as no96, 97 as no97, 98 as no98, 99 as no99, 100 as no100
   ,101 as no101, 102 as no102, 103 as no103, 104 as no104, 105 as no105, 106 as no106, 107 as no107, 108 as no108, 109 as no109, 110 as no110
   ,111 as no111, 112 as no112, 113 as no113, 114 as no114, 115 as no115, 116 as no116, 117 as no117, 118 as no118, 119 as no119, 120 as no120
   ,121 as no121, 122 as no122, 123 as no123, 124 as no124, 125 as no125, 126 as no126, 127 as no127, 128 as no128, 129 as no129, 130 as no130
   ,131 as no131, 132 as no132, 133 as no133, 134 as no134, 135 as no135, 136 as no136, 137 as no137, 138 as no138, 139 as no139, 140 as no140
   ,141 as no141, 142 as no142, 143 as no143, 144 as no144, 145 as no145, 146 as no146, 147 as no147, 148 as no148, 149 as no149, 150 as no150
   )
)
) a
group by a.master_id, a.master_ver

union all

select a.master_id, a.master_ver, 7 as no,  'COLUMN_DESC' as gb
, max(a.no1_col) as col01, max(a.no2_col) as col02, max(a.no3_col) as col03, max(a.no4_col) as col04, max(a.no5_col) as col05, max(a.no6_col) as col06, max(a.no7_col) as col07, max(a.no8_col) as col08, max(a.no9_col) as col09, max(a.no10_col) as col10
, max(a.no11_col) as col11, max(a.no12_col) as col12, max(a.no13_col) as col13, max(a.no14_col) as col14, max(a.no15_col) as col15, max(a.no16_col) as col16, max(a.no17_col) as col17, max(a.no18_col) as col18, max(a.no19_col) as col19, max(a.no20_col) as col20
, max(a.no21_col) as col21, max(a.no22_col) as col22, max(a.no23_col) as col23, max(a.no24_col) as col24, max(a.no25_col) as col25, max(a.no26_col) as col26, max(a.no27_col) as col27, max(a.no28_col) as col28, max(a.no29_col) as col29, max(a.no30_col) as col30
, max(a.no31_col) as col31, max(a.no32_col) as col32, max(a.no33_col) as col33, max(a.no34_col) as col34, max(a.no35_col) as col35, max(a.no36_col) as col36, max(a.no37_col) as col37, max(a.no38_col) as col38, max(a.no39_col) as col39, max(a.no40_col) as col40
, max(a.no41_col) as col41, max(a.no42_col) as col42, max(a.no43_col) as col43, max(a.no44_col) as col44, max(a.no45_col) as col45, max(a.no46_col) as col46, max(a.no47_col) as col47, max(a.no48_col) as col48, max(a.no49_col) as col49, max(a.no50_col) as col50
, max(a.no51_col) as col51, max(a.no52_col) as col52, max(a.no53_col) as col53, max(a.no54_col) as col54, max(a.no55_col) as col55, max(a.no56_col) as col56, max(a.no57_col) as col57, max(a.no58_col) as col58, max(a.no59_col) as col59, max(a.no60_col) as col60
, max(a.no61_col) as col61, max(a.no62_col) as col62, max(a.no63_col) as col63, max(a.no64_col) as col64, max(a.no65_col) as col65, max(a.no66_col) as col66, max(a.no67_col) as col67, max(a.no68_col) as col68, max(a.no69_col) as col69, max(a.no70_col) as col70
, max(a.no71_col) as col71, max(a.no72_col) as col72, max(a.no73_col) as col73, max(a.no74_col) as col74, max(a.no75_col) as col75, max(a.no76_col) as col76, max(a.no77_col) as col77, max(a.no78_col) as col78, max(a.no79_col) as col79, max(a.no80_col) as col80
, max(a.no81_col) as col81, max(a.no82_col) as col82, max(a.no83_col) as col83, max(a.no84_col) as col84, max(a.no85_col) as col85, max(a.no86_col) as col86, max(a.no87_col) as col87, max(a.no88_col) as col88, max(a.no89_col) as col89, max(a.no90_col) as col90
, max(a.no91_col) as col91, max(a.no92_col) as col92, max(a.no93_col) as col93, max(a.no94_col) as col94, max(a.no95_col) as col95, max(a.no96_col) as col96, max(a.no97_col) as col97, max(a.no98_col) as col98, max(a.no99_col) as col99, max(a.no100_col) as col100
, max(a.no101_col) as col101, max(a.no102_col) as col102, max(a.no103_col) as col103, max(a.no104_col) as col104, max(a.no105_col) as col105, max(a.no106_col) as col106, max(a.no107_col) as col107, max(a.no108_col) as col108, max(a.no109_col) as col109, max(a.no110_col) as col110
, max(a.no111_col) as col111, max(a.no112_col) as col112, max(a.no113_col) as col113, max(a.no114_col) as col114, max(a.no115_col) as col115, max(a.no116_col) as col116, max(a.no117_col) as col117, max(a.no118_col) as col118, max(a.no119_col) as col119, max(a.no120_col) as col120
, max(a.no121_col) as col121, max(a.no122_col) as col122, max(a.no123_col) as col123, max(a.no124_col) as col124, max(a.no125_col) as col125, max(a.no126_col) as col126, max(a.no127_col) as col127, max(a.no128_col) as col128, max(a.no129_col) as col129, max(a.no130_col) as col130
, max(a.no131_col) as col131, max(a.no132_col) as col132, max(a.no133_col) as col133, max(a.no134_col) as col134, max(a.no135_col) as col135, max(a.no136_col) as col136, max(a.no137_col) as col137, max(a.no138_col) as col138, max(a.no139_col) as col139, max(a.no140_col) as col140
, max(a.no141_col) as col141, max(a.no142_col) as col142, max(a.no143_col) as col143, max(a.no144_col) as col144, max(a.no145_col) as col145, max(a.no146_col) as col146, max(a.no147_col) as col147, max(a.no148_col) as col148, max(a.no149_col) as col149, max(a.no150_col) as col150

from (
select *
from (
select a.master_id, a.master_ver, a.COLUMN_DESC as col
        , row_number() over (partition by a.master_id, a.master_ver order by column_seq) as no
from TN_AD_MASTER_COLUMN a
)
pivot (max(col) col for no
   in (1 as no1, 2 as no2, 3 as no3, 4 as no4, 5 as no5, 6 as no6, 7 as no7, 8 as no8, 9 as no9, 10 as no10
       ,11 as no11, 12 as no12, 13 as no13, 14 as no14, 15 as no15, 16 as no16, 17 as no17, 18 as no18, 19 as no19, 20 as no20
   ,21 as no21, 22 as no22, 23 as no23, 24 as no24, 25 as no25, 26 as no26, 27 as no27, 28 as no28, 29 as no29, 30 as no30
   ,31 as no31, 32 as no32, 33 as no33, 34 as no34, 35 as no35, 36 as no36, 37 as no37, 38 as no38, 39 as no39, 40 as no40
   ,41 as no41, 42 as no42, 43 as no43, 44 as no44, 45 as no45, 46 as no46, 47 as no47, 48 as no48, 49 as no49, 50 as no50
   ,51 as no51, 52 as no52, 53 as no53, 54 as no54, 55 as no55, 56 as no56, 57 as no57, 58 as no58, 59 as no59, 60 as no60
   ,61 as no61, 62 as no62, 63 as no63, 64 as no64, 65 as no65, 66 as no66, 67 as no67, 68 as no68, 69 as no69, 70 as no70
   ,71 as no71, 72 as no72, 73 as no73, 74 as no74, 75 as no75, 76 as no76, 77 as no77, 78 as no78, 79 as no79, 80 as no80
   ,81 as no81, 82 as no82, 83 as no83, 84 as no84, 85 as no85, 86 as no86, 87 as no87, 88 as no88, 89 as no89, 90 as no90
   ,91 as no91, 92 as no92, 93 as no93, 94 as no94, 95 as no95, 96 as no96, 97 as no97, 98 as no98, 99 as no99, 100 as no100
   ,101 as no101, 102 as no102, 103 as no103, 104 as no104, 105 as no105, 106 as no106, 107 as no107, 108 as no108, 109 as no109, 110 as no110
   ,111 as no111, 112 as no112, 113 as no113, 114 as no114, 115 as no115, 116 as no116, 117 as no117, 118 as no118, 119 as no119, 120 as no120
   ,121 as no121, 122 as no122, 123 as no123, 124 as no124, 125 as no125, 126 as no126, 127 as no127, 128 as no128, 129 as no129, 130 as no130
   ,131 as no131, 132 as no132, 133 as no133, 134 as no134, 135 as no135, 136 as no136, 137 as no137, 138 as no138, 139 as no139, 140 as no140
   ,141 as no141, 142 as no142, 143 as no143, 144 as no144, 145 as no145, 146 as no146, 147 as no147, 148 as no148, 149 as no149, 150 as no150
   )
)
) a
group by a.master_id, a.master_ver

union all


select a.master_id, a.master_ver, 8 as no, 'COLUMN_DISP_YN' as gb
, max(a.no1_col) as col01, max(a.no2_col) as col02, max(a.no3_col) as col03, max(a.no4_col) as col04, max(a.no5_col) as col05, max(a.no6_col) as col06, max(a.no7_col) as col07, max(a.no8_col) as col08, max(a.no9_col) as col09, max(a.no10_col) as col10
, max(a.no11_col) as col11, max(a.no12_col) as col12, max(a.no13_col) as col13, max(a.no14_col) as col14, max(a.no15_col) as col15, max(a.no16_col) as col16, max(a.no17_col) as col17, max(a.no18_col) as col18, max(a.no19_col) as col19, max(a.no20_col) as col20
, max(a.no21_col) as col21, max(a.no22_col) as col22, max(a.no23_col) as col23, max(a.no24_col) as col24, max(a.no25_col) as col25, max(a.no26_col) as col26, max(a.no27_col) as col27, max(a.no28_col) as col28, max(a.no29_col) as col29, max(a.no30_col) as col30
, max(a.no31_col) as col31, max(a.no32_col) as col32, max(a.no33_col) as col33, max(a.no34_col) as col34, max(a.no35_col) as col35, max(a.no36_col) as col36, max(a.no37_col) as col37, max(a.no38_col) as col38, max(a.no39_col) as col39, max(a.no40_col) as col40
, max(a.no41_col) as col41, max(a.no42_col) as col42, max(a.no43_col) as col43, max(a.no44_col) as col44, max(a.no45_col) as col45, max(a.no46_col) as col46, max(a.no47_col) as col47, max(a.no48_col) as col48, max(a.no49_col) as col49, max(a.no50_col) as col50
, max(a.no51_col) as col51, max(a.no52_col) as col52, max(a.no53_col) as col53, max(a.no54_col) as col54, max(a.no55_col) as col55, max(a.no56_col) as col56, max(a.no57_col) as col57, max(a.no58_col) as col58, max(a.no59_col) as col59, max(a.no60_col) as col60
, max(a.no61_col) as col61, max(a.no62_col) as col62, max(a.no63_col) as col63, max(a.no64_col) as col64, max(a.no65_col) as col65, max(a.no66_col) as col66, max(a.no67_col) as col67, max(a.no68_col) as col68, max(a.no69_col) as col69, max(a.no70_col) as col70
, max(a.no71_col) as col71, max(a.no72_col) as col72, max(a.no73_col) as col73, max(a.no74_col) as col74, max(a.no75_col) as col75, max(a.no76_col) as col76, max(a.no77_col) as col77, max(a.no78_col) as col78, max(a.no79_col) as col79, max(a.no80_col) as col80
, max(a.no81_col) as col81, max(a.no82_col) as col82, max(a.no83_col) as col83, max(a.no84_col) as col84, max(a.no85_col) as col85, max(a.no86_col) as col86, max(a.no87_col) as col87, max(a.no88_col) as col88, max(a.no89_col) as col89, max(a.no90_col) as col90
, max(a.no91_col) as col91, max(a.no92_col) as col92, max(a.no93_col) as col93, max(a.no94_col) as col94, max(a.no95_col) as col95, max(a.no96_col) as col96, max(a.no97_col) as col97, max(a.no98_col) as col98, max(a.no99_col) as col99, max(a.no100_col) as col100
, max(a.no101_col) as col101, max(a.no102_col) as col102, max(a.no103_col) as col103, max(a.no104_col) as col104, max(a.no105_col) as col105, max(a.no106_col) as col106, max(a.no107_col) as col107, max(a.no108_col) as col108, max(a.no109_col) as col109, max(a.no110_col) as col110
, max(a.no111_col) as col111, max(a.no112_col) as col112, max(a.no113_col) as col113, max(a.no114_col) as col114, max(a.no115_col) as col115, max(a.no116_col) as col116, max(a.no117_col) as col117, max(a.no118_col) as col118, max(a.no119_col) as col119, max(a.no120_col) as col120
, max(a.no121_col) as col121, max(a.no122_col) as col122, max(a.no123_col) as col123, max(a.no124_col) as col124, max(a.no125_col) as col125, max(a.no126_col) as col126, max(a.no127_col) as col127, max(a.no128_col) as col128, max(a.no129_col) as col129, max(a.no130_col) as col130
, max(a.no131_col) as col131, max(a.no132_col) as col132, max(a.no133_col) as col133, max(a.no134_col) as col134, max(a.no135_col) as col135, max(a.no136_col) as col136, max(a.no137_col) as col137, max(a.no138_col) as col138, max(a.no139_col) as col139, max(a.no140_col) as col140
, max(a.no141_col) as col141, max(a.no142_col) as col142, max(a.no143_col) as col143, max(a.no144_col) as col144, max(a.no145_col) as col145, max(a.no146_col) as col146, max(a.no147_col) as col147, max(a.no148_col) as col148, max(a.no149_col) as col149, max(a.no150_col) as col150

from (
select *
from (
select a.master_id, a.master_ver, a.COLUMN_TYPE as col
        , row_number() over (partition by a.master_id, a.master_ver order by column_seq) as no
from TN_AD_MASTER_COLUMN a
)
pivot (max(col) col for no
   in (1 as no1, 2 as no2, 3 as no3, 4 as no4, 5 as no5, 6 as no6, 7 as no7, 8 as no8, 9 as no9, 10 as no10
       ,11 as no11, 12 as no12, 13 as no13, 14 as no14, 15 as no15, 16 as no16, 17 as no17, 18 as no18, 19 as no19, 20 as no20
   ,21 as no21, 22 as no22, 23 as no23, 24 as no24, 25 as no25, 26 as no26, 27 as no27, 28 as no28, 29 as no29, 30 as no30
   ,31 as no31, 32 as no32, 33 as no33, 34 as no34, 35 as no35, 36 as no36, 37 as no37, 38 as no38, 39 as no39, 40 as no40
   ,41 as no41, 42 as no42, 43 as no43, 44 as no44, 45 as no45, 46 as no46, 47 as no47, 48 as no48, 49 as no49, 50 as no50
   ,51 as no51, 52 as no52, 53 as no53, 54 as no54, 55 as no55, 56 as no56, 57 as no57, 58 as no58, 59 as no59, 60 as no60
   ,61 as no61, 62 as no62, 63 as no63, 64 as no64, 65 as no65, 66 as no66, 67 as no67, 68 as no68, 69 as no69, 70 as no70
   ,71 as no71, 72 as no72, 73 as no73, 74 as no74, 75 as no75, 76 as no76, 77 as no77, 78 as no78, 79 as no79, 80 as no80
   ,81 as no81, 82 as no82, 83 as no83, 84 as no84, 85 as no85, 86 as no86, 87 as no87, 88 as no88, 89 as no89, 90 as no90
   ,91 as no91, 92 as no92, 93 as no93, 94 as no94, 95 as no95, 96 as no96, 97 as no97, 98 as no98, 99 as no99, 100 as no100
   ,101 as no101, 102 as no102, 103 as no103, 104 as no104, 105 as no105, 106 as no106, 107 as no107, 108 as no108, 109 as no109, 110 as no110
   ,111 as no111, 112 as no112, 113 as no113, 114 as no114, 115 as no115, 116 as no116, 117 as no117, 118 as no118, 119 as no119, 120 as no120
   ,121 as no121, 122 as no122, 123 as no123, 124 as no124, 125 as no125, 126 as no126, 127 as no127, 128 as no128, 129 as no129, 130 as no130
   ,131 as no131, 132 as no132, 133 as no133, 134 as no134, 135 as no135, 136 as no136, 137 as no137, 138 as no138, 139 as no139, 140 as no140
   ,141 as no141, 142 as no142, 143 as no143, 144 as no144, 145 as no145, 146 as no146, 147 as no147, 148 as no148, 149 as no149, 150 as no150
   )
)
) a
group by a.master_id, a.master_ver


union all

select a.master_id, a.master_ver, 9 as no, 'SEARCH_COND_LOC' as gb
, max(a.no1_col) as col01, max(a.no2_col) as col02, max(a.no3_col) as col03, max(a.no4_col) as col04, max(a.no5_col) as col05, max(a.no6_col) as col06, max(a.no7_col) as col07, max(a.no8_col) as col08, max(a.no9_col) as col09, max(a.no10_col) as col10
, max(a.no11_col) as col11, max(a.no12_col) as col12, max(a.no13_col) as col13, max(a.no14_col) as col14, max(a.no15_col) as col15, max(a.no16_col) as col16, max(a.no17_col) as col17, max(a.no18_col) as col18, max(a.no19_col) as col19, max(a.no20_col) as col20
, max(a.no21_col) as col21, max(a.no22_col) as col22, max(a.no23_col) as col23, max(a.no24_col) as col24, max(a.no25_col) as col25, max(a.no26_col) as col26, max(a.no27_col) as col27, max(a.no28_col) as col28, max(a.no29_col) as col29, max(a.no30_col) as col30
, max(a.no31_col) as col31, max(a.no32_col) as col32, max(a.no33_col) as col33, max(a.no34_col) as col34, max(a.no35_col) as col35, max(a.no36_col) as col36, max(a.no37_col) as col37, max(a.no38_col) as col38, max(a.no39_col) as col39, max(a.no40_col) as col40
, max(a.no41_col) as col41, max(a.no42_col) as col42, max(a.no43_col) as col43, max(a.no44_col) as col44, max(a.no45_col) as col45, max(a.no46_col) as col46, max(a.no47_col) as col47, max(a.no48_col) as col48, max(a.no49_col) as col49, max(a.no50_col) as col50
, max(a.no51_col) as col51, max(a.no52_col) as col52, max(a.no53_col) as col53, max(a.no54_col) as col54, max(a.no55_col) as col55, max(a.no56_col) as col56, max(a.no57_col) as col57, max(a.no58_col) as col58, max(a.no59_col) as col59, max(a.no60_col) as col60
, max(a.no61_col) as col61, max(a.no62_col) as col62, max(a.no63_col) as col63, max(a.no64_col) as col64, max(a.no65_col) as col65, max(a.no66_col) as col66, max(a.no67_col) as col67, max(a.no68_col) as col68, max(a.no69_col) as col69, max(a.no70_col) as col70
, max(a.no71_col) as col71, max(a.no72_col) as col72, max(a.no73_col) as col73, max(a.no74_col) as col74, max(a.no75_col) as col75, max(a.no76_col) as col76, max(a.no77_col) as col77, max(a.no78_col) as col78, max(a.no79_col) as col79, max(a.no80_col) as col80
, max(a.no81_col) as col81, max(a.no82_col) as col82, max(a.no83_col) as col83, max(a.no84_col) as col84, max(a.no85_col) as col85, max(a.no86_col) as col86, max(a.no87_col) as col87, max(a.no88_col) as col88, max(a.no89_col) as col89, max(a.no90_col) as col90
, max(a.no91_col) as col91, max(a.no92_col) as col92, max(a.no93_col) as col93, max(a.no94_col) as col94, max(a.no95_col) as col95, max(a.no96_col) as col96, max(a.no97_col) as col97, max(a.no98_col) as col98, max(a.no99_col) as col99, max(a.no100_col) as col100
, max(a.no101_col) as col101, max(a.no102_col) as col102, max(a.no103_col) as col103, max(a.no104_col) as col104, max(a.no105_col) as col105, max(a.no106_col) as col106, max(a.no107_col) as col107, max(a.no108_col) as col108, max(a.no109_col) as col109, max(a.no110_col) as col110
, max(a.no111_col) as col111, max(a.no112_col) as col112, max(a.no113_col) as col113, max(a.no114_col) as col114, max(a.no115_col) as col115, max(a.no116_col) as col116, max(a.no117_col) as col117, max(a.no118_col) as col118, max(a.no119_col) as col119, max(a.no120_col) as col120
, max(a.no121_col) as col121, max(a.no122_col) as col122, max(a.no123_col) as col123, max(a.no124_col) as col124, max(a.no125_col) as col125, max(a.no126_col) as col126, max(a.no127_col) as col127, max(a.no128_col) as col128, max(a.no129_col) as col129, max(a.no130_col) as col130
, max(a.no131_col) as col131, max(a.no132_col) as col132, max(a.no133_col) as col133, max(a.no134_col) as col134, max(a.no135_col) as col135, max(a.no136_col) as col136, max(a.no137_col) as col137, max(a.no138_col) as col138, max(a.no139_col) as col139, max(a.no140_col) as col140
, max(a.no141_col) as col141, max(a.no142_col) as col142, max(a.no143_col) as col143, max(a.no144_col) as col144, max(a.no145_col) as col145, max(a.no146_col) as col146, max(a.no147_col) as col147, max(a.no148_col) as col148, max(a.no149_col) as col149, max(a.no150_col) as col150

from (
select *
from (
select a.master_id, a.master_ver, to_char(a.SEARCH_COND_LOC) as col
        , row_number() over (partition by a.master_id, a.master_ver order by column_seq) as no
from TN_AD_MASTER_COLUMN a
)
pivot (max(col) col for no
   in (1 as no1, 2 as no2, 3 as no3, 4 as no4, 5 as no5, 6 as no6, 7 as no7, 8 as no8, 9 as no9, 10 as no10
       ,11 as no11, 12 as no12, 13 as no13, 14 as no14, 15 as no15, 16 as no16, 17 as no17, 18 as no18, 19 as no19, 20 as no20
   ,21 as no21, 22 as no22, 23 as no23, 24 as no24, 25 as no25, 26 as no26, 27 as no27, 28 as no28, 29 as no29, 30 as no30
   ,31 as no31, 32 as no32, 33 as no33, 34 as no34, 35 as no35, 36 as no36, 37 as no37, 38 as no38, 39 as no39, 40 as no40
   ,41 as no41, 42 as no42, 43 as no43, 44 as no44, 45 as no45, 46 as no46, 47 as no47, 48 as no48, 49 as no49, 50 as no50
   ,51 as no51, 52 as no52, 53 as no53, 54 as no54, 55 as no55, 56 as no56, 57 as no57, 58 as no58, 59 as no59, 60 as no60
   ,61 as no61, 62 as no62, 63 as no63, 64 as no64, 65 as no65, 66 as no66, 67 as no67, 68 as no68, 69 as no69, 70 as no70
   ,71 as no71, 72 as no72, 73 as no73, 74 as no74, 75 as no75, 76 as no76, 77 as no77, 78 as no78, 79 as no79, 80 as no80
   ,81 as no81, 82 as no82, 83 as no83, 84 as no84, 85 as no85, 86 as no86, 87 as no87, 88 as no88, 89 as no89, 90 as no90
   ,91 as no91, 92 as no92, 93 as no93, 94 as no94, 95 as no95, 96 as no96, 97 as no97, 98 as no98, 99 as no99, 100 as no100
   ,101 as no101, 102 as no102, 103 as no103, 104 as no104, 105 as no105, 106 as no106, 107 as no107, 108 as no108, 109 as no109, 110 as no110
   ,111 as no111, 112 as no112, 113 as no113, 114 as no114, 115 as no115, 116 as no116, 117 as no117, 118 as no118, 119 as no119, 120 as no120
   ,121 as no121, 122 as no122, 123 as no123, 124 as no124, 125 as no125, 126 as no126, 127 as no127, 128 as no128, 129 as no129, 130 as no130
   ,131 as no131, 132 as no132, 133 as no133, 134 as no134, 135 as no135, 136 as no136, 137 as no137, 138 as no138, 139 as no139, 140 as no140
   ,141 as no141, 142 as no142, 143 as no143, 144 as no144, 145 as no145, 146 as no146, 147 as no147, 148 as no148, 149 as no149, 150 as no150
   )
)
) a
group by a.master_id, a.master_ver

union all

select a.master_id, a.master_ver, 10 as no,  'SEARCH_YNE' as gb
, max(a.no1_col) as col01, max(a.no2_col) as col02, max(a.no3_col) as col03, max(a.no4_col) as col04, max(a.no5_col) as col05, max(a.no6_col) as col06, max(a.no7_col) as col07, max(a.no8_col) as col08, max(a.no9_col) as col09, max(a.no10_col) as col10
, max(a.no11_col) as col11, max(a.no12_col) as col12, max(a.no13_col) as col13, max(a.no14_col) as col14, max(a.no15_col) as col15, max(a.no16_col) as col16, max(a.no17_col) as col17, max(a.no18_col) as col18, max(a.no19_col) as col19, max(a.no20_col) as col20
, max(a.no21_col) as col21, max(a.no22_col) as col22, max(a.no23_col) as col23, max(a.no24_col) as col24, max(a.no25_col) as col25, max(a.no26_col) as col26, max(a.no27_col) as col27, max(a.no28_col) as col28, max(a.no29_col) as col29, max(a.no30_col) as col30
, max(a.no31_col) as col31, max(a.no32_col) as col32, max(a.no33_col) as col33, max(a.no34_col) as col34, max(a.no35_col) as col35, max(a.no36_col) as col36, max(a.no37_col) as col37, max(a.no38_col) as col38, max(a.no39_col) as col39, max(a.no40_col) as col40
, max(a.no41_col) as col41, max(a.no42_col) as col42, max(a.no43_col) as col43, max(a.no44_col) as col44, max(a.no45_col) as col45, max(a.no46_col) as col46, max(a.no47_col) as col47, max(a.no48_col) as col48, max(a.no49_col) as col49, max(a.no50_col) as col50
, max(a.no51_col) as col51, max(a.no52_col) as col52, max(a.no53_col) as col53, max(a.no54_col) as col54, max(a.no55_col) as col55, max(a.no56_col) as col56, max(a.no57_col) as col57, max(a.no58_col) as col58, max(a.no59_col) as col59, max(a.no60_col) as col60
, max(a.no61_col) as col61, max(a.no62_col) as col62, max(a.no63_col) as col63, max(a.no64_col) as col64, max(a.no65_col) as col65, max(a.no66_col) as col66, max(a.no67_col) as col67, max(a.no68_col) as col68, max(a.no69_col) as col69, max(a.no70_col) as col70
, max(a.no71_col) as col71, max(a.no72_col) as col72, max(a.no73_col) as col73, max(a.no74_col) as col74, max(a.no75_col) as col75, max(a.no76_col) as col76, max(a.no77_col) as col77, max(a.no78_col) as col78, max(a.no79_col) as col79, max(a.no80_col) as col80
, max(a.no81_col) as col81, max(a.no82_col) as col82, max(a.no83_col) as col83, max(a.no84_col) as col84, max(a.no85_col) as col85, max(a.no86_col) as col86, max(a.no87_col) as col87, max(a.no88_col) as col88, max(a.no89_col) as col89, max(a.no90_col) as col90
, max(a.no91_col) as col91, max(a.no92_col) as col92, max(a.no93_col) as col93, max(a.no94_col) as col94, max(a.no95_col) as col95, max(a.no96_col) as col96, max(a.no97_col) as col97, max(a.no98_col) as col98, max(a.no99_col) as col99, max(a.no100_col) as col100
, max(a.no101_col) as col101, max(a.no102_col) as col102, max(a.no103_col) as col103, max(a.no104_col) as col104, max(a.no105_col) as col105, max(a.no106_col) as col106, max(a.no107_col) as col107, max(a.no108_col) as col108, max(a.no109_col) as col109, max(a.no110_col) as col110
, max(a.no111_col) as col111, max(a.no112_col) as col112, max(a.no113_col) as col113, max(a.no114_col) as col114, max(a.no115_col) as col115, max(a.no116_col) as col116, max(a.no117_col) as col117, max(a.no118_col) as col118, max(a.no119_col) as col119, max(a.no120_col) as col120
, max(a.no121_col) as col121, max(a.no122_col) as col122, max(a.no123_col) as col123, max(a.no124_col) as col124, max(a.no125_col) as col125, max(a.no126_col) as col126, max(a.no127_col) as col127, max(a.no128_col) as col128, max(a.no129_col) as col129, max(a.no130_col) as col130
, max(a.no131_col) as col131, max(a.no132_col) as col132, max(a.no133_col) as col133, max(a.no134_col) as col134, max(a.no135_col) as col135, max(a.no136_col) as col136, max(a.no137_col) as col137, max(a.no138_col) as col138, max(a.no139_col) as col139, max(a.no140_col) as col140
, max(a.no141_col) as col141, max(a.no142_col) as col142, max(a.no143_col) as col143, max(a.no144_col) as col144, max(a.no145_col) as col145, max(a.no146_col) as col146, max(a.no147_col) as col147, max(a.no148_col) as col148, max(a.no149_col) as col149, max(a.no150_col) as col150

from (
select *
from (
select a.master_id, a.master_ver, to_char(a.SEARCH_YNE) as col
        , row_number() over (partition by a.master_id, a.master_ver order by column_seq) as no
from TN_AD_MASTER_COLUMN a
)
pivot (max(col) col for no
   in (1 as no1, 2 as no2, 3 as no3, 4 as no4, 5 as no5, 6 as no6, 7 as no7, 8 as no8, 9 as no9, 10 as no10
       ,11 as no11, 12 as no12, 13 as no13, 14 as no14, 15 as no15, 16 as no16, 17 as no17, 18 as no18, 19 as no19, 20 as no20
   ,21 as no21, 22 as no22, 23 as no23, 24 as no24, 25 as no25, 26 as no26, 27 as no27, 28 as no28, 29 as no29, 30 as no30
   ,31 as no31, 32 as no32, 33 as no33, 34 as no34, 35 as no35, 36 as no36, 37 as no37, 38 as no38, 39 as no39, 40 as no40
   ,41 as no41, 42 as no42, 43 as no43, 44 as no44, 45 as no45, 46 as no46, 47 as no47, 48 as no48, 49 as no49, 50 as no50
   ,51 as no51, 52 as no52, 53 as no53, 54 as no54, 55 as no55, 56 as no56, 57 as no57, 58 as no58, 59 as no59, 60 as no60
   ,61 as no61, 62 as no62, 63 as no63, 64 as no64, 65 as no65, 66 as no66, 67 as no67, 68 as no68, 69 as no69, 70 as no70
   ,71 as no71, 72 as no72, 73 as no73, 74 as no74, 75 as no75, 76 as no76, 77 as no77, 78 as no78, 79 as no79, 80 as no80
   ,81 as no81, 82 as no82, 83 as no83, 84 as no84, 85 as no85, 86 as no86, 87 as no87, 88 as no88, 89 as no89, 90 as no90
   ,91 as no91, 92 as no92, 93 as no93, 94 as no94, 95 as no95, 96 as no96, 97 as no97, 98 as no98, 99 as no99, 100 as no100
   ,101 as no101, 102 as no102, 103 as no103, 104 as no104, 105 as no105, 106 as no106, 107 as no107, 108 as no108, 109 as no109, 110 as no110
   ,111 as no111, 112 as no112, 113 as no113, 114 as no114, 115 as no115, 116 as no116, 117 as no117, 118 as no118, 119 as no119, 120 as no120
   ,121 as no121, 122 as no122, 123 as no123, 124 as no124, 125 as no125, 126 as no126, 127 as no127, 128 as no128, 129 as no129, 130 as no130
   ,131 as no131, 132 as no132, 133 as no133, 134 as no134, 135 as no135, 136 as no136, 137 as no137, 138 as no138, 139 as no139, 140 as no140
   ,141 as no141, 142 as no142, 143 as no143, 144 as no144, 145 as no145, 146 as no146, 147 as no147, 148 as no148, 149 as no149, 150 as no150
   )
)
) a
group by a.master_id, a.master_ver

union all

select a.master_id, a.master_ver, 11 as no,  'SEARCH_COND_UI' as gb
, max(a.no1_col) as col01, max(a.no2_col) as col02, max(a.no3_col) as col03, max(a.no4_col) as col04, max(a.no5_col) as col05, max(a.no6_col) as col06, max(a.no7_col) as col07, max(a.no8_col) as col08, max(a.no9_col) as col09, max(a.no10_col) as col10
, max(a.no11_col) as col11, max(a.no12_col) as col12, max(a.no13_col) as col13, max(a.no14_col) as col14, max(a.no15_col) as col15, max(a.no16_col) as col16, max(a.no17_col) as col17, max(a.no18_col) as col18, max(a.no19_col) as col19, max(a.no20_col) as col20
, max(a.no21_col) as col21, max(a.no22_col) as col22, max(a.no23_col) as col23, max(a.no24_col) as col24, max(a.no25_col) as col25, max(a.no26_col) as col26, max(a.no27_col) as col27, max(a.no28_col) as col28, max(a.no29_col) as col29, max(a.no30_col) as col30
, max(a.no31_col) as col31, max(a.no32_col) as col32, max(a.no33_col) as col33, max(a.no34_col) as col34, max(a.no35_col) as col35, max(a.no36_col) as col36, max(a.no37_col) as col37, max(a.no38_col) as col38, max(a.no39_col) as col39, max(a.no40_col) as col40
, max(a.no41_col) as col41, max(a.no42_col) as col42, max(a.no43_col) as col43, max(a.no44_col) as col44, max(a.no45_col) as col45, max(a.no46_col) as col46, max(a.no47_col) as col47, max(a.no48_col) as col48, max(a.no49_col) as col49, max(a.no50_col) as col50
, max(a.no51_col) as col51, max(a.no52_col) as col52, max(a.no53_col) as col53, max(a.no54_col) as col54, max(a.no55_col) as col55, max(a.no56_col) as col56, max(a.no57_col) as col57, max(a.no58_col) as col58, max(a.no59_col) as col59, max(a.no60_col) as col60
, max(a.no61_col) as col61, max(a.no62_col) as col62, max(a.no63_col) as col63, max(a.no64_col) as col64, max(a.no65_col) as col65, max(a.no66_col) as col66, max(a.no67_col) as col67, max(a.no68_col) as col68, max(a.no69_col) as col69, max(a.no70_col) as col70
, max(a.no71_col) as col71, max(a.no72_col) as col72, max(a.no73_col) as col73, max(a.no74_col) as col74, max(a.no75_col) as col75, max(a.no76_col) as col76, max(a.no77_col) as col77, max(a.no78_col) as col78, max(a.no79_col) as col79, max(a.no80_col) as col80
, max(a.no81_col) as col81, max(a.no82_col) as col82, max(a.no83_col) as col83, max(a.no84_col) as col84, max(a.no85_col) as col85, max(a.no86_col) as col86, max(a.no87_col) as col87, max(a.no88_col) as col88, max(a.no89_col) as col89, max(a.no90_col) as col90
, max(a.no91_col) as col91, max(a.no92_col) as col92, max(a.no93_col) as col93, max(a.no94_col) as col94, max(a.no95_col) as col95, max(a.no96_col) as col96, max(a.no97_col) as col97, max(a.no98_col) as col98, max(a.no99_col) as col99, max(a.no100_col) as col100
, max(a.no101_col) as col101, max(a.no102_col) as col102, max(a.no103_col) as col103, max(a.no104_col) as col104, max(a.no105_col) as col105, max(a.no106_col) as col106, max(a.no107_col) as col107, max(a.no108_col) as col108, max(a.no109_col) as col109, max(a.no110_col) as col110
, max(a.no111_col) as col111, max(a.no112_col) as col112, max(a.no113_col) as col113, max(a.no114_col) as col114, max(a.no115_col) as col115, max(a.no116_col) as col116, max(a.no117_col) as col117, max(a.no118_col) as col118, max(a.no119_col) as col119, max(a.no120_col) as col120
, max(a.no121_col) as col121, max(a.no122_col) as col122, max(a.no123_col) as col123, max(a.no124_col) as col124, max(a.no125_col) as col125, max(a.no126_col) as col126, max(a.no127_col) as col127, max(a.no128_col) as col128, max(a.no129_col) as col129, max(a.no130_col) as col130
, max(a.no131_col) as col131, max(a.no132_col) as col132, max(a.no133_col) as col133, max(a.no134_col) as col134, max(a.no135_col) as col135, max(a.no136_col) as col136, max(a.no137_col) as col137, max(a.no138_col) as col138, max(a.no139_col) as col139, max(a.no140_col) as col140
, max(a.no141_col) as col141, max(a.no142_col) as col142, max(a.no143_col) as col143, max(a.no144_col) as col144, max(a.no145_col) as col145, max(a.no146_col) as col146, max(a.no147_col) as col147, max(a.no148_col) as col148, max(a.no149_col) as col149, max(a.no150_col) as col150

from (
select *
from (
select a.master_id, a.master_ver, to_char(a.SEARCH_COND_UI) as col
        , row_number() over (partition by a.master_id, a.master_ver order by column_seq) as no
from TN_AD_MASTER_COLUMN a
)
pivot (max(col) col for no
   in (1 as no1, 2 as no2, 3 as no3, 4 as no4, 5 as no5, 6 as no6, 7 as no7, 8 as no8, 9 as no9, 10 as no10
       ,11 as no11, 12 as no12, 13 as no13, 14 as no14, 15 as no15, 16 as no16, 17 as no17, 18 as no18, 19 as no19, 20 as no20
   ,21 as no21, 22 as no22, 23 as no23, 24 as no24, 25 as no25, 26 as no26, 27 as no27, 28 as no28, 29 as no29, 30 as no30
   ,31 as no31, 32 as no32, 33 as no33, 34 as no34, 35 as no35, 36 as no36, 37 as no37, 38 as no38, 39 as no39, 40 as no40
   ,41 as no41, 42 as no42, 43 as no43, 44 as no44, 45 as no45, 46 as no46, 47 as no47, 48 as no48, 49 as no49, 50 as no50
   ,51 as no51, 52 as no52, 53 as no53, 54 as no54, 55 as no55, 56 as no56, 57 as no57, 58 as no58, 59 as no59, 60 as no60
   ,61 as no61, 62 as no62, 63 as no63, 64 as no64, 65 as no65, 66 as no66, 67 as no67, 68 as no68, 69 as no69, 70 as no70
   ,71 as no71, 72 as no72, 73 as no73, 74 as no74, 75 as no75, 76 as no76, 77 as no77, 78 as no78, 79 as no79, 80 as no80
   ,81 as no81, 82 as no82, 83 as no83, 84 as no84, 85 as no85, 86 as no86, 87 as no87, 88 as no88, 89 as no89, 90 as no90
   ,91 as no91, 92 as no92, 93 as no93, 94 as no94, 95 as no95, 96 as no96, 97 as no97, 98 as no98, 99 as no99, 100 as no100
   ,101 as no101, 102 as no102, 103 as no103, 104 as no104, 105 as no105, 106 as no106, 107 as no107, 108 as no108, 109 as no109, 110 as no110
   ,111 as no111, 112 as no112, 113 as no113, 114 as no114, 115 as no115, 116 as no116, 117 as no117, 118 as no118, 119 as no119, 120 as no120
   ,121 as no121, 122 as no122, 123 as no123, 124 as no124, 125 as no125, 126 as no126, 127 as no127, 128 as no128, 129 as no129, 130 as no130
   ,131 as no131, 132 as no132, 133 as no133, 134 as no134, 135 as no135, 136 as no136, 137 as no137, 138 as no138, 139 as no139, 140 as no140
   ,141 as no141, 142 as no142, 143 as no143, 144 as no144, 145 as no145, 146 as no146, 147 as no147, 148 as no148, 149 as no149, 150 as no150
   )
)
) a
group by a.master_id, a.master_ver

union all

select a.master_id, a.master_ver, 12 as no, 'SEARCH_COND_CODE' as gb
, max(a.no1_col) as col01, max(a.no2_col) as col02, max(a.no3_col) as col03, max(a.no4_col) as col04, max(a.no5_col) as col05, max(a.no6_col) as col06, max(a.no7_col) as col07, max(a.no8_col) as col08, max(a.no9_col) as col09, max(a.no10_col) as col10
, max(a.no11_col) as col11, max(a.no12_col) as col12, max(a.no13_col) as col13, max(a.no14_col) as col14, max(a.no15_col) as col15, max(a.no16_col) as col16, max(a.no17_col) as col17, max(a.no18_col) as col18, max(a.no19_col) as col19, max(a.no20_col) as col20
, max(a.no21_col) as col21, max(a.no22_col) as col22, max(a.no23_col) as col23, max(a.no24_col) as col24, max(a.no25_col) as col25, max(a.no26_col) as col26, max(a.no27_col) as col27, max(a.no28_col) as col28, max(a.no29_col) as col29, max(a.no30_col) as col30
, max(a.no31_col) as col31, max(a.no32_col) as col32, max(a.no33_col) as col33, max(a.no34_col) as col34, max(a.no35_col) as col35, max(a.no36_col) as col36, max(a.no37_col) as col37, max(a.no38_col) as col38, max(a.no39_col) as col39, max(a.no40_col) as col40
, max(a.no41_col) as col41, max(a.no42_col) as col42, max(a.no43_col) as col43, max(a.no44_col) as col44, max(a.no45_col) as col45, max(a.no46_col) as col46, max(a.no47_col) as col47, max(a.no48_col) as col48, max(a.no49_col) as col49, max(a.no50_col) as col50
, max(a.no51_col) as col51, max(a.no52_col) as col52, max(a.no53_col) as col53, max(a.no54_col) as col54, max(a.no55_col) as col55, max(a.no56_col) as col56, max(a.no57_col) as col57, max(a.no58_col) as col58, max(a.no59_col) as col59, max(a.no60_col) as col60
, max(a.no61_col) as col61, max(a.no62_col) as col62, max(a.no63_col) as col63, max(a.no64_col) as col64, max(a.no65_col) as col65, max(a.no66_col) as col66, max(a.no67_col) as col67, max(a.no68_col) as col68, max(a.no69_col) as col69, max(a.no70_col) as col70
, max(a.no71_col) as col71, max(a.no72_col) as col72, max(a.no73_col) as col73, max(a.no74_col) as col74, max(a.no75_col) as col75, max(a.no76_col) as col76, max(a.no77_col) as col77, max(a.no78_col) as col78, max(a.no79_col) as col79, max(a.no80_col) as col80
, max(a.no81_col) as col81, max(a.no82_col) as col82, max(a.no83_col) as col83, max(a.no84_col) as col84, max(a.no85_col) as col85, max(a.no86_col) as col86, max(a.no87_col) as col87, max(a.no88_col) as col88, max(a.no89_col) as col89, max(a.no90_col) as col90
, max(a.no91_col) as col91, max(a.no92_col) as col92, max(a.no93_col) as col93, max(a.no94_col) as col94, max(a.no95_col) as col95, max(a.no96_col) as col96, max(a.no97_col) as col97, max(a.no98_col) as col98, max(a.no99_col) as col99, max(a.no100_col) as col100
, max(a.no101_col) as col101, max(a.no102_col) as col102, max(a.no103_col) as col103, max(a.no104_col) as col104, max(a.no105_col) as col105, max(a.no106_col) as col106, max(a.no107_col) as col107, max(a.no108_col) as col108, max(a.no109_col) as col109, max(a.no110_col) as col110
, max(a.no111_col) as col111, max(a.no112_col) as col112, max(a.no113_col) as col113, max(a.no114_col) as col114, max(a.no115_col) as col115, max(a.no116_col) as col116, max(a.no117_col) as col117, max(a.no118_col) as col118, max(a.no119_col) as col119, max(a.no120_col) as col120
, max(a.no121_col) as col121, max(a.no122_col) as col122, max(a.no123_col) as col123, max(a.no124_col) as col124, max(a.no125_col) as col125, max(a.no126_col) as col126, max(a.no127_col) as col127, max(a.no128_col) as col128, max(a.no129_col) as col129, max(a.no130_col) as col130
, max(a.no131_col) as col131, max(a.no132_col) as col132, max(a.no133_col) as col133, max(a.no134_col) as col134, max(a.no135_col) as col135, max(a.no136_col) as col136, max(a.no137_col) as col137, max(a.no138_col) as col138, max(a.no139_col) as col139, max(a.no140_col) as col140
, max(a.no141_col) as col141, max(a.no142_col) as col142, max(a.no143_col) as col143, max(a.no144_col) as col144, max(a.no145_col) as col145, max(a.no146_col) as col146, max(a.no147_col) as col147, max(a.no148_col) as col148, max(a.no149_col) as col149, max(a.no150_col) as col150

from (
select *
from (
select a.master_id, a.master_ver, to_char(a.SEARCH_COND_CODE) as col
        , row_number() over (partition by a.master_id, a.master_ver order by column_seq) as no
from TN_AD_MASTER_COLUMN a
)
pivot (max(col) col for no
   in (1 as no1, 2 as no2, 3 as no3, 4 as no4, 5 as no5, 6 as no6, 7 as no7, 8 as no8, 9 as no9, 10 as no10
       ,11 as no11, 12 as no12, 13 as no13, 14 as no14, 15 as no15, 16 as no16, 17 as no17, 18 as no18, 19 as no19, 20 as no20
   ,21 as no21, 22 as no22, 23 as no23, 24 as no24, 25 as no25, 26 as no26, 27 as no27, 28 as no28, 29 as no29, 30 as no30
   ,31 as no31, 32 as no32, 33 as no33, 34 as no34, 35 as no35, 36 as no36, 37 as no37, 38 as no38, 39 as no39, 40 as no40
   ,41 as no41, 42 as no42, 43 as no43, 44 as no44, 45 as no45, 46 as no46, 47 as no47, 48 as no48, 49 as no49, 50 as no50
   ,51 as no51, 52 as no52, 53 as no53, 54 as no54, 55 as no55, 56 as no56, 57 as no57, 58 as no58, 59 as no59, 60 as no60
   ,61 as no61, 62 as no62, 63 as no63, 64 as no64, 65 as no65, 66 as no66, 67 as no67, 68 as no68, 69 as no69, 70 as no70
   ,71 as no71, 72 as no72, 73 as no73, 74 as no74, 75 as no75, 76 as no76, 77 as no77, 78 as no78, 79 as no79, 80 as no80
   ,81 as no81, 82 as no82, 83 as no83, 84 as no84, 85 as no85, 86 as no86, 87 as no87, 88 as no88, 89 as no89, 90 as no90
   ,91 as no91, 92 as no92, 93 as no93, 94 as no94, 95 as no95, 96 as no96, 97 as no97, 98 as no98, 99 as no99, 100 as no100
   ,101 as no101, 102 as no102, 103 as no103, 104 as no104, 105 as no105, 106 as no106, 107 as no107, 108 as no108, 109 as no109, 110 as no110
   ,111 as no111, 112 as no112, 113 as no113, 114 as no114, 115 as no115, 116 as no116, 117 as no117, 118 as no118, 119 as no119, 120 as no120
   ,121 as no121, 122 as no122, 123 as no123, 124 as no124, 125 as no125, 126 as no126, 127 as no127, 128 as no128, 129 as no129, 130 as no130
   ,131 as no131, 132 as no132, 133 as no133, 134 as no134, 135 as no135, 136 as no136, 137 as no137, 138 as no138, 139 as no139, 140 as no140
   ,141 as no141, 142 as no142, 143 as no143, 144 as no144, 145 as no145, 146 as no146, 147 as no147, 148 as no148, 149 as no149, 150 as no150
   )
)
) a
group by a.master_id, a.master_ver


union all

select a.master_id, a.master_ver, 13 as no,  'COLUMN_ALIGN' as gb
, max(a.no1_col) as col01, max(a.no2_col) as col02, max(a.no3_col) as col03, max(a.no4_col) as col04, max(a.no5_col) as col05, max(a.no6_col) as col06, max(a.no7_col) as col07, max(a.no8_col) as col08, max(a.no9_col) as col09, max(a.no10_col) as col10
, max(a.no11_col) as col11, max(a.no12_col) as col12, max(a.no13_col) as col13, max(a.no14_col) as col14, max(a.no15_col) as col15, max(a.no16_col) as col16, max(a.no17_col) as col17, max(a.no18_col) as col18, max(a.no19_col) as col19, max(a.no20_col) as col20
, max(a.no21_col) as col21, max(a.no22_col) as col22, max(a.no23_col) as col23, max(a.no24_col) as col24, max(a.no25_col) as col25, max(a.no26_col) as col26, max(a.no27_col) as col27, max(a.no28_col) as col28, max(a.no29_col) as col29, max(a.no30_col) as col30
, max(a.no31_col) as col31, max(a.no32_col) as col32, max(a.no33_col) as col33, max(a.no34_col) as col34, max(a.no35_col) as col35, max(a.no36_col) as col36, max(a.no37_col) as col37, max(a.no38_col) as col38, max(a.no39_col) as col39, max(a.no40_col) as col40
, max(a.no41_col) as col41, max(a.no42_col) as col42, max(a.no43_col) as col43, max(a.no44_col) as col44, max(a.no45_col) as col45, max(a.no46_col) as col46, max(a.no47_col) as col47, max(a.no48_col) as col48, max(a.no49_col) as col49, max(a.no50_col) as col50
, max(a.no51_col) as col51, max(a.no52_col) as col52, max(a.no53_col) as col53, max(a.no54_col) as col54, max(a.no55_col) as col55, max(a.no56_col) as col56, max(a.no57_col) as col57, max(a.no58_col) as col58, max(a.no59_col) as col59, max(a.no60_col) as col60
, max(a.no61_col) as col61, max(a.no62_col) as col62, max(a.no63_col) as col63, max(a.no64_col) as col64, max(a.no65_col) as col65, max(a.no66_col) as col66, max(a.no67_col) as col67, max(a.no68_col) as col68, max(a.no69_col) as col69, max(a.no70_col) as col70
, max(a.no71_col) as col71, max(a.no72_col) as col72, max(a.no73_col) as col73, max(a.no74_col) as col74, max(a.no75_col) as col75, max(a.no76_col) as col76, max(a.no77_col) as col77, max(a.no78_col) as col78, max(a.no79_col) as col79, max(a.no80_col) as col80
, max(a.no81_col) as col81, max(a.no82_col) as col82, max(a.no83_col) as col83, max(a.no84_col) as col84, max(a.no85_col) as col85, max(a.no86_col) as col86, max(a.no87_col) as col87, max(a.no88_col) as col88, max(a.no89_col) as col89, max(a.no90_col) as col90
, max(a.no91_col) as col91, max(a.no92_col) as col92, max(a.no93_col) as col93, max(a.no94_col) as col94, max(a.no95_col) as col95, max(a.no96_col) as col96, max(a.no97_col) as col97, max(a.no98_col) as col98, max(a.no99_col) as col99, max(a.no100_col) as col100
, max(a.no101_col) as col101, max(a.no102_col) as col102, max(a.no103_col) as col103, max(a.no104_col) as col104, max(a.no105_col) as col105, max(a.no106_col) as col106, max(a.no107_col) as col107, max(a.no108_col) as col108, max(a.no109_col) as col109, max(a.no110_col) as col110
, max(a.no111_col) as col111, max(a.no112_col) as col112, max(a.no113_col) as col113, max(a.no114_col) as col114, max(a.no115_col) as col115, max(a.no116_col) as col116, max(a.no117_col) as col117, max(a.no118_col) as col118, max(a.no119_col) as col119, max(a.no120_col) as col120
, max(a.no121_col) as col121, max(a.no122_col) as col122, max(a.no123_col) as col123, max(a.no124_col) as col124, max(a.no125_col) as col125, max(a.no126_col) as col126, max(a.no127_col) as col127, max(a.no128_col) as col128, max(a.no129_col) as col129, max(a.no130_col) as col130
, max(a.no131_col) as col131, max(a.no132_col) as col132, max(a.no133_col) as col133, max(a.no134_col) as col134, max(a.no135_col) as col135, max(a.no136_col) as col136, max(a.no137_col) as col137, max(a.no138_col) as col138, max(a.no139_col) as col139, max(a.no140_col) as col140
, max(a.no141_col) as col141, max(a.no142_col) as col142, max(a.no143_col) as col143, max(a.no144_col) as col144, max(a.no145_col) as col145, max(a.no146_col) as col146, max(a.no147_col) as col147, max(a.no148_col) as col148, max(a.no149_col) as col149, max(a.no150_col) as col150

from (
select *
from (
select a.master_id, a.master_ver, to_char(a.COLUMN_ALIGN) as col
        , row_number() over (partition by a.master_id, a.master_ver order by column_seq) as no
from TN_AD_MASTER_COLUMN a
)
pivot (max(col) col for no
   in (1 as no1, 2 as no2, 3 as no3, 4 as no4, 5 as no5, 6 as no6, 7 as no7, 8 as no8, 9 as no9, 10 as no10
       ,11 as no11, 12 as no12, 13 as no13, 14 as no14, 15 as no15, 16 as no16, 17 as no17, 18 as no18, 19 as no19, 20 as no20
   ,21 as no21, 22 as no22, 23 as no23, 24 as no24, 25 as no25, 26 as no26, 27 as no27, 28 as no28, 29 as no29, 30 as no30
   ,31 as no31, 32 as no32, 33 as no33, 34 as no34, 35 as no35, 36 as no36, 37 as no37, 38 as no38, 39 as no39, 40 as no40
   ,41 as no41, 42 as no42, 43 as no43, 44 as no44, 45 as no45, 46 as no46, 47 as no47, 48 as no48, 49 as no49, 50 as no50
   ,51 as no51, 52 as no52, 53 as no53, 54 as no54, 55 as no55, 56 as no56, 57 as no57, 58 as no58, 59 as no59, 60 as no60
   ,61 as no61, 62 as no62, 63 as no63, 64 as no64, 65 as no65, 66 as no66, 67 as no67, 68 as no68, 69 as no69, 70 as no70
   ,71 as no71, 72 as no72, 73 as no73, 74 as no74, 75 as no75, 76 as no76, 77 as no77, 78 as no78, 79 as no79, 80 as no80
   ,81 as no81, 82 as no82, 83 as no83, 84 as no84, 85 as no85, 86 as no86, 87 as no87, 88 as no88, 89 as no89, 90 as no90
   ,91 as no91, 92 as no92, 93 as no93, 94 as no94, 95 as no95, 96 as no96, 97 as no97, 98 as no98, 99 as no99, 100 as no100
   ,101 as no101, 102 as no102, 103 as no103, 104 as no104, 105 as no105, 106 as no106, 107 as no107, 108 as no108, 109 as no109, 110 as no110
   ,111 as no111, 112 as no112, 113 as no113, 114 as no114, 115 as no115, 116 as no116, 117 as no117, 118 as no118, 119 as no119, 120 as no120
   ,121 as no121, 122 as no122, 123 as no123, 124 as no124, 125 as no125, 126 as no126, 127 as no127, 128 as no128, 129 as no129, 130 as no130
   ,131 as no131, 132 as no132, 133 as no133, 134 as no134, 135 as no135, 136 as no136, 137 as no137, 138 as no138, 139 as no139, 140 as no140
   ,141 as no141, 142 as no142, 143 as no143, 144 as no144, 145 as no145, 146 as no146, 147 as no147, 148 as no148, 149 as no149, 150 as no150
   )
)
) a
group by a.master_id, a.master_ver

union all

select a.master_id, a.master_ver, 14 as no,  'COLUMN_HIDDEN_YN' as gb
, max(a.no1_col) as col01, max(a.no2_col) as col02, max(a.no3_col) as col03, max(a.no4_col) as col04, max(a.no5_col) as col05, max(a.no6_col) as col06, max(a.no7_col) as col07, max(a.no8_col) as col08, max(a.no9_col) as col09, max(a.no10_col) as col10
, max(a.no11_col) as col11, max(a.no12_col) as col12, max(a.no13_col) as col13, max(a.no14_col) as col14, max(a.no15_col) as col15, max(a.no16_col) as col16, max(a.no17_col) as col17, max(a.no18_col) as col18, max(a.no19_col) as col19, max(a.no20_col) as col20
, max(a.no21_col) as col21, max(a.no22_col) as col22, max(a.no23_col) as col23, max(a.no24_col) as col24, max(a.no25_col) as col25, max(a.no26_col) as col26, max(a.no27_col) as col27, max(a.no28_col) as col28, max(a.no29_col) as col29, max(a.no30_col) as col30
, max(a.no31_col) as col31, max(a.no32_col) as col32, max(a.no33_col) as col33, max(a.no34_col) as col34, max(a.no35_col) as col35, max(a.no36_col) as col36, max(a.no37_col) as col37, max(a.no38_col) as col38, max(a.no39_col) as col39, max(a.no40_col) as col40
, max(a.no41_col) as col41, max(a.no42_col) as col42, max(a.no43_col) as col43, max(a.no44_col) as col44, max(a.no45_col) as col45, max(a.no46_col) as col46, max(a.no47_col) as col47, max(a.no48_col) as col48, max(a.no49_col) as col49, max(a.no50_col) as col50
, max(a.no51_col) as col51, max(a.no52_col) as col52, max(a.no53_col) as col53, max(a.no54_col) as col54, max(a.no55_col) as col55, max(a.no56_col) as col56, max(a.no57_col) as col57, max(a.no58_col) as col58, max(a.no59_col) as col59, max(a.no60_col) as col60
, max(a.no61_col) as col61, max(a.no62_col) as col62, max(a.no63_col) as col63, max(a.no64_col) as col64, max(a.no65_col) as col65, max(a.no66_col) as col66, max(a.no67_col) as col67, max(a.no68_col) as col68, max(a.no69_col) as col69, max(a.no70_col) as col70
, max(a.no71_col) as col71, max(a.no72_col) as col72, max(a.no73_col) as col73, max(a.no74_col) as col74, max(a.no75_col) as col75, max(a.no76_col) as col76, max(a.no77_col) as col77, max(a.no78_col) as col78, max(a.no79_col) as col79, max(a.no80_col) as col80
, max(a.no81_col) as col81, max(a.no82_col) as col82, max(a.no83_col) as col83, max(a.no84_col) as col84, max(a.no85_col) as col85, max(a.no86_col) as col86, max(a.no87_col) as col87, max(a.no88_col) as col88, max(a.no89_col) as col89, max(a.no90_col) as col90
, max(a.no91_col) as col91, max(a.no92_col) as col92, max(a.no93_col) as col93, max(a.no94_col) as col94, max(a.no95_col) as col95, max(a.no96_col) as col96, max(a.no97_col) as col97, max(a.no98_col) as col98, max(a.no99_col) as col99, max(a.no100_col) as col100
, max(a.no101_col) as col101, max(a.no102_col) as col102, max(a.no103_col) as col103, max(a.no104_col) as col104, max(a.no105_col) as col105, max(a.no106_col) as col106, max(a.no107_col) as col107, max(a.no108_col) as col108, max(a.no109_col) as col109, max(a.no110_col) as col110
, max(a.no111_col) as col111, max(a.no112_col) as col112, max(a.no113_col) as col113, max(a.no114_col) as col114, max(a.no115_col) as col115, max(a.no116_col) as col116, max(a.no117_col) as col117, max(a.no118_col) as col118, max(a.no119_col) as col119, max(a.no120_col) as col120
, max(a.no121_col) as col121, max(a.no122_col) as col122, max(a.no123_col) as col123, max(a.no124_col) as col124, max(a.no125_col) as col125, max(a.no126_col) as col126, max(a.no127_col) as col127, max(a.no128_col) as col128, max(a.no129_col) as col129, max(a.no130_col) as col130
, max(a.no131_col) as col131, max(a.no132_col) as col132, max(a.no133_col) as col133, max(a.no134_col) as col134, max(a.no135_col) as col135, max(a.no136_col) as col136, max(a.no137_col) as col137, max(a.no138_col) as col138, max(a.no139_col) as col139, max(a.no140_col) as col140
, max(a.no141_col) as col141, max(a.no142_col) as col142, max(a.no143_col) as col143, max(a.no144_col) as col144, max(a.no145_col) as col145, max(a.no146_col) as col146, max(a.no147_col) as col147, max(a.no148_col) as col148, max(a.no149_col) as col149, max(a.no150_col) as col150

from (
select *
from (
select a.master_id, a.master_ver, to_char(a.COLUMN_HIDDEN_YN) as col
        , row_number() over (partition by a.master_id, a.master_ver order by column_seq) as no
from TN_AD_MASTER_COLUMN a
)
pivot (max(col) col for no
   in (1 as no1, 2 as no2, 3 as no3, 4 as no4, 5 as no5, 6 as no6, 7 as no7, 8 as no8, 9 as no9, 10 as no10
       ,11 as no11, 12 as no12, 13 as no13, 14 as no14, 15 as no15, 16 as no16, 17 as no17, 18 as no18, 19 as no19, 20 as no20
   ,21 as no21, 22 as no22, 23 as no23, 24 as no24, 25 as no25, 26 as no26, 27 as no27, 28 as no28, 29 as no29, 30 as no30
   ,31 as no31, 32 as no32, 33 as no33, 34 as no34, 35 as no35, 36 as no36, 37 as no37, 38 as no38, 39 as no39, 40 as no40
   ,41 as no41, 42 as no42, 43 as no43, 44 as no44, 45 as no45, 46 as no46, 47 as no47, 48 as no48, 49 as no49, 50 as no50
   ,51 as no51, 52 as no52, 53 as no53, 54 as no54, 55 as no55, 56 as no56, 57 as no57, 58 as no58, 59 as no59, 60 as no60
   ,61 as no61, 62 as no62, 63 as no63, 64 as no64, 65 as no65, 66 as no66, 67 as no67, 68 as no68, 69 as no69, 70 as no70
   ,71 as no71, 72 as no72, 73 as no73, 74 as no74, 75 as no75, 76 as no76, 77 as no77, 78 as no78, 79 as no79, 80 as no80
   ,81 as no81, 82 as no82, 83 as no83, 84 as no84, 85 as no85, 86 as no86, 87 as no87, 88 as no88, 89 as no89, 90 as no90
   ,91 as no91, 92 as no92, 93 as no93, 94 as no94, 95 as no95, 96 as no96, 97 as no97, 98 as no98, 99 as no99, 100 as no100
   ,101 as no101, 102 as no102, 103 as no103, 104 as no104, 105 as no105, 106 as no106, 107 as no107, 108 as no108, 109 as no109, 110 as no110
   ,111 as no111, 112 as no112, 113 as no113, 114 as no114, 115 as no115, 116 as no116, 117 as no117, 118 as no118, 119 as no119, 120 as no120
   ,121 as no121, 122 as no122, 123 as no123, 124 as no124, 125 as no125, 126 as no126, 127 as no127, 128 as no128, 129 as no129, 130 as no130
   ,131 as no131, 132 as no132, 133 as no133, 134 as no134, 135 as no135, 136 as no136, 137 as no137, 138 as no138, 139 as no139, 140 as no140
   ,141 as no141, 142 as no142, 143 as no143, 144 as no144, 145 as no145, 146 as no146, 147 as no147, 148 as no148, 149 as no149, 150 as no150
   )
)
) a
group by a.master_id, a.master_ver


union all

select a.master_id, a.master_ver, 15 as no,  'COLUMN_WIDTH' as gb
, max(a.no1_col) as col01, max(a.no2_col) as col02, max(a.no3_col) as col03, max(a.no4_col) as col04, max(a.no5_col) as col05, max(a.no6_col) as col06, max(a.no7_col) as col07, max(a.no8_col) as col08, max(a.no9_col) as col09, max(a.no10_col) as col10
, max(a.no11_col) as col11, max(a.no12_col) as col12, max(a.no13_col) as col13, max(a.no14_col) as col14, max(a.no15_col) as col15, max(a.no16_col) as col16, max(a.no17_col) as col17, max(a.no18_col) as col18, max(a.no19_col) as col19, max(a.no20_col) as col20
, max(a.no21_col) as col21, max(a.no22_col) as col22, max(a.no23_col) as col23, max(a.no24_col) as col24, max(a.no25_col) as col25, max(a.no26_col) as col26, max(a.no27_col) as col27, max(a.no28_col) as col28, max(a.no29_col) as col29, max(a.no30_col) as col30
, max(a.no31_col) as col31, max(a.no32_col) as col32, max(a.no33_col) as col33, max(a.no34_col) as col34, max(a.no35_col) as col35, max(a.no36_col) as col36, max(a.no37_col) as col37, max(a.no38_col) as col38, max(a.no39_col) as col39, max(a.no40_col) as col40
, max(a.no41_col) as col41, max(a.no42_col) as col42, max(a.no43_col) as col43, max(a.no44_col) as col44, max(a.no45_col) as col45, max(a.no46_col) as col46, max(a.no47_col) as col47, max(a.no48_col) as col48, max(a.no49_col) as col49, max(a.no50_col) as col50
, max(a.no51_col) as col51, max(a.no52_col) as col52, max(a.no53_col) as col53, max(a.no54_col) as col54, max(a.no55_col) as col55, max(a.no56_col) as col56, max(a.no57_col) as col57, max(a.no58_col) as col58, max(a.no59_col) as col59, max(a.no60_col) as col60
, max(a.no61_col) as col61, max(a.no62_col) as col62, max(a.no63_col) as col63, max(a.no64_col) as col64, max(a.no65_col) as col65, max(a.no66_col) as col66, max(a.no67_col) as col67, max(a.no68_col) as col68, max(a.no69_col) as col69, max(a.no70_col) as col70
, max(a.no71_col) as col71, max(a.no72_col) as col72, max(a.no73_col) as col73, max(a.no74_col) as col74, max(a.no75_col) as col75, max(a.no76_col) as col76, max(a.no77_col) as col77, max(a.no78_col) as col78, max(a.no79_col) as col79, max(a.no80_col) as col80
, max(a.no81_col) as col81, max(a.no82_col) as col82, max(a.no83_col) as col83, max(a.no84_col) as col84, max(a.no85_col) as col85, max(a.no86_col) as col86, max(a.no87_col) as col87, max(a.no88_col) as col88, max(a.no89_col) as col89, max(a.no90_col) as col90
, max(a.no91_col) as col91, max(a.no92_col) as col92, max(a.no93_col) as col93, max(a.no94_col) as col94, max(a.no95_col) as col95, max(a.no96_col) as col96, max(a.no97_col) as col97, max(a.no98_col) as col98, max(a.no99_col) as col99, max(a.no100_col) as col100
, max(a.no101_col) as col101, max(a.no102_col) as col102, max(a.no103_col) as col103, max(a.no104_col) as col104, max(a.no105_col) as col105, max(a.no106_col) as col106, max(a.no107_col) as col107, max(a.no108_col) as col108, max(a.no109_col) as col109, max(a.no110_col) as col110
, max(a.no111_col) as col111, max(a.no112_col) as col112, max(a.no113_col) as col113, max(a.no114_col) as col114, max(a.no115_col) as col115, max(a.no116_col) as col116, max(a.no117_col) as col117, max(a.no118_col) as col118, max(a.no119_col) as col119, max(a.no120_col) as col120
, max(a.no121_col) as col121, max(a.no122_col) as col122, max(a.no123_col) as col123, max(a.no124_col) as col124, max(a.no125_col) as col125, max(a.no126_col) as col126, max(a.no127_col) as col127, max(a.no128_col) as col128, max(a.no129_col) as col129, max(a.no130_col) as col130
, max(a.no131_col) as col131, max(a.no132_col) as col132, max(a.no133_col) as col133, max(a.no134_col) as col134, max(a.no135_col) as col135, max(a.no136_col) as col136, max(a.no137_col) as col137, max(a.no138_col) as col138, max(a.no139_col) as col139, max(a.no140_col) as col140
, max(a.no141_col) as col141, max(a.no142_col) as col142, max(a.no143_col) as col143, max(a.no144_col) as col144, max(a.no145_col) as col145, max(a.no146_col) as col146, max(a.no147_col) as col147, max(a.no148_col) as col148, max(a.no149_col) as col149, max(a.no150_col) as col150

from (
select *
from (
select a.master_id, a.master_ver, to_char(a.COLUMN_WIDTH) as col
        , row_number() over (partition by a.master_id, a.master_ver order by column_seq) as no
from TN_AD_MASTER_COLUMN a
)
pivot (max(col) col for no
   in (1 as no1, 2 as no2, 3 as no3, 4 as no4, 5 as no5, 6 as no6, 7 as no7, 8 as no8, 9 as no9, 10 as no10
       ,11 as no11, 12 as no12, 13 as no13, 14 as no14, 15 as no15, 16 as no16, 17 as no17, 18 as no18, 19 as no19, 20 as no20
   ,21 as no21, 22 as no22, 23 as no23, 24 as no24, 25 as no25, 26 as no26, 27 as no27, 28 as no28, 29 as no29, 30 as no30
   ,31 as no31, 32 as no32, 33 as no33, 34 as no34, 35 as no35, 36 as no36, 37 as no37, 38 as no38, 39 as no39, 40 as no40
   ,41 as no41, 42 as no42, 43 as no43, 44 as no44, 45 as no45, 46 as no46, 47 as no47, 48 as no48, 49 as no49, 50 as no50
   ,51 as no51, 52 as no52, 53 as no53, 54 as no54, 55 as no55, 56 as no56, 57 as no57, 58 as no58, 59 as no59, 60 as no60
   ,61 as no61, 62 as no62, 63 as no63, 64 as no64, 65 as no65, 66 as no66, 67 as no67, 68 as no68, 69 as no69, 70 as no70
   ,71 as no71, 72 as no72, 73 as no73, 74 as no74, 75 as no75, 76 as no76, 77 as no77, 78 as no78, 79 as no79, 80 as no80
   ,81 as no81, 82 as no82, 83 as no83, 84 as no84, 85 as no85, 86 as no86, 87 as no87, 88 as no88, 89 as no89, 90 as no90
   ,91 as no91, 92 as no92, 93 as no93, 94 as no94, 95 as no95, 96 as no96, 97 as no97, 98 as no98, 99 as no99, 100 as no100
   ,101 as no101, 102 as no102, 103 as no103, 104 as no104, 105 as no105, 106 as no106, 107 as no107, 108 as no108, 109 as no109, 110 as no110
   ,111 as no111, 112 as no112, 113 as no113, 114 as no114, 115 as no115, 116 as no116, 117 as no117, 118 as no118, 119 as no119, 120 as no120
   ,121 as no121, 122 as no122, 123 as no123, 124 as no124, 125 as no125, 126 as no126, 127 as no127, 128 as no128, 129 as no129, 130 as no130
   ,131 as no131, 132 as no132, 133 as no133, 134 as no134, 135 as no135, 136 as no136, 137 as no137, 138 as no138, 139 as no139, 140 as no140
   ,141 as no141, 142 as no142, 143 as no143, 144 as no144, 145 as no145, 146 as no146, 147 as no147, 148 as no148, 149 as no149, 150 as no150
   )
)
) a
group by a.master_id, a.master_ver

union all

select a.master_id, a.master_ver, 16 as no,  'LINK_TYPE' as gb
, max(a.no1_col) as col01, max(a.no2_col) as col02, max(a.no3_col) as col03, max(a.no4_col) as col04, max(a.no5_col) as col05, max(a.no6_col) as col06, max(a.no7_col) as col07, max(a.no8_col) as col08, max(a.no9_col) as col09, max(a.no10_col) as col10
, max(a.no11_col) as col11, max(a.no12_col) as col12, max(a.no13_col) as col13, max(a.no14_col) as col14, max(a.no15_col) as col15, max(a.no16_col) as col16, max(a.no17_col) as col17, max(a.no18_col) as col18, max(a.no19_col) as col19, max(a.no20_col) as col20
, max(a.no21_col) as col21, max(a.no22_col) as col22, max(a.no23_col) as col23, max(a.no24_col) as col24, max(a.no25_col) as col25, max(a.no26_col) as col26, max(a.no27_col) as col27, max(a.no28_col) as col28, max(a.no29_col) as col29, max(a.no30_col) as col30
, max(a.no31_col) as col31, max(a.no32_col) as col32, max(a.no33_col) as col33, max(a.no34_col) as col34, max(a.no35_col) as col35, max(a.no36_col) as col36, max(a.no37_col) as col37, max(a.no38_col) as col38, max(a.no39_col) as col39, max(a.no40_col) as col40
, max(a.no41_col) as col41, max(a.no42_col) as col42, max(a.no43_col) as col43, max(a.no44_col) as col44, max(a.no45_col) as col45, max(a.no46_col) as col46, max(a.no47_col) as col47, max(a.no48_col) as col48, max(a.no49_col) as col49, max(a.no50_col) as col50
, max(a.no51_col) as col51, max(a.no52_col) as col52, max(a.no53_col) as col53, max(a.no54_col) as col54, max(a.no55_col) as col55, max(a.no56_col) as col56, max(a.no57_col) as col57, max(a.no58_col) as col58, max(a.no59_col) as col59, max(a.no60_col) as col60
, max(a.no61_col) as col61, max(a.no62_col) as col62, max(a.no63_col) as col63, max(a.no64_col) as col64, max(a.no65_col) as col65, max(a.no66_col) as col66, max(a.no67_col) as col67, max(a.no68_col) as col68, max(a.no69_col) as col69, max(a.no70_col) as col70
, max(a.no71_col) as col71, max(a.no72_col) as col72, max(a.no73_col) as col73, max(a.no74_col) as col74, max(a.no75_col) as col75, max(a.no76_col) as col76, max(a.no77_col) as col77, max(a.no78_col) as col78, max(a.no79_col) as col79, max(a.no80_col) as col80
, max(a.no81_col) as col81, max(a.no82_col) as col82, max(a.no83_col) as col83, max(a.no84_col) as col84, max(a.no85_col) as col85, max(a.no86_col) as col86, max(a.no87_col) as col87, max(a.no88_col) as col88, max(a.no89_col) as col89, max(a.no90_col) as col90
, max(a.no91_col) as col91, max(a.no92_col) as col92, max(a.no93_col) as col93, max(a.no94_col) as col94, max(a.no95_col) as col95, max(a.no96_col) as col96, max(a.no97_col) as col97, max(a.no98_col) as col98, max(a.no99_col) as col99, max(a.no100_col) as col100
, max(a.no101_col) as col101, max(a.no102_col) as col102, max(a.no103_col) as col103, max(a.no104_col) as col104, max(a.no105_col) as col105, max(a.no106_col) as col106, max(a.no107_col) as col107, max(a.no108_col) as col108, max(a.no109_col) as col109, max(a.no110_col) as col110
, max(a.no111_col) as col111, max(a.no112_col) as col112, max(a.no113_col) as col113, max(a.no114_col) as col114, max(a.no115_col) as col115, max(a.no116_col) as col116, max(a.no117_col) as col117, max(a.no118_col) as col118, max(a.no119_col) as col119, max(a.no120_col) as col120
, max(a.no121_col) as col121, max(a.no122_col) as col122, max(a.no123_col) as col123, max(a.no124_col) as col124, max(a.no125_col) as col125, max(a.no126_col) as col126, max(a.no127_col) as col127, max(a.no128_col) as col128, max(a.no129_col) as col129, max(a.no130_col) as col130
, max(a.no131_col) as col131, max(a.no132_col) as col132, max(a.no133_col) as col133, max(a.no134_col) as col134, max(a.no135_col) as col135, max(a.no136_col) as col136, max(a.no137_col) as col137, max(a.no138_col) as col138, max(a.no139_col) as col139, max(a.no140_col) as col140
, max(a.no141_col) as col141, max(a.no142_col) as col142, max(a.no143_col) as col143, max(a.no144_col) as col144, max(a.no145_col) as col145, max(a.no146_col) as col146, max(a.no147_col) as col147, max(a.no148_col) as col148, max(a.no149_col) as col149, max(a.no150_col) as col150

from (
select *
from (
select a.master_id, a.master_ver, to_char(a.LINK_TYPE) as col
        , row_number() over (partition by a.master_id, a.master_ver order by column_seq) as no
from TN_AD_MASTER_COLUMN a
)
pivot (max(col) col for no
   in (1 as no1, 2 as no2, 3 as no3, 4 as no4, 5 as no5, 6 as no6, 7 as no7, 8 as no8, 9 as no9, 10 as no10
       ,11 as no11, 12 as no12, 13 as no13, 14 as no14, 15 as no15, 16 as no16, 17 as no17, 18 as no18, 19 as no19, 20 as no20
   ,21 as no21, 22 as no22, 23 as no23, 24 as no24, 25 as no25, 26 as no26, 27 as no27, 28 as no28, 29 as no29, 30 as no30
   ,31 as no31, 32 as no32, 33 as no33, 34 as no34, 35 as no35, 36 as no36, 37 as no37, 38 as no38, 39 as no39, 40 as no40
   ,41 as no41, 42 as no42, 43 as no43, 44 as no44, 45 as no45, 46 as no46, 47 as no47, 48 as no48, 49 as no49, 50 as no50
   ,51 as no51, 52 as no52, 53 as no53, 54 as no54, 55 as no55, 56 as no56, 57 as no57, 58 as no58, 59 as no59, 60 as no60
   ,61 as no61, 62 as no62, 63 as no63, 64 as no64, 65 as no65, 66 as no66, 67 as no67, 68 as no68, 69 as no69, 70 as no70
   ,71 as no71, 72 as no72, 73 as no73, 74 as no74, 75 as no75, 76 as no76, 77 as no77, 78 as no78, 79 as no79, 80 as no80
   ,81 as no81, 82 as no82, 83 as no83, 84 as no84, 85 as no85, 86 as no86, 87 as no87, 88 as no88, 89 as no89, 90 as no90
   ,91 as no91, 92 as no92, 93 as no93, 94 as no94, 95 as no95, 96 as no96, 97 as no97, 98 as no98, 99 as no99, 100 as no100
   ,101 as no101, 102 as no102, 103 as no103, 104 as no104, 105 as no105, 106 as no106, 107 as no107, 108 as no108, 109 as no109, 110 as no110
   ,111 as no111, 112 as no112, 113 as no113, 114 as no114, 115 as no115, 116 as no116, 117 as no117, 118 as no118, 119 as no119, 120 as no120
   ,121 as no121, 122 as no122, 123 as no123, 124 as no124, 125 as no125, 126 as no126, 127 as no127, 128 as no128, 129 as no129, 130 as no130
   ,131 as no131, 132 as no132, 133 as no133, 134 as no134, 135 as no135, 136 as no136, 137 as no137, 138 as no138, 139 as no139, 140 as no140
   ,141 as no141, 142 as no142, 143 as no143, 144 as no144, 145 as no145, 146 as no146, 147 as no147, 148 as no148, 149 as no149, 150 as no150
   )
)
) a
group by a.master_id, a.master_ver


union all

select a.master_id, a.master_ver, 17 as no,  'LINK_PARAM' as gb
, max(a.no1_col) as col01, max(a.no2_col) as col02, max(a.no3_col) as col03, max(a.no4_col) as col04, max(a.no5_col) as col05, max(a.no6_col) as col06, max(a.no7_col) as col07, max(a.no8_col) as col08, max(a.no9_col) as col09, max(a.no10_col) as col10
, max(a.no11_col) as col11, max(a.no12_col) as col12, max(a.no13_col) as col13, max(a.no14_col) as col14, max(a.no15_col) as col15, max(a.no16_col) as col16, max(a.no17_col) as col17, max(a.no18_col) as col18, max(a.no19_col) as col19, max(a.no20_col) as col20
, max(a.no21_col) as col21, max(a.no22_col) as col22, max(a.no23_col) as col23, max(a.no24_col) as col24, max(a.no25_col) as col25, max(a.no26_col) as col26, max(a.no27_col) as col27, max(a.no28_col) as col28, max(a.no29_col) as col29, max(a.no30_col) as col30
, max(a.no31_col) as col31, max(a.no32_col) as col32, max(a.no33_col) as col33, max(a.no34_col) as col34, max(a.no35_col) as col35, max(a.no36_col) as col36, max(a.no37_col) as col37, max(a.no38_col) as col38, max(a.no39_col) as col39, max(a.no40_col) as col40
, max(a.no41_col) as col41, max(a.no42_col) as col42, max(a.no43_col) as col43, max(a.no44_col) as col44, max(a.no45_col) as col45, max(a.no46_col) as col46, max(a.no47_col) as col47, max(a.no48_col) as col48, max(a.no49_col) as col49, max(a.no50_col) as col50
, max(a.no51_col) as col51, max(a.no52_col) as col52, max(a.no53_col) as col53, max(a.no54_col) as col54, max(a.no55_col) as col55, max(a.no56_col) as col56, max(a.no57_col) as col57, max(a.no58_col) as col58, max(a.no59_col) as col59, max(a.no60_col) as col60
, max(a.no61_col) as col61, max(a.no62_col) as col62, max(a.no63_col) as col63, max(a.no64_col) as col64, max(a.no65_col) as col65, max(a.no66_col) as col66, max(a.no67_col) as col67, max(a.no68_col) as col68, max(a.no69_col) as col69, max(a.no70_col) as col70
, max(a.no71_col) as col71, max(a.no72_col) as col72, max(a.no73_col) as col73, max(a.no74_col) as col74, max(a.no75_col) as col75, max(a.no76_col) as col76, max(a.no77_col) as col77, max(a.no78_col) as col78, max(a.no79_col) as col79, max(a.no80_col) as col80
, max(a.no81_col) as col81, max(a.no82_col) as col82, max(a.no83_col) as col83, max(a.no84_col) as col84, max(a.no85_col) as col85, max(a.no86_col) as col86, max(a.no87_col) as col87, max(a.no88_col) as col88, max(a.no89_col) as col89, max(a.no90_col) as col90
, max(a.no91_col) as col91, max(a.no92_col) as col92, max(a.no93_col) as col93, max(a.no94_col) as col94, max(a.no95_col) as col95, max(a.no96_col) as col96, max(a.no97_col) as col97, max(a.no98_col) as col98, max(a.no99_col) as col99, max(a.no100_col) as col100
, max(a.no101_col) as col101, max(a.no102_col) as col102, max(a.no103_col) as col103, max(a.no104_col) as col104, max(a.no105_col) as col105, max(a.no106_col) as col106, max(a.no107_col) as col107, max(a.no108_col) as col108, max(a.no109_col) as col109, max(a.no110_col) as col110
, max(a.no111_col) as col111, max(a.no112_col) as col112, max(a.no113_col) as col113, max(a.no114_col) as col114, max(a.no115_col) as col115, max(a.no116_col) as col116, max(a.no117_col) as col117, max(a.no118_col) as col118, max(a.no119_col) as col119, max(a.no120_col) as col120
, max(a.no121_col) as col121, max(a.no122_col) as col122, max(a.no123_col) as col123, max(a.no124_col) as col124, max(a.no125_col) as col125, max(a.no126_col) as col126, max(a.no127_col) as col127, max(a.no128_col) as col128, max(a.no129_col) as col129, max(a.no130_col) as col130
, max(a.no131_col) as col131, max(a.no132_col) as col132, max(a.no133_col) as col133, max(a.no134_col) as col134, max(a.no135_col) as col135, max(a.no136_col) as col136, max(a.no137_col) as col137, max(a.no138_col) as col138, max(a.no139_col) as col139, max(a.no140_col) as col140
, max(a.no141_col) as col141, max(a.no142_col) as col142, max(a.no143_col) as col143, max(a.no144_col) as col144, max(a.no145_col) as col145, max(a.no146_col) as col146, max(a.no147_col) as col147, max(a.no148_col) as col148, max(a.no149_col) as col149, max(a.no150_col) as col150

from (
select *
from (
select a.master_id, a.master_ver, to_char(a.LINK_PARAM) as col
        , row_number() over (partition by a.master_id, a.master_ver order by column_seq) as no
from TN_AD_MASTER_COLUMN a
)
pivot (max(col) col for no
   in (1 as no1, 2 as no2, 3 as no3, 4 as no4, 5 as no5, 6 as no6, 7 as no7, 8 as no8, 9 as no9, 10 as no10
       ,11 as no11, 12 as no12, 13 as no13, 14 as no14, 15 as no15, 16 as no16, 17 as no17, 18 as no18, 19 as no19, 20 as no20
   ,21 as no21, 22 as no22, 23 as no23, 24 as no24, 25 as no25, 26 as no26, 27 as no27, 28 as no28, 29 as no29, 30 as no30
   ,31 as no31, 32 as no32, 33 as no33, 34 as no34, 35 as no35, 36 as no36, 37 as no37, 38 as no38, 39 as no39, 40 as no40
   ,41 as no41, 42 as no42, 43 as no43, 44 as no44, 45 as no45, 46 as no46, 47 as no47, 48 as no48, 49 as no49, 50 as no50
   ,51 as no51, 52 as no52, 53 as no53, 54 as no54, 55 as no55, 56 as no56, 57 as no57, 58 as no58, 59 as no59, 60 as no60
   ,61 as no61, 62 as no62, 63 as no63, 64 as no64, 65 as no65, 66 as no66, 67 as no67, 68 as no68, 69 as no69, 70 as no70
   ,71 as no71, 72 as no72, 73 as no73, 74 as no74, 75 as no75, 76 as no76, 77 as no77, 78 as no78, 79 as no79, 80 as no80
   ,81 as no81, 82 as no82, 83 as no83, 84 as no84, 85 as no85, 86 as no86, 87 as no87, 88 as no88, 89 as no89, 90 as no90
   ,91 as no91, 92 as no92, 93 as no93, 94 as no94, 95 as no95, 96 as no96, 97 as no97, 98 as no98, 99 as no99, 100 as no100
   ,101 as no101, 102 as no102, 103 as no103, 104 as no104, 105 as no105, 106 as no106, 107 as no107, 108 as no108, 109 as no109, 110 as no110
   ,111 as no111, 112 as no112, 113 as no113, 114 as no114, 115 as no115, 116 as no116, 117 as no117, 118 as no118, 119 as no119, 120 as no120
   ,121 as no121, 122 as no122, 123 as no123, 124 as no124, 125 as no125, 126 as no126, 127 as no127, 128 as no128, 129 as no129, 130 as no130
   ,131 as no131, 132 as no132, 133 as no133, 134 as no134, 135 as no135, 136 as no136, 137 as no137, 138 as no138, 139 as no139, 140 as no140
   ,141 as no141, 142 as no142, 143 as no143, 144 as no144, 145 as no145, 146 as no146, 147 as no147, 148 as no148, 149 as no149, 150 as no150
   )
)
) a
group by a.master_id, a.master_ver

union all

select a.master_id, a.master_ver, 18 as no,  'USE_YN' as gb
, max(a.no1_col) as col01, max(a.no2_col) as col02, max(a.no3_col) as col03, max(a.no4_col) as col04, max(a.no5_col) as col05, max(a.no6_col) as col06, max(a.no7_col) as col07, max(a.no8_col) as col08, max(a.no9_col) as col09, max(a.no10_col) as col10
, max(a.no11_col) as col11, max(a.no12_col) as col12, max(a.no13_col) as col13, max(a.no14_col) as col14, max(a.no15_col) as col15, max(a.no16_col) as col16, max(a.no17_col) as col17, max(a.no18_col) as col18, max(a.no19_col) as col19, max(a.no20_col) as col20
, max(a.no21_col) as col21, max(a.no22_col) as col22, max(a.no23_col) as col23, max(a.no24_col) as col24, max(a.no25_col) as col25, max(a.no26_col) as col26, max(a.no27_col) as col27, max(a.no28_col) as col28, max(a.no29_col) as col29, max(a.no30_col) as col30
, max(a.no31_col) as col31, max(a.no32_col) as col32, max(a.no33_col) as col33, max(a.no34_col) as col34, max(a.no35_col) as col35, max(a.no36_col) as col36, max(a.no37_col) as col37, max(a.no38_col) as col38, max(a.no39_col) as col39, max(a.no40_col) as col40
, max(a.no41_col) as col41, max(a.no42_col) as col42, max(a.no43_col) as col43, max(a.no44_col) as col44, max(a.no45_col) as col45, max(a.no46_col) as col46, max(a.no47_col) as col47, max(a.no48_col) as col48, max(a.no49_col) as col49, max(a.no50_col) as col50
, max(a.no51_col) as col51, max(a.no52_col) as col52, max(a.no53_col) as col53, max(a.no54_col) as col54, max(a.no55_col) as col55, max(a.no56_col) as col56, max(a.no57_col) as col57, max(a.no58_col) as col58, max(a.no59_col) as col59, max(a.no60_col) as col60
, max(a.no61_col) as col61, max(a.no62_col) as col62, max(a.no63_col) as col63, max(a.no64_col) as col64, max(a.no65_col) as col65, max(a.no66_col) as col66, max(a.no67_col) as col67, max(a.no68_col) as col68, max(a.no69_col) as col69, max(a.no70_col) as col70
, max(a.no71_col) as col71, max(a.no72_col) as col72, max(a.no73_col) as col73, max(a.no74_col) as col74, max(a.no75_col) as col75, max(a.no76_col) as col76, max(a.no77_col) as col77, max(a.no78_col) as col78, max(a.no79_col) as col79, max(a.no80_col) as col80
, max(a.no81_col) as col81, max(a.no82_col) as col82, max(a.no83_col) as col83, max(a.no84_col) as col84, max(a.no85_col) as col85, max(a.no86_col) as col86, max(a.no87_col) as col87, max(a.no88_col) as col88, max(a.no89_col) as col89, max(a.no90_col) as col90
, max(a.no91_col) as col91, max(a.no92_col) as col92, max(a.no93_col) as col93, max(a.no94_col) as col94, max(a.no95_col) as col95, max(a.no96_col) as col96, max(a.no97_col) as col97, max(a.no98_col) as col98, max(a.no99_col) as col99, max(a.no100_col) as col100
, max(a.no101_col) as col101, max(a.no102_col) as col102, max(a.no103_col) as col103, max(a.no104_col) as col104, max(a.no105_col) as col105, max(a.no106_col) as col106, max(a.no107_col) as col107, max(a.no108_col) as col108, max(a.no109_col) as col109, max(a.no110_col) as col110
, max(a.no111_col) as col111, max(a.no112_col) as col112, max(a.no113_col) as col113, max(a.no114_col) as col114, max(a.no115_col) as col115, max(a.no116_col) as col116, max(a.no117_col) as col117, max(a.no118_col) as col118, max(a.no119_col) as col119, max(a.no120_col) as col120
, max(a.no121_col) as col121, max(a.no122_col) as col122, max(a.no123_col) as col123, max(a.no124_col) as col124, max(a.no125_col) as col125, max(a.no126_col) as col126, max(a.no127_col) as col127, max(a.no128_col) as col128, max(a.no129_col) as col129, max(a.no130_col) as col130
, max(a.no131_col) as col131, max(a.no132_col) as col132, max(a.no133_col) as col133, max(a.no134_col) as col134, max(a.no135_col) as col135, max(a.no136_col) as col136, max(a.no137_col) as col137, max(a.no138_col) as col138, max(a.no139_col) as col139, max(a.no140_col) as col140
, max(a.no141_col) as col141, max(a.no142_col) as col142, max(a.no143_col) as col143, max(a.no144_col) as col144, max(a.no145_col) as col145, max(a.no146_col) as col146, max(a.no147_col) as col147, max(a.no148_col) as col148, max(a.no149_col) as col149, max(a.no150_col) as col150

from (
select *
from (
select a.master_id, a.master_ver, to_char(a.USE_YN) as col
        , row_number() over (partition by a.master_id, a.master_ver order by column_seq) as no
from TN_AD_MASTER_COLUMN a
)
pivot (max(col) col for no
   in (1 as no1, 2 as no2, 3 as no3, 4 as no4, 5 as no5, 6 as no6, 7 as no7, 8 as no8, 9 as no9, 10 as no10
       ,11 as no11, 12 as no12, 13 as no13, 14 as no14, 15 as no15, 16 as no16, 17 as no17, 18 as no18, 19 as no19, 20 as no20
   ,21 as no21, 22 as no22, 23 as no23, 24 as no24, 25 as no25, 26 as no26, 27 as no27, 28 as no28, 29 as no29, 30 as no30
   ,31 as no31, 32 as no32, 33 as no33, 34 as no34, 35 as no35, 36 as no36, 37 as no37, 38 as no38, 39 as no39, 40 as no40
   ,41 as no41, 42 as no42, 43 as no43, 44 as no44, 45 as no45, 46 as no46, 47 as no47, 48 as no48, 49 as no49, 50 as no50
   ,51 as no51, 52 as no52, 53 as no53, 54 as no54, 55 as no55, 56 as no56, 57 as no57, 58 as no58, 59 as no59, 60 as no60
   ,61 as no61, 62 as no62, 63 as no63, 64 as no64, 65 as no65, 66 as no66, 67 as no67, 68 as no68, 69 as no69, 70 as no70
   ,71 as no71, 72 as no72, 73 as no73, 74 as no74, 75 as no75, 76 as no76, 77 as no77, 78 as no78, 79 as no79, 80 as no80
   ,81 as no81, 82 as no82, 83 as no83, 84 as no84, 85 as no85, 86 as no86, 87 as no87, 88 as no88, 89 as no89, 90 as no90
   ,91 as no91, 92 as no92, 93 as no93, 94 as no94, 95 as no95, 96 as no96, 97 as no97, 98 as no98, 99 as no99, 100 as no100
   ,101 as no101, 102 as no102, 103 as no103, 104 as no104, 105 as no105, 106 as no106, 107 as no107, 108 as no108, 109 as no109, 110 as no110
   ,111 as no111, 112 as no112, 113 as no113, 114 as no114, 115 as no115, 116 as no116, 117 as no117, 118 as no118, 119 as no119, 120 as no120
   ,121 as no121, 122 as no122, 123 as no123, 124 as no124, 125 as no125, 126 as no126, 127 as no127, 128 as no128, 129 as no129, 130 as no130
   ,131 as no131, 132 as no132, 133 as no133, 134 as no134, 135 as no135, 136 as no136, 137 as no137, 138 as no138, 139 as no139, 140 as no140
   ,141 as no141, 142 as no142, 143 as no143, 144 as no144, 145 as no145, 146 as no146, 147 as no147, 148 as no148, 149 as no149, 150 as no150
   )
)
) a
group by a.master_id, a.master_ver

union all

select a.master_id, a.master_ver, 19 as no,  'DELETE_YN' as gb
, max(a.no1_col) as col01, max(a.no2_col) as col02, max(a.no3_col) as col03, max(a.no4_col) as col04, max(a.no5_col) as col05, max(a.no6_col) as col06, max(a.no7_col) as col07, max(a.no8_col) as col08, max(a.no9_col) as col09, max(a.no10_col) as col10
, max(a.no11_col) as col11, max(a.no12_col) as col12, max(a.no13_col) as col13, max(a.no14_col) as col14, max(a.no15_col) as col15, max(a.no16_col) as col16, max(a.no17_col) as col17, max(a.no18_col) as col18, max(a.no19_col) as col19, max(a.no20_col) as col20
, max(a.no21_col) as col21, max(a.no22_col) as col22, max(a.no23_col) as col23, max(a.no24_col) as col24, max(a.no25_col) as col25, max(a.no26_col) as col26, max(a.no27_col) as col27, max(a.no28_col) as col28, max(a.no29_col) as col29, max(a.no30_col) as col30
, max(a.no31_col) as col31, max(a.no32_col) as col32, max(a.no33_col) as col33, max(a.no34_col) as col34, max(a.no35_col) as col35, max(a.no36_col) as col36, max(a.no37_col) as col37, max(a.no38_col) as col38, max(a.no39_col) as col39, max(a.no40_col) as col40
, max(a.no41_col) as col41, max(a.no42_col) as col42, max(a.no43_col) as col43, max(a.no44_col) as col44, max(a.no45_col) as col45, max(a.no46_col) as col46, max(a.no47_col) as col47, max(a.no48_col) as col48, max(a.no49_col) as col49, max(a.no50_col) as col50
, max(a.no51_col) as col51, max(a.no52_col) as col52, max(a.no53_col) as col53, max(a.no54_col) as col54, max(a.no55_col) as col55, max(a.no56_col) as col56, max(a.no57_col) as col57, max(a.no58_col) as col58, max(a.no59_col) as col59, max(a.no60_col) as col60
, max(a.no61_col) as col61, max(a.no62_col) as col62, max(a.no63_col) as col63, max(a.no64_col) as col64, max(a.no65_col) as col65, max(a.no66_col) as col66, max(a.no67_col) as col67, max(a.no68_col) as col68, max(a.no69_col) as col69, max(a.no70_col) as col70
, max(a.no71_col) as col71, max(a.no72_col) as col72, max(a.no73_col) as col73, max(a.no74_col) as col74, max(a.no75_col) as col75, max(a.no76_col) as col76, max(a.no77_col) as col77, max(a.no78_col) as col78, max(a.no79_col) as col79, max(a.no80_col) as col80
, max(a.no81_col) as col81, max(a.no82_col) as col82, max(a.no83_col) as col83, max(a.no84_col) as col84, max(a.no85_col) as col85, max(a.no86_col) as col86, max(a.no87_col) as col87, max(a.no88_col) as col88, max(a.no89_col) as col89, max(a.no90_col) as col90
, max(a.no91_col) as col91, max(a.no92_col) as col92, max(a.no93_col) as col93, max(a.no94_col) as col94, max(a.no95_col) as col95, max(a.no96_col) as col96, max(a.no97_col) as col97, max(a.no98_col) as col98, max(a.no99_col) as col99, max(a.no100_col) as col100
, max(a.no101_col) as col101, max(a.no102_col) as col102, max(a.no103_col) as col103, max(a.no104_col) as col104, max(a.no105_col) as col105, max(a.no106_col) as col106, max(a.no107_col) as col107, max(a.no108_col) as col108, max(a.no109_col) as col109, max(a.no110_col) as col110
, max(a.no111_col) as col111, max(a.no112_col) as col112, max(a.no113_col) as col113, max(a.no114_col) as col114, max(a.no115_col) as col115, max(a.no116_col) as col116, max(a.no117_col) as col117, max(a.no118_col) as col118, max(a.no119_col) as col119, max(a.no120_col) as col120
, max(a.no121_col) as col121, max(a.no122_col) as col122, max(a.no123_col) as col123, max(a.no124_col) as col124, max(a.no125_col) as col125, max(a.no126_col) as col126, max(a.no127_col) as col127, max(a.no128_col) as col128, max(a.no129_col) as col129, max(a.no130_col) as col130
, max(a.no131_col) as col131, max(a.no132_col) as col132, max(a.no133_col) as col133, max(a.no134_col) as col134, max(a.no135_col) as col135, max(a.no136_col) as col136, max(a.no137_col) as col137, max(a.no138_col) as col138, max(a.no139_col) as col139, max(a.no140_col) as col140
, max(a.no141_col) as col141, max(a.no142_col) as col142, max(a.no143_col) as col143, max(a.no144_col) as col144, max(a.no145_col) as col145, max(a.no146_col) as col146, max(a.no147_col) as col147, max(a.no148_col) as col148, max(a.no149_col) as col149, max(a.no150_col) as col150

from (
select *
from (
select a.master_id, a.master_ver, to_char(a.DELETE_YN) as col
        , row_number() over (partition by a.master_id, a.master_ver order by column_seq) as no
from TN_AD_MASTER_COLUMN a
)
pivot (max(col) col for no
   in (1 as no1, 2 as no2, 3 as no3, 4 as no4, 5 as no5, 6 as no6, 7 as no7, 8 as no8, 9 as no9, 10 as no10
       ,11 as no11, 12 as no12, 13 as no13, 14 as no14, 15 as no15, 16 as no16, 17 as no17, 18 as no18, 19 as no19, 20 as no20
   ,21 as no21, 22 as no22, 23 as no23, 24 as no24, 25 as no25, 26 as no26, 27 as no27, 28 as no28, 29 as no29, 30 as no30
   ,31 as no31, 32 as no32, 33 as no33, 34 as no34, 35 as no35, 36 as no36, 37 as no37, 38 as no38, 39 as no39, 40 as no40
   ,41 as no41, 42 as no42, 43 as no43, 44 as no44, 45 as no45, 46 as no46, 47 as no47, 48 as no48, 49 as no49, 50 as no50
   ,51 as no51, 52 as no52, 53 as no53, 54 as no54, 55 as no55, 56 as no56, 57 as no57, 58 as no58, 59 as no59, 60 as no60
   ,61 as no61, 62 as no62, 63 as no63, 64 as no64, 65 as no65, 66 as no66, 67 as no67, 68 as no68, 69 as no69, 70 as no70
   ,71 as no71, 72 as no72, 73 as no73, 74 as no74, 75 as no75, 76 as no76, 77 as no77, 78 as no78, 79 as no79, 80 as no80
   ,81 as no81, 82 as no82, 83 as no83, 84 as no84, 85 as no85, 86 as no86, 87 as no87, 88 as no88, 89 as no89, 90 as no90
   ,91 as no91, 92 as no92, 93 as no93, 94 as no94, 95 as no95, 96 as no96, 97 as no97, 98 as no98, 99 as no99, 100 as no100
   ,101 as no101, 102 as no102, 103 as no103, 104 as no104, 105 as no105, 106 as no106, 107 as no107, 108 as no108, 109 as no109, 110 as no110
   ,111 as no111, 112 as no112, 113 as no113, 114 as no114, 115 as no115, 116 as no116, 117 as no117, 118 as no118, 119 as no119, 120 as no120
   ,121 as no121, 122 as no122, 123 as no123, 124 as no124, 125 as no125, 126 as no126, 127 as no127, 128 as no128, 129 as no129, 130 as no130
   ,131 as no131, 132 as no132, 133 as no133, 134 as no134, 135 as no135, 136 as no136, 137 as no137, 138 as no138, 139 as no139, 140 as no140
   ,141 as no141, 142 as no142, 143 as no143, 144 as no144, 145 as no145, 146 as no146, 147 as no147, 148 as no148, 149 as no149, 150 as no150
   )
)
) a
group by a.master_id, a.master_ver

order by  master_id, master_ver, no, gb
```
<!-- AUTO:END definition -->

# 참조 객체
<!-- AUTO:BEGIN deps -->
- [TN_AD_MASTER_COLUMN](/schemas/SETADAMSUSER/tables/TN_AD_MASTER_COLUMN.md)
<!-- AUTO:END deps -->

# T2S 힌트
(사람이 보완하거나 P7 에서 규칙 문서를 링크한다)

<!-- ES-REFLECT:BEGIN (add_info/es_index_generated.csv + DB grain 실측 2026-10-15) -->### 그레인 (DB 실측 2026-10-16, 키 비유일 — 전체 스캔)
- 키 후보 `COL09` — 어떤 식별 컬럼을 추가해도 dup 불변 (전체 스캔 dup 370).
  완전 복제행(이력·스냅샷) 또는 자연스러운 1:N 관계. 집계/JOIN 시 DISTINCT 또는 최신값(RN=1) 처리 필요.
<!-- ES-REFLECT:END -->
