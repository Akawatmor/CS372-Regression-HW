import hashlib

# 1. กำหนดข้อความ (Message)
M = "COMPUTER"

# 2. คำนวณค่า digest ด้วย hash algorithm SHA-256
# ต้องเข้ารหัสข้อความเป็น utf-8 ก่อนนำไปเข้าฟังก์ชันแฮช
#hash_object = hashlib.sha256(M.encode('utf-8'))
hash_object = hashlib.sha256(M.encode('ascii'))

# 3. แปลงผลลัพธ์ให้อยู่ในรูปแบบเลขฐาน 16 และทำให้ตัวอักษรเป็นตัวพิมพ์ใหญ่ทั้งหมด (A-F)
digest_hex = hash_object.hexdigest().upper()

# 4. แสดงผลลัพธ์ (จะไม่มีช่องว่างโดยอัตโนมัติ)
print(digest_hex)