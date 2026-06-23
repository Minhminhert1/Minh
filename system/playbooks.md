# playbooks.md — Đường ray theo loại câu hỏi

> Orchestrator chọn playbook theo intent để **chỉ gọi agent cần thiết** (tiết kiệm token)
> và giữ chất lượng nhất quán. Không gọi thừa researcher.

---

## PB-1 · "Đây là 1 đường curve, phân tích đi"
```
A1 (mổ curve) → R1 + R4 + R5 (giải thích nền) → A2 (insight/tenor) → A3 (dự báo) → Reviewer
```
Dùng khi: user dán swap curve / bảng swap points các tenor.

## PB-2 · "Vì sao tenor X biến động?"
```
R1 + R5 (+ R4 nếu nghi chính sách) → A2 (đa giả thuyết) → Reviewer
```
Dùng khi: hỏi nguyên nhân một tenor cụ thể nhảy/tụt.

## PB-3 · "Tuần/tháng tới ra sao?"
```
R3 + R4 (sự kiện sắp tới từ calendar) → A3 (kịch bản base/up/down) → Reviewer
```
Dùng khi: hỏi triển vọng, dự báo phía trước.

## PB-4 · Báo cáo sáng (DAILY — tự động 5h)
```
R1 + R3 (Haiku, gom số qua đêm) → A1 (curve có đổi?) → A2 (1–2 insight nóng) → Orchestrator tóm tắt
```
Output ngắn: "có gì đổi qua đêm + 1–2 điểm đáng chú ý". Ghi vào `reports/YYYY-MM-DD.md`.

## PB-5 · Cảnh báo watchlist (TRIGGERED — biến động nóng)
```
R(mảng liên quan) → A2 (tìm nguyên do) → JOURNALIST (tìm tiền lệ quá khứ trong memory) → Reviewer
```
Dùng khi: một chỉ số chạm ngưỡng trong `system/watchlist.md`. Xem chi tiết ở watchlist.

## PB-6 · "Giải thích khái niệm / dạy tôi"
```
Orchestrator trả lời trực tiếp (giai đoạn học) — gọi A2 nếu cần ví dụ từ data thật
```
Dùng khi: user hỏi kiến thức nền, không cần data realtime.

---

## Quy tắc chung
- Playbook là gợi ý, không phải xiềng — thiếu data thì bổ sung researcher.
- Luôn kết thúc bằng Reviewer trừ PB-6.
- Mọi dự báo (A3) phải có mốc thời gian → Journalist mới chấm được.
