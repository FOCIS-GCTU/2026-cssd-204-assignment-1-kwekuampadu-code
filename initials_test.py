import os.path
import sys
from kaa import main


def test_initials():
    try:
        exists = os.path.exists("kaa.py")
        assert exists == True
    except:
        sys.exit()


    main()
