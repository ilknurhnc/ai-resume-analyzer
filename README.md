# AI Resume Analyzer with ATS Scoring

AI Resume Analyzer, kullanıcıların CV dosyalarını yükleyerek hedefledikleri pozisyona göre yapay zekâ destekli analiz almalarını sağlayan bir web uygulamasıdır.

Uygulama, yüklenen CV dosyasının içeriğini okur, metne dönüştürür, hedef pozisyonla karşılaştırır ve ATS uyumluluğu açısından değerlendirme yapar.

## Projenin Amacı

Bu projenin amacı, bir CV'nin hedeflenen pozisyona ne kadar uygun olduğunu analiz eden basit ama gerçekçi bir AI destekli ürün geliştirmektir.

Proje özellikle şu konulara odaklanır:

* CV dosyası yükleme
* PDF/DOCX içerik okuma
* FastAPI ile backend geliştirme
* Frontend ile backend entegrasyonu
* LLM kullanarak analiz üretme
* ATS uyumluluk skoru hesaplama
* Yapılandırılmış JSON çıktısı üretme
* Docker ile uygulamayı paketleme

## Uygulama Ne Yapar?

Kullanıcı sisteme bir CV dosyası yükler ve hedef pozisyonu yazar.

Örneğin:

```txt
Hedef Pozisyon: Backend Developer
CV Dosyası: resume.pdf
```

Sistem bu CV'yi analiz eder ve şu çıktıları üretir:

* ATS uygunluk skoru
* Genel CV özeti
* Güçlü yönler
* Eksik veya zayıf alanlar
* Eksik anahtar kelimeler
* İyileştirme önerileri
* Hedef role göre uygunluk değerlendirmesi

Örnek çıktı:

```json
{
  "ats_score": 78,
  "summary": "CV backend developer rolü için temel teknik becerileri içeriyor ancak ölçülebilir başarılar ve bazı önemli anahtar kelimeler eksik.",
  "strengths": [
    "Python ve FastAPI deneyimi belirtilmiş.",
    "Backend geliştirme odaklı projeler yer alıyor."
  ],
  "weaknesses": [
    "Projelerde ölçülebilir sonuçlar yeterince vurgulanmamış.",
    "Veritabanı deneyimi daha açık yazılmalı."
  ],
  "missing_keywords": [
    "REST API",
    "PostgreSQL",
    "Docker",
    "CI/CD"
  ],
  "suggestions": [
    "Projelerde kullanılan teknolojileri daha net listele.",
    "Başarıları sayısal verilerle destekle.",
    "Hedef pozisyona uygun teknik anahtar kelimeleri ekle."
  ]
}
```

## Kullanılacak Teknolojiler

### Backend

* Python
* FastAPI
* Pydantic
* Uvicorn
* pypdf
* python-docx
* OpenAI API veya farklı bir LLM servisi

### Frontend

* HTML
* CSS
* JavaScript

### DevOps

* Docker
* Docker Compose

## Proje Mimarisi

Proje iki ana bölümden oluşur:

```txt
frontend
↓
FastAPI backend
↓
dosya okuma servisi
↓
LLM analiz servisi
↓
JSON sonuç
↓
frontend ekranı
```

Temel akış:

1. Kullanıcı CV dosyasını yükler.
2. Kullanıcı hedef pozisyonu girer.
3. Frontend dosyayı backend'e gönderir.
4. Backend dosyanın içeriğini okur.
5. CV metni LLM analiz servisine gönderilir.
6. AI, ATS uyumluluk analizi üretir.
7. Sonuç frontend'de kullanıcıya gösterilir.

## Planlanan Dosya Yapısı

```txt
ai-resume-analyzer/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── schemas.py
│   │   │
│   │   ├── routes/
│   │   │   └── analyze.py
│   │   │
│   │   ├── services/
│   │   │   ├── analyzer_service.py
│   │   │   ├── file_parser.py
│   │   │   └── llm.py
│   │   │
│   │   └── prompts/
│   │       └── resume_prompt.py
│   │
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── app.js
│   └── Dockerfile
│
├── docker-compose.yml
├── README.md
└── .gitignore
```

## Dosyaların Görevleri

### `backend/app/main.py`

FastAPI uygulamasının başlangıç dosyasıdır.

Görevleri:

* FastAPI uygulamasını başlatmak
* Route dosyalarını uygulamaya bağlamak
* CORS ayarlarını yapmak
* Backend servisinin çalışır durumda olmasını sağlamak

### `backend/app/schemas.py`

Backend'de kullanılan veri modellerini içerir.

Görevleri:

* Request modellerini tanımlamak
* Response modellerini tanımlamak
* API'den dönen verinin düzenli olmasını sağlamak

### `backend/app/routes/analyze.py`

CV analiz endpoint'lerini içerir.

Görevleri:

* Dosya yükleme isteğini almak
* Hedef pozisyon bilgisini almak
* Gelen isteği analiz servisine yönlendirmek
* Sonucu frontend'e döndürmek

Planlanan endpoint:

```txt
POST /analyze-file
```

### `backend/app/services/file_parser.py`

Yüklenen CV dosyasının içeriğini okur.

Görevleri:

* PDF dosyalarından metin çıkarmak
* DOCX dosyalarından metin çıkarmak
* Desteklenmeyen dosya türlerinde hata döndürmek
* Temiz metni analiz servisine göndermek

### `backend/app/services/analyzer_service.py`

CV analiz sürecinin iş mantığını yönetir.

Görevleri:

* CV metnini almak
* Hedef pozisyonu almak
* Prompt hazırlamak
* LLM servisini çağırmak
* Analiz sonucunu düzenlemek

### `backend/app/services/llm.py`

LLM bağlantısını yönetir.

Görevleri:

* OpenAI veya başka bir LLM servisine istek atmak
* Modelden gelen cevabı almak
* Hataları yönetmek

İlk aşamada mock cevap döndürebilir. Daha sonra gerçek AI entegrasyonu yapılacaktır.

### `backend/app/prompts/resume_prompt.py`

LLM'e gönderilecek prompt şablonlarını içerir.

Görevleri:

* CV analiz prompt'unu merkezi bir yerde tutmak
* ATS değerlendirme kriterlerini tanımlamak
* Modelden istenen JSON formatını belirtmek

### `frontend/index.html`

Kullanıcı arayüzünün HTML iskeletidir.

İçeriğinde şunlar bulunur:

* CV dosyası yükleme alanı
* Hedef pozisyon input'u
* Analiz butonu
* Sonuçların gösterileceği alan

### `frontend/style.css`

Frontend tasarım dosyasıdır.

Görevleri:

* Sayfa düzenini oluşturmak
* Butonları tasarlamak
* Sonuç kartlarını biçimlendirmek
* Kullanıcı deneyimini iyileştirmek

### `frontend/app.js`

Frontend davranışlarını yönetir.

Görevleri:

* Kullanıcının seçtiği dosyayı almak
* Hedef pozisyon bilgisini almak
* Backend'e `FormData` ile istek atmak
* Analiz sonucunu ekranda göstermek

### `backend/requirements.txt`

Backend bağımlılıklarını içerir.

Başlangıçta kullanılacak paketler:

```txt
fastapi
uvicorn
pydantic
python-multipart
pypdf
python-docx
python-dotenv
openai
```

### `Dockerfile`

Backend ve frontend servislerini Docker ortamında çalıştırmak için kullanılır.

İlk aşamada Docker kullanılmayacaktır. Uygulama önce lokal olarak çalıştırılacaktır.

### `docker-compose.yml`

Backend ve frontend servislerini birlikte ayağa kaldırmak için kullanılır.

İleride tek komutla uygulamayı çalıştırmak için kullanılacaktır:

```bash
docker compose up
```

## ATS Skoru Nasıl Hesaplanacak?

ATS skoru 0 ile 100 arasında bir değer olacaktır.

İlk versiyonda skor LLM değerlendirmesine dayalı olacaktır. Ancak değerlendirme belirli kriterlere göre yapılacaktır.

Planlanan kriterler:

```txt
Anahtar kelime uyumu: 30 puan
Deneyim uygunluğu: 25 puan
Teknik beceri uygunluğu: 20 puan
CV formatı ve okunabilirlik: 15 puan
Ölçülebilir başarılar: 10 puan
Toplam: 100 puan
```

Bu skor kesin bir işe alım sonucu anlamına gelmez. CV'nin hedef role göre ne kadar güçlü ve ATS dostu göründüğünü tahmini olarak gösterir.

## MVP Kapsamı

İlk versiyonda yapılacaklar:

* CV dosyası yükleme
* PDF dosyasından metin çıkarma
* DOCX dosyasından metin çıkarma
* Hedef pozisyon bilgisi alma
* Mock analiz sonucu döndürme
* Frontend'de sonucu gösterme
* Daha sonra gerçek LLM entegrasyonu ekleme

## MVP Dışında Bırakılanlar

Bu projenin ilk versiyonunda şu özellikler olmayacaktır:

* Kullanıcı hesabı
* Veritabanı
* CV geçmişi kaydetme
* RAG
* Vector database
* Memory
* Agent sistemi
* Authentication
* Payment sistemi

Bu özellikler bilinçli olarak kapsam dışı bırakılmıştır. Amaç, önce sade ve çalışan bir AI entegrasyonu geliştirmektir.

## Geliştirme Aşamaları

### Aşama 1: Proje iskeleti

* Backend klasör yapısı oluşturulur.
* Frontend klasör yapısı oluşturulur.
* README ve `.gitignore` eklenir.

### Aşama 2: Mock backend endpoint

* FastAPI uygulaması başlatılır.
* `/analyze-file` endpoint'i oluşturulur.
* Dosya yükleme alınır.
* Gerçek AI kullanılmadan mock analiz sonucu döndürülür.

### Aşama 3: Dosya okuma

* PDF dosyalarından metin çıkarılır.
* DOCX dosyalarından metin çıkarılır.
* Hatalı dosya türleri kontrol edilir.

### Aşama 4: Frontend entegrasyonu

* Kullanıcı dosya yükler.
* Hedef pozisyon girer.
* Frontend backend'e istek gönderir.
* Sonuçlar ekranda gösterilir.

### Aşama 5: LLM entegrasyonu

* OpenAI API veya başka bir LLM servisi bağlanır.
* CV metni ve hedef pozisyon prompt içine yerleştirilir.
* Modelden yapılandırılmış JSON çıktı alınır.

### Aşama 6: Docker

* Backend Dockerfile hazırlanır.
* Frontend Dockerfile hazırlanır.
* Docker Compose ile servisler birlikte çalıştırılır.

## API Tasarımı

### `POST /analyze-file`

CV dosyasını ve hedef pozisyon bilgisini alır.

Request tipi:

```txt
multipart/form-data
```

Alanlar:

```txt
file: PDF veya DOCX CV dosyası
target_role: Hedef pozisyon
```

Örnek response:

```json
{
  "ats_score": 82,
  "summary": "CV hedef pozisyon için uygun bir temel sunuyor ancak bazı teknik anahtar kelimeler eksik.",
  "strengths": [
    "Backend geliştirme deneyimi mevcut.",
    "Proje bazlı teknik deneyim belirtilmiş."
  ],
  "weaknesses": [
    "Başarılar sayısal verilerle desteklenmemiş.",
    "Bazı teknolojiler detaylandırılmamış."
  ],
  "missing_keywords": [
    "REST API",
    "Docker",
    "PostgreSQL"
  ],
  "suggestions": [
    "Projelerde kullanılan teknolojileri daha açık belirt.",
    "Her deneyim maddesine ölçülebilir sonuç ekle.",
    "Hedef pozisyona uygun anahtar kelimeleri CV'ye doğal şekilde yerleştir."
  ]
}
```

## Öğrenilecek Konular

Bu proje tamamlandığında şu konularda pratik kazanılmış olacaktır:

* FastAPI ile REST API geliştirme
* Dosya yükleme işlemleri
* PDF ve DOCX dosyalarından metin çıkarma
* Frontend'den backend'e dosya gönderme
* LLM API entegrasyonu
* Prompt engineering
* Yapılandırılmış AI çıktısı alma
* ATS mantığını anlama
* Katmanlı backend mimarisi
* Docker ile uygulama çalıştırma

## Kurulum

Bu bölüm geliştirme sırasında doldurulacaktır.

Planlanan lokal çalıştırma:

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Windows için:

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Durum

Proje geliştirme aşamasındadır.

İlk hedef:

```txt
Dosya yüklenen, mock ATS sonucu döndüren çalışan bir FastAPI endpoint'i oluşturmak.
```

## Lisans

Bu proje eğitim ve portfolyo amacıyla geliştirilmektedir.
