from django.db import models


class Message(models.Model):
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'ticket_messages'
        
    def __str__(self) -> str:
        return self.ticket.title
