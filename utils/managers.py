from django.db.models import QuerySet, Q, Sum


class CustomQuerySet(QuerySet):
    """
    Custom queryset that will be reused by different models.
    It enables soft delete and precise filtering, (ie to get all
    property that has not been soft deleted, simply run:
        Property.active_objects.all_objects()
        )
    """

    def _active(self):
        """Return only objects that haven't been soft deleted."""
        return self.filter(is_deleted=False)

    def all_objects(self):
        """Return all objects that haven't been soft deleted"""
        return self._active()

    def all_approved(self):
        """ return client companies that are approved"""
        return self._active().filter(approval_status='approved')
