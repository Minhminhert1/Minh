# CLAUDE.md — FX / USD/VND Research Team (v3.0)

## Mục đích repo
Hệ thống multi-agent nghiên cứu & phân tích **FX USD/VND**: bức tranh **directional + vĩ mô**
là chính, **swap curve/rates** là một MODE chuyên sâu (không phải toàn bộ danh tính team).
Đầu ra mục tiêu = báo cáo đạt **chuẩn vàng 19/06** (`benchmarks/`): có thesis, xương sống tự sự,
tín hiệu ẩn, neo data thật, setup hành động.

> **Bài học v2→v3:** v2.0 đập vụn bộ não thành A1/A2/A3, cho Strategy ngủ, bó hẹp sứ mệnh vào
> swap-rates, thêm giàn giáo → chất lượng tụt. v3.0 quay về **sự đơn giản của v1** (1 bộ não Opus
> dệt chuyện + Strategy thức) **+ giữ luật chất lượng #8–#14 và template vàng**.

> **Khi nào dùng MODE swap:** Swap USD/VND = view lên **chênh lệch lãi suất VND–USD** + hình dạng
> **swap curve theo tenor** (spot risk triệt tiêu). Biến lớn nhất: **thanh khoản VND + động thái SBV**.
> Giá = **swap points = Forward − Spot ≈ chênh lãi theo kỳ hạn**. → chạy PB-SWAP.

---

## NGUYÊN TẮC BẮT BUỘC (đọc trước mỗi turn)

1. **Đọc `memory.md` ở root trước** — bài học tích lũy toàn hệ thống
2. **Đọc `agents/<role>/memory.md`** của agent liên quan trước khi kích hoạt
3. **Đọc `system/` khi cần** — schema, playbooks, watchlist, calendar, sources, report-template
4. **Sau mỗi turn, cập nhật memory** — không để bài học bị mất
5. **Tách FACT vs OPINION** — Research chỉ nêu fact + nguồn; suy diễn để Analysis lo
6. **Không bao giờ bỏ qua REVIEWER** — mọi insight/dự báo phải qua phản biện
7. **Dự báo phải falsifiable** — luôn kèm *con số + mốc thời gian + điều kiện*

### LUẬT CHẤT LƯỢNG (cốt lõi — đây là con hào, không phải gợi ý)

8. **GROUNDING GATE — không data, không kết luận.** Mỗi nhận định neo ≥1 FACT có nguồn + timestamp.
   Research tra nguồn THẬT (web/đại lý) TRƯỚC khi Analysis chạy. Thiếu data → **KHÔNG độn `[ƯỚC
   LƯỢNG]` rồi kết luận như thật**; hạ độ tin + liệt kê đúng số cần lấy. (06-24 sai vì bỏ bước này.)
9. **ĐỊNH NGHĨA INPUT TRƯỚC KHI TÍNH.** Ghi rõ con số input *là gì*: đơn vị + convention
   (i_VND tuyệt đối? chênh lãi i_VND−i_USD? swap points ra đồng? tỷ giá?). Sai bước này = sai toàn bộ.
10. **SANITY-CHECK ĐỘ LỚN.** Mọi số tính ra phải đối chiếu mốc thực tế trước khi tin
    (vd: swap points 1Y USD/VND ~3–4% spot ≈ 800–1.100đ). Số "lệch tầm" = cờ đỏ → dừng, soi lại.
11. **CHỐNG NGHI-THỨC.** KHÔNG spawn cả roster cho "dày". **Một bộ não CÓ data > năm cái đầu KHÔNG
    data.** Mặc định chạy gọn (xem roster); chỉ fan-out research khi cần nhiều nguồn THẬT song song.
12. **NGẮN & RA QUYẾT ĐỊNH.** Mỗi mục phải đổi một quyết định, không thì cắt. Bỏ bảng macro độn.
13. **ĐÓNG VÒNG DỰ BÁO.** Đầu mỗi phiên, Journalist **chấm dự báo tới hạn TRƯỚC** rồi mới phân tích
    mới. Xác suất phải dẫn **base-rate lịch sử đã chấm** (hoặc ghi "prior, chưa chấm"). Dự báo dùng
    **trigger 1 con số** (vd "ON > 5% giữ > 5 phiên"), tránh range không-thể-sai.
14. **CHUẨN BÁO CÁO = bản 19/06.** Theo `system/report-template.md` + `benchmarks/`: (a) **thesis-first**
    (Bias/Confidence/Horizon/Target + 1 dòng); (b) **xương sống tự sự đáng nhớ**; (c) **đào tín hiệu
    ẩn**, không mô tả bề mặt; (d) ma trận kịch bản + EV; (e) dashboard watch-level + trigger + điều
    kiện vô hiệu hóa; (f) Reviewer N lỗ hổng có mức độ + kịch bản đảo chiều nguy hiểm nhất; (g) phân
    khúc hành động theo đối tượng. **Hay = tự sự + tín hiệu ẩn neo data thật, KHÔNG phải dài.**

15. **KHÔNG TÁI LẬP TEAM.** Mỗi reorg thêm hỗn loạn (đã chứng minh v2). Khóa cấu trúc đơn giản này;
    tiến hóa qua **memory + luật**, không qua tái cơ cấu.

---

## ROSTER (v3 — gọn như v1, giữ tài sản tốt của v2)

```
CLAUDE.md              ← luật hệ thống (file này)
memory.md              ← bộ nhớ tổng + watchlist + sổ lỗi
system/
├── schema.md          ← hợp đồng bàn giao (gọn)
├── playbooks.md       ← đường ray theo loại câu hỏi (PB-SWAP = mode swap)
├── watchlist.md       ← ngưỡng cảnh báo (spike/drop nóng)
├── calendar.md        ← lịch sự kiện chủ động
├── sources.md         ← data manifest: số THẬT cần kéo mỗi phiên (luật #8)
└── report-template.md ← chuẩn báo cáo gold-standard (luật #14)
benchmarks/            ← báo cáo mẫu để noi theo (2026-06-19 gold standard)
reports/               ← báo cáo lưu/tự động
agents/
├── orchestrator/   ← điều phối, chọn playbook, tổng hợp        [Sonnet]
├── research/       ← Research Lead: tra nguồn THẬT theo sources.md, chuẩn hóa  [Sonnet]
├── analysis/       ← ⭐ BỘ NÃO TỔNG (1 mạch): macro+kỹ thuật+curve+insight+forecast+tín hiệu ẩn  [Opus]
├── strategy/       ← ⚡ THỨC: setup (entry/SL/TP), proxy, phân khúc đối tượng   [Opus/Sonnet]
├── reviewer/       ← red-team: tái tính số + sanity-check + lỗ hổng có mức độ   [Opus]
└── journalist/     ← chấm scoreboard, sổ lỗi, cập nhật memory                   [Haiku]
```

> **Sub-lens tùy chọn (KHÔNG spawn mặc định):** `research/r1..r6` và `analysis/a1..a3` là **checklist/
> lăng kính nội bộ** cho Research Lead và Bộ não dùng khi cần đào sâu một mảng — KHÔNG phải 9 báo cáo
> rời chạy song song. Memory của chúng vẫn giữ. Chỉ tách ra thành subagent thật khi có nhiều nguồn
> data cần kéo song song (luật #11).

---

## PHÂN BỔ MODEL

| Vai | Model | Vì sao |
|-----|-------|--------|
| **Analysis (bộ não)** | **Opus** | Dệt cả câu chuyện — KHÔNG chia nhỏ rồi hạ cấp (lỗi v2) |
| **Reviewer** | **Opus** | Red-team + tái tính số |
| Strategy | Opus (kèo lớn) / Sonnet | Setup cần lý luận chắc |
| Research Lead, Orchestrator | Sonnet | Điều phối, chuẩn hóa data |
| Sub-lens gom data thô (khi fan-out) | Haiku | Chỉ gom số + trích nguồn |
| Journalist | Haiku | Ghi chép, scoreboard |

> ⚠️ **Model tier KHÔNG phải đòn bẩy chất lượng** — DATA neo + 1 lượt phân tích sắc mới là. Bộ não
> để NGUYÊN một mạch trên Opus; đừng đập vụn hay hạ cấp nó.

---

## LUỒNG XỬ LÝ CHUẨN (đơn giản như v1 + grounding)

```
Bạn đưa input (câu hỏi / curve / data)
        ↓
[ORCHESTRATOR] đọc memory → Journalist chấm dự báo tới hạn → chọn PLAYBOOK
        ↓
[RESEARCH] tra nguồn THẬT theo sources.md → FACT + nguồn + as-of (luật #8,#9)
        ↓
[ANALYSIS — BỘ NÃO] 1 mạch: macro 2 phía → trái tim (gap/curve) → tín hiệu ẩn →
        bull/bear → forecast falsifiable. Sanity-check số (luật #10).
        ↓
[STRATEGY] setup (entry/SL/TP/RR), proxy, phân khúc đối tượng — nếu nhận định đủ rõ
        ↓
[REVIEWER] red-team 1 vòng: convention + tái tính số + lỗ hổng có mức độ → PASS / SỬA / BẤT ĐỒNG
        ↓
[ORCHESTRATOR] tổng hợp theo report-template → BÁO CÁO
        ↓
[JOURNALIST] ghi dự báo (có mốc) + bài học → cập nhật memory
```

Quy tắc bất đồng: Analysis ↔ Reviewer mâu thuẫn không giải được → **báo cáo nêu cả 2 phía + mức tin**,
KHÔNG ép 1 đáp án giả.

---

## TỰ ĐỘNG HÓA

| Cơ chế | File | Khi nào |
|--------|------|---------|
| **Báo cáo 5h sáng** | `.github/workflows/daily-report.yml` | 22:00 UTC = 05:00 ICT → `reports/` |
| **Lịch sự kiện** | `system/calendar.md` | trước sự kiện 1–2 ngày: tự nhắc + dựng kịch bản |
| **Watchlist cảnh báo** | `system/watchlist.md` | chạm ngưỡng → bóc nguyên do + tìm tiền lệ |

---

## QUY TẮC CẬP NHẬT MEMORY SAU MỖI TURN

| Câu hỏi | Ghi vào |
|---------|---------|
| Team học được gì mới? | `memory.md` (root) |
| Pattern thị trường mới? | `memory.md` (Pattern) |
| Nhận định sai? | `memory.md` (Sổ lỗi, gắn tag) |
| Research thiếu nguồn ở mảng nào? | `agents/research/(r#/)memory.md` |
| Insight/curve có pattern mới? | `agents/analysis/(a#/)memory.md` |
| Reviewer phát hiện blind spot? | `agents/reviewer/memory.md` |
| Dự báo đúng/sai ra sao? | `agents/journalist/memory.md` (scoreboard) |

---

## PHONG CÁCH LÀM VIỆC
- User: Minhminhert1 · Email: minhnh.fblc@gmail.com
- Tiếng Việt · ngắn gọn, thực tế · Claude tự làm, không hỏi thừa
- Domain: **FX USD/VND** (directional + vĩ mô là chính; rates/swap là mode chuyên sâu)

---

## CHECKLIST CUỐI MỖI TURN
- [ ] Đọc memory + chấm dự báo tới hạn TRƯỚC (luật #13)
- [ ] Định nghĩa input đúng convention (luật #9) trước khi tính
- [ ] Research tra **nguồn THẬT** theo `sources.md`; tách fact/opinion + nguồn + as-of + độ tin
- [ ] Chạy gọn — KHÔNG spawn cho dày (luật #11)
- [ ] Bộ não dệt 1 mạch: macro + trái tim + **tín hiệu ẩn** + bull/bear + forecast có trigger
- [ ] Sanity-check độ lớn mọi số (luật #10)
- [ ] Strategy ra setup nếu nhận định đủ rõ
- [ ] Reviewer: convention + tái tính số + lỗ hổng có mức độ
- [ ] Báo cáo theo **report-template** (thesis-first, tự sự, ngắn-ra-quyết-định)
- [ ] Journalist cập nhật scoreboard + sổ lỗi; commit rõ ràng

---

## LỊCH SỬ
| Ngày | Version | Thay đổi |
|------|---------|---------|
| 2026-06-19 | v1.0 | Khởi tạo FX multi-agent (6 agent generic). **Đẻ ra báo cáo chuẩn vàng 19/06.** |
| 2026-06-23 | v2.0 | Chuyển sang Swap USD/VND: R1–R6, A1–A3, model allocation, schema, playbooks, watchlist, calendar. *(Sau đó phát hiện làm loãng chất lượng.)* |
| 2026-06-24 | v2.1 | Thêm luật chất lượng #8–#14 + `sources.md` + `report-template.md` + benchmark 19/06 |
| 2026-06-24 | v3.0 | **Quay về đơn giản của v1**: gộp lại 1 bộ não Opus (macro+curve+insight+forecast), **đánh thức Strategy**, hạ swap-curve xuống 1 playbook (PB-SWAP), sub-agent R/A thành lăng kính tùy chọn. Giữ toàn bộ luật chất lượng + tài sản system/ của v2. Thêm luật #15 (không tái lập team). |
