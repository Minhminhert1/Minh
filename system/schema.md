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

## 3. Analysis → Reviewer / Orchestrator

```
## ANALYSIS — [chủ đề] — [ngày]

### A1 · Curve
- Hình dạng: [steepen/flatten/twist/...] | điểm bất thường: [kink ở tenor nào]
- Fair value gap: [tenor X lệch ~Y điểm so với CIP/lịch sử]

### A2 · Insight theo tenor (ĐA GIẢ THUYẾT)
- Tenor [X]: hiện tượng [...]
  • Giả thuyết 1: [...] — ủng hộ: [...] | phản đối: [...]
  • Giả thuyết 2: [...] — ủng hộ: [...] | phản đối: [...]
  • Nghiêng về: [GT số mấy] vì [...]
- Base rate: [thống kê lịch sử liên quan]

### A3 · Forecast (FALSIFIABLE — bắt buộc)
- Dự báo: [tenor/curve] về [con số] trong [mốc thời gian]
- Điều kiện kích hoạt: [...]
- Xác suất: [%] | Pre-mortem: "nếu sai, lý do khả dĩ nhất: [...]"
```

---

## 4. Reviewer → Orchestrator

```
## REVIEW
- Tấn công luận điểm mạnh nhất của A2/A3: [...]
- Data nào sẽ chứng minh nhận định SAI? [nếu không trả lời được → loại]
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
