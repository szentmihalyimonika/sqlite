import sqlite3
conn = sqlite3.connect('questions.db')
def get_questions():
  cur = conn.cursor()
  res = cur.execute('select*from questions')
  return res.fetchall()
questions  = get_questions()
get_answers(questions ID):




  
