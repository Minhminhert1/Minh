# BÁO CÁO TỔNG HỢP — USD/VND · FX · SWAP
**Ngày: 2026-06-24 · Hệ thống multi-agent (toàn squad chạy Opus theo yêu cầu) · Giai đoạn: HỌC**

> Quy trình: Wave 1 (Global/US macro · VN macro+SBV · Curve+swap) → Wave 2 (Insight+Forecast+Strategy) → Wave 3 (Reviewer red-team). Các con số xác suất & kết luận **đã áp chỉnh sửa của Reviewer**. Phần dưới tách rõ **FACT / OPINION / [ƯỚC LƯỢNG]**.

---

## 0. TÓM TẮT ĐIỀU HÀNH (đọc cái này trước)

- **Bức tranh:** Đường cong funding VND **gãy đôi** — ON sụp 0.55% (thừa thanh khoản qua đêm) trong khi **1W vọt 3.70%** (có bid 4.0 xuyên offer 3.80). Spot USD/VND ~**26.43 sát trần** (tâm 25.183, trần ~26.442). Đây là cấu hình **"turn-of-quarter premium dồn vào tenor ôm đêm chốt quý 30/06"** chồng lên **nền phòng thủ tỷ giá** của SBV.
- **Bản chất:** Mâu thuẫn "ON rẻ vs spot căng" **không** phải nghịch lý — VND **dư tức thời** nhưng **chênh lãi VND–USD âm** + kỳ vọng mất giá khiến không ai muốn giữ VND → ép spot. Vấn đề là **giá vốn VND, không phải thiếu VND**.
- **Câu hỏi quyết định:** Cú căng 1W là **thời vụ thuần** (xẹp sau 30/06) hay **khởi đầu một đợt siết bền** của SBV để đỡ đồng? → **Điểm chấm dứt khoát: lãi 1W ngày 03/07.**
- **Trade ưu tiên #1 (sau red-team):** **RV bán 1W / mua 2W** đánh hội tụ hậu turn — chứ KHÔNG phải turn-play receive-ON (cái này EV gần 0/âm nếu SBV bơm OMO phủ turn).
- **3 việc phải làm trước khi xuống tiền:** (1) xác nhận **lịch đáo hạn tín phiếu/OMO** quanh 30/06; (2) soi **NDF/CCS offshore** (kỳ vọng phá giá thật); (3) kiểm **độ sâu của bid 4.0** (có phải lệnh lẻ/ảo không).

---

## 1. CURVE — SỐ LIỆU & HÌNH DẠNG

### 1.1 Bảng lãi suất LNH/implied VND (%/năm) — FACT (giá thị trường)

| Tenor | Bid | Ask | Mid | Δ vs 06-23 (bps) |
|---|---|---|---|---|
| ON | 0.40 | 0.70 | **0.55** | −110 |
| 1W | 3.60 | 3.80 | **3.70** (bid 4.0 xuyên offer) | +190 |
| 2W | 3.10 | 3.50 | 3.30 | −25 |
| 3W | 3.40 | 3.70 | 3.55 | — |
| 1M | 3.10 | 3.60 | 3.35 | −20 |
| 2M | 3.30 | 3.60 | 3.45 | — |
| 3M | 3.10 | 3.60 | 3.35 | −35 |
| 6M | 3.40 | 3.90 | 3.65 | — |
| 9M | 3.50 | 3.90 | 3.70 | — |
| 1Y | 3.60 | 4.00 | 3.80 | 0 |

### 1.2 Hình dạng — mổ từng đoạn (A1)

```
i_VND mid (%)
3.8 |                                         ●9M ●1Y
3.7 |  ●1W                                ●6M
3.5 |       ●3W     ●2M
3.4 |
3.3 | ●2W       ●1M     ●3M
0.6 |●ON
    +-ON-1W-2W-3W-1M-2M-3M---6M-9M-1Y->
```

- **(a) ON dip 0.55%:** đáy curve, thanh khoản qua đêm dư, tiền gần như free.
- **(b) Kim 1W 3.70% (turn premium):** bước nhảy ON→1W = **+315bps**. 1W là tenor *duy nhất bắc trọn đêm chốt quý 30/06* → toàn bộ phí "ôm qua turn" dồn vào đây, khiến 1W **cao hơn cả 2W/1M/3M**. Bid 4.0 xuyên offer = cầu thật (cần xác nhận độ sâu — xem §7).
- **(c) Lõm 2W 3.30%:** 2W (14 ngày) cũng trùm 30/06 nhưng cú spike 1 đêm bị **pha loãng trên 14 ngày** → mid thấp hơn 1W. Dấu hiệu kinh điển: turn nằm gọn trong 1W.
- **(d) Belly phẳng 2W–3M (~3.3–3.55), răng cưa:** đi ngang, dao động ~25bps. Spread bid/ask 50bps → **thanh khoản mỏng, mid độ tin THẤP**.
- **(e) Đuôi dốc nhẹ lên (6M 3.65 → 1Y 3.80):** +15bps/bước, định giá chênh lãi cấu trúc, **không stress dài hạn**.

> **Tóm:** toàn bộ "drama" nằm ở đoạn ≤1W; từ 1M trở đi curve lành. Dịch chuyển 06-23→06-24 là **re-pricing riêng đoạn ngắn** (không song song) → sự kiện **thanh khoản/lịch**, không phải đổi view lãi suất cấu trúc.

---

## 2. SWAP POINTS & FAIR VALUE (A1)

### 2.1 Swap points theo tenor (ra ĐỒNG)
Công thức: `SP = 26.430 × (i_VND − i_USD)/100 × days/360`. *(i_USD = [ƯỚC LƯỢNG]: SOFR ON 3.62; 1W 3.6 / 1M 3.7 / 3M 3.9 / 6M 4.0 / 1Y 4.1)*

| Tenor | i_VND | i_USD* | Δi (bps) | days | Swap points (đồng) | Dấu |
|---|---|---|---|---|---|---|
| ON | 0.55 | 3.62 | −307 | 1 | **−2.3** | discount |
| 1W | 3.70 | 3.60 | +10 | 7 | **+0.5** | ~0 / premium nhẹ |
| 2W | 3.30 | 3.65 | −35 | 14 | **−3.6** | discount |
| 1M | 3.35 | 3.70 | −35 | 30 | **−7.7** | discount |
| 3M | 3.35 | 3.90 | −55 | 90 | **−36.3** | discount |
| 6M | 3.65 | 4.00 | −35 | 180 | **−46.3** | discount |
| 1Y | 3.80 | 4.10 | −30 | 360 | **−79.3** | discount |

- Hầu hết tenor **forward discount (SP âm)**: i_VND < i_USD → mua USD kỳ hạn rẻ hơn spot. Trạng thái "bình thường mới" khi VND yếu hơn USD về lãi suất.
- **Vết lõm về ~0 tại 1W (+0.5 đồng):** cú spike i_VND 1W kéo Δi về dương nhẹ → swap points 1W **nhô ngược lên** giữa vùng âm = **dấu vân tay của turn chốt quý**.
- Đuôi discount sâu dần (1Y −79) thuần do **carry tích lũy theo days**, không phải stress.

### 2.2 Fair value / CIP & "tính ngược ON đêm chốt"
- **1W lệch CIP rõ nhất:** đường trơn cho 1W "đáng lẽ" ~3.3–3.4; phần **+30–40bps dư = turn premium thuần** (phí khan thanh khoản qua mốc, KHÔNG phải arbitrage free-lunch).
- **Term-spread ON→1W = +315bps** là **phần thưởng cho rủi ro turn** (phải roll ON 6–7 đêm, đêm 30/06 ON có thể bắn 2 chữ số), **không phải lệch giá hốt được không rủi ro**.
- **Tính ngược (đã hạ cấp theo Reviewer):** 1W 3.70 ngụ ý ON đêm chốt có thể **bắn lên 2 chữ số**. Con số minh họa ~20–23% (giả định 6 đêm ~0.55% + 1 đêm turn) là **kịch bản cực đoan, không phải dự báo điểm** — vì mid của một thị trường *inverted* (bid>offer) là số kém tin để tính ngược, và mức cao có thể trải đều nhiều đêm thay vì một đêm.

---

## 3. VĨ MÔ — VIỆT NAM & CHÍNH SÁCH SBV

### 3.1 Macro VN (R2)
> Số liệu 2026 nằm **sau cutoff 1/2026** → [ƯỚC LƯỢNG]; chỉ **cơ chế/xu hướng** là chắc.

- **Nền không xấu:** VN cấu trúc **xuất siêu** + **FDI giải ngân** ổn định + **kiều hối** → lo phần **cung USD cấu trúc** (độ tin cơ chế 4/5).
- **Áp lực tỷ giá KHÔNG do macro xấu** mà do **chênh lãi VND–USD âm + kỳ vọng mất giá + mùa vụ + tâm lý**.
- **Dự trữ ngoại hối mỏng** [ƯỚC LƯỢNG ~3 tháng nhập khẩu] → **hạn chế dư địa bán USD kéo dài** → SBV ưu tiên **công cụ lãi suất** hơn đốt dự trữ.
- Tăng trưởng tín dụng (room ~14–16%) → cầu VND cao, áp lực thanh khoản kỳ hạn.

### 3.2 Khung & hành vi can thiệp SBV (R4)
- **Tỷ giá trung tâm** công bố hằng ngày, spot dao động **biên ±5%**. Tâm 25.183 → **trần ≈ 26.442**; spot 26.43 = **gần chạm trần** (room ~0.05%).
- **3 lớp phòng thủ khi spot ép trần:** (1) nới tỷ giá trung tâm; (2) bán USD giao ngay/kỳ hạn; (3) **hút VND / đẩy lãi suất ngắn lên** (tín phiếu, ngưng bơm OMO) để thu hẹp chênh lãi âm.
- **Đọc trạng thái hiện tại:** ON 0.55% ⇒ SBV **chưa hút mạnh kênh qua đêm**; 1W 3.70%+ ⇒ thị trường đang **định giá lại funding bắc qua chốt quý**. Đường funding **dốc đứng đoạn ngắn** = căng *kỳ hạn cụ thể*, không phải căng *tổng lượng*.

### 3.3 Flow & seasonality (R5)
- **Chốt quý 30/06 (cơ chế, tin 5/5):** window-dressing + CAR + dự trữ bắt buộc/LDR → **cầu VND kỳ hạn ôm 30/06 vọt, cung nhỏ giọt** → đẩy lãi tenor *chứa ngày 30/06* (chính là 1W lúc này) lên cao, trong khi ON (đáo trong tháng) vẫn rẻ. **Đây là lời giải trực tiếp cho ON 0.55% vs 1W 3.70%+.**
- **Nộp thuế cuối quý** (GTGT/TNDN) → hút VND về KBNN → thêm áp lực funding.
- **Đáo hạn tín phiếu/OMO quanh 30/06: CHƯA BIẾT — biến quyết định** (xem §7).

---

## 4. VĨ MÔ — MỸ & TOÀN CẦU (R3, chân USD của swap)

> **Chỉ 1 số là FACT:** SOFR ON **3.62%** (as-of 2026-06-18). Mọi số khác sau cutoff → [ƯỚC LƯỢNG], tin ≤ 3/5.

- **Fed & USD rate:** SOFR 3.62% ⇒ band suy ra ~3.50–3.75% [ƯỚC LƯỢNG]; Fed **gần trung tính**, kỳ vọng **giữ hoặc 1–2 lần cắt 25bp nửa cuối 2026**. Chân USD term ~**3.4–3.6%** (3M–1Y) — đây là **mẫu số** của swap points.
- **Bảng chân USD [ƯỚC LƯỢNG]:** 1W ~3.60 · 1M ~3.58 · 3M ~3.52 · 6M ~3.45 · 1Y ~3.38 (SOFR term, đảo nhẹ → phẳng); UST 10Y ~4.1–4.35.
- **DXY ~97–101** (USD hạ nhiệt so đỉnh); **DXY > 103 = cờ đỏ** cho VND.
- **Trung Quốc — neo dẫn truyền mạnh nhất:** USD/CNH ~7.10–7.30; **CNH > 7.30 = cờ đỏ** kéo VND mất giá theo → SBV phải can thiệp.
- **Hàm ý:** Fed nghiêng cắt + DXY hạ + CNY ổn → **giảm sức ép VND**, dư địa swap points nhích lên (bớt âm). Ngược lại "higher for longer" / DXY>103 / CNH>7.30 → **cộng hưởng ép VND**.

---

## 5. INSIGHT THEO TENOR (A2 — đa giả thuyết)

### ON (0.55%) — "VND thừa qua đêm vs spot sát trần"
- **GT-A (~70%):** lệch pha thanh khoản kỳ hạn — VND dư *tức thời*, nhưng thị trường định giá căng *phía trước* (turn + chênh lãi âm). ON rẻ không mâu thuẫn spot căng.
- **GT-B (~30%):** SBV chủ động giữ ON thấp để không bóp nghẹt kinh tế, xử tỷ giá bằng công cụ khác → ON 0.55 là *được phép*, có thể bị kéo lên đột ngột.
- **Loại bỏ phản đề:** "ON rẻ = VND dồi dào nên tỷ giá tự hạ" — SAI; carry âm vẫn ép VND yếu dù không thiếu VND.

### 1W (3.70, bid 4.0 xuyên offer) — KIM TURN
- **GT-A (~55% — đã hạ từ 75% theo Reviewer):** turn-of-quarter premium thuần, xẹp sau 30/06.
- **GT-B (~30%):** khởi đầu siết bền của SBV để đỡ tỷ giá → sẽ lan ra 2W–1M, không xẹp.
- **"Lai" (~15%):** turn **khuếch đại** một xu hướng siết đã chớm (GT-A và GT-B **không loại trừ nhau**).
- **Phân định:** ON *đêm 30/06* và 1W *ngày 03/07*. A → xẹp nhanh; B → giữ cao + lan tenor.

### Belly 2W–1M (3.30–3.55) — LÕM SAU KIM, MẤP MÔ
- **GT-A (~60%):** hiệu ứng pha loãng turn; răng cưa = nội suy trên sổ mỏng, **mid độ tin THẤP**.
- **GT-B (~30%):** belly là vùng "thật" nhất (3.3–3.55 = mặt bằng cân bằng), ON/1W mới là méo.
- **Hệ quả:** belly **không dùng làm neo trade trực tiếp** (spread 50bps), chỉ đọc hướng hội tụ.

### Đuôi 3M–1Y (3.35–3.80) — ĐỊNH GIÁ CHÊNH LÃI CẤU TRÚC
- **GT-A (~65%):** định giá hợp lý theo carry, đuôi **ít méo nhất**.
- **GT-B (~35%):** đuôi đang định giá **thiếu** rủi ro mất giá/siết → nếu SBV siết bền, 6M–1Y phải dốc hơn → đuôi **rẻ = cơ hội pay**.

---

## 6. DỰ BÁO (FALSIFIABLE — đã sửa theo Reviewer)

> Mỗi dự báo: số + mốc + điều kiện + xác suất + pre-mortem. Đây là **OPINION** của A3.

### Ngắn hạn (→ 03/07)
- **DB-1 — ON đêm chốt:** đêm 30/06 ON LNH **bắn lên 2 chữ số (≥ ~8%, có thể test 15–20%+)** rồi **về < 3% trong ≤ 02/07**. *Xác suất 60%.* **Bác bỏ nếu:** ON đêm 30/06 < 8% (SBV phủ OMO) HOẶC ON vẫn > 5% sau 02/07 (siết bền). *Pre-mortem:* SBV bơm OMO/repo phủ turn (kịch bản B) → ON bị ghìm.
- **DB-2 — 1W hậu turn:** 1W xẹp từ 3.70 về **2.8–3.4 trong 02–04/07**, bid 4.0 biến mất. *Xác suất 60%.* **Bác bỏ nếu:** 1W vẫn > 3.5% ngày 04/07 hoặc bật > 4%. *Pre-mortem:* GT-B đúng (siết bền).

### Trung hạn (1–3 tháng, → ~24/09)
- **DB-3 — hình curve:** sau turn curve **mượt lại**, kim 1W & lõm 2W biến mất, belly hội tụ **3.35–3.50**, đuôi giữ dốc nhẹ 3.6–3.9 (1Y). *Xác suất 55%.* **Bác bỏ nếu:** belly ra ngoài 3.3–3.6 sau 1 tuần hoặc đuôi dốc mạnh > 4.2. *Pre-mortem:* sốc CNH>7.30 / DXY>103, hoặc SBV siết bền.
- **DB-4 — chênh lãi đuôi:** 3M–1Y giữ **âm nhẹ đến cân bằng (−0.5% đến +0.5%)**; discount 1Y trong **−60 đến −95 điểm**. *Xác suất 55%.* *Pre-mortem:* Fed cắt sớm (USD<3.4) hoặc SBV nâng nền VND.

### Tỷ giá
- **DB-5 — spot vs trần:** spot **dán trần ~26.44 nhưng KHÔNG đóng cửa dưới (trần −0.3%) quá 3 phiên liên tiếp trước 31/07**; nếu chạm, SBV phản ứng bằng **lãi suất (1W/ON) trước, bán USD sau**. *Xác suất 60%.* *Pre-mortem:* CNY phá mạnh → SBV nới tâm thay vì đốt dự trữ.
- **DB-6 — nới tâm:** xác suất SBV **nới biên/tăng tỷ giá trung tâm trong 3 tháng ~25%** (cao hơn nếu CNH>7.30 / DXY>103). Mốc chấm: tỷ giá trung tâm công bố hằng ngày.

---

## 7. RỦI RO, BẤT ĐỒNG & BLIND SPOT (Reviewer)

### Kịch bản can thiệp SBV quanh 30/06 — **đã calibrate**
| # | Kịch bản | Xác suất (sửa) | Tác động swap |
|---|---|---|---|
| A | Đỡ tỷ giá bằng lãi suất, để 1W căng | **~37%** (hạ từ 45%) | swap points kỳ ngắn dâng & giữ |
| B | Bơm OMO phủ turn rồi hạ nhiệt | **~38%** (nâng từ 30%) | 1W xẹp nhanh đầu Q3 |
| C | Bán USD giao ngay | **~15–20%** | spot dịu nhưng hút VND → 1W căng thêm |
| D | Nới tỷ giá trung tâm | **~10%** | giải toả spot; swap points dài dâng |

> ⚠️ **A và B KHÔNG loại trừ nhau** — SBV thường làm *cả hai* (bơm OMO VÀ giữ lãi ngắn nhỉnh). Bộ xác suất gốc nghiêng về "câu chuyện đẹp" (A + GT-A), under-weight kịch bản nhàm-nhưng-base-rate-cao (B).

### Blind spot bắt buộc lấp trước khi giao dịch
1. **NDF / cross-currency basis offshore** — toàn bộ phân tích là onshore; "view chênh lãi" sống ở NDF/CCS. NDF 1M–3M phá giá rộng hơn onshore → GT-B nặng hơn. **Không nhìn NDF = mù một mắt.**
2. **Lịch đáo hạn tín phiếu/OMO quanh 30/06** — nếu lượng lớn đáo hạn → VND tự bơm về, turn premium tự xẹp, turn-play hỏng. **Biến quyết định đang để trống.**
3. **Độ sâu bid 4.0** — inverted market thường mỏng; cả "kim 1W" có thể dựng trên 1 lệnh lẻ.
4. **KBNN/thuế cuối quý**, **rủi ro CITAD/settlement đêm chốt** (ảnh hưởng *thực thi* trade), **can thiệp hành chính SBV** (room tín dụng, "trần phi chính thức", gọi điện NHTM — không nằm trong A–D).
5. **i_USD ước lượng** chảy thẳng vào mọi swap point.

### Đánh giá cuối: **CẦN SỬA → đã áp** (probabilities & falsifiability đã chỉnh ở trên)

---

## 8. CHIẾN LƯỢC TRADE (đã xếp lại ưu tiên theo Reviewer)

> Giai đoạn HỌC — chưa risk limit. "pay X" = trả lãi VND kỳ X (lời nếu lãi VND lên). "sell&buy USD" = bán USD spot + mua lại forward (≈ cho vay VND).

| # | Trade | Verdict Reviewer | Vào khi |
|---|---|---|---|
| **(b)** | **RV bán 1W / mua 2W** (đánh hội tụ hậu turn) | **PASS — ƯU TIÊN #1** | Ngay |
| (c) | Tránh term-spread ON→1W naked | **PASS** | — (kỷ luật) |
| (d) | Pay đuôi 6M–1Y nếu siết bền | **PASS có điều kiện** | Sau trigger |
| (a) | Turn play receive-ON đêm chốt | **BẤT ĐỒNG** | Chỉ sau khi xác nhận §7 |

### (b) ⭐ RV bán 1W / mua 2W — **ưu tiên #1**
- **Hướng:** receive 1W (~3.7–4.0) + pay 2W (~3.3) — đánh **hội tụ** khi turn qua.
- **Lý do:** 1W bị bóp turn (tạm), 2W bị pha loãng (tạm); sau 30/06 hội tụ về belly. **Lời dù mức tuyệt đối ON thế nào** (ít phụ thuộc đoán mức ON), self-financing.
- **Entry:** ngay. **Mục tiêu:** spread 1W−2W từ +40bps về < +10bps. **Thoát:** 03–07/07.
- **Rủi ro:** GT-B đúng (1W không xuống, 2W lên theo); spread bid/ask belly 50bps ăn mòn lời → **chỉ vào nếu nửa spread < kỳ vọng lời.** Size nhỏ-trung bình.

### (c) Tránh term-spread ON→1W naked
- 315bps là **phí bảo hiểm rủi ro roll**, không phải arbitrage. Roll ON fund 1W = nhặt xu trước xe lu (đêm 30/06 ON có thể nuốt sạch carry). **Giữ kỷ luật: không làm naked.**

### (d) Pay đuôi 6M–1Y — directional, có điều kiện
- **Hướng:** pay 6M–1Y nếu tin SBV siết bền (GT-B đuôi); đuôi 3.65–3.80 đang rẻ so rủi ro.
- **Trigger (định nghĩa trước, chờ xác nhận):** (i) 1W vẫn ≥ 3.8 *sau* 03/07; HOẶC (ii) CNH>7.30 / DXY>103; HOẶC (iii) ON > 5% giữ > 5 phiên sau 03/07; HOẶC (iv) NDF 3M phá giá nới rộng.
- **Mục tiêu:** 1Y 3.80 → 4.3–4.6. **Thoát:** SBV hạ nhiệt / CNH < 7.10. Size trung bình khi trigger bật, 0 khi chưa.

### (a) Turn play receive-ON đêm chốt — **BẤT ĐỒNG, hoãn**
- **Team:** hấp dẫn nhất (catalyst ngày rõ). **Reviewer:** EV gần 0/âm — payoff nằm ở đuôi mỏng (ON bắn 2 chữ số) mà ≥38% xác suất SBV bơm OMO phủ turn làm ON không bắn; lại chịu **carry âm** khi chờ.
- **Chỉ vào nếu cả 3 đúng:** (1) lịch tín phiếu **không** bơm VND quanh turn; (2) độ sâu bid 4.0 thật; (3) break-even ON < ~10%. **Trước đó: KHÔNG vào.**

---

## 9. ĐỘ TIN & FRESHNESS FLAGS

| Mục | Trạng thái |
|---|---|
| Curve LNH, spot 26.43, biên ±5%, chốt quý 30/06 | **FACT** (giá thị trường) |
| SOFR ON 3.62% | FACT nhưng **as-of 18/06 (cũ ~6 ngày)** |
| Chân USD term (1W–1Y) | **[ƯỚC LƯỢNG]** → mọi swap points & lệch CIP belly/đuôi phụ thuộc trực tiếp |
| Macro VN 2026 (CPI/GDP/tín dụng/dự trữ) | **[ƯỚC LƯỢNG] sau cutoff** — cần TCTK/SBV/GSO |
| Lịch đáo hạn tín phiếu/OMO quanh 30/06 | **THIẾU — quyết định kịch bản A/B** |
| OMO bơm-hút ròng tuần này, lượng SBV bán USD | **THIẾU** |
| NDF/CCS offshore | **THIẾU — blind spot lớn nhất** |
| Độ sâu bid 4.0 (1W) | **CHƯA xác nhận** |
| Xác suất kịch bản & dự báo | OPINION — đã red-team & calibrate |

---

*Báo cáo do hệ thống multi-agent tạo (toàn squad Opus theo yêu cầu phiên này; các phiên sau quay về phân bổ model trong CLAUDE.md). FACT/OPINION tách bạch; dự báo falsifiable có mốc; đã qua Reviewer.*
