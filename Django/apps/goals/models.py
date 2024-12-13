from django.db import models
from django.conf import settings


class StudyGoal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='goals')
    title = models.CharField(max_length=200)  # 目標タイトル
    description = models.TextField(blank=True, null=True)  # 詳細な説明
    start_date = models.DateField()  # 開始日
    end_date = models.DateField()  # 終了予定日
    is_completed = models.BooleanField(default=False)  # 完了状態

    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時
    updated_at = models.DateTimeField(auto_now=True)  # 更新日時

    def __str__(self):
        return self.title
    
class Progress(models.Model):
    goal = models.ForeignKey('StudyGoal', on_delete=models.CASCADE, related_name='progresses')
    date = models.DateField()  # 進捗記録の日付
    progress_percentage = models.PositiveIntegerField()  # 進捗率（0～100）
    note = models.TextField(blank=True, null=True)  # メモや詳細

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.goal.title} - {self.date}"

class Comment(models.Model):
    goal = models.ForeignKey('StudyGoal', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()  # コメント内容
    created_at = models.DateTimeField(auto_now_add=True)  # コメント作成日時

    def __str__(self):
        return f"Comment by {self.user.username} on {self.goal.title}"
