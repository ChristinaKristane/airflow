from stackapi import StackAPI
SITE = StackAPI('stackoverflow')
questions = SITE.fetch('questions', fromdate=1457136000, todate=1457222400,
min=20, tagged='python', sort='votes')
questions
{
'backoff': 0,
'has_more': False,
'items': [
            {
                u'accepted_answer_id': 35818398,
                u'answer_count': 2,
                u'creation_date': 1457186774,
                u'is_answered': True,
                u'last_activity_date': 1457246584,
                u'last_edit_date': 1457200889,
                u'link': u'http://stackoverflow.com/questions/35815093/sine-calculation-orders-of-magnitude-slower-than-cosine',
                u'owner': {u'accept_rate': 80,
                            u'display_name': u'Finwood',
                            u'link': u'http://stackoverflow.com/users/1525423/finwood',
                            u'profile_image': u'https://i.stack.imgur.com/xkRry.png?s=128&g=1',
                            u'reputation': 1575,
                            u'user_id': 1525423,
                            u'user_type': u'registered'},
                u'question_id': 35815093,
                u'score': 22,
                u'tags': [u'python', u'numpy', u'scipy', u'signal-processing'],
                u'title': u'sine calculation orders of magnitude slower than cosine',
                u'view_count': 404
            }
        ],
'page': 1,
'quota_max': 300,
'quota_remaining': 171,
'total': 0
}