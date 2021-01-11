from .models import Company

def company_info_to_context(request):
    company = Company.objects.first()
    return {
        'phone_number': company.phone_number,
        'email': company.email,
        'address': company.address,
        'twitter': company.twitter_link,
        'facebook': company.fb_link,
        'instagram': company.instagram_link
    }
