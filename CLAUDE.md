# CLAUDE.md — FX Research Multi-Agent System

## Mục đích repo
Hệ thống multi-agent phục vụ nghiên cứu và phân tích thị trường Forex.
Gồm 7 agent với vai trò riêng biệt, phối hợp để đưa ra phân tích chất lượng cao.

---

## NGUYÊN TẮC BẮT BUỘC (đọc trước mỗi turn)

1. **Đọc `memory.md` ở root trước** — chứa bài học tích lũy của toàn hệ thống
2. **Đọc `agents/<role>/memory.md`** của agent liên quan trước khi kích hoạt
3. **Sau mỗi turn, cập nhật memory** — không để bài học bị mất
4. **Commit CLAUDE.md + memory.md cùng nhau** — không commit riêng lẻ
5. **Không bao giờ bỏ qua bước REVIEWER** — mọi setup phải qua phản biện

---

## CẤU TRÚC HỆ THỐNG

```
CLAUDE.md              ← luật hệ thống (file này)
memory.md              ← bộ nhớ tổng của toàn team
agents/
├── orchestrator/      ← điều phối, tổng hợp
├── research/          ← thu thập data
├── analysis/          ← phân tích kỹ thuật + macro
├── strategy/          ← đề xuất setup giao dịch
├── reviewer/          ← phản biện, tìm lỗ hổng
├── journalist/        ← ghi chép, học từ kết quả
└── teacher/           ← giải thích cho user dễ hiểu, liền mạch
```

---

## LUỒNG XỬ LÝ CHUẨN

```
User query
    ↓
[ORCHESTRATOR] phân tích intent
    ↓
[RESEARCH] thu thập data thô
    ↓
[ANALYSIS] phân tích & đánh giá
    ↓
[STRATEGY] đề xuất setup cụ thể
    ↓
[REVIEWER] phản biện, tìm rủi ro
    ↓
[ORCHESTRATOR] tổng hợp → báo cáo cho user
    ↓
[JOURNALIST] ghi lại toàn bộ quá trình

[TEACHER] kích hoạt khi user chưa hiểu / cần giải thích lại
   → dịch kết quả của team thành 1 mạch dễ hiểu, không rời rạc
```

---

## QUY TẮC CẬP NHẬT MEMORY SAU MỖI TURN

| Câu hỏi | Ghi vào |
|---------|---------|
| Team học được gì mới? | `memory.md` (root) |
| Research thiếu data nguồn nào? | `agents/research/memory.md` |
| Analysis có pattern mới nào? | `agents/analysis/memory.md` |
| Strategy có rule mới nào? | `agents/strategy/memory.md` |
| Reviewer phát hiện blind spot gì? | `agents/reviewer/memory.md` |
| Trade outcome ra sao? | `agents/journalist/memory.md` |
| User hiểu lầm gì / cách giảng nào hiệu quả? | `agents/teacher/memory.md` |

---

## PHONG CÁCH LÀM VIỆC

- User: Minhminhert1
- Ngôn ngữ: Tiếng Việt
- Phong cách: Ngắn gọn, thực tế, không dài dòng
- Kỳ vọng: Claude tự làm, không hỏi thừa
- Domain: FX Research & Analysis

---

## CHECKLIST CUỐI MỖI TURN

- [ ] Đọc memory.md trước khi làm
- [ ] Chạy đúng luồng 6 agent
- [ ] Không bỏ qua REVIEWER
- [ ] Cập nhật memory các agent liên quan
- [ ] Push PR với message rõ ràng

---

## LỊCH SỬ

| Ngày | Version | Thay đổi |
|------|---------|---------|
| 2026-06-19 | v1.0 | Khởi tạo FX multi-agent system |
| 2026-06-22 | v1.1 | Thêm agent TEACHER (giáo viên) — giải thích cho user dễ hiểu, liền mạch |
