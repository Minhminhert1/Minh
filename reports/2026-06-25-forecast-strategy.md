# Forecast + Strategy — Swap USD/VND — 2026-06-25

> Turn đặc biệt: **cả team chạy Opus** (A3 Forecast + Strategy + Reviewer), theo yêu cầu user.
> Giai đoạn HỌC — ý tưởng để phản biện, KHÔNG phải lệnh trade. Chưa có risk/compliance.
> Curve nguồn: interbank thực (user thu thập, mid). **Thiếu Bid/Ask** → xem mục Blind spot.

---

## TỔNG QUAN
Curve LNH gãy ở đầu ngắn do **chốt quý 30/06** (ON 0.30 sụp vì thừa thanh khoản, 1W 4.35 vọt vì vắt qua mốc quý). Nền vĩ mô nóng + đối ngoại căng (CPI 5.6%, nhập siêu kỷ lục, spot sát trần, thuế Mỹ 8/2026) tạo **áp lực mất giá VND**, nhưng SBV đang **chọn thả thanh khoản** (ưu tiên tăng trưởng) thay vì hút VND cứu tỷ giá. **Trục lật toàn cục: SBV còn thả hay xoay sang hút.**

---

## DỰ BÁO (đã hiệu chỉnh theo Reviewer)

> Reviewer cảnh báo: dự báo dễ thành "cược ngược lỗi 23/06" — vừa sai vì tưởng SBV hút, nay đừng neo cứng "SBV thả". Đã **hạ Base, nâng Up**.

### Sau chốt quý (02–07/07)
| Tenor | Base ~45–50% | Up (SBV hút) ~35% | Down ~15% |
|-------|-------------|-------------------|-----------|
| ON | 0.5–1.2% | 2.0–3.5% | <0.30% |
| 1W | 2.3–2.8% | 3.5–4.0% | ~2.0% |
- Điều kiện Base: spot <26.50 **và** không có tín phiếu SBV hút ròng tuần 30/06–04/07.
- Mốc chấm: **07/07**. Rủi ro nằm SAU chốt quý (02–04/07), không phải trước.

### 1 tháng (cuối 7, trước thuế 8/2026)
- Base ~50%: term 1M–1Y đi ngang (3.4–3.75%), ON 0.8–1.8%. **Chênh lãi suất VND–USD 3M ~ −0.1 đến −0.2%** (âm nhẹ — bất thường, là nguồn áp lực mất giá VND).
- Up ~35%: CPI T6 >5% + spot phá trần → SBV hút/nâng OMO → cả đường +30–50bp.
- Down ~15%: SBV bơm tiếp ưu tiên tăng trưởng.

### 3 tháng (Q3, gồm thuế 8/2026)
- Base ~50%: H2 tín dụng bung + thuế siết cung USD → SBV **dần trung tính–thắt nhẹ** → term VND nhích +10–30bp, chênh VND–USD bò về **0 đến +0.4%**. VND mất giá có kiểm soát (lộ trình 26.8 hợp lý).
- Up ~35%: CPI >6% → SBV thắt thật, cả curve dịch lên.
- Down ~15%: thuế làm tăng trưởng hụt → ép nới → LNH mềm, VND mất giá nhanh.

### Swap points USD/VND (suy từ chênh lãi suất; SOFR ~3.62%)
| Tenor | Dấu | Ghi chú |
|-------|-----|---------|
| ON | **ÂM mạnh** | VND 0.30 << USD 3.62 |
| 1W | **DƯƠNG tạm** | méo chốt quý, sẽ về ~0/âm sau 30/06 |
| 1M–3M | **~0 / âm nhẹ** | |
| 1Y | **~0 / dương nhẹ** | dốc lên dần |
Xu hướng 3 tháng: nếu Base đúng (SBV thắt nhẹ H2) → points **dương hóa dần**, curve points dốc lên.

### Biến số lật kịch bản (theo dõi hằng ngày)
SBV phát tín phiếu hút ròng · spot phá trần & SBV bán USD · CPI T6/T7 >6% · thực thi thuế 8/2026 · Fed cắt SOFR (tự nới chênh dương).

---

## CHIẾN LƯỢC (xếp theo risk-reward, đã ghép phản biện)

| # | Chiến lược | Loại | Carry | Tin (sau review) | Phán quyết Reviewer |
|---|-----------|------|-------|------------------|---------------------|
| 1 | Pay 1W / Receive 1M | flattener méo chốt quý | **ÂM ~95bp** | VỪA (hạ từ CAO) | CẦN SỬA |
| 2 | Receive 3M–6M | carry chênh âm | mỏng/âm | **BẤT ĐỒNG** | nêu cả 2 phía |
| 3 | Pay 1Y / Receive 3M | steepener bear | âm | THẤP–VỪA | nửa học |
| 4 | Pay 1M–3M | hedge tail SBV hút | âm khi chờ | VỪA kịch bản | gộp với #2 |
| 5 | Quan sát 1W–ON | observe | n/a | thuần học | OK |

### #1 — Pay 1W / Receive 1M (đặt cược 1W xẹp sau chốt quý)
- **Luận điểm:** bướu 1W thuần do vắt 30/06, sẽ tan khi qua mốc.
- **Reviewer đập:** (a) đây là consensus ai cũng thấy → có thể **đã nằm trong giá**; (b) **carry âm ~95bp** (pay 4.35 / receive 3.40) — chờ lâu là chảy máu; (c) rủi ro thực nằm 02–04/07, không phải trước 30/06.
- **Vào/Ra:** chỉ vào nếu spread 1W–1M còn ≥ +0.80; thoát ngay 01–03/07 khi 1W reset. **Invalidation: ON >1.5% trước 30/06, hoặc tín phiếu hút ròng, hoặc 1W chưa xẹp sau 04/07.**

### #2 — Receive 3M–6M (carry) ⟷ #4 — Pay 1M–3M (hedge): CHỌN MỘT
- Reviewer: giữ cả hai = **book tự chống nhau trên đoạn 3M, đốt carry hai chiều = trả tiền để không có view** (triệu chứng hedge-mọi-hướng sau cú trượt 23/06).
- **BẤT ĐỒNG về #2 (nêu cả 2 phía):**
  - *Phía Strategy:* receive đầu term ăn carry khi SBV còn thả, thanh khoản dư — **tin VỪA**, ưu tiên 1–2M (ngắn) hơn 3–6M.
  - *Phía Reviewer:* receive 3–6M **đi ngược chính forecast 3M của A3** (thắt nhẹ H2) + carry âm/mỏng (VND 3.45 < SOFR 3.62) — **tin THẤP** cho hold dài.
- **Khuyến nghị tổng hợp:** nếu tin "SBV còn thả" → **net receive ngắn (1–2M), bỏ #4**. Nếu lo tail FX → **net pay (#4), bỏ #2**. Đừng giữ cả hai.

### #3 — Pay 1Y / Receive 3M (steepener bear)
- View đúng hướng rủi ro vĩ mô (lạm phát/tỷ giá/thuế đẩy term dài lên) nhưng **carry âm mỗi ngày** → chỉ đặt nhỏ để học phản ứng curve dài. Tin THẤP–VỪA.

### #5 — Quan sát 1W–ON
- Đo tốc độ 1W hội tụ ON sau 30/06 → calibrate playbook chốt quý cho 30/09. Ghi vào memory.

---

## RỦI RO / BẤT ĐỒNG (Reviewer)
- **Phán quyết tổng: 4 CẦN SỬA + 1 BẤT ĐỒNG, không cái nào PASS thẳng.**
- Cảnh báo tâm lý: cú trượt 23/06 đang biến Forecast thành **cược-ngược** và Strategy thành **hedge-mọi-hướng** — phản ứng sau lỗi, không phải edge.
- **Blind spot CHẶN:** **không có Bid/Ask** → không xác nhận được "cạnh thực" của bất kỳ trade nào (mid không phản ánh chi phí thực thi). Còn thiếu: **depth/thanh khoản thực thi, NDF offshore, kết cấu kỳ hạn can thiệp SBV, outflow chuyển lợi nhuận FDI cuối quý**.

---

## ĐỘ TIN & FRESHNESS
- Curve LNH: interbank thực, độ tin 4–5 — nhưng **mid-only**.
- Cần làm mới trước khi đặt cược thật: **Bid/Ask, OMO/tín phiếu phiên nay (R1/R4), tỷ giá trung tâm & spot realtime, NDF**.
- Mọi dự báo đều có mốc chấm: 07/07 · cuối 7 · cuối Q3.
