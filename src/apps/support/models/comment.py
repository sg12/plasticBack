from django.db import models


class Comment(models.Model):
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    text = models.TextField()
    
    class Meta:
        db_table = 'ticket_comments'

    def __str__(self) -> str:
        return self.ticket.theme
