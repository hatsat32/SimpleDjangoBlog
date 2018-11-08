# Simple Django Blog

Django öğrenirken youtubedaki video derslerden çalışırken yaptığım küçük bir blog projesi. Django 2.1, python 3.6 ve bootstrap 3 kullanılmıştır. 

## Video dersler hakkında

Tabikide bu derslerin yayınlanma tarihinden bi kaç yıl geçti. Dolayısıyla bende hem yeni sürümlere adapte olmak hemde projenin daha güncel halinin bulunması için video dersleri tekrardan izledim ve projeyi tekrardan kodladım.

Eğer djangoya yeni başladıysanız bu video dersleri izlemenizi tavsiye ederim. Linkler aşağıda.

* [Barış aslan Django ile Web Programlama](https://www.youtube.com/playlist?list=PLPrHLaayVkhny4WRNp05C1qRl1Aq3Wswh)
* [django-dersleri github sayfası](https://github.com/barissaslan/django-dersleri)

## Proje Özellikleri

* Blog post ekleme, silme, güncelleme.
* Yorum ekleme
* Blog yazısına resim, dosya ekleme.
* Kullanıcı üyelikleri için kayıt olma ve giriş yapma.
* Basit bir editörle html bilgisi olmadan yezı yazabilme.

## Bağımlılıklar

* django
* django-ckeditor
* django-crispy-forms
* Pillow

## Kurulum

Kurulumları `virtualenv` içine yapmanızı tavsiye ederiz. Bu sayede proje sistemden soyutlanmış olarak çalışabilecek.

```
virtualenv venv
source venv/bin/activate
```

Eğer django kurulu değilse şu komutla kurabilirsiniz.

```
pip install django
```

Bağımlılıkları şu komut ile kurabilirsiniz.

```
pip install -r requirements.txt
```

Django kurulumunu tamamladıktan sonra proje dizinini istediğiniz bir dizine taşıyın. Ardından terminal üzerinden  `manage.py` nin bulunduğu dizine girin. Veritabanını oluşturmak için şu 2 komutu girin.

```
python manage.py makemigrations
python manage.py migrate
```

Veritabanı oluşacaktır. Ardından bir `superuser` oluşturmalıyız. Admin arayüzüne girmek için.

```
python manage.py createsuperuser
```

Gerekli bilgileri girdikten ve admin hesabını oluşturduktan sonra artık projeyi çalıştırabiliriz.

```
python manage.py runserver
```