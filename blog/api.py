from blog.models import Blog
from rest_framework import viewsets, permissions
from .serializer import BlogSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BlogSerializer