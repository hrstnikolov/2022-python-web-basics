from music_app.web.models import Profile


def get_profile():
    try:
        # TODO: fix the case when there are multiple profiles: Profile.MultipleObjectsReturned
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None

