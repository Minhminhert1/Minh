# Memory — Journalist Agent

## Tổng kết hiệu suất team

| Tháng | Số setup | Thắng | Thua | Winrate | R:R TB |
|-------|----------|-------|------|---------|--------|
| - | - | - | - | - | - |

---

## Bài học lớn nhất theo tháng

*(ghi insight quan trọng nhất mỗi tháng)*

---

## Log các trade / dự báo

### SCOREBOARD DIRECTIONAL — dự báo bản 19/06 (đang mở, chấm khi data tới)
| # | Dự báo (con số + mốc) | Trigger 1 con số | Hạn chấm | Base | Trạng thái |
|---|----------------------|------------------|----------|------|-----------|
| D1 | USD/VND Q4/2026 = **26.600–26.840** | đóng cửa Q4 trong range | 31/12/2026 | 60% (bear) | 🟡 mở |
| D2 | EV cuối Q4 ~ **26.500–26.700** (prob-weighted) | spot cuối Q4 | 31/12/2026 | base | 🟡 mở |
| D3 | Fed **giữ 3.50–3.75%** cả 2026 (kịch bản 50%) | không cắt/tăng tới 31/12 | mỗi FOMC | 50% | 🟡 mở |
| D4 | Chợ đen chạm **26.550** (trần ngầm forward) | giá bán chợ đen ≥ 26.550 | rolling | — | 🟡 mở |
| D5 | Cán cân TM Q2 **vẫn thâm hụt** (thesis cấu trúc) | Q2 < 0 | ~đầu T8 | 55% | 🟡 mở |
> Quy tắc #13: đầu mỗi phiên chấm D# nào tới hạn TRƯỚC khi phân tích mới. Đúng/sai → cập nhật base-rate.

### Log swap (mode rates)
- **[2026-06-23] Dự báo ON ≥3.0% trong 3–7 phiên (quanh 26–30/06), base 55%.**
  → [2026-06-24] ON literal vẫn 0.55% (chưa đạt theo ON); nhưng funding turn căng thật ở **1W 3.70%**.
  Dự báo neo nhầm tenor (ON) thay vì 1W. Chấm chốt sau 30/06.
- **[2026-06-24] Dự báo 1W ≥ 3.5% tới 30/06; ON có thể vẫn < 1.5%, base 55%.** Chấm sau 30/06.

### Bài học calibration đang hình thành
- **Neo dự báo đúng tenor:** seasonality cuối quý hiện ở 1W/2W (bắc qua ngày chốt), không ở ON.
  Phát biểu dự báo "ON tăng" dễ sai dù bản chất (funding turn căng) đúng.
- **Bẫy 1 điểm dữ liệu sai đổi cả luận điểm:** turn này đọc nhầm 1W (1.15 vs 3.70) → đảo kết luận
  curve. Quy trình: verify giá 1W/2W trước khi chốt hình dạng front.

---

## Xu hướng lỗi của team

*(ghi khi thấy cùng loại sai lặp lại nhiều lần)*
