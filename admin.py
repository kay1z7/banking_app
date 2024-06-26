from django.contrib import admin
from .models import Project, Category, CategoryProject


class ProjectAdmin(admin.ModelAdmin):
    list_display=('name','description','total_budget')

admin.site.register(Project,ProjectAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','description')

admin.site.register(Category,CategoryAdmin)


class CategoryProjectAdmin(admin.ModelAdmin):
    list_display=('budget', )

admin.site.register(CategoryProject, CategoryProjectAdmin)
