# notes

This repo is for me to take notes on all kind of subjects.

For example: c-programming, python, algorithms(leetcode, elements of coding interview),...

### File naming:

each folder like algorithms or c-programming, it represents a deck(topic)

in algorithms, there will be 2 folders: questions, solutions

in questions: we name file in this convention: `yyyy-mm-dd_question_name.md`
in solution: we name the corresponding file: `question_name.md`, and this will contain the solutions


### Spaced Repetition Learning System

| Rating | Description | Next Review |
|--------|-------------|-------------|
| 0      | New         |      +1 day |
| 1      | Wrong       | +1 day      |
| 2      | Hard (right but difficult) | +3 days |
| 3 | Good (right and okay) | +7 days |
| 4 | Easy | +14 days |
| 5 | Trivial | +28 days |

### Other files:

review.py: the cli tool
log.csv: logs my progress and daily time


### Usage:

Please follow the folder structure and naming convention, which are easy to do


```bash
review.py      # review all cards due today
review.py <topic>  # review cards due today for that topic
review.py --stats # show analytics
```


### Workflow

`review.py`
1. opens the question.md file in browser, timer starts
2. user codes the solution in one of the .temp files, e.g. temp.py
3. user ends this card, timer logs time, opens the solution.md in browser
4. user compares the solution, rate performance, files names are incremented based on rules 
5. select next question or end session
    + end session: timer stops, logs total time for this question, Rollover all unreviewed-cards to the next day, i.e. all undone questions today gets +1 in their date part of the filename, cleans the files in /temp, and regenerate clean blank ones, close the current question.md, solution.md in browser
    + next question: timeer stops, logs total time for this question, repeat step 1, cleans the files in temp, and regenrate clean blank ones, close the current question.md, solution.md in browser


### Log format
timestamp, topic, question, rating, used_time_in_mins, attempts