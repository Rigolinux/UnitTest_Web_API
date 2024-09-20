import os
from dotenv import load_dotenv
import pytest

load_dotenv()

def run_tests():
    pytest.main(["GetDialgaName.py", "GetFirstGenerationPokemons.py"])

run_tests();
