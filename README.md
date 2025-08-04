# 🪑 `#takoy_mebel` — Django asosida mebel internet-do‘koni

> **Loyiha turi:** Portfolio loyihasi  
> **Texnologiya:** Django, Django Templates  
> **Maqsad:** Takoy o‘quvchilari uchun amaliy portfel loyihasi

---

## 📦 Texnologiyalar

- Python 3.10+
- Pillow
- Html
- Css
- Postgress
- REST
- SQL

---

## 🧱 Tuzilma

```
takoy_mebel/
├── manage.py
├── dashboard/             # Dashboard uchun app
├── core/                  # Umumiy sahifalar (bosh sahifa, kontaktlar, haqida)
├── templates/             # Umumiy front shablonlar
└── static/                # Statik fayllar (CSS, JS)
└── media/                 # Media fayllar (png, svg, pdf ...)
```

---

## 📁 Ilovalar

### 1. `products` — mahsulotlar bilan ishlash

#### Modellar:

- `Category`  
  - `name` — nomi  
  - `slug` — url uchun  
  - `image` — rasm (ixtiyoriy)

- `Product`  
  - `title` — mahsulot nomi  
  - `slug` — mahsulot url  
  - `description` — to‘liq tavsif  
  - `price` — narx  
  - `discount_price` — chegirmali narx (ixtiyoriy)  
  - `image` — asosiy surat  
  - `category` — FK → Category  
  - `is_available` — mavjudligi  
  - `created_at`, `updated_at`

- `ProductImage`  
  - `product` — FK → Product  
  - `image` — qo‘shimcha suratlar

#### Views:

- Barcha mahsulotlar ro‘yxati
- Mahsulot tafsilotlari
- Kategoriya asosida filtr

---

### 2. `core` — umumiy sahifalar

#### Modellar:

- `ContactRequest`  
  - `name`  
  - `email`  
  - `message`  
  - `created_at`

#### Views:

- Bosh sahifa
- Kompaniya haqida sahifa
- Aloqa formasi
- Kontakt formasi yuborish

---

## 🧰 Admin panelda boshqariladiganlar

- Kategoriyalar va mahsulotlar
- Mahsulot suratlari
- Kontakt so‘rovlari
- Har bir model uchun `list_display`, `search_fields`, `prepopulated_fields` (`slug` uchun)

---

## 💡 Qo‘shimcha imkoniyatlar (ixtiyoriy)

- Mahsulotlar bo‘yicha qidiruv
- Pagination (12 ta mahsulot sahifasiga)

---

## 🎯 Maqsad

Ushbu loyiha orqali biz halq uchun qulay internet magazin yaratamiz:

- takoy_mebel moliaviy tomonday ko'tarish
- appachi serverga yuklash
- keyin chalik shu projectni yahshiroq summaga sotish
