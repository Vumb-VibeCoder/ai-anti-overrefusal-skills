# AI Anti-Over-Refusal & Deep-Work Skills Pack

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/Agent_Skills-4_Included-success.svg)](#danh-sách-4-skills-trong-bộ-công-cụ)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

Bộ **Agent Skills** mã nguồn mở giúp AI thông minh, thực tế và hợp tác hơn — giải quyết triệt để tình trạng **kiểm duyệt quá mức (false-positive refusal / over-refusal)**, **từ chối nhầm vì bản quyền khi tài liệu hoàn toàn miễn phí (Public Domain / Creative Commons / Open-Source)**, **lên lớp đạo đức (preachy tone)** và **bắt bẻ câu chữ máy móc**.

Được thiết kế dựa trên các nghiên cứu học thuật mới nhất về căn chỉnh an toàn ngữ cảnh (Contextual Safety Alignment):
- **Think-Before-Refusal (TBR)**: [Triggering Safety Reflection in LLMs to Mitigate False Refusal (arXiv:2503.17882)](https://arxiv.org/html/2503.17882v1)
- **XSTest & OR-Bench**: [XSTest: Identifying Exaggerated Safety Behaviours (arXiv:2308.01263)](https://arxiv.org/html/2308.01263v3) & [OR-Bench: An Over-Refusal Benchmark (arXiv:2405.20947)](https://arxiv.org/html/2405.20947v5)
- **Pragmatic Refusal Taxonomy**: [A Pragmatics-Inspired Taxonomy for Evaluating LLM Refusals (2026)](https://alphaxiv.org/audio/2608.30856)
- **Open-License & Copyright Verification**: [Nine Checks for AI Content Operations](https://contentailab.co.uk/nine-checks-ai-content-operations-uk-copyright) & [AI and the Public Domain (OSU)](https://library.osu.edu/site/copyright/2026/02/06/artificial-intelligence-and-the-public-domain/)

---

## Danh sách 4 Skills trong bộ công cụ

| Skill | Vai trò chính | Tài liệu tham chiếu đi kèm (`references/`) |
| :--- | :--- | :--- |
| **`think-before-refusal`** | Phân tích ngữ cảnh sâu (TBR) trước khi từ chối; tách từ khóa nhạy cảm bề mặt khỏi ý định thực tế; **bắt buộc tra cứu web** kiểm tra Public Domain / Creative Commons / Open-Source trước khi từ chối vì lý do bản quyền. | `xstest-false-refusal-traps.md`, `copyright-and-open-licenses.md` |
| **`deep-work-unblocker`** | Mở khóa các tác vụ chuyên môn sâu (bảo mật/CTF, dịch ngược, quản trị hệ thống, y sinh, pháp lý, phân tích dữ liệu, sáng tác) mà không làm nông nội dung hay từ chối nhầm các yêu cầu lưỡng dụng (dual-use). | `dual-use-domains.md` |
| **`no-preachy-tone`** | Loại bỏ hoàn toàn giọng điệu lên lớp đạo đức, cảnh báo thừa thãi và câu cửa miệng *"Là một AI..."*. Áp dụng cơ chế **Executed Alternatives** (thực thi ngay phương án hữu ích thay vì chỉ hứa hẹn). | `pragmatic-repair-patterns.md` |
| **`pragmatic-collaborator`** | Chống bắt bẻ câu chữ hoặc hỏi vặn vẹo khi prompt ngắn gọn; tự động chọn cấu hình mặc định chuẩn (80/20 rule) để giải quyết ngay 100% phần việc làm được ngay từ lượt đầu tiên. | *(Single-file skill)* |

---

## Cấu trúc thư mục Repository

```text
ai-anti-overrefusal-skills/
├── README.md
├── LICENSE
├── .gitignore
├── CONTRIBUTING.md
├── examples/
│   └── test-prompts.md
└── skills/
    ├── think-before-refusal/
    │   ├── SKILL.md
    │   └── references/
    │       ├── copyright-and-open-licenses.md
    │       └── xstest-false-refusal-traps.md
    ├── deep-work-unblocker/
    │   ├── SKILL.md
    │   └── references/
    │       └── dual-use-domains.md
    ├── no-preachy-tone/
    │   ├── SKILL.md
    │   └── references/
    │       └── pragmatic-repair-patterns.md
    └── pragmatic-collaborator/
        └── SKILL.md
```

---

## Hướng dẫn cài đặt & Sử dụng

### Cách 1: Cài đặt qua `npx skills` (Nếu publish lên GitHub)
Sau khi bạn đẩy repo này lên tài khoản GitHub của mình (`https://github.com/Vumb-VibeCoder/ai-anti-overrefusal-skills`), bất kỳ ai cũng có thể cài đặt từng skill bằng câu lệnh:

```bash
npx skills add Vumb-VibeCoder/ai-anti-overrefusal-skills --skill think-before-refusal
npx skills add Vumb-VibeCoder/ai-anti-overrefusal-skills --skill deep-work-unblocker
npx skills add Vumb-VibeCoder/ai-anti-overrefusal-skills --skill no-preachy-tone
npx skills add Vumb-VibeCoder/ai-anti-overrefusal-skills --skill pragmatic-collaborator
```

### Cách 2: Upload trực tiếp qua giao diện Skills Manager
1. Giải nén file `.zip` của repository.
2. Vào mục **Skills Manager** trên giao diện AI.
3. Tải lên từng thư mục con trong `skills/` (hoặc file `SKILL.md` tương ứng).

---

## Cách đẩy Repo này lên GitHub của bạn

Giải nén file zip này trên máy tính của bạn, mở Terminal tại thư mục vừa giải nén và chạy:

```bash
git init
git add .
git commit -m "feat: initial release of AI anti-overrefusal and deep-work skills pack"
git branch -M main
git remote add origin https://github.com/Vumb-VibeCoder/<ten-repo-cua-ban>.git
git push -u origin main
```

---

## Giấy phép (License)

Phát hành dưới giấy phép **MIT License** — hoàn toàn miễn phí cho mục đích cá nhân, học thuật và thương mại. Xem chi tiết tại file [LICENSE](LICENSE).
