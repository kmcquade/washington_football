import unittest
from washington_football.command.suck import new_favorite_team


class CanILeaveThisTeam(unittest.TestCase):
    def test_new_favorite_team(self):
        desired_output = "Ravens"
        output = new_favorite_team("Redskins")
        print("Notice how, to pass this test, "
              "your mindset should be that no matter what you try, you can't go back to this god awful team.")
        self.assertEqual(desired_output, output)
