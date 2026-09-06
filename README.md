## Selenium ile Otomatik Veri Toplama ve Veri Analizi

Bu projede, web sitelerinden verilerin otomatik olarak toplanması amacıyla Python ve Selenium kullanılmıştır. Projenin temel amacı, farklı web sayfalarına manuel olarak tek tek girilmesine gerek kalmadan belirlenen sayfalara otomatik şekilde erişmek, gerekli verileri almak ve elde edilen verileri analiz etmektir.

Selenium kullanılarak web tarayıcısı otomatik olarak kontrol edilmiş ve belirlenen sayfalara sırasıyla giriş yapılmıştır. Sayfaların yüklenmesi ve gerekli içeriklerin görüntülenmesinin ardından, ilgili veriler sayfalardan alınarak Python ortamında işlenmiştir. Böylece manuel veri toplama işlemi otomatik hale getirilmiştir.

Toplanan veriler daha sonra düzenlenerek analiz edilebilir bir veri yapısına dönüştürülmüştür. Gereksiz veya eksik verilerin kontrol edilmesi, verilerin uygun formatlara dönüştürülmesi ve analiz için hazırlanması işlemleri gerçekleştirilmiştir.

### Kullanılan Teknolojiler

* Python
* Selenium
* Pandas
* NumPy
* Matplotlib
* WebDriver

### Veri Toplama Süreci

Projenin veri toplama aşamasında Selenium ile aşağıdaki işlemler gerçekleştirilmiştir:

1. Web tarayıcısı otomatik olarak başlatılmıştır.
2. Belirlenen web sayfalarına sırasıyla gidilmiştir.
3. Sayfaların yüklenmesi beklenmiştir.
4. Sayfalarda bulunan gerekli bilgiler otomatik olarak alınmıştır.
5. Farklı sayfalardan elde edilen veriler bir araya getirilmiştir.
6. Toplanan veriler Pandas kullanılarak düzenlenmiştir.
7. Elde edilen veri seti analiz ve görselleştirme işlemleri için hazırlanmıştır.

Bu yapı sayesinde çok sayıda sayfanın kısa sürede taranması ve verilerin otomatik olarak elde edilmesi sağlanmıştır.

### Veri Analizi ve Görselleştirme

Web sitelerinden elde edilen veriler toplandıktan sonra Pandas ve NumPy kullanılarak analiz edilmiştir. Verilerin dağılımları, kategoriler arasındaki farklılıklar ve zaman içerisindeki değişimler incelenmiştir.

Analiz sonuçlarının daha anlaşılır hale getirilmesi amacıyla Matplotlib kullanılarak çeşitli grafikler oluşturulmuştur. Grafikler üzerinden elde edilen verilerin karşılaştırılması ve genel eğilimlerin daha kolay yorumlanması sağlanmıştır.

Oluşturulan grafikler, ham verilerde doğrudan fark edilmesi zor olan değişimleri ve ilişkileri görsel olarak ortaya koymaktadır.

### Projenin Amacı

Bu projenin temel amacı, web üzerinden manuel olarak gerçekleştirilen veri toplama işlemlerini otomatikleştirmek ve elde edilen verileri analiz ederek anlamlı sonuçlara dönüştürmektir.

Selenium sayesinde web tarayıcısı üzerinden gerçekleştirilen tekrarlı işlemler otomatik hale getirilirken, Python kütüphaneleri kullanılarak elde edilen verilerin düzenlenmesi, analiz edilmesi ve görselleştirilmesi gerçekleştirilmiştir.

Proje sonucunda web scraping, otomasyon, veri işleme ve veri görselleştirme süreçlerini bir arada içeren bir uygulama geliştirilmiştir.
