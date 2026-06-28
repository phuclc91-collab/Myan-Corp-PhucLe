---
trigger: always_on
---


# Rules — CRM Myan Corp

## Tech Stack — Không thay đổi
- Frontend: React 18 + TypeScript
- Styling: Tailwind CSS v3 với glassmorphism custom classes
- Backend, Auth, Database: Supabase
- State management: React Context + useReducer
- Router: React Router v6
- Charts: Recharts
- Drag and drop: @dnd-kit/core và @dnd-kit/sortable
- CSV: PapaParse

## Auth — Email/Password và tự tạo tài khoản
Phương thức: Chỉ sử dụng Đăng nhập & Đăng ký bằng Email/Password qua Supabase Auth.
UI/UX Form:
Phải có đầy đủ form Đăng nhập (Login) và Đăng ký (Register).
Tất cả các input phải có validation rõ ràng (Email đúng định dạng, Password tối thiểu 6 ký tự).
Hiển thị thông báo lỗi trực quan (bằng tiếng Việt) khi sai tài khoản/mật khẩu hoặc email đã tồn tại.
Luồng dữ liệu: Sau khi Đăng ký thành công và user được tạo trong Supabase Auth, tự động tạo record tương ứng trong bảng profiles (khuyến khích dùng Database Trigger trong Supabase để đảm bảo tính toàn vẹn).
Session: Được quản lý tự động bởi Supabase — không tự ý lưu vào localStorage thủ công.

## Bảo mật dữ liệu — Bắt buộc
- Tất cả Supabase queries phải có điều kiện user_id = auth.uid()
- Không bao giờ query data mà không có user_id filter
- Không bao giờ disable RLS


## Cấu trúc thư mục
- /src/components/[module]/ cho từng module
- /src/lib/supabase/ cho tất cả database queries
- /src/types/ cho TypeScript interfaces
- /src/hooks/ cho custom React hooks

## Convention
- TypeScript interface cho tất cả data types — không dùng "any"
- Tên file: PascalCase cho components, camelCase cho utils
- Luôn handle error khi gọi Supabase
- Số tiền: định dạng VND với Intl.NumberFormat('vi-VN')

## Nội dung
- Tất cả text hiển thị bằng tiếng Việt
- Thuật ngữ nhất quán.
