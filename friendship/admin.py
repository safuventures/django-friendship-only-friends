from django.contrib import admin

from .models import Block, Friend, FriendshipRequest


class BlockAdmin(admin.ModelAdmin):
    model = Block
    raw_id_fields = ("blocker", "blocked")


class FriendAdmin(admin.ModelAdmin):
    model = Friend
    raw_id_fields = ("to_user", "from_user")


class FriendshipRequestAdmin(admin.ModelAdmin):
    model = FriendshipRequest
    raw_id_fields = ("from_user", "to_user")


admin.site.register(Block, BlockAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(FriendshipRequest, FriendshipRequestAdmin)
