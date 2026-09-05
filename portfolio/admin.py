from django.contrib import admin
from .models import Achievement, Certification, ContactMessage, Education, Experience, Profile, Project, Skill


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('name', 'headline', 'bio', 'objective')}), ('Details', {'fields': ('location', 'education', 'availability', 'email', 'github_url', 'linkedin_url', 'resume', 'profile_image')}))


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'sort_order', 'created_at')
    list_filter = ('is_featured',)
    search_fields = ('title', 'summary', 'technologies')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('sort_order', '-created_at')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level', 'sort_order')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)


for model in (Certification, Education, Experience, Achievement):
    admin.site.register(model)

admin.site.site_header = 'Portfolio Content Studio'
admin.site.site_title = 'Portfolio Admin'
admin.site.index_title = 'Manage your developer portfolio'