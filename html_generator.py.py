Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

>>> def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

>>> TEST_TEXT = """TITLE: How the Internet Works
DESCRIPTION: The internet is a collection of computers and 
servers that are connected to each other.
The WEB is a collection of HTML pages.
Web browser use HTML as there language to communicate.
HTML allows computers to interpret web pages and display 
them so users can easily read them. """

>>> print get_title(TEST_TEXT)
How the Internet Works
>>> print get_description(TEST_TEXT)
The internet is a collection of computers and 
servers that are connected to each other.
The WEB is a collection of HTML pages.
Web browser use HTML as there language to communicate.
HTML allows computers to interpret web pages and display 
them so users can easily read them. 
>>> #The above will find the Title and display the text after the word title until it
#gets to the word description.  The same goes for get_descripition.  This will get
#the information for one concept. The print statement displays
#The text without the words TITLE: and DESCRIPTION:

>>> Project_TEXT = """TITLE: How the Internet Works
DESCRIPTION: The internet is a collection of computers and 
servers that are connected to each other.
The WEB is a collection of HTML pages.
Web browser use HTML as there language to communicate.
HTML allows computers to interpret web pages and display 
them so users can easily read them.
TITLE: HTML
DESCRIPTION: HTML is made up of the following:
Text Content (The plain text you write you what you actually see)
Mark ups (What it looks like. Tags are used to display images and video's)
References to other Web sites
Links to other pages
In-Line vs Block
Block elements form an invisible box around the elements, div tags are an example.
In-line applies to that spefic line of code. Span tags are a good example.
TITLE: TAGS
DESCRIPTION: HTML Mark-ups are made with "tags"
Tags have "Contents" between them
Contents are what the computer will display and 
tags are what tell the computer how to display them.
Tags are contained with in the angles brackets like this <and>
Tags must have openings < and may have closing /> but some are void and 
do not need a closing tag.
TITLE: Why Computers are Stupid
DESCRIPTION: Computers are stupid. They take everything in code literally. 
When using code you need to make sure you tell the computer 
exactly what to say."""

>>> def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        concept = text[next_concept_start:next_concept_end]
        text = text[next_concept_end:]
    return concept   

>>> print get_concept_by_number(Project_TEXT,3)
TITLE: TAGS
DESCRIPTION: HTML Mark-ups are made with "tags"
Tags have "Contents" between them
Contents are what the computer will display and 
tags are what tell the computer how to display them.
Tags are contained with in the angles brackets like this <and>
Tags must have openings < and may have closing /> but some are void and 
do not need a closing tag.

>>> #This defines how you can scroll through the text and find each concept #. This defines
#how the concepts are broken up and numbered.
#The print displays the 3rd "Concept."
#Note: that it actually displays the entire concept including TITLE: and DESCRIPTION.

>>> def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="lessonbox">
    <div class="lesson-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="lesson-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

>>> print generate_concept_HTML(get_title(Project_TEXT),get_description(Project_TEXT))

<div class="lessonbox">
    <div class="lesson-title">
        How the Internet Works
    </div>
    <div class="lesson-description">
        The internet is a collection of computers and 
servers that are connected to each other.
The WEB is a collection of HTML pages.
Web browser use HTML as there language to communicate.
HTML allows computers to interpret web pages and display 
them so users can easily read them.
TITLE: HTML
DESCRIPTION: HTML is made up of the following:
Text Content (The plain text you write you what you actually see)
Mark ups (What it looks like. Tags are used to display images and video's)
References to other Web sites
Links to other pages
In-Line vs Block
Block elements form an invisible box around the elements, div tags are an example.
In-line applies to that spefic line of code. Span tags are a good example.
TITLE: TAGS
DESCRIPTION: HTML Mark-ups are made with "tags"
Tags have "Contents" between them
Contents are what the computer will display and 
tags are what tell the computer how to display them.
Tags are contained with in the angles brackets like this <and>
Tags must have openings < and may have closing /> but some are void and 
do not need a closing tag.
TITLE: Why Computers are Stupid
DESCRIPTION: Computers are stupid. They take everything in code literally. 
When using code you need to make sure you tell the computer 
exactly what to say.
    </div>
</div>
>>> #This adds the div tags to the "Concepts" to generate the output in HTML form.
#Note: this def does not call on the get_concept_by_number.
#The print statement above displays everything after the first
#<div class="concept-description"> as the first description because it will not call
# concept_by_number.  This generates one full HTML for each concept.  A full concept 
#includes the (div tags, Concept Title, and Concept description)

>>> def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html

>>> #Finally this def calls on all previous def and puts a counter for the concepts.
#This breaks the text into the concepts and inserts the div tags.  It continues through
#the loop until it reaches the end of the text.

>>> print generate_all_html(Project_TEXT)

<div class="lessonbox">
    <div class="lesson-title">
        How the Internet Works
    </div>
    <div class="lesson-description">
        The internet is a collection of computers and 
servers that are connected to each other.
The WEB is a collection of HTML pages.
Web browser use HTML as there language to communicate.
HTML allows computers to interpret web pages and display 
them so users can easily read them.

    </div>
</div>
<div class="lessonbox">
    <div class="lesson-title">
        HTML
    </div>
    <div class="lesson-description">
        HTML is made up of the following:
Text Content (The plain text you write you what you actually see)
Mark ups (What it looks like. Tags are used to display images and video's)
References to other Web sites
Links to other pages
In-Line vs Block
Block elements form an invisible box around the elements, div tags are an example.
In-line applies to that spefic line of code. Span tags are a good example.

    </div>
</div>
<div class="lessonbox">
    <div class="lesson-title">
        TAGS
    </div>
    <div class="lesson-description">
        HTML Mark-ups are made with "tags"
Tags have "Contents" between them
Contents are what the computer will display and 
tags are what tell the computer how to display them.
Tags are contained with in the angles brackets like this <and>
Tags must have openings < and may have closing /> but some are void and 
do not need a closing tag.

    </div>
</div>
<div class="lessonbox">
    <div class="lesson-title">
        Why Computers are Stupid
    </div>
    <div class="lesson-description">
        Computers are stupid. They take everything in code literally. 
When using code you need to make sure you tell the computer 
exactly what to say
    </div>
</div>
>>> 
