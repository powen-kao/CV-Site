from django.contrib import admin
from .models import Experience, Education, Skill

# Register your models here.
# admin.site.register(Experience)
# admin.site.register(Education)
# admin.site.register(Skill)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'department', 'start_date', 'end_date')
    save_as = True


@admin.register(Education)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('university', 'major', 'start_date', 'end_date')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
