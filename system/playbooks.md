# playbooks.md — Đường ray theo loại câu hỏi (v3)

> Orchestrator chọn playbook theo intent. v3: mặc định chạy GỌN (Research → Bộ não → Strategy →
> Reviewer), KHÔNG spawn cả roster (luật #11). Sub-lens R/A chỉ dùng nội bộ khi cần đào sâu.
> Mọi báo cáo lớn theo `report-template.md` (luật #14).

---

## PB-FULL · "Phân tích USD/VND cho tôi" (báo cáo directional/macro — KIỂU BẢN 19/06) ⭐
```
Research (tra sources.md: tỷ giá TT, spot, chợ đen, Fed/DXY, CPI/cán cân TM, dự trữ, NDF…)
   → Bộ não (macro 2 phía → trái tim: gap lãi suất → tín hiệu ẩn → bull/bear → forecast)
   → Strategy (setup + proxy + phân khúc đối tượng)
   → Reviewer (lỗ hổng có mức độ + kịch bản đảo chiều)
   → Orchestrator dựng báo cáo theo report-template
```
Dùng khi: hỏi tổng quan/hướng USD/VND, báo cáo đầy đủ. **Đây là playbook chủ lực.**

## PB-SWAP · "Đây là curve/tenor, phân tích đi" (MODE swap)
```
Research (R1 rates/liquidity + R4 SBV + R5 flow) → Bộ não MODE SWAP
   (định nghĩa convention #9 → shape → swap points #10 → fair value → insight/tenor → forecast)
   → Strategy (pay/receive, RV tenor, turn play) → Reviewer
```
Dùng khi: user dán swap curve / bảng theo tenor. **Bắt buộc định nghĩa convention trước khi tính.**

## PB-WHY · "Vì sao [tenor/spot/chỉ số] biến động?"
```
Research (mảng liên quan) → Bộ não (đa giả thuyết, tìm tín hiệu ẩn) → Reviewer
```

## PB-FWD · "Tuần/tháng tới ra sao?"
```
Research (calendar sự kiện sắp tới + global) → Bộ não (kịch bản + ma trận + EV) → Reviewer
```

## PB-DAILY · Báo cáo sáng (tự động 5h)
```
Research gom số qua đêm (gọn) → Bộ não (có gì đổi? 1–2 điểm nóng) → Orchestrator tóm tắt → reports/
```
Output ngắn: "đổi gì qua đêm + 1–2 điểm đáng chú ý + watch level".

## PB-ALERT · Cảnh báo watchlist (chạm ngưỡng)
```
Research (mảng liên quan) → Bộ não (nguyên do, đa giả thuyết) → Journalist (tiền lệ quá khứ) → Reviewer
```
Xem `watchlist.md`. Báo ngay, không chờ 5h sáng.

## PB-LEARN · "Giải thích khái niệm / dạy tôi"
```
Orchestrator/Bộ não trả lời trực tiếp — gọi ví dụ từ data thật nếu cần
```

---

## Quy tắc chung
- Playbook là gợi ý, không phải xiềng — thiếu data thì bổ sung research (nguồn THẬT, luật #8).
- Luôn kết thúc bằng Reviewer trừ PB-LEARN.
- Mọi dự báo phải có **trigger 1 con số + mốc** → Journalist mới chấm được (luật #13).
- Mặc định **1 bộ não dệt 1 mạch**; chỉ tách sub-lens thành subagent khi cần nhiều nguồn song song.
