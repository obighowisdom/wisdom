from django.contrib import admin

# Register your models here.

from .models import prove
from .models import grate
from .models import hmm

admin.site.register(prove)
admin.site.register(grate)
admin.site.register(hmm)