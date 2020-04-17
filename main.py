import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    my_input = os.environ["INPUT_MYINPUT"]

    my_output = f"Hello {my_input}"

    print(f"::set-output name=myOutput::{my_output}")
    with open('bamboozle.txt', 'a') as f:
    	write("this works")
    	

if __name__ == "__main__":
    main()
