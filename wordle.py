from english_words import english_words_lower_set

first  = raw_input("Enter the mandatory first  letter of the word [press enter if none]: ")
first_x  = raw_input("Enter the letter\s that cannot be in the first position [press enter if none]: ")
print ('_'*100)
second = raw_input("Enter the mandatory second letter of the word [press enter if none]: ")
second_x  = raw_input("Enter the letter\s that cannot be in the second position [press enter if none]: ")
print ('_'*100)
third  = raw_input("Enter the mandatory third  letter of the word [press enter if none]: ")
third_x  = raw_input("Enter the letter\s that cannot be in the third position [press enter if none]: ")
print ('_'*100)
fourth = raw_input("Enter the mandatory fourth letter of the word [press enter if none]: ")
fourth_x  = raw_input("Enter the letter\s that cannot be in the fourth position [press enter if none]: ")
print ('_'*100)
fifth  = raw_input("Enter the mandatory fifth  letter of the word [press enter if none]: ")
fifth_x  = raw_input("Enter the letter\s that cannot be in the fifth position [press enter if none]: ")
print ('_'*100)

contain = raw_input("Enter the letters to contain from the the word [press enter if none]: ")
exclude = raw_input("Enter the letters to exclude from the the word [press enter if none]: ")
final_word_list = ''
final_word_list_without_repeated_letters = ''

#contain = "aes"
#exclude = "udiocrmbltg"



for word in english_words_lower_set:
    if len(word) == 5 :
        current_word = word
        if first:
            if not word[0] == first:
                current_word = None
        if current_word and second:
            if not word[1] == second:
                current_word = None
        if current_word and third:
            if not word[2] == third:
                current_word = None
        if current_word and fourth:
            if not word[3] == fourth:
                current_word = None
        if current_word and fifth:
            if not word[4] == fifth:
                current_word = None
        if current_word and contain:
            for contain_letter in contain:
                if contain_letter not in current_word:
                    current_word = None
                    break
        if current_word and exclude:
            for exclude_letter in exclude:
                if exclude_letter in current_word:
                    current_word = None
                    break
        if current_word and first_x:
            for exclude_letter in first_x:
                if exclude_letter in current_word[0]:
                    current_word = None
                    break
        if current_word and second_x:
            for exclude_letter in second_x:
                if exclude_letter in current_word[1]:
                    current_word = None
                    break
        if current_word and third_x:
            for exclude_letter in third_x:
                if exclude_letter in current_word[2]:
                    current_word = None
                    break
        if current_word and fourth_x:
            for exclude_letter in fourth_x:
                if exclude_letter in current_word[3]:
                    current_word = None
                    break
        if current_word and fifth_x:
            for exclude_letter in fifth_x:
                if exclude_letter in current_word[4]:
                    current_word = None
                    break
        if current_word:
            if len(set(current_word)) == 5:
                final_word_list_without_repeated_letters = final_word_list_without_repeated_letters + " " + current_word
        
        if current_word:
            final_word_list = final_word_list + " " + current_word
            
if final_word_list:
    print ("\nfinal_word_list:\n" + final_word_list)
if final_word_list_without_repeated_letters:
    print ("\nfinal_word_list_without_repeated_letters:\n" + final_word_list_without_repeated_letters + "\n")
else:
    print ("\nSorry!! No such word/s found." + "\n")
    
    
    
#udiocrmbl