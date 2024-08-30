from .models import CompanyProfile, ExpertProfile


def update_profile_type(user, profile_data):
    if profile_data.get("is_company"):
        user.is_company = True
        user.is_expert = False
    elif profile_data.get("is_expert"):
        user.is_expert = True
        user.is_company = False
    user.save()
    return user


def create_company_profile(user, profile_data):
    if not CompanyProfile.objects.filter(user=user).exists():
        company_profile = CompanyProfile.objects.create(user=user, **profile_data)
        return company_profile
    else:
        raise Exception("Company profile already exists")


def create_expert_profile(user, profile_data):
    if not ExpertProfile.objects.filter(user=user).exists():
        expert_profile = ExpertProfile.objects.create(user=user, **profile_data)
        return expert_profile
    else:
        raise Exception("Expert profile already exists")
