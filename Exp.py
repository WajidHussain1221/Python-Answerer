
# You Need To Install Following Packages  To Complete The Task:

# pip install wikipedia
# pip install text-to-speech



import wikipedia        #This Can Be Usefull In Summarizing Tons Of Topics

import webbrowser        # We Will Use The Webbrowser(python built-in),
                        # To Search For The Similar Results.

import pickle       # We Will Use Pickle(built-in)To Save The Data(optional)



import text_to_speech as speech     # You Can Use This To
                                    # Speak The Answers Aloud



# A Dictionary Can Be BestChoice To Find A Key(question)
# And Print It's Value(answer)
# We Will Store Questions In Keys And Answers As Values


# Create A Dictionary And Name It 'vocab' as Follows


vocab = {"hi": "Hello"}




# Create And Save A  File And Save The Vocab In It..

pickle.dump(vocab,open('Data.pickle','wb'))



# Use A Loop To Make Use Able To Ask
# As Many As Times He/She Wants

while True:

    # Load The Dictionary From Disk And Update The Dictionary
    vocab = pickle.load(open("Data.pickle",'rb'))


    # Get The Question From User
    question = input("Type Something: ")

    # Changing The Question To Lower Case
    # *String Comparasion Is Case Sensitive In Python And in Most Langauges*
    toFind = question.lower()


    # Check If We Have Answer For Question
    # And If We Have The Answer Print It on Screen...


    if toFind in vocab:
        print('')           # Leaving A Little Empty Space To Seprate Answer From Other Text
        print(vocab[toFind])        
        print('')






    # And If We Don't Have The Answer So,
    # We Have To Get Answer From Wikipedia,
    # And Open Browser With Search Results Related To User's Question


    # Looking In Wikipedia If We Don't Have Answer
    elif toFind not in vocab:
        print("We Don't Have Answer At The Moment Plz Wait..")
        print('')                   # Leaving Some Empty Space
        answer = wikipedia.summary(toFind)
        print(answer)
        print('')                   # Leaving Some Empty Space

        # Finally If We Got The Answer We
        # Need To Make Python Memrorize The Answer


        # We Will Do That By Adding A Key To Dictionary

        vocab[toFind] = answer

        # Re Save The Data After Adding A New Answer
        pickle.dump(vocab, open("Data.pickle",'wb'))





        # In Case We Don't Find Any Answer From
        # Wiki We Need To Let User Chosse The Answer Suggestions
        # We Get From Browser


        webbrowser.open(toFind, new = 2)




        # Speaking The Answer(Optional) **Slows Down The Script**
        
        speech.speak(answer, 'en')

                




