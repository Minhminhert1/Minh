# ANALYSIS SQUAD — Tổng quan

Nhóm phân tích gồm 3 con, chạy song song, đọc DATA PACK từ Research Lead:

| Agent | File | Model | Việc |
|-------|------|-------|------|
| **A1 · Curve** | `a1-curve/prompt.md` | Opus | Mổ hình dạng curve, fair value, điểm bất thường |
| **A2 · Insight** | `a2-insight/prompt.md` | Opus | Giải thích lý do từng tenor (đa giả thuyết) |
| **A3 · Forecast** | `a3-forecast/prompt.md` | Sonnet | Kịch bản & dự báo có mốc thời gian |

Luồng: A1 + A2 chạy trước/song song → A3 dùng output A1+A2 dựng dự báo → tất cả qua Reviewer.
Output tổng theo schema §3.
