# report-template.md — Chuẩn báo cáo (gold standard)

> **Mẫu tham chiếu:** `benchmarks/2026-06-19-USDVND-gold-standard.pdf` — bản user tâm đắc nhất.
> Mọi báo cáo lớn nhắm tới mức này. Báo cáo daily/alert có thể gọn hơn nhưng giữ DNA #1–#4.
> Số liệu vẫn tuân luật #8–#10 (grounding, định-nghĩa-input, sanity-check). KHÔNG độn ước lượng.

---

## DNA bắt buộc (cái làm bản 19/06 hay)

1. **THESIS-FIRST.** Mở bằng box: **Bias · Confidence · Horizon · Target** + **một dòng tóm tắt**.
   Đọc 10 giây là biết "kèo" gì. (vd: 🔴 Bearish VND / Med-High / 3–6T / 26.600–26.840.)
2. **XƯƠNG SỐNG TỰ SỰ.** Một câu chuyện trung tâm, khung đặt tên đáng nhớ ("Ba làn sóng",
   "Cuộc chiến thầm lặng"). Người đọc phải NHỚ được luận điểm, không chỉ đọc bảng số.
3. **ĐÀO TÍN HIỆU ẨN.** Tìm cơ chế ít người thấy (vd: forward hủy ngang 26.550 = trần ngầm
   "câu giờ không đốt dự trữ"). Insight = phơi cái dưới bề mặt, KHÔNG mô tả lại giá.
4. **MỌI SỐ NEO NGUỒN + NGÀY** + list nguồn cuối bài. Có layer "Data thô".
5. **MỘT "TRÁI TIM" phân tích** — chọn driver cốt lõi (vd gap lãi suất thực) đào sâu + lịch sử.
6. **MA TRẬN KỊCH BẢN + EV** — lưới xác suất 2 chiều (vd Fed × thuế quan → vùng giá), target weighted.
7. **REVIEWER CỤ THỂ** — N lỗ hổng có mức độ (HIGH/MED/LOW) + **kịch bản đảo chiều nguy hiểm nhất**.
8. **DASHBOARD VẬN HÀNH** — watch-level + **action trigger** + **điều kiện vô hiệu hóa thesis**.
9. **PHÂN KHÚC HÀNH ĐỘNG** theo đối tượng (trader / NK / XK / FDI / nhà đầu tư).
10. **CONTEXT** — so sánh peer (EM Asia) + lịch sử để định cỡ luận điểm.
11. **THÀNH THẬT VỀ GIỚI HẠN** — managed float, data stale, độ tin từng mục.

---

## Skeleton (theo mẫu 19/06)

```
1. EXECUTIVE SUMMARY        — box thesis (Bias/Confidence/Horizon/Target) + 1 dòng
2. CÂU CHUYỆN THỊ TRƯỜNG    — big picture, khung tự sự, các "làn sóng"
3. DATA THÔ (Research)      — bảng số có nguồn + as-of
4. PHÂN TÍCH SÂU (Analysis) — macro 2 phía + TRÁI TIM (gap/curve) + tín hiệu ẩn + bull/bear
5. SETUP/CHIẾN LƯỢC         — proxy + setup trực tiếp (entry/SL/TP/RR) + theo đối tượng
6. PHẢN BIỆN (Reviewer)     — N lỗ hổng + mức độ + kịch bản đảo chiều nguy hiểm nhất + verdict
7. KẾT LUẬN                 — bức tranh + roadmap mốc + ma trận kết quả + EV + khuyến nghị
8. APPENDIX                 — lịch sự kiện + dashboard trigger + so sánh peer + nguồn
```

> **Phân biệt sản phẩm:** bản 19/06 là **directional SPOT/macro** (3–6 tháng). Báo cáo **swap
> curve/rates** dùng cùng DNA nhưng "trái tim" là chênh lãi theo tenor + swap points (luật #9!).

---

## SCORECARD — Reviewer tự chấm TRƯỚC khi gửi (mỗi mục 0/1/2; cần ≥ 16/20)

| # | Tiêu chí | 0 = thiếu | 2 = đạt chuẩn 19/06 |
|---|----------|-----------|---------------------|
| 1 | Thesis box (Bias/Conf/Horizon/Target + 1 dòng) | không có | đọc 10s hiểu kèo |
| 2 | Xương sống tự sự đáng nhớ | liệt kê rời | có khung tên + nhớ được |
| 3 | Tín hiệu ẩn (cơ chế dưới bề mặt) | mô tả giá | phát hiện cơ chế ít người thấy |
| 4 | Mọi số neo nguồn + ngày | số trôi nổi | có nguồn + as-of + list cuối |
| 5 | Một "trái tim" đào sâu + base-rate | dàn trải | 1 driver + lịch sử |
| 6 | Ma trận kịch bản + EV | 1 chiều | lưới 2D + EV |
| 7 | Reviewer N lỗ hổng có mức độ + kịch bản đảo chiều | khen suông | ≥3 lỗ hổng + worst-case |
| 8 | Dashboard watch-level + trigger + vô hiệu hóa | không | có trigger 1 con số |
| 9 | Phân khúc hành động theo đối tượng | chung chung | trader/NK/XK/FDI riêng |
| 10 | Ngắn-ra-quyết-định + sanity-check số (luật #10,#12) | độn | mỗi mục đổi 1 quyết định |

> < 16/20 → **chưa gửi**: Reviewer chỉ rõ mục thiếu, trả về Bộ não/Strategy bổ sung.
> Số bất thường về độ lớn (luật #10) = tự động trượt mục #10 → dừng soi lại.
