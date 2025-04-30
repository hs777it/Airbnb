from .models import SiteInfo,Link

def myfooter(request):
    myfooter = SiteInfo.objects.last()
    return {'myfooter':myfooter}


def link_context(request):
    link = Link.objects.last()
    return {'logo': link}
