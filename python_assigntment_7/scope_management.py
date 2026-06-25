#scope management local .global, global keyword
score =79#global veriable
def single_run():
    score =79-40
    print("single run",score)

single_run()


def others():
    global score
    score= score-39
    print(score)

others()