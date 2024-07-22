def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return
        
    except ValueError as v:
        print("Errrooorrr!")
        print(v)
        return
        
    # in a function if even a function returns then also finally will be executed
    finally:
        print("I am inside finally!")
        
main()