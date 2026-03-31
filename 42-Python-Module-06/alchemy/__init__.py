# Metadata asked by the subject...cringe
__version__ = "1.0.0"
__author__ = "Master Pythonicus"

# We only wanna import fire and water to the demo script
from .elements import create_fire, create_water

# And this below me is...idk flake8 gets fussy
# but basically this is like "what available stuff i have"
__all__ = ["create_fire", "create_water"]


"""
why init.py? u might ask
basically besides init being a constructor in OOP,
init is also a "diy module maker" so you can import your
custom things as well, so its like "hey! im a module too!"
"""
