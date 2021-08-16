import pytest

from boj import BOJProblem


def test_init():
    problem = BOJProblem(1000)


def test_init_TypeError():
    with pytest.raises(TypeError):
        problem = BOJProblem()


def test_init_KR_Description():
    problem = BOJProblem(1000, language="0")

    assert problem.document.problem_id == "1000"
    assert problem.document.problem_lang == "0"
    assert problem.document.title == "A+B"
    assert problem.document.description == "<p>\ub450 \uc815\uc218 A\uc640 B\ub97c \uc785\ub825\ubc1b\uc740 \ub2e4\uc74c,&nbsp;A+B\ub97c \ucd9c\ub825\ud558\ub294 \ud504\ub85c\uadf8\ub7a8\uc744 \uc791\uc131\ud558\uc2dc\uc624.</p>\r\n"
    assert problem.document.input == "<p>\uccab\uc9f8 \uc904\uc5d0 A\uc640 B\uac00 \uc8fc\uc5b4\uc9c4\ub2e4. (0 &lt; A, B &lt; 10)</p>\r\n"
    assert problem.document.output == "<p>\uccab\uc9f8 \uc904\uc5d0 A+B\ub97c \ucd9c\ub825\ud55c\ub2e4.</p>\r\n"
    assert problem.document.hint == "<p><a href=\"https://www.acmicpc.net/help/language\">\uc5ec\uae30</a>\ub97c \ub204\ub974\uba74 1000\ubc88 \uc608\uc81c \uc18c\uc2a4\ub97c \ubcfc \uc218 \uc788\uc2b5\ub2c8\ub2e4.</p>\r\n"
    assert problem.document.original == "1"
    assert problem.document.html_title == "0"
    assert problem.document.problem_lang_tcode == "Korean"


def test_init_EN_Description():
    problem = BOJProblem(1000, language="1")

    assert problem.document.problem_id == "1000"
    assert problem.document.title == "A+B"
    assert problem.document.description == "<p>Given two integers A and B, calculate their sum.</p>\r\n"
    assert problem.document.description == "<p>Given two integers A and B, calculate their sum.</p>\r\n"
    assert problem.document.input == "<p>The first line contains&nbsp;two integers A and B. (0 &lt; A, B &lt; 10)</p>\r\n"
    assert problem.document.output == "<p>Output one line of one integer, A+B.</p>\r\n"
    assert problem.document.hint == ""
    assert problem.document.original == "0"
    assert problem.document.html_title == "0"
    assert problem.document.problem_lang == "1"
    assert problem.document.problem_lang_tcode == "English"
