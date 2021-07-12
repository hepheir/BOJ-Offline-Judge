from boj import BOJProblem


def test_BOJProblem():
    problem = BOJProblem(1000)

    assert problem.problem_id == 1000
    assert problem.title == 'A+B'
