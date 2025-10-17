# for letter in "this a good day)":
#     print(letter)
# my_list = [1,2,3,4,5]
# iter_list = iter(my_list)
# print(iter_list)

# def raise_to_the_degrees(number,max_degree):
#     i = 0
#     for _ in range(max_degree):
#         yield number**1
#         i += 1
# res = raise_to_the_degrees(12332245,700)
# print(res)
# for _ in res:
#      print(_)

# class Helper:
#     def __init__(self,works):
#         self.works = works
#     def __call__(self,works):
#         return f"""I can do {self.works} for you. I help you with {works}"""
    
# helper = Helper("test")
# print(helper("exercise 2"))

# import os
# import logging 

# filename = os.path.normpath("\\qef\\app.log")
 
# logging.basicConfig(
 
    
#     filename="app.log",
#     filemode="a",
#     level=logging.DEBUG,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )
# logging.warning("file not founded")
# logging.debug("Programe bagged")
# logging.critical("Founded critical error in program")

import logging

# logging.basicConfig(
#     filename ="error.log",
#     filemode="w",
#     level=logging.ERROR,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )
# try:
#     print(f"{2+2*6}")
# except Exception as e:
#     logging.exception("Something went wrong")

import logging
import unittest
from unit_test_lesson2 import*
logging.basicConfig(
    filename ="trace.log",
    filemode="a",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class TestAdder(unittest.TestCase):
    def test_adder(self):
        self.assertEqual(adder(1,2,3),6)
    def test_adder_kwargs(self):
        self.assertEqual(adder(a=1,b=2,c=3), 6)
        self.assertEqual(adder(1,2,a=3,b=4), 10)

if __name__ == "__main__":
    logging.info(unittest.main())
    logging.info("Session ended")

