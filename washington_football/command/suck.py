import click


@click.command()
@click.option(
    '--so-bad',
    is_flag=True,
    help='For some reason, you love a football team that just disappoints you again and again.'
)
def suck(so_bad):
    """Remind yourself why it's not worth it to root for a team that doesn't care about you"""
    if so_bad:
        print("Life is short, bro. "
              "They won't win a super bowl or even the NFC Championship \n"
              "anytime in the next decade. So why are you wasting your time? \n"
              "Learn to love the Ravens and move on with your life.")


def new_favorite_team(supplied_team):
    return "Ravens"
