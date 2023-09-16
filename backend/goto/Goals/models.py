from django.db import models
from django.utils.translation import gettext_lazy as _

from Users.models import Profile


class Goal(models.Model):
    """Model to store a profile's goals."""

    profile = models.ForeignKey(
        Profile,
        verbose_name=_("Profile"),
        related_name="goals",
        on_delete=models.CASCADE,
    )
    name = models.CharField(_("Goal"), max_length=255)
    description = models.CharField(
        _("Description"), max_length=255, blank=True
    )
    deadline = models.DateField(_("Deadline"), blank=True, null=True)
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    def __str__(self):
        return f"{self.profile.id} goal {self.id}"

    class Meta:
        verbose_name=_("Goal")
        verbose_name_plural=_("Goals")


class Milestone(models.Model):
    """Model to store milestones for a profile's goals."""

    goal = models.ForeignKey(
        Goal,
        verbose_name=_("Goal"),
        related_name="milestones",
        on_delete=models.CASCADE,
    )
    name = models.CharField(_("Milestone"), max_length=255)
    deadline = models.DateField(_("Deadline"), blank=True, null=True)
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    def __str__(self):
        return f"{self.goal.profile.id} goal {self.goal.id} milestone {self.id}"

    class Meta:
        verbose_name = _("Milestone")
        verbose_name_plural = _("Milestones")


class Update(models.Model):
    """Model to store a profile's updates for their goals."""

    goal = models.ForeignKey(
        Goal,
        verbose_name=_("Goal"),
        related_name="updates",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        upload_to="update_images/",
        verbose_name=_("Image"),
        blank=True,
        null=True
    )
    text = models.CharField(_("Text"), max_length=800)
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    def __str__(self):
        return f"{self.goal.profile.id} goal {self.goal.id} update {self.id}"
    
    class Meta:
        verbose_name = _("Update")
        verbose_name_plural = _("Updates")
