from stackapi import StackAPI
SITE = StackAPI("stackoverflow")
SITE.max_pages=2
SITE.page_size=100
questions = SITE.fetch('questions', min=10, sort='votes')
for quest in questions['items']:
    if 'title' not in quest or quest['is_answered'] == False:
        continue
    title = quest['title'] 
    print('Question :- {0}'.format(title))
    question_id = quest['question_id']
    print('Question ID :- {0}'.format(question_id))
    top_answer = SITE.fetch('questions/' + str(question_id) + '/answers', order = 'desc', sort='votes')
    print(top_answer)