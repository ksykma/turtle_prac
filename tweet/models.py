from django.db import models
from users.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # on_delete는 삭제했을때 어떻게 할건지!! CASCADE는 삭제할 때 다 없애겠다.
    
    def __str__(self):  # admin 페이지 tweet앱에서 article object말고 게시글 이름이 뜨게 한다.
        return str(self.title)