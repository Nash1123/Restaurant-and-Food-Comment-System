from django.contrib import admin
from restaurants.models import Restaurant, Food, Comment, FoodComment

class RestaurantAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone_number', 'address')
	search_fields = ('name',)

class FoodAdmin(admin.ModelAdmin):
	list_display = ('name', 'restaurant', 'price')
	list_filter = ('is_Spicy',)
	# fields = ('price', 'restaurant')
	# odering = ('-price',)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('content', 'visitor', 'email', 'date_time', 'restaurant')	

class FoodCommentAdmin(admin.ModelAdmin):
	list_display = ('content', 'visitor', 'email', 'date_time', 'food')	

# Register your models here.
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(FoodComment, FoodCommentAdmin)
