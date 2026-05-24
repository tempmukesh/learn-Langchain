from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """If you love reading books, read away. If you hate reading, then go watch my
videos or listen to my podcast because there’s no one way of learning.
There is only one way of growing though, and that is through little
accomplishments.
Life is all about little accomplishments. I don’t want you to read the
whole book right away; I want you to read this one chapter, that’s it. Put
this book down if you want to finish reading this book in one go. Frankly, I
don’t want you to complete this book. I don’t want you to take away
anything from it apart from the fact that you have to finish one chapter a
day. That’s it.
It’s hard to form good habits, even harder to stick to them. When we look
at a project as a whole, we see how much we have to do, and it becomes
burdensome. Take this book for instance. Writing 50,000 words? Oh, God!
I’m panicking even at the idea.
I don’t know how to fill so many pages! I’m legit staring at my laptop
screen, typing these sentences and trying to figure out if it makes any sense.
But then again, I’m doing it one sentence at a time, one paragraph at a time,
one chapter at a time. And soon enough this book will be in your hands and
I’d have done my job.
Writing a book is uncomfortable. Getting out of our beds in the morning
is uncomfortable. Attending that online class where you have no idea what
the tutor is teaching is uncomfortable. Going to that job that you absolutely
hate is uncomfortable. Executing all those plans that you have been making,
or let’s say daydreaming about, is uncomfortable. They are all
uncomfortable. But just because something is uncomfortable doesn’t mean 
you stop doing it. Growth is uncomfortable, but being uncomfortable is the
only way you grow.
If you’re thinking, ‘But Raj, I just don’t think I can do it today. I want to
give my best’, then you need to accept that there are going to be days when
you won’t be able to give your best, and that’s completely okay. Sometimes
trying is all you need to do. Sometimes, showing up is the most you can do.
This is the reason I don’t want you to finish this book in a day, because I
didn’t write it in a day. Ever heard that phrase, ‘Rome wasn’t built in a
day’? One brick at a time, one sentence at a time, and one chapter at a time,
that is how we are going to do this.
If you do that, that’s a win for me. Complete one chapter a day so that
you are building small habits and you’re achieving small things every day.
That’s a good habit to inculcate in your life: little accomplishments every
day, consistently."""


splitter = RecursiveCharacterTextSplitter(
    chunk_size = 101,
    chunk_overlap = 0,
    separators=["\n\n", "\n", "."]
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)