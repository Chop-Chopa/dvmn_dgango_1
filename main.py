import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard


posts = Passcard.objects.all()
some_post = posts[0]
published_posts = Passcard.objects.filter(is_active=True)


if __name__ == '__main__':
    print(f'owner_name: {some_post.owner_name}')
    print(f'passcode: {some_post.passcode}')
    print(f'created_at: {some_post.created_at}')
    print(f'is_active: {some_post.is_active}')
    print(f'Активных пропусков: {len(published_posts)}')
    print('Количество пропусков:', Passcard.objects.count())
