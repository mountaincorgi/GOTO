from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    """Model to store custom information and settings on a user."""

    user = models.OneToOneField(
        User,
        verbose_name="User",
        related_name="profile",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")


class UserProxy(User):
    """Proxy the user model to create a profile for each user."""

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super().save(*args, **kwargs)
        if is_new:
            Profile.objects.create(user=self)

    class Meta:
        proxy = True


class Friendship(models.Model):
    """Model to save and track friendships."""

    requestor = models.ForeignKey(
        Profile,
        null=True,
        verbose_name=_("Requestor"),
        related_name="requested_friendships",
        on_delete=models.SET_NULL,
    )
    requestee = models.ForeignKey(
        Profile,
        null=True,
        verbose_name=_("Requestee"),
        related_name="received_friendship_requests",
        on_delete=models.SET_NULL,
    )
    sent = models.DateTimeField(_("Sent"), auto_now_add=True)
    confirmed = models.BooleanField(_("Confirmed"), default=False)

    def __str__(self):
        id_1 = self.requestor.id if self.requestor else "none"
        id_2 = self.requestee.id if self.requestee else "none"
        return f"Friendship from {id_1} to {id_2} sent at {self.sent}"

    class Meta:
        verbose_name = _("Friendship")
        verbose_name_plural = _("Friendships")


class Message(models.Model):
    """Model to store and track messages."""

    sender = models.ForeignKey(
        Profile,
        null=True,
        verbose_name=_("Sender"),
        related_name="sent_messages",
        on_delete=models.SET_NULL,
    )
    receiver = models.ForeignKey(
        Profile,
        null=True,
        verbose_name=_("Receiver"),
        related_name="received_messages",
        on_delete=models.SET_NULL,
    )
    sent = models.DateTimeField(_("Sent"), auto_now_add=True)
    text = models.CharField(_("Text"), max_length=255)

    def __str__(self):
        id_1 = self.sender.id if self.sender else "none"
        id_2 = self.receiver.id if self.receiver else "none"
        return f"Message from {id_1} to {id_2} sent at {self.sent}"

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")
