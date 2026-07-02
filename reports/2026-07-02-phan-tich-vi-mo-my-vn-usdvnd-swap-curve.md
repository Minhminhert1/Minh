# Phân tích vĩ mô Mỹ – Việt Nam, USD/VND & Swap Curve — 02/07/2026

> **Input:** yêu cầu phân tích tổng quan vi mô/vĩ mô Mỹ + VN + USDVND + swap curve.
> **Playbook:** PB-3 mở rộng (full research squad R1–R6 → A1/A2/A3 → Reviewer).
> **Model:** toàn bộ agent chạy Fable 5 theo yêu cầu user. Tầng Analysis chạy trong phiên chính (subagent chạm session limit) — vẫn Fable 5.
> **Quy ước:** [FACT] có nguồn + as-of. [DERIVED] suy từ CIP, chỉ tin dấu & hướng. [SUY LUẬN] là diễn giải của team.

---

## 0. TỔNG QUAN (Orchestrator)

Bức tranh đã **đổi chế độ hoàn toàn so với báo cáo 23/06**:

1. **Thanh khoản VND đảo cực:** ON liên ngân hàng từ vùng thấp giữa tháng 6 vọt lên **13% phiên 30/06** (cao nhất từ cuối tháng 3) đúng ngày khóa sổ quý II; 1W–1M neo **8–8,5%**. SBV phản ứng bằng bơm ròng OMO kỳ hạn dài (35–56 ngày) + **kích hoạt lại swap USD/VND 7 ngày** (lần 3 trong 2026).
2. **Chênh lệch lãi suất VND–USD đảo dấu sang DƯƠNG LỚN:** ON +9,3 điểm %, 1M ~+4,5 điểm % so SOFR 3,68% → **swap points USD/VND dương (forward premium) trên toàn curve** — ngược hẳn trạng thái âm sâu đầu cong hôm 23/06.
3. **Nghịch lý trung tâm:** carry VND dương lớn nhưng **spot vẫn kịch trần 26.466** (VCB bán đúng trần từ 01/07, tự do 26.610–26.720). Flow (nhập siêu ~16,8 tỷ USD + khối ngoại bán ròng ~3 tỷ USD + kiều hối −17%) và kỳ vọng phá giá đang **thắng carry**.
4. **Chân USD chuyển hawkish:** CPI Mỹ 4,2% (sốc dầu Iran/Hormuz), dot plot 6/2026 median cuối năm **3,8% — hàm ý TĂNG lãi suất**; SOFR khó giảm → không trông chờ chênh lệch co lại từ phía USD.
5. **Event risk dồn dập tháng 7:** NFP 03/07 · GDP Q2 + CPI T6 VN ~06/07 · điều trần Section 301 (đề xuất thuế 12,5% với VN) 07/07 · Section 122 hết hạn ~24/07 · FOMC 28–29/07.

---

## 1. DATA PACK — FACT CHÍNH (Research squad R1–R6)

### 1.1 Vĩ mô Mỹ (R3)

| Chỉ số | Giá trị | as-of | Độ tin |
|---|---|---|---|
| Fed funds | 3,50–3,75%, giữ nguyên 12-0 (FOMC 17/06, phiên đầu của Chủ tịch Warsh) | 17/06 | 5 |
| Dot plot | Median cuối 2026 = **3,8%** (↑ từ 3,4%) → hàm ý ≥1 lần **TĂNG**; 8 giữ/9 tăng/1 cắt | 17/06 | 5 |
| CPI | +4,2% YoY (cao nhất từ 4/2023); core 2,9%; năng lượng +23,5% YoY | T5, cb 10/06 | 5 |
| PCE | 4,07% YoY; core 3,41%; 3m-annualized headline 6,28% | T5, cb 25/06 | 5 |
| NFP | T5: +172K (kỳ vọng 80K), thất nghiệp 4,3%. **T6 công bố 03/07**, consensus ~+100K | 05/06 | 5 |
| GDP Q1 (final) | +2,1% annualized (Q4/25: +0,5%); tiêu dùng thực chỉ +0,5% | 25/06 | 5 |
| ISM Mfg T6 | 53,3 (T5: 54,0); Prices Index rơi 9,1đ còn 73,0 | 01/07 | 5 |
| SOFR ON | **3,68%** | 30/06 | 5 |
| UST 2Y / 10Y | 4,17% / 4,47% (2s10s ~+30bp) | 01/07 | 4 |
| DXY | 101,4 (+0,21%) — safe-haven + Fed hawkish | 01/07 | 4 |
| USD/CNY fix | 6,8175, liên tục cao hơn ước Reuters → PBoC dung thứ CNY yếu dần | 29/06 | 3 |
| Dầu Brent | ~$74 (từ đỉnh >$110 T5) sau ngừng bắn Mỹ–Iran, Hormuz mở lại — **mong manh** | 29/06 | 4 |
| Thuế quan | S.122 10% toàn cầu hết hạn ~**24/07**; S.301 đề xuất **12,5%** với VN — comment 06/07, điều trần **07/07**; reciprocal VN giữ 20% | 06/2026 | 4 |

**[SUY LUẬN]** Fed đang ở chế độ "sốc cung dầu + lạm phát 4%" → chân USD của swap **không hạ trong tầm nhìn 1–2 quý**; rủi ro nghiêng về SOFR/term SOFR tăng.

### 1.2 Vĩ mô Việt Nam (R2)

| Chỉ số | Giá trị | as-of | Độ tin |
|---|---|---|---|
| CPI | T5: **+5,60% YoY**; bình quân 5T: +4,31% — **vượt mục tiêu ~4,5%**; kịch bản BTC: 4,5/5,0/5,5% | 06/06 | 5 |
| GDP | Q1: +7,83%; mục tiêu năm 2 con số (Q2 cần ~11%). **Q2 công bố ~06/07** | 04/04 | 5 |
| Cán cân TM | **Nhập siêu 16,8 tỷ USD** (đến 15/6) — đảo chiều sau 3 năm xuất siêu; FDI vẫn xuất siêu 5,8 tỷ | 15/06 | 4 |
| FDI | Đăng ký 5T: 24,81 tỷ (+34,9%); giải ngân 9,75 tỷ (+9,6%, cao nhất 5 năm) | 31/05 | 4–5 |
| Tín dụng | +4,42% YTD (28/4); **+18,26% YoY**; định hướng năm ~15% | 28/04 | 4 |
| Kiều hối | TP.HCM Q1: 2,0 tỷ USD, **−16,9% YoY** | Q1 | 4 |
| Dự trữ ngoại hối | ~**87,6 tỷ USD** (↑ từ 83,6 tỷ cuối 2025; đỉnh cũ 109,6 tỷ) | 18/06 | 4 |
| PMI T6 | **51,8** (T5: 52,8); tháng 12 liên tiếp >50; đơn XK chậm lại; việc làm giảm tháng thứ 4 | 01/07 | 5 |
| Khối ngoại CK | Bán ròng T6 ~15,3 nghìn tỷ; 6T: **~3 tỷ USD** (tháng thứ 6 liên tiếp) | 30/06 | 3 |

**[SUY LUẬN]** Tam giác ràng buộc của SBV 2026: **lạm phát vượt mục tiêu + tỷ giá kịch trần + mục tiêu tăng trưởng 2 con số** — ba mục tiêu kéo ba hướng; đây là biến số chi phối mọi tenor.

### 1.3 Rates & thanh khoản VND (R1, R5)

| Chỉ số | Giá trị | as-of | Độ tin |
|---|---|---|---|
| ON | ~3% (26/06, nguồn yếu) → 3,6% (29/06) → **13,0% (30/06)** | 30/06 | 4 |
| 1W / 2W / 1M | 8,5% / 8,0% / 8,1% (1M tăng từ 7,6%) | 30/06 | 4 |
| 3M | 7,75% (03/06) — 8,10% (tuần 22–26/06) · **DATA CŨ** | 06/2026 | 3 |
| ON/1W… phiên 01–02/07 | **CHƯA CÓ DATA** — điểm mù lớn nhất | — | — |
| OMO tuần 22–26/06 | Đảo chiều **bơm ròng ~3.962 tỷ**; bơm mới 30.962 tỷ kỳ hạn **35–56 ngày @4,5%**; lưu hành ~244.000 tỷ | 26/06 | 4 |
| OMO 30/06 | Chào 31.550 tỷ (7/35/56N), trúng 100% @4,5% → **bơm ròng ~14.600 tỷ** | 30/06 | 4 |
| Swap USD/VND SBV | Kích hoạt lại kỳ hạn **7 ngày**: mở 29/06, thực hiện 30/06 (mua USD spot – bơm VND – bán lại sau 7d); khối lượng KHÔNG công bố; **đáo hạn ~07/07**. Lần 3 trong 2026 (26/05, 01/06) | 30/06 | 4 |
| Tín phiếu SBV | Không thấy phát hành mới 26/06–02/07; nghi ~45.000 tỷ đáo hạn tuần 22–26/06 (chênh lệch số học, **chưa xác nhận**) | — | 2 |
| Swap points thị trường | Không có quote; định tính: "swap VND–USD dương và cao trên phần lớn kỳ hạn" (SHS/24hmoney) | ~T6 | 2 |

### 1.4 FX & chính sách SBV (R4, R6)

| Chỉ số | Giá trị | as-of | Độ tin |
|---|---|---|---|
| Tỷ giá trung tâm | **25.206** (giữ nguyên 01–02/07); +23đ/8 phiên; **tuần tăng thứ 7 liên tiếp**; YTD +0,3% | 02/07 | 4 |
| Trần / sàn ±5% | 26.466 / 23.946 | 02/07 | 5 |
| VCB | Mua 26.106 / **bán 26.466 = KỊCH TRẦN** (nhiều NH lớn cùng mức) | 01–02/07 | 3–4 |
| Tự do | 26.610 ÷ 26.720 (2 nguồn lệch ~100đ) — premium **150–250đ** trên trần | 01/07 | 2–3 |
| Sở GD SBV | Bán 26.404 (thấp hơn trần ~50đ) | 27/06 | 4 |
| Can thiệp | Kênh **forward 180 ngày @26.850** (hủy ngang) mở từ 24/03; KHÔNG thấy đợt bán spot mới 26/06–02/07; tuyên bố "sẵn sàng can thiệp" | 06/2026 | 3–4 |
| Lãi suất điều hành | Tái cấp vốn 4,5% / tái chiết khấu 3,0% — không đổi | 02/07 | 3 |
| **TT25/2026/TT-NHNN** | Hiệu lực **01/07**: nới tỷ lệ vốn ngắn hạn cho vay trung-dài hạn **30% → 40%** — thay đổi lớn nhất từ 2019 | 22/06 | 4 |
| Vàng SJC | Premium ~18,8 tr/lượng (**~14,6%**) so thế giới quy đổi | 01/07 | 4 |
| NDF offshore | KHÔNG TÌM ĐƯỢC quote (mảng mù kinh niên — cần terminal) | — | — |

---

## 2. CURVE (A1 · Curve Analyst)

### 2.1 Hình dạng curve LNH VND 30/06 [TÍNH TRỰC TIẾP]

```
ON 13,0 ──┐ inverted front cực gắt (ON − 1W = +450bps)
1W  8,5   ├─ belly phẳng ~8%, micro-kink trũng tại 2W
2W  8,0   │
1M  8,1   │
3M ~7,75–8,1 ┘ 6M–1Y: MẤT QUOTE (lỗ hổng data lặp lại khi thị trường căng)
```

- **Inverted front:** ON cao hơn toàn bộ phần còn lại — chữ ký kinh điển của **cú siết kỹ thuật cuối quý**, không phải kỳ vọng lãi suất.
- **Test kỳ hạn xác nhận tính kỹ thuật:** trong phiên 30/06 belly chỉ nhích +40–90bps trong khi ON +940bps → thị trường KHÔNG price căng thẳng kéo dài từ cú spike này.
- **Nhưng cái đáng chú ý hơn là LEVEL của belly:** 1W–3M đã đứng ~7,5–8,5% **suốt tháng 6** (trước cả chốt quý) — mặt bằng term funding VND đắt là hiện tượng **bền**, không phải nhiễu cuối quý.

### 2.2 So với snapshot 23/06 — CỜ TƯƠNG THÍCH DỮ LIỆU 🔴

Bộ mid user cung cấp 23/06 (ON 1,65 / 1M 3,55 / 1Y 3,80) **không tương thích** với chuỗi bình quân báo chí/SBV cùng kỳ (ON 6,2% ngày 22/06; 1M 7,6–7,8% suốt tháng). Không thể trộn hai nguồn để tính Δ "+450bps repricing":
- Mid quote màn hình tại 1 thời điểm ≠ bình quân gia quyền giao dịch cả ngày; ngày biến động mạnh lệch vài trăm bps là có thể.
- Không loại trừ bộ 23/06 ở thang/loại lãi suất khác.
→ **Kết luận về mức độ dịch chuyển curve chỉ dùng chuỗi báo chí (nội bộ nhất quán): belly ~8% ổn định cả tháng, front whipsaw 3%↔13%.** Cần user xác nhận nguồn/metric của bộ mid để đối chiếu.

### 2.3 Swap curve USD/VND [DERIVED từ CIP — chỉ tin dấu & hướng]

| Tenor | i_VND | i_USD (proxy) | Spread | Swap points (ước, spot 26.466) |
|---|---|---|---|---|
| ON | 13,0% (spike) | SOFR 3,68% | **+9,3đpt** | ~+6,8đ/ngày — sẽ xẹp cùng ON |
| 1W | 8,5% | ~3,68% | +4,8đpt | ~+25đ/tuần |
| 1M | 8,1% | ~3,6% | **+4,5đpt** | ~**+97đ** |
| 3M | ~7,9% | ~3,6% | +4,3đpt | ~**+265–290đ** |
| 6M (anchor thực) | — | — | — | Forward SBV 26.850 vs trần 26.466 = **+384đ ≈ 2,94%/năm** |

- **Đảo dấu lịch sử trong 1 tuần:** 23/06 đầu cong âm (~−2đpt) → 30/06 dương +9đpt tại ON — swing ~+1.100bps. Trạng thái "forward discount" ngắn hạn đã chết.
- **Per-annum spread giảm dần theo tenor** → swap curve (tính %/năm) **dốc xuống** từ front; điểm 6M của SBV (2,94%/năm) thấp hơn hẳn spread LNH-implied (~4đpt) → **forward SBV 26.850 mang tính "trợ giá/trấn an", KHÔNG dùng làm fair value CIP**.
- **Gap OMO 4,5% vs LNH 8% (+350bps) không tự khép** → nghi cạn collateral GTCG / phân mảng bank lớn–nhỏ; không giả định arbitrage hoàn hảo trên LNH VN.

### 2.4 Cờ chuyển A2
1. Vì sao belly đứng ~8% cả tháng dù ON có lúc rất thấp?
2. Vì sao spot kịch trần khi carry VND dương 4–9đpt?
3. SBV bơm VND (OMO dài + swap 7d) trong khi cần VND đắt để đỡ tỷ giá — logic gì?
4. TT25/2026 sẽ kéo đoạn dài curve đi đâu?

---

## 3. INSIGHT (A2 · đa giả thuyết)

### 3.1 ON 13% phiên 30/06 — kỹ thuật hay cấu trúc?
- **GT1 — Chốt quý kỹ thuật (NGHIÊNG VỀ MẠNH):** đúng ngày khóa sổ Q2; SBV bơm ròng 14.600 tỷ cùng phiên; belly không đuổi theo; pattern BCTC cuối quý trong memory **xác nhận lần đầu có data** (thẻ pattern: ✅ đúng). *Base rate:* mọi spike ON 2026 (17% T2, 11% đầu T6) xẹp sau 1–3 phiên khi SBV bơm.
- **GT2 — Căng cấu trúc lộ ra ở điểm yếu nhất:** tín dụng +18,26% YoY vượt xa huy động, LDR cao, hệ thống lệ thuộc OMO (~244.000 tỷ lưu hành). *Ủng hộ:* belly 8% bền cả tháng; SBV phải dùng swap FX 3 lần trong 5 tuần. *Phản đối:* không giải thích được timing chính xác 30/06.
- **Kết luận:** GT1 giải thích **cú spike**, GT2 giải thích **mặt bằng**. Hai tầng cùng đúng — và tầng GT2 mới là thứ định giá swap curve từ 1M trở ra.

### 3.2 Belly 8% bền — cái gì tái định giá?
- **GT1 — Funding gap cấu trúc + mùa vụ Q3 (NGHIÊNG VỀ):** tín dụng chạy trước huy động; kỳ thuế T7 + nhu cầu VND nửa cuối năm; bank price sẵn căng thẳng kéo dài (kỳ hạn 1W–3M "bắc qua" các sự kiện hút tiền).
- **GT2 — Phòng thủ tỷ giá ngầm:** giữ lãi suất VND term cao để carry đỡ spot kịch trần; SBV bơm @4,5% nhưng để LNH đứng 8% (không ép xuống). *Ủng hộ:* spot kịch trần cùng lúc; SBV chỉ bơm kỳ hạn, không hạ giá vốn. *Phản đối:* thiếu phát ngôn chính sách xác nhận.
- **GT3 — CPI 5,6% đẩy kỳ vọng lãi suất danh nghĩa:** lạm phát vượt mục tiêu → mặt bằng lãi suất thực phải dương hơn. *Ủng hộ:* CPI trend lên từ đầu năm. *Phản đối:* lãi suất điều hành chưa đổi.
- **Kết luận:** cộng hưởng cả ba, trọng số GT1 > GT2 > GT3.

### 3.3 Nghịch lý: carry dương lớn nhưng spot kịch trần
- **GT1 — Flow áp đảo (NGHIÊNG VỀ):** nhập siêu 16,8 tỷ + khối ngoại rút 3 tỷ + kiều hối −17% + mùa chuyển lợi nhuận FDI Q2–Q3 → cầu USD thực, không phải đầu cơ; carry không bù được cho nhà nhập khẩu **phải** mua USD.
- **GT2 — Kỳ vọng phá giá ăn hết carry:** premium tự do 150–250đ + vàng SJC +14,6% + trung tâm tăng 7 tuần liên tiếp → thị trường price tiếp tục trượt; nếu kỳ vọng mất giá ~4–5%/năm thì carry 4,5đpt ≈ hòa. *Đây chính là thông điệp của swap points dương lớn: "giá của phòng thủ", không phải free lunch.*
- **GT3 — Event risk thuế quan:** trước 07/07 và 24/07, không ai dám short USD/VND dù carry hấp dẫn.
- **Kết luận:** GT1 nền + GT2/GT3 khuếch đại. Falsify GT2: nếu sau tin thuế quan tích cực mà spot vẫn dính trần → GT1 thuần flow.

### 3.4 SBV đang chơi chiến lược gì? [đọc hành vi]
Bơm OMO **kỳ hạn dài** (không phải 7N thuần) + swap FX 7d (bơm VND mà **không tốn dự trữ**, còn tăng dự trữ tạm thời) + trung tâm tăng **chậm có kiểm soát** + **chưa** bán USD spot + forward 180d @26.850 "treo trấn an":
→ **Chiến lược câu giờ 3 mặt trận:** giữ hệ thống đủ VND qua chốt quý/kỳ thuế (tránh sự cố thanh khoản), giữ spot bằng trần hành chính thay vì đốt dự trữ (87,6 tỷ ≈ vùng đệm mỏng so chuẩn 3 tháng nhập khẩu khi NK đang phi mã), và chờ qua event risk thuế quan tháng 7 rồi mới quyết hướng. **Chấp nhận:** LNH term đắt (8%) và spot dính trần kéo dài.
→ **Hàm ý quan trọng nhất:** khi cả 3 mặt trận cùng căng (thuế xấu + Fed tăng + kỳ thuế), công cụ "câu giờ" hết tác dụng → bước kế tiếp là **nâng trung tâm nhanh hơn** hoặc **bán USD spot** — cả hai đều làm swap curve giật mạnh.

### 3.5 TT25/2026 (30%→40%) và đoạn dài curve
- **Ngắn hạn:** giảm áp lực huy động vốn trung-dài hạn → hạ nhiệt cạnh tranh lãi suất huy động 6M–12M → **đoạn dài curve có lực xuôi xuống tương đối so với belly** (flatten 3M–12M).
- **Trung hạn:** chính là để mở room tín dụng phục vụ mục tiêu tăng trưởng → cầu funding tổng thể TĂNG → không đổi hướng mặt bằng.
- **Rủi ro đuôi:** nới ratio khi LDR đã cao = tăng maturity mismatch hệ thống → nhạy cảm hơn với spike thanh khoản tương lai.

### 3.6 Ba insight quan trọng nhất (ranked)
1. **Đọc curve 2 tầng:** spike ON là nhiễu chốt quý — **belly 8% mới là tín hiệu**; swap points 1M–3M dương ~4–4,5đpt/năm phản ánh căng funding cấu trúc + phòng thủ tỷ giá, sẽ không biến mất trong vài phiên.
2. **Swap points dương lớn = giá của rủi ro phá giá, không phải cơ hội một chiều:** spot kịch trần + premium tự do + vàng + 2 mốc thuế quan (07/07, 24/07) — vị thế ăn carry VND term đang bán bảo hiểm cho đúng các sự kiện đó.
3. **SBV đang câu giờ bằng công cụ phi dự trữ** — theo dõi **ngày 07/07 (đáo swap 7d: roll hay không?)** như tín hiệu sớm nhất về việc SBV còn muốn đỡ thanh khoản hay chuyển sang siết để bảo vệ tỷ giá.

---

## 4. DỰ BÁO (A3 · falsifiable)

### 4.1 ON & front-end (mốc: 03–08/07)
- **Base (65%):** ON rơi từ 13% về **4–7%** trong 1–4 phiên sau chốt quý (chậm nhất phiên 08/07); 1W về 6,5–8%. *Điều kiện:* SBV duy trì bơm/roll swap 7d ngày 07/07. *Cơ sở:* tiền lệ 100% các spike 2026 xẹp ≤3 phiên.
- **Up (20%):** ON giữ **>8%** qua 08/07 nếu SBV không roll swap (hút VND đáo hạn 07/07) + tỷ giá căng sau điều trần 301.
- **Down (15%):** ON về **<3,5%** nếu SBV bơm mạnh tay + tin thuế quan tích cực.
- **Pre-mortem:** nếu sai, khả năng cao nhất là đánh giá thấp lượng VND bị hút khi swap 7d đáo + kỳ quyết toán thuế sớm — ON kẹt 8–10% thêm 1 tuần.

### 4.2 USD/VND đến 31/07
- **Base (60%):** spot **bám/sát trần suốt tháng 7** (chênh với trần <80đ); trung tâm tăng đều **+10–25đ/tuần** → **25.250–25.310** cuối T7 (trần ~26.51–26.58); SBV **chưa** bán USD spot, tiếp tục swap/forward. *Điều kiện:* S.301 chưa chốt mức thuế cuối; FOMC giữ lãi suất 29/07.
- **Up-risk phá giá nhanh (25%):** S.301 áp 12,5% với VN hoặc S.122 thay bằng mức cao hơn (~24/07) → trung tâm tăng tốc **>30đ/tuần**, premium tự do **>300đ**, SBV buộc bán USD (spot hoặc forward đợt mới) trong **≤2 tuần** sau tin.
- **Down (15%):** VN thoát nhóm 12,5% + NFP 03/07 yếu (<60K) kéo DXY <100 → spot rời trần **>100đ** trước 15/07.
- **Pre-mortem:** nếu sai theo hướng down, lý do khả dĩ nhất là dòng USD đột biến (FDI giải ngân lớn/phát hành TP quốc tế) mà team không track được real-time.

### 4.3 Belly 1M–3M & swap points (đến 31/07)
- **Base (55%):** 1M–3M giữ **7,5–8,5%** qua kỳ thuế (VAT 20/07, TNDN 30/07 — có gia hạn làm nhẹ); swap points 3M dương ~**+250–320đ** (spread ~4đpt/năm ±0,5). *Điều kiện:* SBV giữ khuôn khổ hiện tại, thuế quan chưa ngã ngũ.
- **Soften (30%):** sau chốt quý + TT25 phát huy → belly xuôi về **6,5–7,5%** cuối T7 **nếu** áp lực tỷ giá dịu (spot rời trần); swap points 3M co về ~+180–250đ.
- **Tail (15%):** FOMC hawkish surprise / thuế quan xấu → cả curve VND lên chế độ phòng thủ, **1M >9%**, swap points front bùng nổ như 30/06.
- **Tenor rủi ro repricing nhất:** **1W–2W** (bắc qua đáo swap 07/07 + hạn VAT 20/07) và **mọi kỳ hạn bắc qua 24/07**.
- **Pre-mortem:** nếu Base sai, khả năng cao nhất là đánh giá thấp lực hút của kỳ thuế trong năm tín dụng chạy 18% YoY — belly lên 9% thay vì đứng 8%.

### 4.4 TRIGGER THEO DÕI (ngày check cụ thể)
| Ngày | Trigger | Xác nhận/bác bỏ |
|---|---|---|
| 03/07 | NFP Mỹ T6 (~100K) | DXY/chân USD — kịch bản 4.2 |
| 03–06/07 | ON/1W fixing sau chốt quý | 4.1 Base vs Up |
| ~06/07 | GDP Q2 + CPI T6 VN (GSO) | GT3 mục 3.2; áp lực chính sách |
| **07/07** | **SBV roll swap 7d? + điều trần S.301** | Tín hiệu sớm nhất toàn hệ thống |
| 20/07 | Hạn VAT T6 — ON/1W có bật? | 4.3 |
| ~24/07 | Số phận S.122/thuế mới với VN | 4.2 Up-risk |
| 29/07 | FOMC + họp báo | 4.3 Tail |
| Hằng phiên | OMO ròng; VCB có rời trần 26.466; premium tự do | Tất cả |

---

## 5. RỦI RO / BẤT ĐỒNG (Reviewer · red-team)

1. **Đòn vào luận điểm mạnh nhất ("belly 8% là cấu trúc"):** toàn bộ so sánh "3,7% → 8%" dựa trên **hai nguồn không tương thích** (mid user 23/06 vs bình quân báo chí). Nếu bộ mid của user hôm nay vẫn cho 1M ~3,5% thì narrative đổ. → *Data chứng minh SAI:* user cung cấp snapshot mid 30/06–02/07 từ cùng nguồn cũ. **Yêu cầu số 1 cho turn sau.**
2. **"SBV chưa bán USD spot" là absence of evidence** (không có tin ≠ không xảy ra) — độ tin chỉ 3. Nếu SBV đã âm thầm bán, đánh giá "dự trữ chưa bị đụng" sai.
3. **Base 4.1 (ON xẹp) có gót chân Achilles đúng ngày 07/07:** swap 7d đáo hạn hút VND về SBV ngay giữa cửa sổ dự báo — tiền lệ "xẹp 1–3 phiên" các lần trước KHÔNG có yếu tố này.
4. **Mọi số swap points là DERIVED** (thiếu Term SOFR + quote thật + NDF) — cấm dùng số tuyệt đối để trade; chỉ dùng dấu/hướng/độ lớn tương đối.
5. **Điểm mù 6M–1Y:** mất quote đoạn dài từ 23/06 — kết luận "flatten đoạn dài nhờ TT25" hiện là suy luận chưa có giá kiểm chứng.
6. **Đánh giá: PASS CÓ ĐIỀU KIỆN** — hướng phân tích vững, nhưng (a) mọi so sánh với 23/06 phải mang cờ tương thích; (b) 4 khoảng trống data (mục 6) phải được vá trước khi nâng mức tin.

**Bất đồng còn treo:** A2 nghiêng "belly 8% = cấu trúc bền", Reviewer giữ khả năng "8% chủ yếu là premium mùa vụ Q2/Q3 + phòng thủ tỷ giá, sẽ xuôi nhanh nếu spot rời trần". Không ép một đáp án — trigger phân xử: belly sau 24/07 (qua event thuế quan) còn ≥7,5% hay không.

---

## 6. ĐỘ TIN & FRESHNESS

| Mảng | Độ tin | Ghi chú |
|---|---|---|
| Macro Mỹ (Fed, CPI, PCE, NFP, ISM) | **Cao (5)** | Nguồn gốc chính thức, mới |
| Macro VN (CPI T5, XNK, FDI, PMI) | Cao (4–5) | **CPI T6/GDP Q2 chưa có — chờ ~06/07** |
| Rates VN 30/06 (ON 13%, belly 8%) | Khá (4) | Qua báo chí, chưa đối chiếu bản gốc SBV (proxy 403) |
| **Phiên 01–02/07 (sau chốt quý)** | **KHÔNG CÓ** | Điểm mù lớn nhất của báo cáo |
| Swap points theo tenor | **Thấp (2)** | DERIVED; thiếu Term SOFR, quote thật, NDF |
| "SBV chưa bán USD spot" | Trung bình (3) | Suy từ vắng tin |
| So sánh với curve 23/06 | **Thấp** | Nguồn không tương thích — chờ user xác nhận metric |

**Cần bổ sung để nâng chất (ưu tiên):** (1) snapshot mid curve của user 30/06–02/07 cùng nguồn với 23/06; (2) ON/OMO phiên 01–02/07; (3) SBV có roll swap 07/07; (4) Term SOFR 1M/3M + quote swap points/NDF thực.

---

## 7. CHẤM DỰ BÁO CŨ (Journalist)

**Dự báo 23/06:** "ON bật về ≥3,0% trong 3–7 phiên (quanh 26–30/06)" — Base 55%.
**Thực tế:** ON 3,6% (29/06) → 13% (30/06). → **✅ ĐÚNG** (đúng hướng, đúng cửa sổ thời gian).
**Ghi chú calibration:** biên độ dự báo quá hẹp — thực tế (13%) vượt cả kịch bản up-risk (4–6%); cơ chế cũng lệch một phần: up-risk giả định "SBV hút VND để giữ tỷ giá", thực tế ON spike do cầu chốt quý **trong khi SBV bơm kỷ lục**. Bài học: kịch bản up cần tách "lãi suất tăng do SBV siết" khỏi "lãi suất tăng do cầu mùa vụ khi SBV vẫn bơm".
**Scoreboard: 1/1 (hit-rate 100%, n=1).**

---

## Nguồn chính
Fed/FOMC & SEP 17/06 · BLS CPI/NFP · BEA GDP/PCE · ISM 01/07 · FRED SOFR/UST · NSO/GSO VN · S&P Global PMI VN · Hải quan/VnEconomy (nhập siêu) · Dân trí & VnExpress 01/07 (ON 13%, swap SBV) · Vietstock (OMO tuần) · TBTCVN & VTV Money (tỷ giá trung tâm) · LuatVietnam/MBS (TT25/2026) · Vietnam Briefing/Dorsey/Tax Foundation (thuế quan) · tygiausd.org/giavang.net (tự do, vàng). URL đầy đủ lưu trong log research từng agent.

---
*Báo cáo theo schema bàn giao nội bộ. FACT tách khỏi SUY LUẬN; mọi dự báo có mốc + xác suất để Journalist chấm. Toàn bộ pipeline chạy model Fable 5 theo yêu cầu user.*
