from faker import Faker

fake = Faker()

def generate_fake_paragraph(num_sentences=5):
    paragraph = ' '.join([fake.sentence() for _ in range(num_sentences)])
    return paragraph