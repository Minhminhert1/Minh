# schema.md — Hợp đồng bàn giao giữa agent

> Mọi agent truyền tin theo format CỨNG dưới đây. Lỏng lẻo = lỗi chất lượng + tốn token.
> Quy tắc vàng: **Research chỉ nêu FACT + nguồn. OPINION/suy diễn để Analysis lo.**

---

## 1. Research → Research Lead (mỗi data point)

```
- [chỉ số]: [giá trị]
  nguồn: [tên nguồn] | as-of: [YYYY-MM-DD HH:mm ICT] | độ tin: [1–5]
  ghi chú: [1 dòng FACT, không suy diễn]
```

- **độ tin**: 5 = nguồn chính thức (SBV, Fed); 3 = báo/đại lý; 1 = tin đồn/chưa xác minh
- **as-of**: bắt buộc. Thiếu timestamp = data không dùng được
- Data mâu thuẫn → liệt kê **cả hai**, không tự chọn

---

## 2. Research Lead → Analysis (gói chuẩn hóa)

```
## DATA PACK — [chủ đề] — [ngày]
### Rates & Liquidity (R1)   | ### Macro VN (R2) | ### Global (R3)
### Policy/SBV (R4)          | ### Flow (R5)     | ### Others (R6)
[mỗi mục: data points theo format §1, đã loại trùng/lọc liên quan]

### FRESHNESS FLAGS
- [chỉ số nào quá hạn / thiếu] → Analysis phải tránh kết luận dựa vào
```

---

## 3. Analysis (BỘ NÃO) → Strategy / Reviewer / Orchestrator

> v3: MỘT mạch, không tách A1/A2/A3 thành báo cáo rời. Convention input phải khai báo trước (luật #9).

```
## PHÂN TÍCH — [USD/VND hoặc tenor] — [ngày]
### Thesis (1 dòng) | Bias [BULL/BEAR/NEUTRAL] | Confidence [L/M/H] | Horizon
### Macro 2 phía: VN [...] | Global [...]   — mỗi điểm có FACT + nguồn
### Trái tim: [driver cốt lõi] — đào sâu + base-rate lịch sử
### Tín hiệu ẩn: [cơ chế ít người thấy, không mô tả bề mặt]
### (MODE SWAP nếu input là curve):
    - Convention: [i_VND? chênh lãi? swap points?]  ← BẮT BUỘC
    - Shape | Swap points (đồng, đã sanity-check) | Fair value/CIP | Insight tenor (đa giả thuyết)
### Bull case | Bear case | Điều kiện vô hiệu hóa
### Forecast (FALSIFIABLE): [số] trong [mốc] | trigger 1 con số: [...] | xác suất [%]
    (dẫn base-rate đã chấm hoặc ghi "prior") | Pre-mortem: [nếu sai, lý do khả dĩ nhất]
```

## 3b. Analysis → Strategy (khi nhận định đủ rõ)
```
- Bias + confidence + key levels + điều kiện vô hiệu hóa → Strategy dựng setup (xem agents/strategy)
```

---

## 4. Reviewer → Orchestrator

```
## REVIEW
- **Input đúng convention chưa?** Đơn vị + định nghĩa số gốc (i_VND? chênh lãi? điểm/đồng?) [khớp?]
- **Tái tính số chủ chốt độc lập + sanity-check độ lớn** (đối chiếu mốc thực tế) [khớp / lệch tầm?]
- **Mọi nhận định có FACT + nguồn neo chưa?** Chỗ nào chỉ [ƯỚC LƯỢNG] mà kết luận như thật → cờ.
- Tấn công luận điểm mạnh nhất của A2/A3: [...]
- Data nào sẽ chứng minh nhận định SAI? [observable cụ thể + mốc; không trả lời được → loại]
- Blind spot phát hiện: [...]
- Đánh giá: PASS / CẦN SỬA ([sửa gì]) / BẤT ĐỒNG ([nêu cả 2 phía])
```

---

## 5. Orchestrator → User (báo cáo cuối)

```
## TỔNG QUAN   — bức tranh swap USD/VND hiện tại (2–3 câu)
## CURVE       — hình dạng + điểm đáng chú ý (từ A1)
## INSIGHT     — lý do từng tenor đang vậy (từ A2)
## DỰ BÁO      — kịch bản + mốc thời gian + xác suất (từ A3)
## RỦI RO/BẤT ĐỒNG — Reviewer lưu ý gì
## ĐỘ TIN & FRESHNESS — data đủ mới không, chỗ nào yếu
```
