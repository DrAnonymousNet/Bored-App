from django_filters import filterset


class Bored(filterset.FilterSet):
    type = filterset.CharFilter()
    participant = filterset.NumberFilter()
    accessibility = filterset.NumberFilter()
    min_price = filterset.NumberFilter()
    max_price = filterset.NumberFilter()