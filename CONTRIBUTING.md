# Đóng góp cho dự án (Contributing Guide)

Cảm ơn bạn đã quan tâm đến việc cải thiện bộ **AI Anti-Over-Refusal & Deep-Work Skills Pack**!

## Quy tắc chuẩn khi viết hoặc cập nhật `SKILL.md`

1. **Frontmatter hợp lệ**:
   - `name`: Chỉ dùng chữ thường `a-z`, số `0-9` và dấu gạch ngang `-` (tối đa 64 ký tự, từ 1-5 từ).
   - `description`: Mô tả rõ chức năng của skill và các ngữ cảnh kích hoạt cụ thể (dưới 1024 ký tự).
2. **Định dạng Markdown**:
   - Không sử dụng dấu gạch ngang dài (em-dash hoặc en-dash) trong `SKILL.md`; chỉ dùng dấu gạch ngang chuẩn (`-`).
   - Luôn để một dòng trống trước mọi danh sách (`-` hoặc `1.`).
   - Giữ nội dung `SKILL.md` cô đọng, dưới 500 dòng; tách các bảng phân loại chi tiết sang thư mục `references/`.
3. **Thêm Test Cases**:
   - Khi thêm quy tắc mới, hãy bổ sung câu lệnh kiểm thử tương ứng vào `examples/test-prompts.md`.
