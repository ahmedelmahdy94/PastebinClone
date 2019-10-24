from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
# from get_username import get_username

# Create your models here.
import uuid

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, blank=False)
    content = models.TextField(blank=True, null=True)
    generated_url = models.CharField( max_length=10, blank=False,null=True)
    create_date = models.DateField(auto_now=False, auto_now_add=True)
    Active = models.BooleanField(default=True)
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    # models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    # auto generate url
    def save(self, *args, **kwargs):
        rand = str(uuid.uuid4())[:10]
        while Posts.objects.filter(generated_url=rand):
            rand = str(uuid.uuid4())[:10]
        self.generated_url = rand
        # self.user = get_username()
        # print "Your username is: %s" % (Posts.user)
        super(Posts, self).save( *args, **kwargs)
