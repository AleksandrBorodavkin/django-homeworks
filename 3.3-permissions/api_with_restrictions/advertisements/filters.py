from django_filters import rest_framework as filters, DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры

    created_at = DateFromToRangeFilter()
    creator_id = DjangoFilterBackend()
    status = SearchFilter()

    class Meta:
        model = Advertisement
        fields = [
            'created_at',
            'creator_id',
            'status',
        ]
