import contextlib
import json
import sqlite3

from dataclasses import asdict
from typing import Generator

from boj.settings import DATABASE_FILE
from boj.models import ProblemDTO, SectionDTO, TestCaseDTO


@contextlib.contextmanager
def get_connection() -> Generator[sqlite3.Connection, None, None]:
    connection = sqlite3.connect(DATABASE_FILE)
    try:
        yield connection
    finally:
        connection.close()


def initialize_database():
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS problems (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                sections TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS testcases (
                problem_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                input TEXT NOT NULL,
                output TEXT NOT NULL
            )
        ''')
        connection.commit()


def save_problem(problem: ProblemDTO):
    with get_connection() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                '''
                    INSERT OR REPLACE INTO problems (id, title, sections)
                    VALUES (?, ?, ?)
                ''',
                (
                    problem.id,
                    problem.title,
                    json.dumps([*map(asdict, problem.sections)],
                               ensure_ascii=False),
                ),
            )
            cursor.executemany(
                '''
                    INSERT OR REPLACE INTO testcases (problem_id, name, input, output)
                    VALUES (?, ?, ?, ?)
                ''',
                [
                    (problem.id, testcase.name, testcase.input, testcase.output)
                    for testcase in problem.testcases
                ],
            )
            connection.commit()
        except sqlite3.Error as e:
            print(f'Error saving problem {problem.id}: {e}')

            connection.rollback()
            print('Transaction rolled back due to error.')


def get_problem(problem_id: int) -> ProblemDTO:
    testcases = get_testcases(problem_id)
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            '''
                SELECT id, title, sections
                FROM problems
                WHERE id = ?
            ''',
            (problem_id,),
        )
        row = cursor.fetchone()
        if not row:
            raise ValueError(f'Problem not found: {problem_id}')
        id, title, sections = row
        sections = json.loads(sections)
        return ProblemDTO(
            id=id,
            title=title,
            sections=[SectionDTO(**section) for section in sections],
            testcases=testcases,
        )


def get_testcases(problem_id: int) -> list[TestCaseDTO]:
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            '''
                SELECT name, input, output
                FROM testcases
                WHERE problem_id = ?
            ''',
            (problem_id,),
        )
        rows = cursor.fetchall()
        return [
            TestCaseDTO(
                name=name,
                input=input,
                output=output,
            )
            for name, input, output in rows
        ]
