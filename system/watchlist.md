# watchlist.md — Ngưỡng cảnh báo biến động nóng

> Khi một chỉ số chạm ngưỡng → kích **PB-5**: bóc nguyên do + tìm tiền lệ quá khứ.
> Ngưỡng là khởi điểm — Journalist hiệu chỉnh theo thực tế (ghi vào memory).

---

## Cách hoạt động
1. R-squad (chủ yếu R1 Haiku) đọc số mới → so với phiên trước & ngưỡng dưới.
2. Chạm ngưỡng → gắn cờ `🔴 ALERT` → Orchestrator chạy PB-5.
3. A2 tìm **nguyên do** (đa giả thuyết). Journalist tra `memory.md` tìm **lần tương tự trong quá khứ** → ra rồi sao.
4. Reviewer kiểm tra suy diễn. Báo cáo bạn ngay (không chờ 5h sáng).

---

## Ngưỡng mặc định (tăng/giảm NÓNG)

| Chỉ số | Ngưỡng cảnh báo | Mảng |
|--------|-----------------|------|
| LNH O/N (qua đêm VND) | đổi > **50 bps**/phiên, hoặc vượt 4.5% / dưới 1.0% | R1 |
| Swap points 1M | đổi > **20 điểm**/phiên | R1 |
| Swap points 3M | đổi > **30 điểm**/phiên | R1 |
| Tỷ giá trung tâm SBV | đổi > **15 đồng**/phiên | R4 |
| USD/VND spot | chạm/vượt biên độ trần ±5% | R4 |
| SBV phát hành/đáo hạn tín phiếu | **trạng thái đổi chiều** (ngừng↔phát hành lại) | R1/R4 |
| OMO bơm/hút ròng | > **20.000 tỷ**/phiên | R1 |
| SOFR | đổi > **15 bps**/phiên | R3 |
| DXY | đổi > **0.8%**/phiên | R3 |
| CNY (USD/CNH) | đổi > **0.6%**/phiên | R3 |
| NDF 1M offshore vs onshore | chênh > **ngưỡng bất thường** (cập nhật sau) | R6 |

---

## Format cảnh báo

```
🔴 ALERT — [chỉ số] — [ngày giờ ICT]
- Giá trị: [mới] (trước: [cũ], đổi: [Δ])
- Nguyên do khả dĩ (A2): 1)… 2)…
- Tiền lệ quá khứ (Journalist): [lần gần nhất tương tự] → diễn biến sau đó: […]
- Hàm ý cho curve/tenor: […]
- Độ tin: [1–5]
```

---

## Hiệu chỉnh
- Ngưỡng kêu quá nhiều (nhiễu) → nới. Bỏ sót biến động thật → siết.
- Mỗi lần hiệu chỉnh ghi lý do vào `agents/research/r1-rates-liquidity/memory.md`.
