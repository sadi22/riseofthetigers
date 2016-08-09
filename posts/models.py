from __future__ import unicode_literals


from datetime import datetime

from autoslug import AutoSlugField
from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify
from stdimage.models import StdImageField

# Create your models here.
from taggit.managers import TaggableManager


class Category(models.Model):
    cat_name = models.TextField()

    def __str__(self):
        return self.cat_name

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    category_post = models.ForeignKey(Category, default=1)
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True)
    content = models.TextField()
    image = StdImageField(upload_to= '%Y/%m/%d/')
    FEATURED_POST = (
        ('featured', 'Featured Post'),
        ('not', 'Not Featured'),
    )
    TOP_NEWS = (
        ('top', 'Top News'),
        ('not', 'Not'),
    )
    featured_post = models.CharField(max_length=256, choices=FEATURED_POST, default='not')
    top_news = models.CharField(max_length=256, choices=TOP_NEWS, default='not')
    tags = TaggableManager()
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    # image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="475")
    # image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="464")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article", kwargs={"slug": self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    poll = models.ForeignKey(Poll)
    votes = models.IntegerField(default=0)
    perchant = models.DecimalField(max_digits=5,decimal_places=2,default=Decimal('0.00'))

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.choice_text

