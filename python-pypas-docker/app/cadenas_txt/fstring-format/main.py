def run(number):
    # TODO
    a=f"{round(number,3)}"
    b=f"{number}0"
    c=f"    {round(number,2)}"
    d=f"{number}0e+00"
    e=f"0000{round(number,4)}"
    f=f"            {number}"
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
