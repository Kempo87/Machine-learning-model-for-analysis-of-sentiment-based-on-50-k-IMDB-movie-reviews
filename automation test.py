def test_preprocess_review_lowercase():
    text = 'This is a Review'
    got = text.lower()
    expected = "this is a review"
    assert got == expected 

def test_preprocess_review_replace():
    text = 'This review contains <br /> tag'
    got = text.replace('<br />', ' ')
    expected = "this review contains tag"
    assert got == expected

def test_preprocess_review_split():
    text = 'This is a review'
    got = text.split()
    expected = "This", "is", "a", "review"
    assert got == expected