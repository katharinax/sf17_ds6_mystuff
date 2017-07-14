#!/home/katharina/anaconda3/bin/python
import logging
print("logging in")
from app import app as application
print("app in")

#logger = logging.getLogger("app")

def main(port=5000, debug=False):
    #logger.info("Staring App at Port: {} with Debug Option: {}".format(port, debug))
    application.run(port=port, debug=debug)


if __name__ == '__main__':
    print("start")
    main()
