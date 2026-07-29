#Bài 1
inventory = [
    {"id": "SP1", "ten": "Tai nghe Sony", "gia": 1200000, "danh_muc": "Phụ kiện"},
    {"id": "SP2", "ten": "Chuột không dây", "gia": 450000, "danh_muc": "Phụ kiện"},
    {"id": "SP3", "ten": "Bàn phím Cơ", "gia": 950000, "danh_muc": "Phụ kiện"},
    {"id": "SP4", "ten": "Màn hình Dell 27 inch", "gia": 4500000, "danh_muc": "Thiết bị"},
    {"id": "SP5", "ten": "Sạc dự phòng 20000mAh", "gia": 350000, "danh_muc": "Phụ kiện"}
]
def linear_search_filter(cart, category, price):
    list = []
    for product in cart:
        if (product["gia"] <= price and
                product["danh_muc"] == category):
            list.append(product)
    return list
category = input("Nhập danh mục: ")
price = input("Nhập giá sản phẩm: ")
filtered_products = linear_search_filter(inventory,category,price)
print("KẾT QUẢ LỌC SẢN PHẨM (LINEAR SEARCH MULTI-CRITERIA)")
print(f"Danh mục tìm kiếm: {category} | Giá tối đa: {price:,} VNĐ")
print(f"Tìm thấy {len(filtered_products)} sản phẩm phù hợp:\n")

for product in filtered_products:
    print(f"  -> [{product['id']}] {product['ten']} | Giá: {product['gia']:,} VNĐ")
#Bài 2
students = [
    {"name": "An", "gpa": 7.2},
    {"name": "Bình", "gpa": 9.5},
    {"name": "Cường", "gpa": 6.8},
    {"name": "Dũng", "gpa": 8.4}
]
def bubble_sort_desc(students):
    quantity = len(students)
    for i in range(quantity - 1):
        valid = False
        for j in range(quantity - 1 - i):
            if students[j]["gpa"] < students[j + 1]["gpa"]:
                students[j], students[j + 1] = students[j + 1], students[j]
                valid = True
        if not valid:
            break
    return students
sorted_students = bubble_sort_desc(students)
print("BẢNG XẾP HẠNG SINH VIÊN (BUBBLE SORT - GPA GIẢM DẦN)\n")
for i, student in enumerate(sorted_students, start=1):
    print(f"Top {i}: {student['name']} - {student['gpa']} điểm")