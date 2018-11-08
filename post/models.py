from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model): # Post modeli.
    user = models.ForeignKey("auth.User", on_delete="models.CASCADE", verbose_name="Yazar", related_name="posts")
    title = models.CharField(max_length=120, verbose_name="Başlık") # başlık alanı. max_length belirtmek zorunlu
    content = RichTextField(verbose_name="İçerik") # uzun metinler için
    publishing_date = models.DateTimeField(verbose_name="Tarih", auto_now_add=True) # zaman ve tarih bilgisi
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=120)

    def __str__(self): # post model nesnesi için başlık bilgisi döndürür.
        return self.title

    def get_absolute_url(self):
        #return "/post/{}/detail/".format(self.id) # kötü yöndem daha iyisi var
        return reverse("post:detail", kwargs={"slug": self.slug})

    def get_create_url(self):
        #return "/post/{}/detail/".format(self.id) # kötü yöndem daha iyisi var
        return reverse("post:detail")

    def get_update_url(self):
        #return "/post/{}/detail/".format(self.id) # kötü yöndem daha iyisi var
        return reverse("post:update", kwargs={"slug": self.slug})

    def get_delete_url(self):
        #return "/post/{}/detail/".format(self.id) # kötü yöndem daha iyisi var
        return reverse("post:delete", kwargs={"slug": self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title.replace("ı", "i"))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-publishing_date"]

class Comment(models.Model):
    post = models.ForeignKey("post.Post", on_delete="models.CASCADE", related_name="comments")
    name = models.CharField(max_length=200, verbose_name="İsim")
    content = models.TextField(verbose_name="Yorum")
    created_date = models.DateTimeField(auto_now_add=True)
