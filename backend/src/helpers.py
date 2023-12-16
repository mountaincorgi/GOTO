from django.http import Http404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, SAFE_METHODS, BasePermission
# Custom queryset filter backends



# Custom permission classes
class IsOwnerOrFriendsReadOnly(BasePermission):
    """Custom permissions for objects linked to a single profile.
    
    Grants the owner profile full permissions over all views. Friends have
    read-only access. All requests must be authenticated.
    """
    
    def has_permission(self, request, view):
        context_profile = self._get_context_profile(request.path)
        requestor = request.user.profile
        return super().has_permission(request, view)
    
    # Note: only called if has_permission succeeds
    def has_object_permission(self, request, view, obj):
        owner = obj.get_profile()
        requestor = request.user.profile

        if requestor == owner:
            return True
        elif request.method in SAFE_METHODS and owner.is_friends_with(
            requestor
        ):
            return True
        else:
            return False
        
    def _get_context_profile(self, path):
        """Get the context Profile from the path."""

        from django.contrib.auth.models import User

        # This is closely tied to URL structure. Alternatively could go in a
        # middleware.
        username = path.strip("/").split("/")[0]
        try:
            context_user = User.objects.select_related("profile").get(
                username=username
            )
        except User.DoesNotExist:
            raise Http404
        return context_user.profile
