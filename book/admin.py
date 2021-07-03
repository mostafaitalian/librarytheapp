from django.contrib import admin
from .models import Book, Authar, Reader
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_tags', 'get_authars', 'no_of_reads', 'poster']
    def get_tags(self,obj):
        return ','.join([str(t) for t in obj.tags.all()])
    def get_authars(self, obj):
        return ','.join([str(t) for t in obj.authars.all()])
class BookInline(admin.TabularInline):
    model= Book



@admin.register(Authar)
class AutharAdmin(admin.ModelAdmin):
    list_display = ['name']
    # inlines = [BookInline,]

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created', 'updated', 'no_of_reading_books']
    # inlines=[BookInline,]