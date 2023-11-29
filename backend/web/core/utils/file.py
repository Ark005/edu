def get_song_filepath(instance, filename):
    return f'song/{instance.name}_{instance.id}'


def get_analysis_filepath(instance, filename):
    return f'analysis/{instance.name}_{instance.id}'


def get_about_filepath(instance, filename):
    return f'analysis/{instance.name}_{instance.id}'
