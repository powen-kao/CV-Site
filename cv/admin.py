from django.contrib import admin
from .models import Experience, Education, Skill, SkillCategory, Framework, Portfolio, Tag


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'department', 'start_date', 'end_date')
    save_as = True


@admin.register(Education)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('university', 'major', 'start_date', 'end_date')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'category')


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')


@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill')


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'link', 'rank')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'framework')
