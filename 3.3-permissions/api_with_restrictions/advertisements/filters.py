from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateFromToRangeFilter()
    status = SearchFilter()

    class Meta:
        model = Advertisement
        fields = [
            'created_at',
            'creator_id',
            'status',
        ]
